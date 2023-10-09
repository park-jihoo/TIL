---
id: 48e22df0-5810-4a43-b8a8-70709c6f343b
title: 17. Convex Parametrization for Linear Dynamical Systems
created_time: 2023-08-02T11:25:00.000Z
last_edited_time: 2023-08-17T06:46:00.000Z
cover_image: https://www.notion.so/images/page-cover/solid_yellow.png
하위 항목: []
subclass: RL Theory
class: RL
작성일시: 2023-08-02T11:25:00.000Z
pdf: https://wensun.github.io/CS6789_data_fall_2021/SLS_linear_system_annotated.pdf
상위 항목: []
_thumbnail: https://www.notion.so/images/page-cover/solid_yellow.png

---

> 📖 What if the cost function is arbitary convex function, and how to handle adversarial noise?

# Linear Dynamical System and Convex cost function

```undefined
x_{t+1} = Ax_t+Bu_t+w_t,x_0\sim\mathscr{D},w_t\sim\mathscr{N}(0,\sigma^2I)
```

```undefined
\max\mathbb E\left[\sum_{h=0}^{H-1}c(x_h,a_h)|\pi \right]
```

*   We cannot guarantee the optimal policy is linear, but we consider a restricted policy class

    ```undefined
    \Pi=\left\{\pi=\{-K_t\}_{t=0}^{H-1}:K_t\in\mathscr K,\forall t \right\}
    ```

*   Goal: find the best linear controllers

    ```undefined
    \{-K_t^*\}_{t=0}^{H-1}:=\argmin_{\pi\in\Pi}\mathbb E\left[\sum_{t=0}^{H-1}c(x_t,u_t)|\pi \right]
    ```

*   However, even with quadratic cost, \max\mathbb E\left\[\sum\_{h=0}^{H-1}c(x\_h,a\_h)|\pi \right] is not convex, so we need new convex parameter

    ```undefined
    u_t = \underbrace{\left[-K_t\left(\prod_{\tau=1}^t(A-BK_{t-\tau})\right)\right]}_{M_t}x_0+\sum_{\tau=0}^{t-1}\underbrace{\left[-K_t\prod_{h=1}^{t-1-\tau}(A-BK_{t-h})\right]}w_\tau
    ```

*   Claim: for any linear controllers \pi:={-K\_t}*{t=0}^{H-1}, there exists a parametrization \left{{M\_t,M*{t-1;t},...,M\_{0;t}}\right}*{t=0}^{H-1}, that generates the same sequencen trajectory, given any fixed x\_0 and fixed noise w\_0,…,w*{H-1}

*   Claim: Given controller \tilde\pi:={{M\_t,M\_{0;t},...,M\_{t-1;t}}}\_{t=0}^{H-1}, u\_t\&x\_t are all llinear with respect to the parameters, \forall t

*   Claim: Given controller \tilde\pi:={{M\_t,M\_{0;t},...,M\_{t-1;t}}}*{t=0}^{H-1}, \sum*{t=0}^{H-1}c(x\_t,u\_t) is convex with respect to the parameters \forall t

# Convexity and Gradient Descent

*   Claim: Given controller \tilde\pi:={{M\_t,M\_{0;t},...,M\_{t-1;t}}}*{t=0}^{H-1}, \mathbb E\left\[\sum*{t=0}^{H-1}c(x\_t,u\_t)|\pi\right] is convex with respect to the parameters \forall t

*   Convexity allows to perform GD directly on parameters {{M\_t,M\_{0;t},...,M\_{t-1;t}}}\_{t=0}^{H-1}

*   Algorithm

    *   Execute the control {{M\_t,M\_{0;t},...,M\_{t-1;t}}}*{t=0}^{H-1} to generate the trajectory (x\_0,u\_0,…,x*{H-1},u\_{H-1})

    *   Compute gradient of \sum\_{t=0}^{H-1}c(x\_t,u\_t) wrt all parameters M, perform gradient descent

# Extension to adversarial online control

## Setting

On the k-th day,

*   adversary decides sequence of noises {w\_0^k,...,w\_{H-1}^k} and (convex) cost function c^k(x,u)

*   Without knowing noises and cost, learner proposes a sequence of controllers {{M\_t,M\_{0;t},...,M\_{t-1;t}}}\_{t=0}^{H-1}

*   Learner executes controllers, and suffers total cost \sum\_{h=0}^H c\_k(x\_h^k,a\_h^k)

Goal: No-regret

```undefined
\sum_{k=0}^{K-1}\sum_{h=0}^Hc^k(x_h^k,a_h^k)-\min_{\{-K_h^*\}_{h=0}^{H-1}}\sum_{k=0}^{K-1}J^k(\{-K_h^*\}_{h=0})=o(K)
```

## The online gradient descent algorithm

*   At iteration t, learner proposes

    ```undefined
    z_k:=P_{\mathscr E}(z_{k-1}-\eta\nabla\mathcal l_{k-1}(z_{k-1}))
    ```

*   The OGD guarantee: Although the OGD learner makes choice z\_t without seeing the loss l\_t, it is no regret

    *   Assume \mathscr X is convex, and bounded \max\_{z,y\in\mathscr E}|z-y|\_2\le F, and loss is G-lipschitz, then OGD has following regret

    ```undefined
    \sum_{k=1}^Kl_k(z_k)-\min_{x\in\mathscr E}\sum_{k=1}^Kl_k(z)\le O\left((F^2+G^2)\sqrt K\right) 
    ```

## Reduce online control to online learning

*   We define parameter z:={{M\_t,M\_{0;t},...,M\_{t-1;t}}}\_{t=0}^{H-1}

*   At iteration t, given w\_0^k,…w\_{H-1}^k and c^k which are determined by adversary, we define loss function l\_t(z) as

    ```undefined
    l_k(z) :=\sum_{h=0}^{H-1}c^k(x_h,u_h)
    ```

    where

    ```undefined
    x_0,u_0=M_0x_0, \ x_1=Ax_0+BM_0x_0,\ u_1=M_1x_0+M_{0;1}w_0^k,\ x_2=Ax_1+BM_1x_0+BM_{0;1}w_0^k
    ```
