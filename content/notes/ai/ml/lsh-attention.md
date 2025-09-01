---
title: "LSH Attention: Multiple Hyperplanes and Bucketing"
description: "Understanding how multiple random hyperplanes create better locality-sensitive hashing for attention mechanisms"
date: 2025-09-01
draft: false
math: true
---

# LSH Attention: Multiple Hyperplanes and Bucketing

Great follow-up 👌 — let's go carefully.

When you use **multiple random hyperplanes** (say $L$ of them), you're no longer just splitting into two buckets; you get a **bit-string signature** for each token.

---

## 1. Hashing with multiple hyperplanes

* Suppose you pick $L$ random hyperplanes: $r_1,\dots,r_L \in \mathbb{R}^d$.
* For each token $x$, compute:

  $$
  h_{r_\ell}(x) = \text{sign}(r_\ell^\top x) \in \{+1,-1\}.
  $$
* Collect them into a vector (bitstring):

  $$
  H(x) = \big(h_{r_1}(x), h_{r_2}(x), \dots, h_{r_L}(x)\big).
  $$

This is the **LSH signature** of token $x$.
There are at most $2^L$ different signatures → up to $2^L$ buckets.

---

## 2. Example

Take $L=3$ hyperplanes.

* Token $x_1$: signature = (+1, +1, –1) → bucket "110"
* Token $x_2$: signature = (+1, +1, –1) → bucket "110"
* Token $x_3$: signature = (–1, +1, +1) → bucket "011"

So $x_1, x_2$ end up in the same bucket, $x_3$ in a different one.

---

## 3. Bucketing procedure

* After computing signatures for all tokens, **group tokens with the same signature together**.
* Practically, you can treat the bitstring as an integer ID and then **sort tokens by bucket ID**.
* Then attention is computed **within each bucket only**.

---

## 4. Why multiple hyperplanes help

* With a single hyperplane, the chance of missing a "true neighbor" can be high (they may land on opposite sides).
* With multiple hyperplanes:

  * If two tokens are **very similar**, their bitstrings are likely to match in all positions → high chance of same bucket.
  * If they are dissimilar, their signatures diverge.

So **collision probability matches similarity** more finely.

---

## 5. Multiple "rounds" of hashing (Reformer trick)

* Sometimes you repeat the entire procedure with several **independent sets of hyperplanes**.
* Each round gives a separate bucketing.
* Each token participates in attention within its bucket(s) for all rounds.
* This further reduces the risk of missing important interactions.

---

## Summary

* With **$L$ hyperplanes**, each token gets an $L$-bit signature.
* Tokens with identical signatures go into the **same bucket**.
* Attention is computed **within buckets only**, giving a block-sparse attention matrix.
* More hyperplanes → finer granularity.
* More independent rounds → lower probability of missing neighbors.

---

## Mathematical Details

The probability of collision for cosine similarity: two vectors at angle $\theta$ collide with probability $1-\theta/\pi$ per hyperplane, and $(1-\theta/\pi)^L$ for $L$ hyperplanes.

This approach provides a principled way to trade off computational efficiency with attention quality in transformer models.
