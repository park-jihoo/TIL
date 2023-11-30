---
id: 0012457f-f278-4109-8e70-90b3aa017b66
title: Linear Thompson Sampling Revisited
created_time: 2023-06-29T00:00:00.000Z
last_edited_time: 2023-08-17T06:45:00.000Z
cover_image: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1649.jpg
하위 항목: []
subclass: Bandits
class: Paper
작성일시: 2023-06-29T00:00:00.000Z
pdf: https://arxiv.org/pdf/1611.06534.pdf
상위 항목: []
_thumbnail: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1649.jpg

---

# Linear Thompson Sampling Revisited

## Introductions

*   The major contributions of this paper are

    *   Following the intuition of Thompson Sampling for contextual bandits with linear payoffs, and we show that TS doesn't need to sample from an actual Bayesian posterior distribution

    *   We provide an alternative proof of TS. Regret is related to thegradient of objective function, that is ultimately controlled by the norm of the optimal arms. This shows that \theta\_t is chosen, then optimal arm x\_t=\argmax\_xx^\top\theta\_t represents *useful exploration* step

    *   Show howour proof can easily adapted to Generalized Linear Model

## PreLiminaries

### Setting

*   We consider the stochastic linear bandit model, and reward is generated as r(x)=x^\top\theta^\*+\xi

*   An arm is evaluated due to its expected reward x^\top\theta^\* and for any \theta we denote the optimal arm and its value by

    ```undefined
    x^(\theta) = \argmax_{x\in\chi}x^\top\theta,\space J(\theta) = \sup_{x\in\chi}x^\top\theta
    ```

### Notations

*   We impose the following **assumptions** on the problem structure and the noise \xi\_{t+1}

    *   The arm set \chi is a bounded closed(compact) subset of \R^d such that ||x||\le1 for all x\in\chi

    *   There exists S\in\R^+ such that ||\theta^\*||\le S and S is known

    *   The noise process {\xi\_t}\_t is a martingale differencne sequence given F\_t^x and it is conditionally R-subgaussian for some constant R\ge 0

*   **Proposition 1)** For any \theta\in(0,1) under assumption above, for any F\_t^x adapted sequence (x\_1,\dots,x\_t), the RLS estimator \hat{\theta^\*}t *is such that for any fixed* t\ge 1\_, and with probability\_ 1-\delta\_,\_

    ```undefined
    ||\hat\theta_t-\theta^*||{V_t}\le\beta_t(\delta)\\
    \forall x\in\R^d, |x^\top(\hat\theta_t-\theta^*)|\le||x||_{V_t^{-1}}\beta_t(\delta)\\
    \beta_t(\delta) = R\sqrt{2\log\frac{(\lambda+t)^{d/2}\lambda^{-d/2}}{\delta}}+\sqrt\lambda S
    ```

*   At step t, we can define ellipsoid centered around \hat\theta\_t and radius \beta\_t(\delta/4T)

*   **Proposition 2)** Let \lambda\ge 1, for any arbitrary sequence (x\_1,\dots,x\_t)\in\chi^t let V\_{t+1} = \lambda I+\sum\_{s=1}^{t}x\_sx\_s^\top, then

    ```undefined
    \sum_{s=1}^{t}||x_s||^2_{V_x^{-1}} \le 2\log\frac{\det(V_{t+1})}{\det(\lambda I)} \le 2d\log\left({1+\frac t \lambda}\right)
    ```

## Linear Thompson Sampling

*   Algorithms

    > 📖 Input: \hat\theta\_1, V\_1=\lambda I, \delta,T

          Set \delta' = \delta/(4T)

          for t =\{1,...,T\} do

          	Sample \eta_t\sim\mathcal{D}^{TS}

          	Compute parameter

          	```undefined
          	\widetilde\theta_t = \hat\theta_t+\beta_t(\delta')V_t^{-1/2}\eta_t
          	```

          	Compute optimal arm

          	```undefined
          	x_t = x^*(\widetilde\theta_t)=\argmax_{x\in\mathcal X}x^\top\widetilde\theta_t
          	```

          	Pull arm x_t and observe reward r_{t+1}

          	Compute V_{t+1} and \hat\theta_{t+1} using Regularized Least square

          end for

*   Thompson sampling samples a perturbed parameter \widetilde\theta\_t as

    ```undefined
    \widetilde\theta_t = \hat\theta_t+\beta_t(\delta')V_t^{-1/2}\eta_t
    ```

    where \eta\_t is a random sample drawn iid from suitable multivariate distribution \mathcal D^{TS}.

*   \mathcal D^{TS} is a multibvariate distribution on \R^d absolutely continuous with respect to the Lebesgue measure which satisfies the following properties

    *   (anti-concentration) there exists a strictly positive probability p such that for any u\in\R^d with |u|=1,

        ```undefined
        \mathbb P_{\eta\sim\mathcal D^{TS}}(u^\top\eta\ge1)\ge p
        ```

    *   (concentration) there exists c,c' posisitve constants such that \forall\delta\in(0,1)

        ```undefined
        \mathbb P_{\eta\sim\mathcal D^{TS}}\left(\|\eta\|\le\sqrt{cd\log\frac{c'd}{\delta}}\right)\ge1-\delta
        ```

# Sketch of the proof

*   Bounding R^{\text{RLS}}(T)

    ```undefined
    \sum_{t=1}^T|r_{t+1}-x_t^\top\hat\theta_{T+1}|^2+\lambda\|\hat\theta_{T+1}\|^2\ge\sum_{t=1}^T|r_{t+1}-x_t^\top\hat\theta_{t+1}|^2+\lambda\|\hat\theta_1\|^2
    ```

*   Bounding R^{\text{TS}}(T)

    *   Regret and sensitively of J

    *   Sensitivity of J and optimal arm

    *   Optimism

# Formal Proof

*   Theorem: Under assumptions above, the regret of Thompson Sampling is bounded w\.p 1-\delta as(\delta'=\frac{\delta}{4T})

    ```undefined
    R(T)\le\left((\beta_t(\delta')+\gamma_T(\delta')\left(1+\frac 4p\right)\right)\sqrt{2Td\log\left(1+\frac T\lambda\right)}+\frac{4\gamma_T(\delta')}p\sqrt{\frac{8T}\lambda\log\frac4\delta}
    ```

*   Definition: we define the filtration \mathcal F\_t as the accumulated information up to time t before the sampling procedure

*   Definition: Let \delta\in(0,1) and \delta'=\delta/(4T) and t\in\[1,T]. We define \hat E\_t as the event where the RLS estimate concentrates around \theta^\* for all steps s \le t. We also define \widetilde E\_t as the event where the sampled parameter \widetilde\theta\_s concentrates around \hat\theta\_s for all steps s \le t

*   Regret and gradient of J(\theta): On event E\_t,\widetilde\theta\_t belongs to \varepsilon\_t^{TS} and thus

    ```undefined
    R_t^{TS}\mathbf{1}\{E_t\}\le(J(\theta^*)-\inf_{\theta\in\varepsilon_t^{TS}}J(\theta))\mathbf{1}\{\hat E_t\}
    ```

    then,

    ```undefined
    R_t^{TS}\le\mathbb E\left[(J(\widetilde\theta)-\inf_{\theta\in\varepsilon_t^{TS}}J(\theta))\mathbf1 \{\hat E_t\}|\mathcal F_t,\widetilde\theta\in\Theta_t^{opt}\right]
    ```

    *   Proposition: For any set of arm \mathcal X satisfying assumption 1, J(\theta)=\sup\_x x^\top\theta has the following properties

        *   J is real-valued as superemum is attained in \mathcal X

        *   J is convex on \R^d

        *   J is continuous with continuous first derivative except for a zero-measure set w\.r.t the Lebesgue’s measure

*   From gradient of J(\theta) to optimal arm x^\*(\theta)

    *   In the sketch of the proof, there was a direct relationship between \nabla J(\theta) and the optimal arm

    *   Lemma: Under assumption 1, for any \theta\in\R^d, we have \nabla J(\theta) = x^\*(\theta) except for a zero-measure set w\.r.t the Lebesgue’s measure

*   Optimism: The optimism of TS is a direct consequence of the convexity of J and the fact that the distribution of \eta is oversampling by a factor \sqrt d w\.r.t. the ellipsoid \varepsilon\_t^{\text{RLS}}

*   Finally, with probability at least $$1-\delta

    ```undefined
    R^{TS}(T) \le \frac{4\gamma_{T}(\delta')}p\left(\sum_{t=1}^T\|x_t\|_{V_t^{-1}}+\sqrt{\frac{8T}\lambda\log\frac4\delta}\right)
    ```
