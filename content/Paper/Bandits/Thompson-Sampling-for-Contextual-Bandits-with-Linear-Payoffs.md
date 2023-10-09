---
id: aa5f7638-3ff7-4a35-b283-612dbab5a8aa
title: Thompson Sampling for Contextual Bandits with Linear Payoffs
created_time: 2023-03-20T11:04:00.000Z
last_edited_time: 2023-08-17T06:45:00.000Z
cover_image: https://www.notion.so/images/page-cover/solid_yellow.png
하위 항목: []
subclass: Bandits
class: Paper
작성일시: 2023-03-20T11:04:00.000Z
pdf: https://arxiv.org/pdf/1209.3352.pdf
상위 항목: []
_thumbnail: https://www.notion.so/images/page-cover/solid_yellow.png

---

# Introduction

### General Structure for Thompson Sampling

*   a set  \Theta  of parameters \tilde\mu

*   a prior distribution P(\tilde\mu) on these parameters

*   past observations D consisting for the past time msteps

*   a likelihood function P(r|b, \tilde\mu) which gives the probability of reward given a context b and parameter \tilde\mu

*   a posterior distribution P(\tilde\mu|D)\propto P(D|\tilde\mu)P(\tilde\mu) where P(D|\tilde\mu) is the likelihood function

### In Contextual Bandit

*   Then, this TS plays an arm according to its posterior probability of having the best parameter

*   In contextual bandit, we are going to provide regret bound of $\tilde O(d^{3/2}\sqrt T)$ or $\tilde{O}(d \sqrt{T\log(N)})$

## Problem setting and Algorithm Description

### Problem Setting

*   There are N arms, and a context vector b\_i(t)\in\mathbb{R}^d is revealed

*   History H\_{t-1} = { a(\tau), r\_{a(\tau)}(\tau),b\_i(\tau),i=1,\dots,N,\tau =1,\dots,t-1 }

*   Reward for arm i at time t is generated from distribution with mean b\_i(t)^\top\mu

*   An algorithm for contextuala bandit problem needs to choose, at every time t, an arm a(t) to play, and let  a^\*(t)=\mathrm{argmax}\_i b\_i(t)^\top\mu

*   Then Regret becomes difference between the optimal arm and of arm i at time t

    ```undefined
    \Delta_i(t) = b_{a^*(t)}(t)^\top\mu - b_i(t)^\top\mu
    ```

    ```undefined
    regret(t) = \Delta_{a(t)}(t)
    ```

*   We need to minimize total regret in time T

*   We assume that \eta\_{i,t} = r\_i(t)-b\_i(t)^\top\mu is conditionally R-sub-gaussian for a constant R\ge 0

    ```undefined
    \forall\lambda\in\reals,\Bbb{E}[e^{\lambda_{\eta_{i,t}}}|\{b_i(t)\}{i=1}^N, H{t-1}]\le\exp(\frac{\lambda^2R^2}{2})
    ```

### Thompson Sampling Algorithm

*   Suppose that the likelihood of reward r\_i(t) at time t, given context b\_i(t) and parameter \mu, were given by the pdf of Gaussian distribution N(b\_i(t)^\top\mu, v^2), v=R\sqrt{9d\ln(\frac T \delta)}

    ```undefined
    B(t) = I_d + \sum_{r=1}^{t-1}b_{a(\tau)}(\tau)b_{a(\tau)}(\tau)^\top
    \\
    \tilde{\mu}(t) = B(t)^{-1}(\sum_{r=1}^{t-1}b_{a(\tau)}(\tau)r_{a(\tau)}(\tau))
    ```

*   If **prior** for \mu at time t is given by N(\tilde{\mu}(t), v^2B(t)^{-1}), **posterior** distribution at t+1 is \Pr(\tilde{\mu}|r\_i(t))\propto\Pr(r\_i(t)|\tilde\mu)\Pr(\tilde\mu)

*   Algorithm: Thompson Sampling for Contextual Bandits

    ```plain text
    for all t= 1, 2, ... do
      Sample mu(t) from distribution N(mu(t), v^2B(t)^-1)
      Play arm a(t):= argmax_i b_i(t).T * mu(t) and observe the reward

    ```

### Our Results

### Theorem 1

With Probability $1-\delta$, the total regret for Thompson Sampling algorithm in time T is bounded as

```undefined
R(T) = O\left({d^{3/2} \sqrt{T} \left({ \ln(T) \sqrt{\ln(T)\ln(\frac 1 \delta)}}\right) }\right)
\\ \text{or}
R(T) = O\left({d \sqrt{T\log(N)} \left({ \ln(T) \sqrt{\ln(T)\ln(\frac 1 \delta)}}\right) }\right)
\\ \text{whichever is smaller, for any} 0<\delta<1
```

## Regret Analysis - Proof of Theorem 1

### Technical Outline

At any time step t, we divide the arms into two groups

*   *saturated arms* defined as those with \delta\_i(t)>g\_ts\_i(t)

*   *unsaturated arms* defined as those with \delta\_i(t)\le g\_ts\_i(t)

where s\_i(t) = \sqrt{b\_i(t)^\top B(t)^{-1}b\_i(t)}

We use concentration bounds for \tilde\mu(t) and \hat\mu(t) to bound the regret

### Formal Proof
