---
id: a8c00dcf-6a71-41dd-abc9-68eafbd21732
title: '14. Policy Optimization: Global Convergence'
created_time: 2023-07-17T12:09:00.000Z
last_edited_time: 2023-08-17T06:46:00.000Z
하위 항목: []
subclass: RL Theory
class: RL
작성일시: 2023-07-17T12:09:00.000Z
pdf: https://wensun.github.io/CS6789_data_fall_2021/PG_OPT1_annotated.pdf
상위 항목: []

---

# Policy Gradient Derivation

> 💡 How to compute the gradient?

```undefined
\nabla_\theta J(\theta) := \frac 1 {1-\gamma}\mathbb{E}_{s,a\sim d^{\pi_\theta}}\left[\nabla_\theta \ln \pi_\theta (a|s) Q^{\pi_\theta}(s,a) \right]
```

> 💡 When to PG methods converge to a global optima?

# PG as non-convex optimization

## Convergence to Stationary points of GD

*   Proposition(Stationary point convergence): Assume F(\theta) is \beta-smooth. Suppose we run gradient **ascent** \theta\_{t+1} = \theta\_{t}+\eta \nabla\_\theta F(\theta\_t) with \eta = 1/2\beta. Then

    ```undefined
    \min_{t\le T}\|\nabla_\theta F(\theta_t)\|_2^2 \le \frac{2\beta(\max_\theta F(\theta)-F(\theta_0))}{T}
    ```

# Vanila PG for the Softmax

*   Given our starting distribution \rho over states, recall objectives \max\_{\theta\in\Theta}V^{\pi\_\theta}(\rho) where { \pi\_\theta|\theta\in\Theta\subset\R^d} is some class of parametric policies

*   While we are interested in good performance over \rho, it is helpful to optimize under a different measure \mu

*   d\_{s\_0}^\pi will be our state distribution measure

## The Softmax Policy Class

```undefined
\pi_\theta(a|s) = \frac{\exp(\theta_{s,a})}{\sum_{a'}\exp(\theta_{s,a})}
```

*   We have that

    ```undefined
    \frac{\partial\log\pi_\theta(a|s)}{\partial\theta_{s',a'}} = 1[s=s'](1[a=a']-\pi_\theta(a'|s))
    ```

    where 1\[\cdot] is the indicator function

*   Lemma: For the softmax policy class, we have

    ```undefined
    \frac{\partial V^{\pi_\theta}(\mu)}{\partial\theta_{s,a}} = \frac1{1-\gamma}d_\mu^{\pi_\theta}(s)\pi_\theta(a|s)A^{\pi_\theta}(s,a)
    ```

## Global Convergence

*   Concerns: Non convex functions, and flat gradients if \theta\_t \rightarrow \infty

*   Theorem: Assume the \mu is strictly possible i.e \mu(s)>0 for all states s. For \eta\le(1-\gamma)^3/8, then we have that for all states s, V^{(t)}(s) \rightarrow V^\*(s), as t\rightarrow\infty

# PG+Log Barrier Regularization

## Log Barrier Regularization

*   Relative entropy for distributions p,q is KL(p,q) := \mathbb{E}\_{x\sim p}\[-\log q(x)/p(x)]

*   Consider the log barrier \lambda-regularized objective:

    ```undefined
    \begin{aligned}L_\lambda(\theta)&\coloneqq V^{\pi_\theta}(\mu) - \lambda \mathbb{E}_{s\sim\text{Unif}(s)}[KL(\text{Unif}_A, \pi_\theta(\cdot|s))]\\ &= V^{\pi_\theta}(\mu) + \frac{\lambda}{SA}\sum_{s,a}\log\pi_\theta(a|s)+\lambda\log A\end{aligned}
    ```

## Stationarity and Optimality

*   Theorem(Log barrier Regularization) Suppose \theta is such that |\nabla\_\theta L\_\lambda(\theta)|*2\le\varepsilon*{opt} and \varepsilon\_{opt}\le\lambda/(2SA) then we have for all starting state distributions \rho

    ```undefined
    V^{\pi_\theta}(\rho)\ge V^*(\rho)-\frac{2\lambda}{1-\gamma}\left\| \frac{d_\rho^{\pi^*}}{\mu}\right\|_\infty
    ```

    where the **distribution mismatch coefficient** is

    ```undefined
    \left\| \frac{d_\rho^{\pi^*}}{\mu}\right\|_\infty = \max_s\left( \frac{d_\rho^{\pi^*}(s)}{\mu(s)}\right)
    ```

## Global Convergence with Log Barrier

*   The smoothness of L\_\lambda(\theta) is \beta\_\lambda:= \frac{8\gamma}{(1-\gamma)^3}+\frac{2\lambda}S

*   Corollary(Iteration complexity with log barrier regularization): Set \lambda = \frac{\epsilon(1-\gamma)}{2\left| \frac{d\_\rho^{\pi^*}}{\mu}\right|*\infty} and \eta = 1/\beta*\lambda. Starting from any initial \theta^0, then for all starting state distributions \rho, we have \min\_{t\<T}{V^*(\rho)-V^t(\rho)}\le\epsilon whenever T\ge c\frac{S^2A^2}{(1-\gamma)^6\epsilon^2}\left| \frac{d\_\rho^{\pi^\*}}{\mu}\right|\_\infty^2
