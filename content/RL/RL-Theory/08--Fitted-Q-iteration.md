---
id: 9b5505cd-a878-43e6-96b2-012135804648
title: 08. Fitted Q iteration
created_time: 2023-07-03T11:26:00.000Z
last_edited_time: 2023-08-17T06:46:00.000Z
cover_image: https://www.notion.so/images/page-cover/met_william_morris_1877_willow.jpg
하위 항목: []
subclass: RL Theory
class: RL
작성일시: 2023-07-03T11:26:00.000Z
pdf: https://wensun.github.io/CS6789_data_fall_2021/fitted_Q_iteration_annoated.pdf
상위 항목: []
_thumbnail: https://www.notion.so/images/page-cover/met_william_morris_1877_willow.jpg

---

> 💡 What happens when we do nonlinear function regression?

# Setting: Assumptions

## Setting

*   Infinite horizon Discounted MDPs \gamma \in (0,1)

*   A given sampling distribution \nu \in \Delta(S\times A)

*   Function class \mathscr{F} = { f:S\times A \rightarrow\[0,1/(1-\gamma)]}

## Key Assumptions

*   Sampling distribution \nu has full coverage(diverse)

    ```undefined
    \max_\pi\max_{s,a}\frac{d^\pi(s,a)}{\nu(s,a)}\le C < \infty
    ```

*   Small inherent Bellman error, i.e. near Bellman completion

    ```undefined
    \max_{g\in\mathscr{F}}\min_{f\in\mathscr{F}}\mathbb{E}_{s,a\sim\nu}(f(s,a)-\mathscr{T}g(s,a))^2\le\epsilon_{approx, \nu}
    ```

# Fitted Q Iteration

*   Sample data points in an i.i.d fashion:

    ```undefined
    \mathscr{D} = \{s,a,r,s'\}, \ (s,a)\sim\nu,r=r(s,a),s'\sim P(\cdot|s,a)
    ```

*   Initialize f\_0 \in \mathscr{F}, and iterate

    ```undefined
    f_{t+1} = \arg\min_{\mathscr{f\in F}} \sum_{\mathscr{s,a,r,s'\in D}}\left( f(s,a) - r - \gamma\max_{a'}f_t(s',a') \right)^2
    ```

*   After K iterations, return \pi(s) = \arg\max\_a f\_K(s,a),\forall s

### Why we could expect it to work?

*   Near Bellman completion means regression target \mathscr{T}f\_t nearby belongs to \mathscr{F}

    ```undefined
    \mathbb{E}_{s,a\sim\nu} (f_{t+1}(s,a)-\mathscr{T}f_t(s,a))^2 \approx \frac 1 N + \epsilon_{appprox, \nu}
    ```

*   f\_{t+1} \approx \mathscr{T}f\_t(under the diverse \nu)

### Theorem

Fixed iteration number K, with probability at least 1-\delta,

```undefined
V^*-V^\pi \le O \left(\frac 1 {(1-\gamma)^4}\sqrt{\frac{C\ln(|\mathscr{F}|K/\delta)}{N}} + \frac 1 {(1-\gamma)^3}\sqrt{C\epsilon_{approx, \nu}}\right) + \frac {2\gamma^K} {(1-\gamma)^2}
```

*   Least Squares regression ensure near Bellman consistency

    *   Denote: \hat f := \arg\min\_{f\in\mathscr{F}}\sum
        \_{i=1}^N(f(x\_i)-y\_i)^2 as the least square minimizer, then with probability 1-\delta:

        ```undefined
        \mathbb{E}_{x\sim\nu}\left(\hat f(x) - f^*(x)\right)^2\le O \left( \frac {Y^2\ln|\mathscr{F}|/\delta}{N} + \epsilon \right)
        ```

    *   Via small inherent BE, we know that \min\_{\mathscr{f \in F}} \mathbb{E}*{s,a\sim\nu}(f(s,a)-\mathscr{T}f\_t(s,a))^2\le\epsilon*{approx, \nu}

    ```undefined
    \mathbb{E}_{s,a\sim\nu}(f_{t+1}(s,a)-\mathscr{T}f_t(s,a))^2 \le \frac 1 {(1-\gamma)^2} \frac{\ln(|\mathscr{F}|/\delta)}N+\epsilon_{approx, \nu}
    ```

    *   Let \epsilon\_{regress} =\sqrt{\frac 1 {(1-\gamma)^2} \frac{\ln(|\mathscr{F}|/\delta)}N+\epsilon\_{approx, \nu}}

*   Near Bellman consistency implies convergence

    *   Consider any state-action distribution \beta(s,a) and

        ```undefined
        \sqrt{\mathbb{E}_{s,a\sim\beta}(f_t(s,a)-Q^*(s,a))^2}:= ||f_t-Q^*||_{\beta,2}\le \mathscr{||f_t - Tf_{t-1}||_{2,\beta}+||T}f_{t-1}-Q^*||_{2,\beta}
        ```

    *   Apply 1, then this is smaller than \sqrt{C}\epsilon\_{regress} + \gamma ||f\_{t-1}-Q^\*||\_{2, \beta'}

    *   Do it until t = 0, then ||f\_t-Q^\*||*{\beta,2} \le \frac{\sqrt{C}\epsilon*{regress}}{1-\gamma}+\gamma^k/(1-\gamma)

*   Turn in error ||f\_k - Q^\*||\_{2,\beta} to policy \pi^k performance

    ```undefined
    V^* - V^{\pi_k} =\mathbb{E}_{s_0\sim\mu} [Q^*(s_0, \pi^*(s_0)) - Q^{\pi^k}(s_0, \pi^k(s_0)]\\=\frac{1}{1-\gamma}\mathbb{E}_{s\sim d^{\pi^k}}[Q^*(s,\pi^*(s))-Q^*(s, a)] \\ \le \frac 1{1-\gamma}\mathbb{E}_{s\sim d^{\pi^k}}[Q^*(s,\pi^*(s))-f_k(s,\pi^*(s))+f_k(s, \pi^k(s))-Q^*(s, a)] 
    ```

    *   This converges by 2
