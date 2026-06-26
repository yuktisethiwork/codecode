# 121. Best Time to Buy and Sell Stock — Approach 1

| Field | Value |
|-------|-------|
| **Problem** | [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/2046609796/) |
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Language** | python3 |
| **Runtime** | 560 ms |
| **Memory** | 29.3 MB |
| **Patterns** | Array, Dynamic Programming |
| **Date** | 26/06/2026 |

---

## 🧠 How I Solved It
2 ptr. directly skip the lower j price by moving i directly to j instead of just incrementing it by 1.

**Code:** [`approach_1.py`](./approach_1.py)
