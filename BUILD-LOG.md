# Build log — One Line That Makes a Builder Fund a Bounty

- Competition: One Line That Makes a Builder Fund a Bounty
  (slug `u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf`)
- Competition opened: 2026-11-23 04:00 WAT (03:00 UTC)
- Builder session began: ~04:05 WAT (post-opening, window rule satisfied)
- Recorder: N/A — `makefun record` returns HTTP 400 for this competition
  ("does not take recorded transcripts: its entries upload their transcripts
  (a bundle or loose files)"); same as the earlier joke entry. The
  coordinator bundles this builder session afterwards (bundle path).
- Entries close: 2026-11-23 05:00 WAT. $5 pot (1st $2, 2nd $2, 3rd $1).

## The line entered

> Fund a bounty and let AI agents race to build it — the best entry wins the reward, and you pay for results, not promises.

- 121 characters, 1 sentence, 123 UTF-8 bytes (line itself; 124 bytes in
  entry.txt including the trailing newline). Gate is 1–240 characters.
- Used exactly as crafted and gate-checked; not rewritten or retargeted.

## Program

- `main.py`: deterministic Python, stdlib only, no network, no randomness.
  Writes the line to `/output/entry.txt` via `MAKEFUN_OUTPUT_DIR`
  (default `/output`), validates 1–240 characters, empties the output
  directory's contents only (never the directory itself, which the grader
  mounts), and ends the file with a trailing newline.

## Tests (run 2026-11-23 ~04:06 WAT)

- Ran `main.py` twice with `MAKEFUN_OUTPUT_DIR` set to two temp dirs:
  byte-identical output, sha256
  `c8f2bc01c74f7f37c4e3657f9a42142d054918ccf00ef7bf39e7ffdd94175b7c`
  for both runs.
- `entry.txt` content is exactly the line + `"\n"`: 121 chars, 123 bytes
  for the line, 124 bytes for the file. All assertions passed.
- Bind-mount style check: placed a stale file and a stale subdirectory in
  the temp output dir, re-ran — stale contents cleared, the directory
  itself survived, `entry.txt` sha256 unchanged
  (`c8f2bc01c74f7f37c4e3657f9a42142d054918ccf00ef7bf39e7ffdd94175b7c`).

## Repository

- Repo: https://github.com/Victorcollin123/one-line-that-makes-a-builder-fund-a-bounty-20261123-0318
- Repo created: 2026-11-23 04:07:25 WAT (03:07:25 UTC), public, under Victorcollin123
- About: homepage https://make.fun/bounty/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf, topics makefun, ai-agents, bounties, growth (set below)
- Entry commit (first commit, all entry files): PLACEHOLDER_SHA
- This log was committed with the entry files; the final HEAD sha is
  reported by the builder to the coordinator (it changes if the log is
  updated after the first commit — see git history).

## Notes

- Do NOT submit without the user's separate go-ahead in the main chat.
- Referral code qp17c3xn is referral-only; no makefun- play code applies
  to this bounty.
