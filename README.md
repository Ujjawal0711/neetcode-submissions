# 🧩 NeetCode Solutions — Ujjawal

![Solved](https://img.shields.io/badge/Solved-9-brightgreen)
![Language](https://img.shields.io/badge/Language-Python-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-NeetCode-000000)
![Last Updated](https://img.shields.io/badge/Updated-Jul%202026-informational)
![License](https://img.shields.io/badge/License-MIT-yellow)

My worked solutions to [NeetCode.io](https://neetcode.io) / LeetCode-style problems, kept as a personal DSA study log. Every file has a comment header explaining the **problem, the approach, and the time/space complexity**, plus inline notes on the tricky parts — so future-me can re-read a solution and instantly remember *why* it works.

Solutions are auto-synced from NeetCode via GitHub Sync and then annotated by hand.

---

## 📊 Progress

| # | Problem | Difficulty | Topic | Approach | Time | Space | Solution |
|---|---------|:---:|-------|----------|------|-------|----------|
| 1 | Two Sum | 🟢 Easy | Arrays & Hashing | One-pass hashmap of complements | O(n) | O(n) | [link](Data%20Structures%20%26%20Algorithms/two-integer-sum/submission-0.py) |
| 2 | Contains Duplicate | 🟢 Easy | Arrays & Hashing | Set of seen values | O(n) | O(n) | [link](Data%20Structures%20%26%20Algorithms/duplicate-integer/submission-2.py) |
| 3 | Valid Anagram | 🟢 Easy | Arrays & Hashing | Single tally dict (+s / −t) | O(n) | O(1) | [link](Data%20Structures%20%26%20Algorithms/is-anagram/submission-0.py) |
| 4 | Group Anagrams | 🟡 Medium | Arrays & Hashing | 26-slot count tuple as key | O(n·k) | O(n·k) | [link](Data%20Structures%20%26%20Algorithms/anagram-groups/submission-0.py) |
| 5 | Valid Palindrome | 🟢 Easy | Two Pointers | Two pointers, skip non-alnum | O(n) | O(1) | [link](Data%20Structures%20%26%20Algorithms/is-palindrome/submission-0.py) |
| 6 | Best Time to Buy/Sell | 🟢 Easy | Sliding Window | Track min price, max profit | O(n) | O(1) | [link](Data%20Structures%20%26%20Algorithms/buy-and-sell-crypto/submission-0.py) |
| 7 | Top K Frequent Elements | 🟡 Medium | Arrays & Hashing | ⭐ Bucket sort (freq as index) | **O(n)** | O(n) | [link](Data%20Structures%20%26%20Algorithms/top-k-elements-in-list/bucket-sort/submission-1.py) |
| 7 | ↳ *same problem, 2nd way* | 🟡 Medium | Heap | Min-heap capped at size k | O(n log k) | O(n) | [link](Data%20Structures%20%26%20Algorithms/top-k-elements-in-list/heap/submission-0.py) |
| 8 | Product of Array Except Self | 🟡 Medium | Prefix Sum | ⭐ Prefix × suffix products | **O(n)** | O(n) | [link](Data%20Structures%20%26%20Algorithms/products-of-array-discluding-self/prefix-suffix/submission-0.py) |
| 8 | ↳ *same problem, 2nd way* | 🟡 Medium | Brute Force | Re-scan array for each index | O(n²) | O(1) | [link](Data%20Structures%20%26%20Algorithms/products-of-array-discluding-self/brute-force/submission-1.py) |
| 9 | Valid Sudoku | 🟡 Medium | Arrays & Hashing | 27 sets: rows, cols, 3×3 boxes | O(1)\* | O(1)\* | [link](Data%20Structures%20%26%20Algorithms/valid-sudoku/submission-0.py) |

<sub>\* Board is always 9×9, so the work is constant by definition.</sub>

*🟢 Easy · 5   🟡 Medium · 4   🔴 Hard · 0*

*Solved so far: **9** (11 solutions — 2 problems solved 2 ways)*

*Language: **Python** 🐍*

---

## 🗂️ Repository structure

```
neetcode-submissions/
└── Data Structures & Algorithms/
    ├── <problem-id>/
    │   └── submission-N.py         ← N = attempt number (0 = first)
    │
    ├── top-k-elements-in-list/     ← solved 2 ways -> one subfolder per method
    │   ├── bucket-sort/
    │   │   └── submission-1.py     ← ⭐ optimal O(n)
    │   └── heap/
    │       └── submission-0.py     ← O(n log k)
    │
    └── products-of-array-discluding-self/
        ├── prefix-suffix/
        │   └── submission-0.py     ← ⭐ optimal O(n)
        └── brute-force/
            └── submission-1.py     ← O(n²), kept for contrast
```

Files are grouped by topic folder, then problem slug. Multiple `submission-N` files for one problem are successive attempts.

**Convention:** when a problem is solved with more than one *approach*, each approach gets its own named subfolder (`bucket-sort/`, `heap/`, …) instead of sitting flat as `submission-0/1`. Every file's header block names the method and cross-references the alternative, so the trade-off is obvious on revisit.

---

## 🏷️ Topics covered

- **Arrays & Hashing** — Two Sum, Contains Duplicate, Valid Anagram, Group Anagrams, Top K Frequent Elements, Valid Sudoku
- **Two Pointers** — Valid Palindrome
- **Sliding Window** — Best Time to Buy and Sell
- **Prefix Sum** — Product of Array Except Self *(optimal approach)*
- **Heap / Priority Queue** — Top K Frequent Elements *(alt. approach)*
- **Bucket Sort** — Top K Frequent Elements *(optimal approach)*

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

> ⚠️ **Heads-up:** NeetCode auto-generates a `README.md` on sync. If auto-commit stays on, a future sync may overwrite this custom README. To keep it, either turn off auto-commit or re-apply this file after syncs.

---

*Studying data structures & algorithms one problem at a time.*
