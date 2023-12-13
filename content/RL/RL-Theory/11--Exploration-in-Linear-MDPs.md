---
id: 1589c10b-ac1b-40a3-9eaa-817912b596d6
title: 11. Exploration in Linear MDPs
created_time: 2023-07-13T08:59:00.000Z
last_edited_time: 2023-08-17T06:46:00.000Z
cover_image: https://www.notion.so/images/page-cover/webb3.jpg
하위 항목: []
subclass: RL Theory
class: RL
작성일시: 2023-07-13T08:59:00.000Z
pdf:
  - https://wensun.github.io/CS6789_data_fall_2021/linearMDPs_annotated.pdf
  - https://wensun.github.io/CS6789_data_fall_2021/linearMDPs_2_annotated.pdf
상위 항목: []
_thumbnail: https://www.notion.so/images/page-cover/webb3.jpg

---

*   Lemma \[Self Normalized bound for vector-valued martingales]

    Suppose {\epsilon\_n}*{n=1}^\infty are mean zero random variables with |\epsilon\_n|\le\alpha,\forall n; Let {x\_i \in \R^d}*{n=1}^\infty be some stochastic random process. Define \Lambda^n = \lambda I + \sum\_{i=1}^nx\_ix\_i^\top, then with probability at least 1-\delta, \forall n \ge 1,

    ```undefined
    \left\| \sum_{i=1}^nx_ie_i \right\|^2 \le 2\delta^2\ln\left(\frac{\det(\Lambda^n)^{1/2}\det(\lambda I)^{-1/2}}\delta\right)
    ```

> 💡 Can we extend discrete MDPs to some kind linear MDPs?

# Introduction of low-rank MDP

## Notations and Useful Inequalities

*   For real-value matrix A

    ```undefined
    ||A||_F^2 = \sum_{i,j}A_{i,j}^2 \ ||A||_2 = \sup_{x:\|x\|_2 \le1}\|Ax\|_2 \le \|A\|_2\|x\|_2
    ```

*   For positive definite matrix \Lambda

    ```undefined
    \det(\Lambda)=\prod_{i=1}^d\sigma_i, \ \|x\|_\lambda^2 = x^\top\Lambda x \\ \mathbb{E}_{s'\sim P_h(\cdot|s,a)}f(s') = P_h(\cdot|s,a)\cdot f
    ```

## Definition of Low-rank MDP

*   Finite horizon time-dependent episodic MDP \mathscr{M} = {S,A,H,{r}\_h,{P}\_h, s\_0 }, S & A could be large or even continuous, hence poly(S,A) is not acceptable

    ```undefined
    P_h(s'|s,a) = \mu_h^*(s') \cdot \phi(s,a), \ \mu_h^* \in S \rightarrow \R^d, \ \phi \in S\times A \rightarrow \R^d\\r(s,a) = \theta_h^*\cdot \phi(s,a), \theta_h^* \in \R^d
    ```

*   Feature map \phi is known to the learner!

## Example

### Linear MDP

*   Generalize tabular MDP: \phi(s,a) is one-hot vector, and P(\cdot|s,a) = P\_\phi(s,a) where P \in \R^{|S|\times|SA|} is the transition matrix

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/73c05bfe-8868-449c-bc3e-1445af5a630f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256\&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD\&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20231213%2Fus-west-2%2Fs3%2Faws4_request\&X-Amz-Date=20231213T004436Z\&X-Amz-Expires=3600\&X-Amz-Signature=cec86042a169086b0e100807b2c1ff9087a201394f5a2b3fb71a79286bac481d\&X-Amz-SignedHeaders=host\&x-id=GetObject)

### Low-Rank

*   Can encode latent variables

*   Discrete latent state space S: |S| is small, transition T : S \times A \rightarrow S

*   Large observation space X( hense any poly dependency on |X| is bad)

*   Each state s has an emission distribution \mu\_s \in \Delta(X), also \mu\_s, \mu\_{s'} have disjoint support for any s \not= s'

    ```undefined
    P(x'|x,a) = \sum_{s'\in\{s_1,s_2,s_3\}}T(s'|\omega(x),a)\mu_{s'}(x')
    ```

# Planning in low-rank MDP and UCBVI algorithm

## Value Iteration

*   initialize V\_H^\*(s) = 0, \forall s

*   Q\_H^*(s,a) = r\_h(s,a) + \mathbb{E}*{s'\sim P\_h(\cdot|s,a)}V*{h+1}^*(s') = \phi(s,a)^\top w\_h

*   V\_h^*(s) = \max\_a \phi(s,a)^\top w\_h, \pi\_h^*(s) = \arg\max\_a \phi(s,a)^\top w\_h

## Apply UCBVI

At the beginning of iteration n:

*   Learn transition model {\hat P\_h^n }*{h=0}^{H-1} from all previous data {s\_h^i, a\_h^i, s*{h+1}^i}\_{i=0}^{n-1}

*   Design reward bonus b\_n^n(s,a),\forall s,a

*   Plan \pi^{n+1} = VI({\hat P^n}\_h, {r\_h+b\_h^n})

*   Execute \pi^{n+1} for H steps

# Non-parametric model learning in Linear MDPS

*   Additional Assumptions in Linear MDPs to permit linear regression analysis

    ```undefined
    \sup\| \phi(s,a)\|_2 \le1, \|\theta_h^*\|_2\le W, \|v^\top\mu_h^*\|_2\le\sqrt{d} ,\forall v \text{ s.t.} \|v\|_\infty\le1
    ```

## Model Learning in Linear MDPs

```undefined
\hat\mu_h^n - \mu_h^* = -\lambda\mu_h^*(\Lambda_h^n)^{-1} + \sum_{i=1}^{n-1}\epsilon_h^i \phi(s_h^i,a_h^i)^\top(\Lambda_h^n)^{-1}
```

Lemma(model average error under a fixed V)

*   Consider a fixed V : S \rightarrow\[0,H]. With probability at least 1-\delta, for all s,a,n,h, we have:

    ```undefined
    \left|\left(\hat P_h^n(\cdot|s,a) - P_h(\cdot|s,a) \right)\cdot V\right| \le \|\phi(s,a)^\top\|_{(\Lambda_h^n)^{-1}}\times \left(2H\sqrt{\frac{H\det(\Lambda_h^n)^{1/2}\det(\lambda I)^{-1/2}}{\delta}}+H\sqrt{\lambda D} \right) = \widetilde{O}(H\sqrt{d} + H\sqrt{\ln(1/\delta)})\|\phi(s,a)\|_{(\Lambda_h^n)^{-1}}
    ```

> Can we get a uniform convergence argument for a function class \mathscr{F}?

### Covering argument bound (\hat P(\cdot|s,a) - P(\cdot|s,a))^\top V, \forall V \in \mathscr{F}

Lemma(covering of \Theta)

*   We have \mathscr{|N|*\epsilon} \le (1+2R/\epsilon)^d, and \ln(\mathscr{|N|}*\epsilon) \le d\ln(1+2R/\epsilon), then \epsilon/L - net on \Theta gives us an \epsilon-Net on \mathscr{F} with d(f\_{\theta\_1}, f\_{\theta\_2}):= |f\_{\theta\_1}, f\_{\theta\_2}|\_\infty

Lemma(uniform convergence)

*   With probability at least 1-\delta, and for all s,a,h,n and all f \in \mathscr{F}:

    ```undefined
    \left|\left(\hat P(\cdot|s,a) - P(\cdot|s,a)\right) \cdot f\right| = \widetilde{O}(Hd)\cdot \|\phi(s,a)\|_{(\Lambda_h^n)^{-1}}
    ```

### UCBVI in Linear MDPs

At the beginning of iteration n:

*   Learn transition model {\hat P\_h^n }\_{h=0}^{H-1} from all previous data via Ridge regression

*   Design reward bonus b\_n^h(s,a) = \beta\sqrt{\phi(s,a)(\Lambda\_h^n)^{-1}\phi(s,a)}

*   Plan \pi^{n+1} = VI({\hat P^n}\_h, {r\_h+b\_h^n})

*   Execute \pi^{n+1} for H steps

### Regret bound for UCBVI in linear MDP

```undefined
\mathbb{E}\left[\sum_{n=1}^N\left(V^* - V^{\pi^n}\right) \right] \le \widetilde O(H^2d^{1.5}\sqrt{N})
```

## Value Iteration in Learned model with reward bonus

```undefined
\pi^{n+1} = VI(\{\hat P^n\}_h, \{r_h+b_h^n\})
```

*   \hat Q\_h^n(s,a)=\beta\sqrt{\phi(s,a)(\Lambda\_h^n)^{-1}\phi(s,a)} + \phi(s,a)^\top\hat w\_h^n

*   \hat V\_h^n(s) = \min\left{\max\_a\left(\beta\sqrt{\phi(s,a)(\Lambda\_h^n)^{-1}\phi(s,a)} + \phi(s,a)^\top\hat w\_h^n\right), H \right}, \ \pi\_h^n(s) = \arg\max\_a \hat Q\_h^n(s,a)

## Prove Optimism

With high probability, for all n, h, s

```undefined
\hat V_h^n(s) \ge V_h^*(s)
```

## Regret Decomposition

```undefined
\mathbb{E}\left[\sum_{n=1}^N (V_0^*(s_0) - V_0^{\pi^n}(s_0))\right]\lesssim \beta\mathbb{E}\left[\sum_{h=0}^{H-1}\sqrt N \sqrt{\sum_{n=1}^N\phi(s_h^n,a_h^n)^\top (\Lambda_h^n)^{-1}\phi(s_h^n,a_h^n)} \right] +\delta NH \lesssim \widetilde O (H^2 d^{1.5}\sqrt N)
```
