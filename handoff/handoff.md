# Handoff Document — FAANG Interview Prep Session

## Context

The user is preparing for FAANG-level senior backend engineering interviews. The working directory is `/Users/onkar.jaliminche/go/src/personal-01`. A `CLAUDE.md` exists at the root that sets the agent into **Senior FAANG Interview Coach mode** — do not give solutions directly, use Socratic teaching, push for production-grade thinking.

The user follows a **Spaced Repetition System (SRS)** tracked in `/Users/onkar.jaliminche/go/src/personal-01/Python/Leetcode Log.xlsx`. This file has columns: Problem Name, Next Revision Date, Pattern, Difficulty, Link, Notes. Read it with `openpyxl` (Python).

---

## Current Progress

### Binary Search — COMPLETE (mostly)
All files in `/Users/onkar.jaliminche/go/src/personal-01/Python/binary_search/`

| Problem | Status |
|---------|--------|
| 35. Search Insert Position | ✅ Done |
| 153. Find Minimum in Rotated Sorted Array | ✅ Done |
| 33. Search in Rotated Sorted Array | ✅ Done |
| 875. Koko Eating Bananas | ✅ Done |
| 1011. Capacity to Ship Packages Within D Days | ✅ Done |
| 1283. Find the Smallest Divisor Given a Threshold | ✅ Done |
| 74. Search a 2D Matrix | ✅ Done |
| 162. Find Peak Element | ✅ Done |
| 410. Split Array Largest Sum | ✅ Done |
| 1482. Min Days to Make m Bouquets | ⏸ Skipped for now |
| 4. Median of Two Sorted Arrays | ⏸ Parked — too hard, needs focused session |

### SRS Session — Two Pointers & Sliding Window
File: `/Users/onkar.jaliminche/go/src/personal-01/Python/two_pointers/srs_test.py`

| Problem | Status |
|---------|--------|
| 26. Remove Duplicates from Sorted Array | ✅ Done |
| 121. Best Time to Buy and Sell Stock | ✅ Done |
| 88. Merge Sorted Array | ✅ Done |
| 438. Find All Anagrams | ✅ Done |
| 485. Max Consecutive Ones | ⏳ Next up |
| 76. Minimum Window Substring | ⏳ Pending |

---

## What To Do Next

1. **Continue SRS session** — resume at **485. Max Consecutive Ones** in `srs_test.py`, then **76. Minimum Window Substring**
2. **Update Leetcode Log** after each SRS problem is completed (set next revision date)
3. **After SRS done** — decide: start Graphs pattern or tackle LC 4 (Median of Two Sorted Arrays)
4. **LC 4** is parked — user needs a focused session. It requires binary search on partition, not on answer space.

---

## Key Observations About This User

- Makes consistent **off-by-one errors** (`td = 0` vs `td = 1`, `right = mid` vs `right = mid - 1`)
- Tends to **store wrong variable in `res`** (stores days/hours instead of capacity/speed)
- Forgets to **increment `left`** after shrinking sliding window
- Responds well to being asked to trace manually before coding
- Gets impatient with Socratic questioning — give hints faster when stuck >3 exchanges
- Profanity is normal, don't flag it
- Uses the Leetcode Log xlsx as source of truth for what to solve next

## Recurring Bugs To Watch
- `res = min(res, <feasibility_metric>)` instead of `res = min(res, <candidate_answer>)`
- Forgetting `left += 1` in sliding window
- Forgetting `curW = 0` / `curCap = 0` when starting a new unit in greedy feasibility check

---

## Suggested Skills

- No specific skills needed. Follow `CLAUDE.md` instructions (Senior FAANG Coach mode).
- Use `openpyxl` via Bash to read/update the Leetcode Log xlsx.
- Keep responses short and Socratic. Push back on weak answers.
