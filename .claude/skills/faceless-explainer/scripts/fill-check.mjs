#!/usr/bin/env node
// fill-check.mjs — portrait fill gate for a rendered faceless explainer.
//
// # reads: a rendered MP4 (via ffmpeg) and the project's assembled index.html
//   (canvas size + frame clip timing); writes nothing, no network.
//
// For every frame clip in index.html it grabs one settled frame (just before the
// next frame's transition starts; the final frame just before its exit fade),
// measures the lowest content row and the tallest empty band above the caption
// band, and checks them against the format's rule in lib/dimensions.mjs
// (FILL_RULES). One line per frame; exit 1 on any failure, 0 when all pass or the
// format has no fill rule.
//
//   node fill-check.mjs --video renders/video.mp4 [--hyperframes .] [--index ./index.html]
//                       [--at 4.2,9.8,...]   # override the derived settled times
import { readFileSync } from "node:fs";
import { spawnSync } from "node:child_process";
import { join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { captionBand, fillRule } from "./lib/dimensions.mjs";

export const SETTLE_BEFORE_NEXT_S = 0.2; // before the incoming transition
export const SETTLE_BEFORE_END_S = 0.6; // final frame: before its exit fade

// index.html → { width, height, clips: [{ id, start, duration }] } (clips by start)
export function parseIndex(html) {
  const num = (s, k) => {
    const m = s.match(new RegExp(`${k}="([0-9.]+)"`));
    return m ? Number(m[1]) : null;
  };
  const rootTag = html.match(/<div[^>]*data-composition-id="[^"]*"[^>]*data-width="[0-9]+"[^>]*>/s)?.[0]
    ?? html.match(/<[^>]*data-width="[0-9]+"[^>]*>/s)?.[0] ?? "";
  const clips = [];
  for (const m of html.matchAll(/<div\b[^>]*data-composition-src="[^"]*"[^>]*>/gs)) {
    const tag = m[0];
    if (/captions\.html/.test(tag)) continue;
    const id = tag.match(/data-composition-id="([^"]*)"/)?.[1] ?? "?";
    const start = num(tag, "data-start");
    const duration = num(tag, "data-duration");
    if (start !== null && duration !== null) clips.push({ id, start, duration });
  }
  clips.sort((a, b) => a.start - b.start);
  return { width: num(rootTag, "data-width"), height: num(rootTag, "data-height"), clips };
}

export function settledTimes(clips) {
  return clips.map((c, i) => {
    const next = clips[i + 1];
    const t = next ? next.start - SETTLE_BEFORE_NEXT_S : c.start + c.duration - SETTLE_BEFORE_END_S;
    return Math.max(c.start, Math.round(t * 100) / 100);
  });
}

// gray: Uint8Array of width*height luma. Ground = median of row 5.
export function analyzeFrame(gray, width, height, rule) {
  const bottom = captionBand(height).bandTopY;
  const ground = Array.from(gray.subarray(5 * width, 6 * width)).sort((a, b) => a - b)[width >> 1];
  const isContent = (y) => {
    let n = 0;
    const row = y * width;
    for (let x = rule.sideMargin; x < width - rule.sideMargin; x++) {
      if (Math.abs(gray[row + x] - ground) > rule.diff && ++n >= rule.minPixels) return true;
    }
    return false;
  };
  let lowest = 0, run = 0, maxEmptyBand = 0;
  for (let y = rule.top; y < bottom; y++) {
    if (isContent(y)) { lowest = y; run = 0; } else { run++; if (run > maxEmptyBand) maxEmptyBand = run; }
  }
  const ok = lowest >= rule.minLowest && maxEmptyBand <= rule.maxEmptyBand;
  return { lowest, maxEmptyBand, ok };
}

function grabGray(video, t, width, height) {
  const r = spawnSync("ffmpeg", ["-v", "error", "-ss", String(t), "-i", video, "-frames:v", "1",
    "-vf", `scale=${width}:${height}`, "-f", "rawvideo", "-pix_fmt", "gray", "-"], { maxBuffer: width * height * 2 });
  if (r.status !== 0 || !r.stdout || r.stdout.length < width * height) {
    throw new Error(`ffmpeg could not read a frame at ${t}s from ${video}: ${String(r.stderr || "").trim()}`);
  }
  return new Uint8Array(r.stdout.buffer, r.stdout.byteOffset, width * height);
}

function flag(argv, name) {
  const i = argv.indexOf(`--${name}`);
  return i >= 0 ? argv[i + 1] : undefined;
}

export function main(argv) {
  const video = flag(argv, "video");
  if (!video) { console.error("usage: fill-check.mjs --video <mp4> [--hyperframes .] [--index index.html] [--at t1,t2]"); return 2; }
  const project = resolve(flag(argv, "hyperframes") ?? ".");
  const index = parseIndex(readFileSync(resolve(flag(argv, "index") ?? join(project, "index.html")), "utf8"));
  const { width, height } = index;
  const rule = fillRule(width, height);
  if (!rule) { console.log(`fill-check: skipped (no fill rule for ${width}x${height})`); return 0; }
  const at = flag(argv, "at");
  const times = at ? at.split(",").map(Number) : settledTimes(index.clips);
  let failed = 0;
  times.forEach((t, i) => {
    const id = at ? `t${i + 1}` : index.clips[i].id;
    const r = analyzeFrame(grabGray(video, t, width, height), width, height, rule);
    if (!r.ok) failed++;
    console.log(`${r.ok ? "ok  " : "FAIL"} ${id} t=${t}s lowest=${r.lowest} (min ${rule.minLowest}) max_empty_band=${r.maxEmptyBand} (max ${rule.maxEmptyBand})`);
  });
  console.log(`fill-check: ${times.length - failed}/${times.length} frames pass (${width}x${height})`);
  return failed ? 1 : 0;
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try { process.exit(main(process.argv.slice(2))); }
  catch (e) { console.error(`fill-check: ${e.message}`); process.exit(2); }
}
