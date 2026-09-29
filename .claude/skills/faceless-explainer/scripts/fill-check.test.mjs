import assert from "node:assert/strict";
import { mkdtempSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { spawnSync } from "node:child_process";
import test from "node:test";
import { analyzeFrame, parseIndex, settledTimes } from "./fill-check.mjs";
import { fillRule } from "./lib/dimensions.mjs";

const script = new URL("./fill-check.mjs", import.meta.url).pathname;
const W = 1080, H = 1350, GROUND = 245, INK = 20;

// Synthetic gray frame: cream ground with ink bars at the given [y0, y1) ranges.
function frame(bars) {
  const g = new Uint8Array(W * H).fill(GROUND);
  for (const [y0, y1] of bars) for (let y = y0; y < y1; y++) g.fill(INK, y * W + 100, y * W + W - 100);
  return g;
}

function indexHtml(w, h, clips) {
  const scenes = clips.map(([id, s, d]) =>
    `<div id="el-${id}" class="scene" data-composition-id="${id}" data-composition-src="compositions/frames/${id}.html" data-start="${s}" data-duration="${d}" data-track-index="0"></div>`).join("\n");
  return `<div id="root" data-composition-id="main" data-start="0" data-duration="10" data-width="${w}" data-height="${h}">\n${scenes}\n</div>`;
}

test("a frame using all three bands passes the 4:5 rule", () => {
  const r = analyzeFrame(frame([[100, 300], [420, 820], [930, 1080]]), W, H, fillRule(W, H));
  assert.equal(r.ok, true);
  assert.equal(r.lowest, 1079);
  assert.ok(r.maxEmptyBand <= 200);
});

test("a top-heavy frame with a dead lower band fails", () => {
  const r = analyzeFrame(frame([[100, 300], [360, 700]]), W, H, fillRule(W, H));
  assert.equal(r.ok, false);
  assert.equal(r.lowest, 699);
  assert.ok(r.maxEmptyBand > 200);
});

test("faint grid lines do not count as content", () => {
  const g = frame([[100, 300], [420, 820], [930, 1080]]);
  for (let y = 0; y < H; y += 60) g.fill(GROUND - 10, y * W, y * W + W);
  assert.equal(analyzeFrame(g, W, H, fillRule(W, H)).ok, true);
});

test("settled times come from clip timing: before the next start, final before its exit", () => {
  const { width, height, clips } = parseIndex(indexHtml(W, H, [["01-a", 0, 4.9], ["02-b", 4.4, 6.1], ["03-c", 10, 4]]));
  assert.deepEqual([width, height], [W, H]);
  assert.deepEqual(settledTimes(clips), [4.2, 9.8, 13.4]);
});

test("formats without a fill rule are skipped with exit 0", () => {
  const dir = mkdtempSync(join(tmpdir(), "fill-check-"));
  try {
    writeFileSync(join(dir, "index.html"), indexHtml(1920, 1080, [["01-a", 0, 3]]));
    const r = spawnSync(process.execPath, [script, "--video", join(dir, "none.mp4"), "--hyperframes", dir], { encoding: "utf8" });
    assert.equal(r.status, 0);
    assert.match(r.stdout, /skipped \(no fill rule for 1920x1080\)/);
  } finally { rmSync(dir, { force: true, recursive: true }); }
});

const hasFfmpeg = spawnSync("ffmpeg", ["-version"]).status === 0;
test("CLI exits 1 on a rendered clip with a dead lower band", { skip: !hasFfmpeg && "ffmpeg not installed" }, () => {
  const dir = mkdtempSync(join(tmpdir(), "fill-check-"));
  try {
    const mp4 = join(dir, "top-heavy.mp4");
    const mk = spawnSync("ffmpeg", ["-v", "error", "-y", "-f", "lavfi", "-i", `color=c=0xFAF9F5:s=${W}x${H}:d=2:r=5`,
      "-vf", "drawbox=x=100:y=120:w=880:h=500:color=0x141413:t=fill", "-pix_fmt", "yuv420p", mp4]);
    assert.equal(mk.status, 0, String(mk.stderr));
    writeFileSync(join(dir, "index.html"), indexHtml(W, H, [["01-a", 0, 2]]));
    const r = spawnSync(process.execPath, [script, "--video", mp4, "--hyperframes", dir], { encoding: "utf8" });
    assert.equal(r.status, 1, r.stdout + r.stderr);
    assert.match(r.stdout, /^FAIL 01-a t=1\.4s lowest=619/m);
  } finally { rmSync(dir, { force: true, recursive: true }); }
});
