---
id: 34379fde-436b-4b10-a7cf-45fc219049b7
title: 16. Linear Quadratic Regulators
created_time: 2023-08-01T01:03:00.000Z
last_edited_time: 2023-08-17T06:46:00.000Z
cover_image: https://www.notion.so/images/page-cover/nasa_robert_stewart_spacewalk_2.jpg
하위 항목: []
subclass: RL Theory
class: RL
작성일시: 2023-08-01T01:03:00.000Z
pdf: https://wensun.github.io/CS6789_data_fall_2021/LQR_annotated.pdf
상위 항목: []
_thumbnail: https://www.notion.so/images/page-cover/nasa_robert_stewart_spacewalk_2.jpg

---

# TRPO/PPO

## TRPO

```undefined
\max_{\pi_\theta}V^{\pi_\theta}(\rho)\text{\  s.t.\  }KL(\Pr^{\pi_{\theta_0}}||\Pr^{\pi_\theta})\le\delta
```

### With second order Taylor’s expansion

```undefined
\max_\theta\nabla V^{\pi_{\theta_0}}(\rho)^\top(\theta-\theta_0)\text{\ s.t \ }(\theta-\theta_0)^\top F_{\theta_0}(\theta-\theta_0)\le\delta
```

*   There is a closed form solution

    ```undefined
    \theta = \theta_0 + \sqrt{\frac{\delta}{(\nabla V^{\pi_{\theta_0}})^\top F_{\theta_0}^{-1}\nabla V^{\pi_{\theta_0}}}}\cdot F_{\theta_0}^{-1}\nabla V^{\pi_{\theta_0}}
    ```

## PPO

*   To find the next policy, use objective

    ```undefined
    \max_\theta \mathbb E_{s\sim d^{\pi_t}}\left[\mathbb E_{a\sim\pi^\theta(\cdot|s)}\left[A^{\pi_t}(s,a)\right]\right]\text{ subject to } \sup_s\left\|\pi^\theta(\cdot|s)-\pi_t(\cdot|s)\right\|_{TV}\le\delta
    ```

*   We can do multiple gradient steps by rewriting the objective function using importance weighting using a clip function

    ```undefined
    \max_\theta \mathbb E_{s\sim d^{\pi_t}}\left[\mathbb E_{a\sim\pi^\theta(\cdot|s)}\left[\text{clip}\left(\frac{\pi^\theta(a|s)}{\pi_t(a|s)}, 1-\epsilon,1+\epsilon\right)A^{\pi_t}(s,a)\right]\right]
    ```

*   Clip: when the ratio is outside of \[1-\epsilon,1+\epsilon], we get gradient zero

# Optimal Control

*   A dynamical system is described as x\_{t+1}=f\_t(x\_t,u\_t,w\_t) where f\_t maps a state x\_t\in\R^d, a control u\_t\in\R^k, and a disturbance w\_t, to the next state x\_{t+1}\in\R^d starting from an initial state x\_0

*   The objective is to find the control policy which minimizes the long term cost

    ```undefined
    \mathbb E_\pi\left[\sum_{t=0}^{H-1}c_t(x_t,u_t)\right] \text{s.t. }x_{t+1}=f_t(x_t,u_t,w_t)
    ```

# LQR

*   The finite horizon LQR(Linear Quadratic Regulator) problem is given by minimizing

    ```undefined
    \mathbb E\left[x_H^\top Qx_H+\sum_{t=0}^{H-1}(x_t^\top Qx_t+u_t^\top Ru_t) \right] \text{ s.t. }x_{t+1}=A_tx_t+b_tu_t+w_t, x_0\sim D,w_t\sim N(0,\sigma^2,1)
    ```

*   The infinite horizon LQR problem is given by minimizing

    ```undefined
    \lim_{H\to\infty}\frac 1H\mathbb E\left[\sum_{t=0}^{H-1}(x_t^\top Qx_t+u_t^\top Ru_t) \right] \text{ s.t. }x_{t+1}=A_tx_t+b_tu_t+w_t, x_0\sim D,w_t\sim N(0,\sigma^2,1)
    ```

    where A and B are time homogenous

# Bellman Optimality

*   Value function

    ```undefined
    V_h^\pi(x) = \mathbb E\left[x_H^\top Qx_h+\sum_{t=h}^{H-1}(x_t^\top Qx_t+u_t^\top Ru_t)| \pi,x_h=x\right]
    ```

*   State-action value function

    ```undefined
    Q_h^\pi(x,u) = \mathbb E\left[x_H^\top Qx_h+\sum_{t=h}^{H-1}(x_t^\top Qx_t+u_t^\top Ru_t)| \pi,x_h=x,u_h=u\right]
    ```

## Value Iteration and Ricatti Equations

*   For finite horizon case, the optimal policy is a linear controller specified by

    ```undefined
    \pi^*(x_t) = -K_t^*x_t \text{ where }K_t^* = (B^\top P_{t+1} B+R)^{-1}B^\top P_{t+1} A
    ```

    where P\_t can be computed iteratively, in a backwards manner, using the following algebraic Ricatti equation, where for t\in\[H],

    ```undefined
    \begin{aligned}P_t &=A^\top P_{t+1} A+Q-AA^\top P_{t+1} B(B^\top P_{t+1}B+R)^{-1}B^\top P_{t+1} A\\&=A^\top P_{t+1} A+Q-(K_{t+1}^*)^\top(B^\top P_{t+1}B+R)  K_{t+1}^*\end{aligned}
    ```

    and where P\_H=Q

*   Furthermore, for t\in\[H], we have that

    ```undefined
    V_t^*(x)=x^\top P_t x + \sigma^2 \sum_{h=t+1}^H\text{Trace}(P_h)
    ```

*   For infinite horizon case

    ```undefined
    P = A^\top PA+Q-A^\top PB(B^\top PB+R)^{-1}B^\top PA
    ```

    We have that the optimal policy is

    ```undefined
    \pi^*(x) = -K^*x
    ```

    and optimal control gain is

    ```undefined
    K^* = -(B^\top PB+R)^{-1} B^\top PA
    ```

*   P is unique and the optimal average cost is \sigma^2\text{Trace}(P)

# Semidefinite programs to find P

## The Dual SDP

*   The dual optimization is minimize

    ```undefined
    \text{Trace}\left(\Sigma \cdot\begin{bmatrix}Q&0\\0&R\end{bmatrix}\right)\text{ subject to }\Sigma_{xx}=\begin{pmatrix}A&B\end{pmatrix}\Sigma\begin{pmatrix}A&B\end{pmatrix}^\top+\sigma^2I,\Sigma\succeq 0
    ```

*   The SDP has unique solution which is \Sigma^*. The optimal gain matrix is K^* = -\Sigma\_{ux}^*(\Sigma\_{xx}^*)^{-1}

## The Primal SDP for the infinite horizon LQR

*   The primal optimization problem is given as maximizing \sigma^2\text{Trace}(P) subject to

    ```undefined
    \begin{bmatrix}A^\top PA+Q-P&A^\top PB\\B^\top PA&B^\top PB+R\end{bmatrix}\succeq 0, P\succeq 0
    ```

    where the optimization variable is P

*   This SDP has unique solution P^\*, which implies

    *   P^\* satisfies Ricatti equations

    *   The optimal average cost of the infinite horizon LQR is \sigma^2\text{Trace}(P^\*)

    *   The optimal policy use the gain matrix K^\* = -(B^\top PB+R)^{-1} B^\top PA
