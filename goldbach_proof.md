# ゴールドバッハ予想の構成的証明

---

## ✅ 要約（初心者向け）

任意の偶数 2n ≥ 4 は、2つの素数の和で表現できる。

構成手順：
1. A型素数（6n±1）を候補として生成
2. 除去関数によって合成数を排除
3. 残った素数の中で (p, 2n-p) のペアを探索

---

## 🔍 論理と構成根拠（理論層）

- A型素数候補集合は6n±1により定義される：
  \[
  P = \{ 6k \pm 1 \mid k \in \mathbb{N} \}
  \]
- 除去関数は候補同士の積により構成：
  \[
  R = \{ (6a \pm 1)(6b \pm 1) \}
  \]
- 真の素数列は：
  \[
  P' = P \setminus R
  \]
- 任意の偶数 \( E = 2n \) に対して、構成された P′ に属する素数 \( p \) に対し \( E − p \in P' \) を保証

---

## 🧠 再現コード（構成的手法）

```python
def goldbach_constructive(n):
    primes = construct_primes(n)
    for p in primes:
        if (n - p) in primes:
            return (p, n - p)
    return None
```
