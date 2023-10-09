---
id: eb1aea3b-840e-4bb6-bbe8-40115454d5ff
title: 12. Learning in Large Scale MDPs(Bellman Rank)
created_time: 2023-07-13T12:52:00.000Z
last_edited_time: 2023-08-17T06:46:00.000Z
cover_image: https://www.notion.so/images/page-cover/rijksmuseum_claesz_1628.jpg
하위 항목: []
subclass: RL Theory
class: RL
작성일시: 2023-07-13T12:52:00.000Z
pdf:
  - >-
    https://wensun.github.io/CS6789_data_fall_2021/Bellman_rank_part_1_annotated.pdf
  - https://wensun.github.io/CS6789_data_fall_2021/Bellman_rank_2_annotated.pdf
상위 항목: []
_thumbnail: https://www.notion.so/images/page-cover/rijksmuseum_claesz_1628.jpg

---

> 💡 1. We have seen tabular MDP and linear MDP, is there a **more general framework** that captures these two, and potentially many more, where efficient learning is possible?

> 💡 2. Can we design a universal algorithm that learns efficiently for MDPs with low Q/V bellman rank?

# Bellman rank Definitions

## Setting

*   Finite horizon episodic MDP \left{ {S\_h}*{h=0}^H, {A\_h}*{h=0}^{H-1}, H, s\_0, r, P \right}, and state space S\_h is extremely large

*   Policy class \Pi = \left{\pi:\pi(s)=\arg\max\_{a\in A}f(s,a),\forall s\in S|f \in \mathscr{F} \right}

*   Value function class \mathscr{V} = \left{V\_f: V\_f(s)=\max\_a f(s,a)|f\in\mathscr{F} \right}

## Learning Goal

> Given approximation error \epsilon and failure probability \delta, can we learn \epsilon near optimal policy in # samples scaling poly with all relevant parameters(Here, we need poly in \mathscr{\ln(|F|)})

## Definitions

*   Average Bellman error of Q-estimate g

    ```undefined
    \mathscr{E}(g;f,h) = \mathbb{E}_{s_h,a_h\sim d_h^{\pi_f}}\left[g(s_h, a_h)-r(s_h,a_h)-\mathbb{E}_{s_{h+1}\sim P(\cdot|s_h,a_h)}\left[\max_{\mathscr{a\in A}}g(s_{h+1},a) \right] \right]
    ```

*   Average Bellman error w\.r.t the V function induced by g

    ```undefined
    \mathscr{E}(g;f,h) = \mathbb{E}_{s_h,a_h\sim d_h^{\pi_f}}\left[V_g(s_h)-r(s_h,\pi_g(s_h))-\mathbb{E}_{s_{h+1}\sim P(\cdot|s_h,a_h)}\left[V_g(s_{h+1})\right] \right]
    ```

*   Any g such that \mathscr{E}(g;\pi,h) \not=0, is an incorrect Q^\* approximator

*   The Q/V-Bellman Rank

    *   In other words, there are two mappings W\_h : \mathscr{F}\rightarrow\R^d, \ X\_h:\mathscr{F}\rightarrow\R^d(d = Bellman rank) such that

        ```undefined
        \forall f,g\in\mathscr{F : E}(g;f,h) = \langle W_h(g),X_h(f)\rangle
        ```

# Examples that are captured by bellman rank framework

## The Linear Bellman Completion Model

*   Given feature \phi, take any linear function \theta^\top\phi(s,a)

    ```undefined
    \forall h,\exist w\in\R^d,s.t.,w^\top\phi(s,a) = r(s,a)+\mathbb{E}_{s'\sim P_h(s,a)}\max_{a'}\theta^\top\phi(s,a),\forall s,a
    ```

*   Claim: It has Q-bellman rank d

    \mathscr{E}(g;f,h) = \langle \theta- \mathscr{T}*h(\theta), \mathbb{E}*{s\_h,a\_h\sim d\_h^{\pi\_f}}\[\phi(s\_h, a\_h)] \rangle

## The Linear Q^*, V^* model

*   Assume Q^*(s,a) = (w^*)^\top\phi(s,a), V^*(s) = (\theta^*)^\top\psi(s), \forall s, a

*   Claim: It has Q-Bellman-rank 2d

    ```undefined
    \mathscr{F}_h = \left\{(w, \theta) : \max_a w^\top \phi(s,a) = \theta^\top\psi(s),\forall s \right\}
    ```

    ```undefined
    \mathscr{E}(g;f,h) = \left\langle \begin{bmatrix}w-w^* \\ \theta - \theta^* \end{bmatrix}, \mathbb{E}_{s_h, a_h \sim d_h^{\pi^f}}\begin{bmatrix} \phi(s_h, a_h) \\ -\mathbb{E}_{s'\sim P_h(s_h,a_H)}[\psi(s')] \end{bmatrix}\right\rangle
    ```

## Q^\*-state abstraction

*   We have a small latent space Z, and a known mapping \xi from state s to z

    ```undefined
    Q^*(s_1, a) = Q^*(s_2, a), \forall a, \text{if } \xi(s_1)=\xi(s_2)
    ```

*   Claim: this model has Q-Bellman rank |Z||A|+|Z|

    *   We can show that this model is captured by linear Q^\* & V^\*

    *   \phi(s,a)\in\R^{|Z||A|}, \psi(s) \in\R^{|Z|}

## Low-rank MDP

*   P\_h(s'|s,a) = \mu\_h^*(s')^\top\phi\_h^*(s,a)

*   Claim: this model has V-bellman rank d

    ```undefined
    \mathscr{F}_h = \{ \theta^\top\phi(\cdot,\cdot):\|\theta\|_2\le W, \phi\in\Phi\}
    ```

    ```undefined
    \mathscr{E}(g;f,h) = \left\langle \int_{s_h} \nu_{h-1}^*(s_h)\left[V_g(s_h) - r(s,\pi_g(s_h)) - \mathbb{E}_{s_{h+1}\sim P_h(\cdot|s_h,\pi_g(s_h))}[V_g(s_{h+1})]\right]d(s_h), \ \mathbb{E}_{\bar s , \bar a, \sim d_{h-1}^{\pi_f}}[\phi_{h-1}^*(\bar s, \bar a)]\right\rangle
    ```

## Latent variable MDP

*   Latent variable MDP is captured by low-rank MDP, so it has small bellman rank

    ```undefined
    \text{Given }s,a: z\sim\phi^*(s,a), s'\sim\nu^*(z)
    ```

*   V-bellman rank = Number of latent states

# The Bilinear-UCB algorithm

## Two rank cases

### For Q-Bellman rank case

*   Bellman error loss \ell(s\_h, a\_h, s\_{h+1}', g) = g(s\_h,a\_h)-r(s\_h,a\_h)-\max\_{a'}g(s\_{h+1},a')

*   If we had a dataset \mathscr{D}:={s\_h,a\_h,s\_{h+1}} where s\_h, a\_h \sim d\_h^{\pi\_f}, s\_{h+1}\sim P\_h(\cdot|s\_h,a\_h)

    ```undefined
    \forall g : \mathbb{E}_\mathscr{D}[\ell(s_h,a_h,s_{h+1},g)] \text{ is an unbiased set of } \mathscr{E}(g;f,h)
    ```

### For V-Bellman rank case

*   Bellman error loss

    ```undefined
    \frac{\bold{1}\{a_h = \pi_g(s_h)\}}{1/A}\left(g(s_h, a_h) - r(s_h,a_h) - \max_{a'}g(s_{h+1},a') \right)
    ```

*   If we had a dataset \mathscr{D}:={s\_h,a\_h,s\_{h+1}} where s\_h, a\_h \sim U(\mathscr{A}),s\_{h+1}\sim P\_h(\cdot|s\_h,a\_h)

    ```undefined
    \forall g : \mathbb{E}_\mathscr{D}[\ell(s_h,a_h,s_{h+1},g)] \text{ is an unbiased set of } \mathscr{E}(g;f,h)
    ```

## Algorithm

*   At iteration t:

    *   Select f\_t = \arg\max\_{g\in\mathscr{F}}V\_g(s\_0) s. t. \forall h:\sum\_{i=0}^{h-1}\left(\mathbb{E}*{\mathscr{D}*{h,i}}\[\ell(s\_h,a\_h,s\_{h+1},g)] \right)^2 \le R^2

    *   For all h, create \mathscr{D}*{h,t}={s\_h,a\_h,s*{h+1}} with m triples, where

        *   For Q Bellman rank case: s\_h, a\_h \sim d\_h^{\pi\_f}, s\_{h+1}\sim P\_h(\cdot|s\_h,a\_h)

        *   For V Bellman Rank case: s\_h\sim d\_h^{\pi\_f}, a\_h \sim U(A), s\_{h+1}\sim P\_h(\cdot|s\_h,a\_h)

### Intuition behind the algorithm

*   When the batch size is large, \mathbb{E}*{\mathscr{D}*{h,i}}\ell(s\_h,a\_h,s\_{h+1},g)\rightarrow\mathscr{E}(g;f\_i,h)

*   We know that \sum\_{i=1}^{t-1}\mathscr{E}(f^\*;f\_i,h)=0

*   By properly setting batch size and R, we eliminate wrong hypothesis, but keep f^\*

*   This gives optimism: V\_{f\_t}(s\_0)\ge V\_{f^*}(s\_0):=V^*(s\_0)

# Theoretical Guarantee and analysis in BLin-UCB

*   Given any distribution \nu \in \Delta(S\times A\times S) and m i.i.d samples {s\_i,a\_i,s\_i'} from \nu, with probability at least 1-\delta,

    ```undefined
    \forall g: \left|\mathbb{E}_\nu\ell(s,a,s',g) - \mathbb{E}_\mathscr{D}\ell(s,a,s',g) \right| \le \varepsilon_{gen}(m, \mathscr{F}, \delta)
    ```

*   After running BLin-UCB for T=\widetilde O(Hd) many iterations, there exists a policy among T many policies, such that

    ```undefined
    V^*(s_0) - V^\pi(s_0)\le\widetilde O\left(\varepsilon_{gen}(m, \mathscr{F}, \delta/TH)\cdot\sqrt{dH^3}\right)
    ```

*   With probability 1-\delta, BLin-UCB learns a policy with V^\*-V^\pi\le\epsilon, with number of trajectories:

    ```undefined
    \widetilde O\left(\frac{H^6d^2\ln(|\mathscr{F}|/\delta)}{\epsilon^2}\right)
    ```
