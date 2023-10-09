---
id: 7aa9b25b-7637-4b92-a0b0-0d079370e743
title: 06. Learning with Linear Bellman Completion & Generative model
created_time: 2023-07-01T16:09:00.000Z
last_edited_time: 2023-08-17T06:46:00.000Z
cover_image: https://www.notion.so/images/page-cover/solid_red.png
하위 항목: []
subclass: RL Theory
class: RL
작성일시: 2023-07-01T16:09:00.000Z
pdf: https://wensun.github.io/CS6789_data_fall_2021/linear_BC.pdf
상위 항목: []
_thumbnail: https://www.notion.so/images/page-cover/solid_red.png

---

> 💡 What structural Condition can permit efficient learning?

# The Linear Bellman Completion Condition

# Linear Bellman Completion

*   Given feature \phi, take any linear function w^\top\phi(s,a)

    ```undefined
    \forall h, \exist\theta\in\R^d,s.t.,\theta^\top\phi(s,a)=r(s,a)+\mathbb{E}_{s'\sim P_h(s,a)}\max_{a'}w^\top\phi(s',a'),\forall s,a
    ```

*   This implies that Q\_h^\* is linear in \phi: Q\_h^\* = (\theta^\*)^\top,\forall h

## Why this is a reasonable assumption?

*   In tabluar MDP

    *   We can set \phi(s,a) to be one-hot encoding vector in \R^{SA}, i.e., \phi(s,a)=\[0,\dots,0,1,0,\dots,0]^\top

*   Linear System with Quadratic feature \phi

    *   Claim: r(s,a) + \mathbb{E}*{s'\sim P(s,a)}\max*{a'}w^\top\phi(s,a) is a linear function in \phi

## Why this is a strong assumption?

*   Assume that given feature \phi has linear Bellman completion, and adding additional elements to \phi

*   This break conditions! (In supervised learning, adding elements is ok, but not in RL)

***

> Generative Model + Linear Bellman Completion = Sample Efficient Learning

# The Least Square Value Iteration(LSVI) Algorithm

*   Linear bellman completion → Q\_h^*(s,a) = (\theta\_h^*)^\top \phi(s,a),\forall s,a,h

*   Given datasets \mathscr{D\_0, ...D}\_{H-1}, w/ \mathscr{D}\_h = {s,a,r,s}, r=r(s,a), s' \sim P\_h(\cdot|s,a)

## LSVI

*   Set  V\_H(s) = 0,\forall s

*   For h = H-1 to 0:

    *   \theta\_h=\arg\min\_\theta \sum\_{\mathscr{D}*h}\left(\theta^T\phi(s,a) - (r+V*{h+1}(s'))\right)

    *   Set V\_h(s)\coloneqq \max\_a \theta\_h^\top\phi(s,a),\forall s

*   Return \hat\pi\_h(s) = \arg\max\_a \theta\_h^\top\phi(s,a),\forall h

## Why LSVI may work?

*   When we do linear regression at step h:

```undefined
x := \phi(s,a), y:= r+ V_{h+1}(s')
```

*   We note that

    ```undefined
    \mathbb{E}[y|x] = r(s,a) + \mathbb{E}_{s'\sim P_h(s,a)}\max_{a'} \theta_{h+1}^\top\phi(s',a')
    ```

    i.e., our regression target is indeed linear in \phi, and it is close to Q\_h^\* if V\_{h+1} \approx V^\*\_{h+1}

*   If V\_{h+1} \approx V^*\_{h+1}, and linear regression succeeds(e.g., \theta\_h \approx \mathscr{T}*h(\theta*{h+1})), then we should hope \theta\_h^\top\phi(s,a) \approx Q\_h^*(s,a)

# Guarantee and the proof sketch

## Sample complexity of LSVI

*   There exists a way to construct datasets { \mathscr{D}*h}*{h=0}^{H-1},  such that with probability at least 1-\delta, we have

    ```undefined
    V^{\hat\pi} - V^* \le \epsilon
    ```

    with total number of samples in these datasets scaling \tilde O (d^2+H^6d^2/\epsilon^2)

## Detour

### Ordinary Linear Squares

*   OLS: \hat\theta = \arg\min\_\theta\sum\_{i=1}^N(\theta^\top x\_i-y\_i)^2

*   With probability at least 1-\delta, we have

    ```undefined
    (\hat\theta - \theta^*)^\top \Lambda(\hat\theta - \theta^*) \le O \left( \frac {\sigma^2d\ln(1/\delta)}{N} \right)
    ```

*   Issue: it the test point x is not covered by the training data, then we cannot guarantee \hat\theta^\top xis close to (\theta^\*)^\top x

### D-optimal Design

*   Consider a compact space \mathscr{X} \sub \R^d (without loss of generality, assume \text{span}(\mathscr{X}) = \R^d

*   D-optimal design \rho^\* \in \Delta(\mathscr{X}): \ \rho^\* = \arg\max\_{\rho^\* \in\Delta(\mathscr{X})}\ln\det(\mathbb{E}\_{x\sim\rho}\[xx^\top])

*   Properties of D-optimal design:

    *   \text{support}(\rho^\*) \le d(d+1)/2

    *   \max\_{y\in\mathscr{X}}y^\top \[\mathbb{E}\_{x\in\rho}xx^\top]^{-1} y \le d

### OLS with D-optimal design

*   We actively construct a dataset \mathscr{D}, which contains \lceil \rho(x)N \rceil many copies of x

*   For each x \in \mathscr{D}, query y and the OLS solution \hat\theta on \mathscr{D} has the following point-wise guarantee: with probability 1-δ,

    ```undefined
    \max_{x\in\mathscr{X}}\left|\lang \hat\theta - \theta^*,x\rang \right| \le \frac{\sigma d \ln(1/\delta)}{\sqrt{N}}
    ```

### Using D-optimal design to construct \mathscr{D}\_h in LSVI

*   Consider the space \Phi = { \phi(s,a): s,a \in S\times A }

*   Construct \mathscr{D}*h that contains \lceil \rho(s,a)N \rceil many copies of \phi(s,a), for each \phi(s,a), query y:=r(s,a)+V*{h+1}(s'), s' \sim P\_h(\cdot|s,a)

*   OLS with D-optimal design implies that \theta\_h is point-wise accurate

    ```undefined
    \max_{s,a} |\theta_h\phi(s,a)-\mathscr{T}_h(\theta_{h+1})^\top\phi(s,a)| \le O(Hd/\sqrt{N})
    ```

*   This implies our estimator Q\_h := \theta\_h^\top\phi is nearly Bellman-constant

    ```undefined
    ||Q_h-\mathscr{T}_hQ_h^* ||_\infty \le O(Hd/\sqrt{N})
    ```

*   Nearly Bellman consistency implies Q\_h is close to Q\_h^\*(this holds in general)

    ```undefined
    ||Q_h-Q_h^* ||_\infty \le O(H^2d/\sqrt{N})
    ```
