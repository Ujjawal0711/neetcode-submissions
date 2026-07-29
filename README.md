# 🧩 NeetCode Solutions — Ujjawal

![Solved](https://img.shields.io/badge/Solved-17-brightgreen)
![Language](https://img.shields.io/badge/Language-Python-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-NeetCode-000000)
![Last Updated](https://img.shields.io/badge/Updated-Jul%202026-informational)
![License](https://img.shields.io/badge/License-MIT-yellow)

My worked solutions to [NeetCode.io](https://neetcode.io) / LeetCode-style problems, kept as a personal DSA study log. Every file has a comment header explaining the **problem, the approach, and the time/space complexity**, plus inline notes on the tricky parts — so future-me can re-read a solution and instantly remember *why* it works.

Problems are filed into their **NeetCode roadmap topic**. Most solutions are auto-synced from NeetCode via GitHub Sync and then annotated by hand; a few are added manually.

---

## 📊 Progress

**17 problems · 20 solutions** — 🟢 Easy · 6   🟡 Medium · 11   🔴 Hard · 0

### 🗃️ Arrays & Hashing — 9

| Problem | Difficulty | Approach | Time | Space | Solution |
|---------|:---:|----------|------|-------|----------|
| Two Sum | 🟢 Easy | One-pass hashmap of complements | O(n) | O(n) | [link](Data%20Structures%20%26%20Algorithms/Arrays%20%26%20Hashing/two-integer-sum/submission-0.py) |
| Contains Duplicate | 🟢 Easy | Set of seen values | O(n) | O(n) | [link](Data%20Structures%20%26%20Algorithms/Arrays%20%26%20Hashing/duplicate-integer/submission-2.py) |
| Valid Anagram | 🟢 Easy | Single tally dict (+s / −t) | O(n) | O(1) | [link](Data%20Structures%20%26%20Algorithms/Arrays%20%26%20Hashing/is-anagram/submission-0.py) |
| Group Anagrams | 🟡 Medium | 26-slot count tuple as key | O(n·k) | O(n·k) | [link](Data%20Structures%20%26%20Algorithms/Arrays%20%26%20Hashing/anagram-groups/submission-0.py) |
| Top K Frequent Elements | 🟡 Medium | ⭐ Bucket sort (freq as index) | **O(n)** | O(n) | [link](Data%20Structures%20%26%20Algorithms/Arrays%20%26%20Hashing/top-k-elements-in-list/bucket-sort/submission-1.py) |
| ↳ *2nd way* | 🟡 Medium | Min-heap capped at size k | O(n log k) | O(n) | [link](Data%20Structures%20%26%20Algorithms/Arrays%20%26%20Hashing/top-k-elements-in-list/heap/submission-0.py) |
| Encode and Decode Strings | 🟡 Medium | Length-prefix `len#str` framing | O(n) | O(n) | [link](Data%20Structures%20%26%20Algorithms/Arrays%20%26%20Hashing/string-encode-and-decode/submission-2.py) |
| Product of Array Except Self | 🟡 Medium | ⭐ Prefix × suffix products | **O(n)** | O(n) | [link](Data%20Structures%20%26%20Algorithms/Arrays%20%26%20Hashing/products-of-array-discluding-self/prefix-suffix/submission-0.py) |
| ↳ *2nd way* | 🟡 Medium | Re-scan array for each index | O(n²) | O(1) | [link](Data%20Structures%20%26%20Algorithms/Arrays%20%26%20Hashing/products-of-array-discluding-self/brute-force/submission-1.py) |
| Valid Sudoku | 🟡 Medium | 27 sets: rows, cols, 3×3 boxes | O(1)\* | O(1)\* | [link](Data%20Structures%20%26%20Algorithms/Arrays%20%26%20Hashing/valid-sudoku/submission-0.py) |
| Longest Consecutive Sequence | 🟡 Medium | Hashset, expand only from starts | O(n) | O(n) | [link](Data%20Structures%20%26%20Algorithms/Arrays%20%26%20Hashing/longest-consecutive-sequence/submission-0.py) |

### 👉👈 Two Pointers — 4

| Problem | Difficulty | Approach | Time | Space | Solution |
|---------|:---:|----------|------|-------|----------|
| Valid Palindrome | 🟢 Easy | Two pointers, skip non-alnum | O(n) | O(1) | [link](Data%20Structures%20%26%20Algorithms/Two%20Pointers/is-palindrome/submission-0.py) |
| Two Sum II (sorted) | 🟡 Medium | Converge pointers to steer the sum | O(n) | O(1) | [link](Data%20Structures%20%26%20Algorithms/Two%20Pointers/two-integer-sum-ii/submission-0.py) |
| 3Sum | 🟡 Medium | Sort, fix one, Two Sum II the rest | O(n²) | O(1) | [link](Data%20Structures%20%26%20Algorithms/Two%20Pointers/three-integer-sum/submission-1.py) |
| Container With Most Water | 🟡 Medium | Move the shorter side inward | O(n) | O(1) | [link](Data%20Structures%20%26%20Algorithms/Two%20Pointers/max-water-container/submission-0.py) |

### 🪟 Sliding Window — 3

| Problem | Difficulty | Approach | Time | Space | Solution |
|---------|:---:|----------|------|-------|----------|
| Best Time to Buy & Sell | 🟢 Easy | Track min price, max profit | O(n) | O(1) | [link](Data%20Structures%20%26%20Algorithms/Sliding%20Window/buy-and-sell-crypto/min-price-tracking/submission-0.py) |
| ↳ *2nd way* | 🟢 Easy | Two-pointer window, reset on new low | O(n) | O(1) | [link](Data%20Structures%20%26%20Algorithms/Sliding%20Window/buy-and-sell-crypto/sliding-window/submission-1.py) |
| Longest Substring Without Repeating | 🟡 Medium | Window + set, shrink past duplicate | O(n) | O(min(n,m)) | [link](Data%20Structures%20%26%20Algorithms/Sliding%20Window/longest-substring-without-duplicates/submission-2.py) |
| Longest Repeating Char Replacement | 🟡 Medium | Window valid while `len - maxfreq ≤ k` | O(n) | O(1) | [link](Data%20Structures%20%26%20Algorithms/Sliding%20Window/longest-repeating-substring-with-replacement/submission-2.py) |

### 📐 Math & Geometry — 1

| Problem | Difficulty | Approach | Time | Space | Solution |
|---------|:---:|----------|------|-------|----------|
| Max Product of Two Digits | 🟢 Easy | Sort digits, take top two | O(d log d)† | O(d) | [link](Data%20Structures%20%26%20Algorithms/Math%20%26%20Geometry/max-product-of-two-digits/submission-0.py) |

<sub>\* Board is always 9×9, so the work is constant by definition.<br>† d = digit count (≤ 10), so effectively O(1).</sub>

---

## 🗺️ Roadmap coverage

| Topic | Done | | Topic | Done |
|---|:---:|---|---|:---:|
| Arrays & Hashing | **9** | | Backtracking | — |
| Two Pointers | **4** | | Graphs | — |
| Sliding Window | **3** | | Advanced Graphs | — |
| Stack | — | | 1-D DP | — |
| Binary Search | — | | 2-D DP | — |
| Linked List | — | | Greedy | — |
| Trees | — | | Intervals | — |
| Tries | — | | Math & Geometry | **1** |
| Heap / Priority Queue | — | | Bit Manipulation | — |

---

## 🗂️ Repository structure

```
Data Structures & Algorithms/
├── Arrays & Hashing/
│   ├── two-integer-sum/
│   │   └── submission-0.py              ← N = attempt number (0 = first)
│   ├── top-k-elements-in-list/          ← solved 2 ways -> subfolder per method
│   │   ├── bucket-sort/                 ← ⭐ optimal O(n)
│   │   └── heap/                        ← O(n log k)
│   └── ...
├── Two Pointers/
├── Sliding Window/
│   └── buy-and-sell-crypto/
│       ├── min-price-tracking/
│       └── sliding-window/
└── Math & Geometry/
```

Problems are filed by **NeetCode roadmap topic**, then problem slug. Multiple `submission-N` files for one problem are successive attempts.

**Convention:** when a problem is solved with more than one *approach*, each approach gets its own named subfolder (`bucket-sort/`, `heap/`, …) instead of sitting flat as `submission-0/1`. Every file's header names the method and cross-references the alternative, so the trade-off is obvious on revisit.

---

## ▶️ Running a solution locally

Each file defines a `Solution` class (NeetCode/LeetCode format). To try one, paste the class into a Python REPL and call its method:

```python
sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))   # -> [0, 1]
```

---

## 🔄 About the sync

This repo is populated by NeetCode's **GitHub Sync** — submissions on [neetcode.io](https://neetcode.io) auto-commit here. Settings live at [neetcode.io/profile/github](https://neetcode.io/profile/github) (auto-commit toggle, accepted-only filter, bulk sync).

> **Note:** sync writes to the *flat* path `Data Structures & Algorithms/<problem-slug>/`, so newly synced problems land at the top level and just need moving into their topic folder. Auto-commit is unaffected by this repo's structure — it only ever creates its own file. This `README.md` is hand-maintained and is not regenerated by sync.
>
> ⚠️ The one thing to avoid is **Bulk Sync**, which re-pushes *all* past solutions at their flat paths and would duplicate everything already filed into topic folders.

---

*Studying data structures & algorithms one problem at a time.*
