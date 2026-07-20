# 🧩 NeetCode Solutions — Ujjawal

![Solved](https://img.shields.io/badge/Solved-6-brightgreen)
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

*🟢 Easy · 5   🟡 Medium · 1   🔴 Hard · 0*

*Solved so far: **6** · Language: **Python** 🐍*

---

## 🗂️ Repository structure

```
neetcode-submissions/
└── Data Structures & Algorithms/
    └── <problem-id>/
        └── submission-N.py     ← N = attempt number (0 = first)
```

Files are grouped by topic folder, then problem slug. Multiple `submission-N` files for one problem are successive attempts at that problem.

---

## 🏷️ Topics covered

- **Arrays & Hashing** — Two Sum, Contains Duplicate, Valid Anagram, Group Anagrams
- **Two Pointers** — Valid Palindrome
- **Sliding Window** — Best Time to Buy and Sell

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
