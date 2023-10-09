---
id: 71c0fff6-7060-461f-bca8-69eb2ef0462c
title: Improved Algorithms for Linear Stochastic Bandits
created_time: 2023-02-28T06:42:00.000Z
last_edited_time: 2023-08-17T06:45:00.000Z
cover_image: https://www.notion.so/images/page-cover/rijksmuseum_rembrandt_1642.jpg
하위 항목: []
subclass: Bandits
class: Paper
작성일시: 2023-02-28T06:42:00.000Z
pdf: >-
  https://proceedings.neurips.cc/paper_files/paper/2011/file/e1d5be1c7f2f456670de3d53c7b54f4a-Paper.pdf
상위 항목: []
_thumbnail: https://www.notion.so/images/page-cover/rijksmuseum_rembrandt_1642.jpg

---

## Introduction

*   Linear Stochastic Bandit problem is a sequential decision-making problem and based on optimism in the Face of Uncertainty(OFU) principle.

*   We want to get smaller confidence set, and better regret bounds by modifying UCB algorithm for the d-armed bandit problem

*   At each round t, the learner is given a decision set D\_t \subseteq \R^d from which learner has to choose an action X\_t. Subsequently learner get reward Y\_t=\braket{X\_t, \theta\_\*}+\eta\_t and learner need to maximize total reward

*   psuedo-regret is written like this, so it hasa lower variance because noise is removed

```undefined
R_n = \left({\sum_{t=1}^n}\braket{x_t^*,\theta_*}\right) - \left({\sum_{t=1}^n}\braket{X_t,\theta_*}\right) = \left({\sum_{t=1}^n}\braket{x_t^* - X_t,\theta_*}\right)
```

## Optimism in the Face of Uncertainty(OFU)

*   This algorithm chooses the pair which *jointly* maximized the reward

    > 📖 for t:=1,2,… do

          ```undefined
          (X_t, \tilde\theta_t) = \argmax_{(x, \theta) \in D_t \times C_{t-1}}\braket{x, \theta}
          ```

          Play X_t and observe reward Y_t, update C_t

          endfor

## Self-Normalized Tail Inequality for Vector-Valued Martingales

*   Martingale: 확률론에서 과거의 모든 정보를 알고 있다면 미래의 기댓값이 현재 값과 동일한 과정을 의미함

*   Consider \sigma-algebra F\_t = \sigma(X\_1, X\_2, ...,X\_{t+1}, \eta\_1,\eta\_2,...,\eta\_t) then for any t \geq1 X, Y, and \eta is F\_t-measurable

*   Theorem(Self-Normalizied Bound for Vector-Valued Martingales)

    > 📖 Let {F\_t}*{t=0}^{\infty} be a filtration. Let {\eta\_t}*{t=1}^{\infty} be a real-valued stochastic process such that

          ```undefined
          \forall\lambda \in \R \quad E[e^{\lambda_{n_t}}|F_{t-1}] \leq\exp(\frac {\lambda^2R^2}{2})
          ```

          Let \{x_t\}_{t=1}^{\infty} be an stochastic process and assume that V is a d*d positive definite matrix. For any t bigger or equal than 0, define

          ```undefined
          \overline{V}_t = V + \sum_{s=1}^t X_s X_s^\top ~~~~~~ S_t = \sum_{s=1}^t \eta_sX_s
          ```

          Then for any \delta > 0, with probability at least 1-\delta, for all t\geq0,

          ```undefined
          \Vert S_t\Vert ^2 _{\overline{V}_t^{-1}} \leq 2R^2\log \left( \frac {\det (\overline{V}_t)^{1/2}\det (V)^{-1/2}}{\delta} \right)
          ```

## Construction of Confidence Sets

*   Let \hat\theta\_t be l^2-regularized least squares estimate of \theta\_\* with regularization parameter \lambda > 0

    ```undefined
    \hat\theta_t=(X^\top_{1:t}X_{1:t}+\lambda I)^{-1}X_{1:t}^\top Y_{1:t}
    ```

    where X\_{1:t} is the matrix whose rows are X\_1^\top,X\_2^\top,...,X\_t^\top and Y\_{1:t}=(Y\_1,...,Y\_t)^\top

*   Theorem(Confidence Ellipsoid)

    > 📖 Assume same as theorem above. Let V=I\lambda,\lambda >0, define Y\_t=\lang X\_t,\theta\_*\rang+\eta\_t and assume that |\theta\_*|*2\le S. Then for any \delta >0, with probability at least 1-\delta, for all t\le 0, \theta*\* lies in the set

          ```undefined
          C_t=\left\{\theta\in\R^d:\left\|\hat\theta_t - \theta\right\|_{V_t}\le R\sqrt{2\log\left(\frac{\det(\bar V_t)^{1/2}\det(\lambda I)^{-1/2}}{\delta}\right)}+\lambda^{1/2}S \right\}
          ```

          Furthermore, if for all t\ge 1, \|X_t\|_2\le L then with probability at least 1-\delta, for all t\ge 0, \theta_* lies in the set

          ```undefined
          C_t=\left\{\theta\in\R^d:\left\|\hat\theta_t - \theta\right\|_{V_t}\le R\sqrt{d\log\left(\frac{ 1+tL^2/\lambda}{\delta}\right)}+\lambda^{1/2}S \right\}
          ```

## Regret Analysis of the OFUL Algorithm

*   Theorem(The regret of OFUL Algorithm)

    > 💡 Assume that for all t and all x\in D, \lang x,\theta\_\*\rang\in\[-1,1]. Then, with probability at least 1-\delta, the regret of OFUL algorithm satisfies

          ```undefined
          \forall n\ge0,\ R_n\le4\sqrt{nd\log(\lambda+nL/d)}\left(\lambda^{1/2}S+R\sqrt{2\log(1/\delta)+d\log(1+nL/(\lambda d))}\right)
          ```

### Saving Computation

*   We essentially need to recompute \widetilde\theta\_t only O(\log n) times up to time n and hence saving computations.

*   Theorem

    > 💡 Under the same assumptions as in the regret of OFUL Algorithm, with probability at least 1-\delta, for all n\ge0, the regret of the RARELY SWITCHING OFUL ALGORITHM satisfies

          ```undefined
          R_n\le4\sqrt{(1+C)nd\log\left(\lambda+\frac{nL}d\right)}\left\{\sqrt\lambda S + R\sqrt{d\log\left(1+\frac{nL}{\lambda d}\right)+2\log\frac1\delta}\right\}+4\sqrt{d\log\frac nd}
          ```

*   The rarely switching OFUL Algorithm

    > 📖 Input: Constant C > 0

          \tau = 1{This is the last time step that we changed \widetilde\theta_t

          for t:=1,2,… do

            if \det(V_t)>(1+C)\det(V_\tau) then

              (X_t, \widetilde\theta_t) = \argmax_{(x,\theta)\in D_t\times C_{t-1}}\lang\theta,x\rang

          	\tau=t

            end if

            X_t = \argmax_{x\in D_t}\lang\widetilde\theta_\tau,x\rang.

            Play X_t and observe reward Y_t

### Problem Dependent Bound

*   \bar\Delta\_n: smallest gap at timestep n

*   Theorem

    > 📖 Assume that \lambda\ge 1 and |\theta\_\*|\_2\le S where S \ge 1. With probability at least 1-\delta, for all n\ge 1, the regret of the OFUL satisfies

          ```undefined
          R_n\le\frac{16R^2\lambda S^2}{\bar\Delta_n}\left(\log(Ln)+(d-1)\log\frac{64R^2\lambda S^2L}{\bar\Delta_n^2}+2(d-1)\log\left(d\log\frac{d\lambda+nL^2}d+2\log(1/\delta)\right)+2\log(1/\delta)\right)^2
          ```

## Multi-Armed Bandit Problem

*   Confidence interval: With probability at least 1-\delta

    ```undefined
    \forall i\in\{1,2,...,d\},\forall t\ge 0\ \ \ \ |\bar X_{i, t}-\mu_i|\le c_{i, t}
    ```

    where

    ```undefined
    c_{i, t}=\sqrt{\frac{(1+N_{i,t})}{N^2_{i, t}}\left(1+2\log\left(\frac{d(1+N_{i,t})^{1/2}}{\delta}\right)\right)}
    ```

*   Using this confidence interval, we modify UCB algorithm and call it as \text{UCB}(\delta)

*   Regret of \text{UCB}(\delta)

    > 📖 Assume that the noise \eta\_t is conditionally  1-sub-gaussian, with probability at least 1-\delta, the total regret of \text{UCB}(\delta) is bounded as

          ```undefined
          R_n \le\sum_{i:\Delta_i>0}\left(3\Delta_i+\frac{16}{\Delta_i}\log\frac{2d}{\Delta_i\delta}\right)
          ```

*   We can get O(\log t) upper bound on the expected regret
