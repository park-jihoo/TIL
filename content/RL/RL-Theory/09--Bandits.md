---
id: 783ec591-b247-4719-9b6c-fd83f3d7b812
title: 09. Bandits
created_time: 2023-07-05T05:41:00.000Z
last_edited_time: 2023-08-17T06:46:00.000Z
cover_image: https://www.notion.so/images/page-cover/webb2.jpg
하위 항목: []
subclass: RL Theory
class: RL
작성일시: 2023-07-05T05:41:00.000Z
pdf:
  - https://wensun.github.io/CS6789_data_fall_2021/MAB_annoated.pdf
  - https://wensun.github.io/CS6789_data_fall_2021/linUCB_annotated.pdf
상위 항목: []
_thumbnail: https://www.notion.so/images/page-cover/webb2.jpg

---

> 💡 Exploration in very simple MDP, which is called Multi-Armed Bandit

# Introduction

## Setting

*   We have K many arms a\_1,\dots,a\_K

*   Each arm has a unknown reward distribution \nu\_i \in \Delta(\[0,1]) with mean \mu\_i = \mathbb{E}\_{r\sim\nu\_i}\[r]

## Algorithm

```python
for t in range(T-1):
	pull arm
	observes an iid reward of arm
```

## Learning Objective: Regret

```undefined
\text{Regret}_T = T\mu^* - \sum_{t=0}^{T-1}\mu I_t
```

# Greedy Algorithm

*   Try each arm once, and then commit to the one that has the **highest observed** reward

*   A bad arm may generate a high reward by chance!

# Explore and Commit

*   Pull arm-k N times and observe r for each attempt, then calculate arm k;s empirical mean \mu\_k = \sum\_{i=1}^N r\_i/N (Exploration phase)

*   Then for t = NK to T - 1, pull the best empirical arm, I\_t = \arg\max\_{i\in\[K]}\hat\mu\_i

## Tools to calculate

*   Hoeffding inequality

    *   Given a distribution \mu \in \Delta(\[0,1]) and N i.i.d samples with probability at least1-\delta, we have

        ```undefined
        \left|\sum_{i=1}^N r_i/N-\mu \right| \le O \left(\sqrt{\frac{\ln(1/\delta)}N} \right)
        ```

    *   This gives us a confidence interval!

*   After the Exploration phase, with probability at least 1-\delta, \forall k\in\[K], we have

    ```undefined
    |\hat\mu_k -\mu_k| \le O \left(\sqrt{\frac{\ln(K/\delta)}{N}} \right)
    ```

*   Regrets

    *   Exploration phase: \text{Regret} \le N(K-1) \le NK

    *   Exploitation phase: \text{Regret} \le (T-NK)(\mu\_{i^\*}-\mu\_{\hat{I}})\le 2T \sqrt{\frac{\ln(K/\delta)}N}

    *   Final regret bound is NK + 2T\sqrt{\frac{\ln(K/\delta)}{N}}

    *   Minimize the upper bound via optimizing N = \left(\frac{T\sqrt{\ln(K/\delta)}}{2K} \right)^{2/3}, we have  \text{regret}\_T \le O(T^{2/3}K^{1/3} \cdot \ln^{1/3}(K/\delta)

# Upper Confidence Bound(UCB)

*   We can show that for all iteration t, we have \forall k \in \[K] with probability 1-\delta,

    ```undefined
    |\hat\mu_k(i)-\mu_k|\le\sqrt{\frac{\ln(KT/\delta)}{N_t(k)}}
    ```

*   Given the confidence interval, we can pick arm which has the **highest upper confidence bound**

    ```undefined
    I_t = \arg\max_{i\in[K]} \left(\hat\mu_t(i)+\sqrt{\frac{\ln(KT/\delta)}{N_t(i)}} \right)
    ```

*   Regret: With high probability, UCB’s regret os \widetilde{O}(\sqrt{KT})

## Exploration-exploitation tradeoff

*   I\_t has large confidence interval, which means that has high uncertainty → exploration

*   I\_t has small confidence interval, then it is simply a good arm → exploitation

    ```undefined
    \text{Regret}_T = \sum_{t=0}^{T-1}(\mu^*-\mu_{I_t}) \le \sum_{t=0}^{T-1}2\sqrt{\frac{\ln(TK/\delta)}{N_t(I_t)}} \le 2\sqrt{\ln(TK/\delta)}\cdot\sum_{t=0}^{T-1}\sqrt{\frac 1 {N_t(I_t)}}
    ```

# Linear Bandits

## Setting

### Handling Large Action Spaces

*   On each round, we must choose **decision** **x\_t \in D \subset \R^d**

*   Obtain a reward r\_t \in \[-1, 1], where

    ```undefined
    \mathbb{E}[r_t|x_t=x] = \mu^*\cdot x \in[-1,1]
    ```

*   Also, we have the noise sequence \eta\_t = r\_t - \mu^\*\cdot x\_t is iid noise model

### Objective

If x\_0, ...,x\_{T-1} are our decisions, then our cumulative regret is

```undefined
R_T = T\mu^*\cdot x^* - \sum_{t=0}^{T-1}\mu^*\cdot x^*
```

where x^*\in D is an optimial decision for \mu^*, i.e x^\* \in \arg\max\_{x\in D} \mu^\* x

## LinUCB

*   The confidence ball: define our uncertainty region \text{BALL}\_t with center, \hat\mu\_t, and shape, \Sigma\_t, using the \lambda-regularized least squares solution

    ```undefined
    \hat\mu_t = \arg\min_\mu\sum_{\tau=0}^{t-1}||\mu\cdot x_\tau-r_\tau||_2^2 + \lambda ||\mu\\_2^2 = \Sigma_t^{-1}\sum_{\tau=0}^{t-1}r_\tau x_\tau
    ```

    ```undefined
    \Sigma_t = \lambda I + \sum_{\tau=0}^{t-1}x_\tau x_\tau^\top, \text{ with }  \Sigma_0 = \lambda I
    ```

    *   Define the uncertainty region

        ```undefined
        \text{BALL}_t = \left\{\mu| (\hat\mu_t-\mu)^\top \Sigma_t(\hat\mu_t-\mu)\le\beta_t  \right\}
        ```

*   Algorithm

    ```python
    def LinUCB(lam, beta_t):
    	for t in range(T):
    		x[t] = argmax(max(mu dot x))
    		observe reward r_t
    		update ball[t+1]
    ```

*   Regret Bound: R\_t \le O^\*(d\sqrt{T})

    *   Theorem: Suppose bounded noise |\eta\_t|\le\sigma, that ||\mu^\*||\le W, and that ||x|| \le B for all x \in D. Set \lambda = \sigma^2/W^2 and

        ```undefined
        \beta_t := \sigma^2\left(2+4d\log\left(1+\frac{tB^2W^2}{d}\right) + 8\log\left(\frac 4 \delta\right) \right)
        ```

        With probability greater than 1-\delta, for all T \ge 0,

        ```undefined
        R_T \le c_\sigma\sqrt{T}\left( d\log \left( 1 + \frac{TB^2W^2}{d\sigma^2} \right) + \log(4/\delta)\right)
        ```

# Analysis

*   Let \delta > 0, we have that \Pr(\forall t, \mu^\*\in\text{BALL}\_t)\ge1-\delta

*   Sum of squares regret bound: define \text{regret}\_t = \mu^*\cdot x^* - \mu^\* \cdot x\_t

    Suppose ||x||\le B  for x \in D, Suppose \beta\_t is increasing, and \mu^\* \in \text{BALL}\_t, \forall t

          ```undefined
          \sum_{t=0}^{T-1}\text{regret}_t^2 \le 4\beta_T d\log\left(1 + \frac{TB^2}{d\lambda} \right)
          ```

## Regret Analysis

*   Width of confidence ball: |(\mu - \hat\mu\_t)^\top x|\le\sqrt{\beta\_t x^\top\sum\_t^{-1}x}

*   Define w\_t := \sqrt{x\_t^\top \Sigma\_t^{-1}x\_t} which is the normalized width at time t, then

    ```undefined
    \text{regret}_t \le 2\min(\sqrt{\beta_t}w_t,1)\le 2\sqrt{\beta_T}\min(w_t,1)
    ```
