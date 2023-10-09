---
id: 10c72b1b-2945-424d-a417-1a50500ce580
title: 03. Computational Complexity & The LP-formulation
created_time: 2023-06-28T12:21:00.000Z
last_edited_time: 2023-08-17T06:46:00.000Z
cover_image: https://www.notion.so/images/page-cover/met_paul_signac.jpg
하위 항목: []
subclass: RL Theory
class: RL
작성일시: 2023-06-28T12:21:00.000Z
pdf: https://wensun.github.io/CS6789_data_fall_2021/comp_limits_annotated.pdf
상위 항목: []
_thumbnail: https://www.notion.so/images/page-cover/met_paul_signac.jpg

---

> 💡 Given an MDP, can we exactly compute Q^\* in polynomial time?

# Polynomial time & Polynomial Complexity

*   Polytime computation: Suppose that (P, r, \gamma) in our MDP \mathscr{M} is specified with rational entries, where L(P, r, \gamma)is total bit-size required to specity (P, r, \gamma). Can we exactyy compute Q^\* in time \text{poly}(S, A, L(P, r, \gamma))?

*   Strongly polynomial time: Suppose (P,r) is specified with real numbers. Can we compute Q^\* in \text{poly}(S,A,\log(1/(1-\gamma)), with no dependence on L(P, r, \gamma)

## In Value Iteration

*   When the sub-optimality gap between Q^t and Q^\* is less than 2^{-L(P, r, \gamma)}, then the greedy policy will be optimal

*   For an ε-accurate solution, O(\log(1/(\epsilon(1-\gamma))/(1-\gamma)) iterations suffice

*   Value Iteration is poly with O(S^2A \cdot \frac {L(P,r,\gamma)\log(1/(1-\gamma))}{1-\gamma}) complexity for fixed γ

*   But not **strongly poly**

## In Policy Iteration

*   Policy iteration per iteration complexity S^3 + S^2A, so it is more costly than Value Iteration

*   Policy Runtime is O \left( (S^3+S^2A)\frac{L(P,r,\gamma)\log(1/(1-\gamma))}{1-\gamma} \right) for fixed γ

*   After A^S iteration, policy iteration compute an optimal policy in time independent of L(P, r, \gamma)

*   For fixed γ, policy iteration is strongly polynomial. It halts after \frac {S^2A\log(S^2/(1-\gamma))}{1-\gamma} iteration

# The Primal Linear Program

*   Let’s write the bellman equations with values

    ```undefined
    V(s) = \max_a \left\{ r(s,a) + \gamma \mathbb{E}_{s'\sim P(\cdot|s,a)}[V(s)] \right\}
    ```

*   With variables V \in \R ^S, the LP is \min V(s\_0) such that

    ```undefined
    V(s) \ge r(s,a)+\gamma\mathbb{E}_{s'\sim P(\cdot|s,a)}V(s')\ \  \forall s,a \in S \times A
    ```

*   This LP solver gives poly time algorithm S^3AL(P, r, \gamma)

*   In strongly-poly, S^4A^4\log(\frac S{1-\gamma}), so only logarithmic in 1-\gamma

## Dual LP → State-action polytope

*   For a fixed policy π, define the state-action visitation distribution \nu^\pias

    ```undefined
    \nu^\pi(s,a) = (1-\gamma)\sum_{t=0}^\infty \gamma^t\Pr^\pi(s_t=s, a_t=a|s_0)
    ```

*   Then for all states,

    ```undefined
    \sum_a \nu^\pi(s,a) = (1-\gamma)I(s=s_0)+\gamma\sum_{s',a'}P(s|s',a')\nu^\pi(s',a')
    ```

*   Define state-action polytotype K as

    ```undefined
    K := \left\{\nu |\nu\ge0 \text{ and }\sum_a\nu(s,a) = (1-\gamma)I(s=s_0)+\gamma \sum_{s',a'}P(s|s',a')\nu(s',a') \right\}
    ```

*   Lemma: \nu\in K if and only if ther exists a (possibly randomized) policy π s.t \nu^\pi=\nu
