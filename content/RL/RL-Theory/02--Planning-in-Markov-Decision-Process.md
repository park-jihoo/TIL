---
id: 594e2bbc-49f7-45f6-9080-da6d3a8cc77d
title: 02. Planning in Markov Decision Process
created_time: 2023-06-27T11:34:00.000Z
last_edited_time: 2023-08-17T06:46:00.000Z
cover_image: https://www.notion.so/images/page-cover/gradients_11.jpg
하위 항목: []
subclass: RL Theory
class: RL
작성일시: 2023-06-27T11:34:00.000Z
pdf: https://wensun.github.io/CS6789_data_fall_2021/VI_and_PI_annotated.pdf
상위 항목: []
_thumbnail: https://www.notion.so/images/page-cover/gradients_11.jpg

---

> 💡 Given an MDP M = (S, A, P, r, γ), How to find stationary & deterministic function

> Bellman Operator \mathscr{T}

```undefined
(\mathscr{T}f)(s, a) := r(s,a) + \gamma \mathbb{E}_{s'+P(\cdot|s,a)\max_{a'\in A}f(s',a'),\forall s,a \in S \times A}
```

# Value Iteration

## Algorithm

*   Initialization: Q^0 = ||Q^0||\_\infty \in (0, \frac 1 {1-\gamma})

*   Iterate until convergence: Q^{t+1} = \mathscr{T}Q^t

## Convergence of Value Iteration

*   Lemma: Given any Q,Q', we have

    ```undefined
    ||\mathscr{T}Q - \mathscr{T}Q'||_\infty \le \gamma||Q-Q'||_\infty
    ```

    *   Proof: |\mathscr{T}Q(s,a)-\mathscr{T}Q'(s,a)| \le\gamma\max\_{s'}\max\_{a'}|(Q(s',a')-Q'(s',a')| = \gamma||Q-Q'||\_\infty

*   Convergence Lemma: Given Q^0, we have ||Q^t-Q^*||\_\infty\le\gamma^t||Q^0-Q^*||\_\infty

## Final Quality of the policy

Let \pi^t : \pi^t(s) = \arg\max\_a Q^t(s,a)

### Theorem

```undefined
V^{\pi^t}(s)\ge V^*(s)-\frac{2\gamma^t}{1-\gamma}||Q^0-Q^*||_\infty\forall s\in S
```

*   Proof

    ```undefined
    V^{\pi^t}(s) - V^*(s) = Q^{\pi^t}(s, \pi^t(s))-Q^*(s,\pi^*(s)) = Q^{\pi^t}(s, \pi^t(s))-Q^*(s,\pi^t(s))+Q^*(s,\pi^t(s))-Q^*(s,\pi^*(s)) = \gamma \mathbb{E}_{s'\sim P(s,\pi^t(s))}(V^{\pi^t}(s')-V^*(s')) + Q^*(s,\pi^t(s))-Q^*(s,\pi^*(s)) 
    ```

# Policy Iteration

## Algorithm

*   Initialization: \pi^0 = S \rightarrow A

*   Policy Evaluation: Q^{\pi^t}(s,a),\forall s,a

*   Policy Improvement: \pi^{t+1}(s) = \arg\max\_a Q^{\pi^t}(s,a), \forall s

## Analysis

### Lemma: Monotonic Improvement

```undefined
Q^{\pi^{t+1}}(s,a) \ge Q^{\pi^t}(s,a),\forall s,a
```

### Theorem: Convergence

```undefined
||V^{\pi^{t+1}}-V^*||_\infty \le \gamma ||V^{\pi^{t}}-V^*||_\infty
```

*   Proof: Apply Bellman operator!

# VI vs PI

*   VI: fixed point iteration(contraction map)

*   PI: argmax Q value(monotonic improvement)
