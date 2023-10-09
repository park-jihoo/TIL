---
id: 33f8546f-03c1-4abc-9e74-bacce6e0a87e
title: 13. Policy Gradient and convergence
created_time: 2023-07-17T06:26:00.000Z
last_edited_time: 2023-08-17T06:46:00.000Z
cover_image: https://www.notion.so/images/page-cover/woodcuts_8.jpg
하위 항목: []
subclass: RL Theory
class: RL
작성일시: 2023-07-17T06:26:00.000Z
pdf: https://wensun.github.io/CS6789_data_fall_2021/Policy_gradient_annotated.pdf
상위 항목: []
_thumbnail: https://www.notion.so/images/page-cover/woodcuts_8.jpg

---

> 💡 How to compute the gradient of policy?

# Two formation of Policy Gradient

## Examples of Policy Parametrization

*   Softmax policy for Tabluar MDPs: \theta\_{s,a}\in\R, \forall s,a \in S\times A

    ```undefined
    \pi_\theta(a|s) = \frac{\exp(\theta_{s,a})}{\sum_{a'}\exp(\theta_{s,a'})}
    ```

*   Softmax linear policy: Feature vector \phi(s,a)\in\R^d and parameter \theta\in\R^d

    ```undefined
    \pi_\theta(a|s) = \frac{\exp(\theta^\top\phi(s,a))}{\sum_{a'}\exp(\theta^\top\phi(s,a'))}
    ```

*   Neural Policy: Neural lnetwork f\_\theta:S\times A\rightarrow\R

    ```undefined
    \pi_\theta(a|s)=\frac{\exp(f_\theta(s,a))}{\sum_{a'}\exp(f_\theta(s,a'))}
    ```

## Warm up

J(\theta) = \mathbb{E}*{x\sim P*\theta}\[f(x)], then \nabla\_\theta J(\theta)|*{\theta=\theta\_0}=\mathbb{E}*{x\sim P\_{\theta\_0}}\nabla\_\theta\ln P\_{\theta\_0}(x)f(x)

## Derivation of Policy Gradient: REINFORCE

*   Assume: \tau = {s\_0,a\_0,s\_1,a\_1,...}, \rho\_\theta(t) =\rho(s\_0)\pi\_\theta(a\_0|s\_0)P(s\_1|s\_0,a\_0)\pi\_\theta(a\_1|s\_1)..., J(\pi\_\theta) = \mathbb{E}*{\tau\sim\rho*\theta(\tau)}\left\[\sum\_{h=0}^\infty \gamma^hr(s\_h,a\_h) \right]

    ```undefined
    \nabla_\theta J(\pi_\theta) = \mathbb{E}_{\tau\sim\rho_\theta(\tau)}\left[\left(\sum_{h=0}^{\infty}\nabla_\theta\ln\pi_\theta(a_h|s_h)\right)R(\tau)\right]
    ```

## Derivation of Policy Gradient with Q^\pi

*   Recall definition of value function V^{\pi\_\theta}(s)

    ```undefined
    \begin{aligned}\nabla_\theta J(\pi_\theta) &= \nabla_\theta\mathbb{E}_{s_0\sim \rho}\left[V^{\pi_\theta}(s_0) \right]\\&=\nabla_\theta\mathbb{E}_{s_0\sim \rho}\left[\nabla_\theta\mathbb{E}_{a_0\sim \pi_\theta(s_0)}Q^{\pi_\theta}(s_0, a_0) \right]\\&=\frac 1{1-\gamma}\mathbb{E}_{s,a\sim d^{\pi_\theta}}\nabla_\theta\ln\pi_\theta(a|s)Q^{\pi_\theta}(s,a)\end{aligned}
    ```

*   Derivation of unbiased stochastic policy gradient: roll in \pi\_\theta to generate s\_h, a\_h \sim \mathbb{P}*h^{\pi*\theta}

    *   Terminate with probability 1-\gamma, \widetilde Q^{\pi\_\theta}(s\_h,a\_h) = \sum\_{\tau=h}^{t\ge h}r\_\tau

    *   Unbiased estimate \nabla\_\theta\ln\pi\_\theta(a\_h|s\_h)\widetilde Q^{\pi\_\theta}(s\_h,a\_h)

# Variance Reduction

## Variance Reduction via Action-Independent Baseline

```undefined
\nabla_\theta\ln\pi_\theta(a_h|s_h)\left(\widetilde Q^{\pi_\theta}(s_h, a_h)-b(s_h) \right)
```

### The best baseline that minimizes variance is

```undefined
\min_b\mathbb{E}\left[\left(\nabla_\theta\ln\pi_\theta(a_h|s_h)\left(\widetilde Q^{\pi_\theta}(s_h, a_h)-b(s_h) \right) \right)^\top \nabla_\theta\ln\pi_\theta(a_h|s_h)\left(\widetilde Q^{\pi_\theta}(s_h, a_h)-b(s_h) \right) \right]
```

```undefined
b(s_h) = \frac{\mathbb{E}\left[ \nabla_\theta\ln\pi_\theta(a_h|s_h)^\top \nabla_\theta\ln\pi_\theta(a_h|s_h)  \left(\widetilde Q^{\pi_\theta}(s_h, a_h)\right)\right]}{\mathbb{E}\left[\nabla_\theta\ln\pi_\theta(a_h|s_h)^\top \nabla_\theta\ln\pi_\theta(a_h|s_h) \right]}
```

# Convergence of SGD

*   \beta-smooth

```undefined
\|\nabla_\theta J(\theta) -\nabla_\theta J(\theta_0)\|_2\le\beta\|\theta-\theta_0\|_2 \\ \left|J(\theta)-J(\theta_0)-\nabla_\theta J(\theta_0)^\top(\theta-\theta_0) \right|\le \frac\beta2\|\theta-\theta_0\|_2^2\forall\theta,\theta_0
```

*   Theorem: if J(\theta) is \beta-smooth, and we run SGA: \theta\_{t+1} = \theta\_t+\eta\widetilde\nabla\_\theta J(\theta\_t) where

    ```undefined
    \mathbb{E}\left[\widetilde \nabla_\theta J(\theta_t)\right] = \nabla_\theta J(\theta_t), \mathbb{E}\left[\left\| \nabla_\theta J(\theta_t)\right\|^2_2\right]\le\sigma^2
    ```

    then

    ```undefined
    \mathbb{E}\left[\frac 1T\sum_t \| \nabla_\theta J(\theta_t) \|_2^2 \right] \le O\left(\sqrt{\beta\sigma^2/T} \right)
    ```
