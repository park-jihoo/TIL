---
id: 9af15e7d-d542-4297-ad0d-ee8bb29faf55
title: 01. Introduction and Basics of Markov Decision Process
created_time: 2023-06-27T06:34:00.000Z
last_edited_time: 2023-08-17T06:46:00.000Z
cover_image: https://www.notion.so/images/page-cover/gradients_11.jpg
하위 항목: []
subclass: RL Theory
class: RL
작성일시: 2023-06-27T06:34:00.000Z
pdf: https://wensun.github.io/CS6789_data_fall_2021/basics_MDP_annotated.pdf
상위 항목: []
_thumbnail: https://www.notion.so/images/page-cover/gradients_11.jpg

---

# Definition of Infinite horizon discounted MDPs

## Markov Decision Process

*   Policy: determine action based on state

    ```undefined
    a \sim \pi(s)
    ```

*   Send reward and next state form a Markovian transition dynaimcs

    ```undefined
    r(s,a),s' = P(\cdot |s,a)
    ```

## Infinite Horizon Discounted MDP

*   Policy \pi : S \rightarrow \Delta(A)

*   Value Function V^\pi(s) = \textbf{E} \left\[ \sum\_{h=0}^{\infty} \gamma^hr(s\_h, a\_h)|s\_0=s, a\_h \sim \pi(s\_h), s\_{h+1} \sim P(\cdot |s\_h,a\_h) \right]

*   Q function Q^\pi(s,a) = \textbf{E} \left\[ \sum\_{h=0}^{\infty} \gamma^hr(s\_h, a\_h)|(s\_0, a\_0)=(s,a), a\_h \sim \pi(s\_h), s\_{h+1} \sim P(\cdot |s\_h,a\_h) \right]

## Bellman Equation

*   Value Function

    ```undefined
    V^\pi(s) = \textbf{E}_{a\sim \pi(s)} \left[ r(s,a) + \gamma \textbf{E}_{s' \sim P(\cdot|s,a)}V^\pi(s') \right]
    ```

*   Q function

    ```undefined
    Q^\pi(s, a) = r(s,a) + \gamma \textbf{E}_{s' \sim P(\cdot|s,a)}V^\pi(s')
    ```

# Bellman Optimality

## Optimal Policy

*   For infinite horizon discounted MDP, there exists a deterministic stationary policy

    ```undefined
    \pi^* = S \rightarrow A, V^{\pi^*}(s) \ge V^\pi(s) , \forall s, \pi
    ```

### Bellman Optimality

```undefined
V^*(s) = \max_a \left[ r(s,a) +  \gamma \textbf{E}_{s' \sim P(\cdot|s,a)}V^*(s') \right]
```

*   Let \hat\pi(s) := \arg\max\_a Q^*(s,a), then we will prove V^{\hat\pi}(s) = V^*(s), \forall s

*   This implies that \arg\max\_a Q^\*(s,a) is an optimal policy

### Theorem 2

```undefined
\text{For any }V : S \rightarrow \R, \text{if } V(s) = \max_a \left[r(s,a) + \gamma \textbf{E}_{s'\sim P(\cdot|s,a)}V(s')\right] \text{ for all }s, \text{then } V(s) = V^*(s),\forall s 
```

*   Proof: Calculate |V(s) - V^\*(s)|

# State-action distribution

## Trajectory distribution and state-action distribution

*   What is the probability of \pi generating trajectory \tau = {s\_0, a\_0, s\_1, \dots, s\_h,a\_h}?

    ```undefined
    \mathbb{P}^\pi(s_0,a_0,\dots,s_h,a_h) = \pi(a_0|s_0)P(s_1|s_0,a_0)\pi(a_1|s_1)P(s_2|s_1,a_2)\dots P(s_h|s_{h-1},a_{h-1})\pi(a_h|s_h)
    ```

*   What is the probability of \pi visiting state (s, a) at time step h?

    ```undefined
    \mathbb{P}^\pi_h (s,a;s_0)= \sum_{a_0,s_1, a_1,\dots,s_{h-1},a_{h-1}}\mathbb{P}^\pi(s_0,a_0,\dots,s_{h-1},a_{h-1},s_h=s,a_h=a)
    ```

## State action occupancy measure

*   \mathbb{P}\_h(s,a;s\_0,\pi): probability of \pi visiting (s,a) at time step h \in \N, starting at s\_0

    ```undefined
    d_{s_0}^\pi(s,a) = (1-\gamma) \sum_{h=0}^\infty \gamma^h \mathbb{P}_h(s,a;s_0,\pi) \\ V_{s_0}^\pi(s_0) = \frac 1 {1-\gamma} \sum_{s,a} d_{s_0}^\pi(s,a)r(s,a)
    ```
