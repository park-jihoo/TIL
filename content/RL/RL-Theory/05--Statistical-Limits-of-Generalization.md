---
id: 0999f57b-d672-401a-8451-f31a0ab6f074
title: 05. Statistical Limits of Generalization
created_time: 2023-06-30T13:03:00.000Z
last_edited_time: 2023-08-17T06:46:00.000Z
cover_image: https://www.notion.so/images/page-cover/nasa_robert_stewart_spacewalk.jpg
하위 항목: []
subclass: RL Theory
class: RL
작성일시: 2023-06-30T13:03:00.000Z
pdf:
  - >-
    https://wensun.github.io/CS6789_data_fall_2021/Generalization_1_annotated.pdf
  - >-
    https://wensun.github.io/CS6789_data_fall_2021/Generalization_2_annotated.pdf
상위 항목: []
_thumbnail: https://www.notion.so/images/page-cover/nasa_robert_stewart_spacewalk.jpg

---

> 💡 To what extent is generalization in RL similar to(or different from) that in supervised learning?

# Reinforcement Learning vs Supervised Learning

|                   | Supervised Learning                                          | Reinforcement Learning                                                                           |
| ----------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| Agnostic Learning | Try to do as well best classifier in some restricted class H | Can we find the best policy in some (restricted) class Π                                         |
| Linear            | Learn the best linear regressor or binary classifier         | If the optimal value or policy is parameterized with a linear model, can we learn fewer samples? |

# Occams Razor and Generalization

Suppose \mathcal{H} is finite. Let \hat h = \arg\min\_{h\in\mathcal{H}}\hat{err}(h) and h^\* = \arg\min\_{h\in\mathcal{H}} \text{err}(h). With probability at least 1 - δ

    ```undefined
    \text{err}(\hat h) - \text{err}(h^*) \le \sqrt{\frac 2 N \log \frac{2|\cal{H}|}{\delta}}
    ```

# RL and Generalization

## Finite Horizon MDPs

*   Finite horizon, time-dependent Markov Decision Process M = (\mathcal{S}, \mathcal{A}, {P}\_h, {r}\_h, H, \mu)is specified as follows

    *   A integer H which defines the horizon of the problem.

    *   A time-dependent transition function: for h \in H, P\_h: \mathcal{S \times A \rightarrow \Delta (S)}

    *   A time-dependent reward function: for h \in H, r\_h: \mathcal{S \times A} \rightarrow \[0,1]

*   Goal: \arg\max\_\pi E\_{s\_0\sim\mu}V^\pi(s\_0) where V^\pi(s\_0) = \mathbb{E}\left\[\sum\_{t=0}^{H-1} r\_h(s\_t, a\_t)|\pi,s\_0 \right]

## Bellman equations

Define Q\_h^*(s,a) = \sup\_{\pi\in\Pi}Q\_h^\pi(s,a). Suppose that Q\_H=0 and we have that Q\_h = Q^*\_h, \forall h \in H if and only if for all h \in H,

```undefined
Q_h(s,a) = r_h(s,a) + \gamma\mathbb{E}_{s'\sim P_h(\cdot|s,a)}\left[ \max_{a' \in \mathcal{A}}Q_{h+1}(s',a') \right]
```

Furthermore, \pi(s,h) = \arg\max\_{a \in \mathcal{A}} Q\_h^\*(s,a) is an optimal policy

## RL and Agnostic Learning

*   In agnostic learning, we have to optimize \max\_{\pi\in\Pi}V^\pi(s\_0) and we ant to solve this with small numbers of sample trajectories

*   Assume sampling access to the MDP in a <u>μ-reset model</u>

    *   start at a state s\_0 \sim \mu

    *   we can rollout a policy \pi of our choosing

    *   we can terminate the trajectory at will

*   Importance Sampling

    *   Lemma: For any deterministic policy π,

        ```undefined
        V_0^\pi(s_0) = |\mathcal{A}|^H\mathbb{E}_{a_{0:H-1}\sim Unif_{\mathcal{A}}}\left[ 1(\pi(s_0) = a_0, \dots, \pi(s_H)=a_H)\sum_{t=0}^{H-1}r(s_t,a_t)|s_0\right]
        ```

    *   Consider the following empirical estimator of any π

        ```undefined
        \hat V^\pi(s_0) = \frac {|\mathcal{A}|^H}N \sum^N_{n=1} 1(\pi(s_0^n)=a_0^n,\dots,\pi(s_{H-1}^n)=a_{H-1}^n\sum_{t=0}^{H-1}r(s_t^n,a_t^n)
        ```

    *   Generalization in RL: Suppose Π is infinite and let \hat\pi = \arg\max\_{\pi\in\Pi} \hat V^\pi(s\_0), with probability at least 1-δ,

        ```undefined
        V^{\hat\pi}(s_0) \ge \arg\max_{\pi\in\Pi}V^\pi(s_0) - H|\mathcal{A}|^H\sqrt{\frac 2 N \log \frac {2|\Pi|}{\delta}}
        ```

    *   However, for an agnostic samplex complexity, no dependence on S or poly H dependence is not possible

*   An Easy lower Bound: Suppose \mathcal{A} has access to a generative model. There exists a policy class Π, with |Π| = |\mathcal{A}|^H such that if \mathcal{A} returns a policy \pi where

    ```undefined
    V_0^\pi(\mu)\ge \arg\max_{\pi\in\Pi}V_0^\pi(\mu)-0.5
    ```

    with probability greater than 1/2, then \mathcal{A} use a number of samples

    ```undefined
    N \ge c|\mathcal{A}|^H
    ```

# Linear relizability

## RL with Linearly Relizable Q\*-function Approximation

*   Suppose we have feature map \overrightarrow{\phi}(s,a)\in R^d

*   (A1) Assume for all s,a,h\in\[H], there exists w\_1^*, \dots, w\_H^*\in R^d s.t

    ```undefined
    Q_h^*(s,a) = w_h \cdot\phi(s,a)
    ```

*   (A2)For all a \not= \pi^\*(s),

    ```undefined
    V_h^*(s) - Q_h^*(s,a) \ge \text{constant}
    ```

## Linear Relizability is not Sufficient for RL

*   There exists an MDP and \phi satisfying A1 s.t any online RL algorithm requires \Omega(\min(2^d,2^H)) samples to output the value V^\*(s\_0) up to constant additive error with probability ≥ 0.9

*   Let’s make problem even easier, where we also assume A2 then the lower bound also holds even with both A1 and A2

# How should we approach generalization in RL?

*   Structural Assumption

*   Distribution Dependent Results

*   Imitation learning and behavior cloning
