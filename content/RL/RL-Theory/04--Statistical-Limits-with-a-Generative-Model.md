---
id: a8b18c9d-65b8-44b1-962d-3e943a9749f4
title: 04. Statistical Limits with a Generative Model
created_time: 2023-06-28T14:09:00.000Z
last_edited_time: 2023-08-17T06:46:00.000Z
cover_image: https://www.notion.so/images/page-cover/webb3.jpg
하위 항목: []
subclass: RL Theory
class: RL
작성일시: 2023-06-28T14:09:00.000Z
pdf: https://wensun.github.io/CS6789_data/Sample_Complexity_annotated.pdf
상위 항목: []
_thumbnail: https://www.notion.so/images/page-cover/webb3.jpg

---

> 💡 Given an MDP \mathscr{M} = (S,A,P,r,\gamma) how many observed transitions do we need to estimate Q^\*?

# A generative model

*   A generative model provides sample s' \sim P(\cdot|s,a) upon input of a state action pair (s,a)

    ```undefined
    \hat P (s'|s,a) = \frac {\text{count}(s',s,a)}{N}
    ```

*   Each sample calls the generative model SA times, so total number of call is SAN

*   Since P has a S^2A parameters, a naive approach to estimate P uses O(S^2A) samples

## Naive model-based approach

### Model Accuracy

*   C is an absolute constant. \epsilon > 0. For N \ge \frac{c\gamma}{(1-\gamma)^4}\frac{S\log(cSA/\delta)}{\epsilon^2}and with probability greater than 1-\delta

*   The transition model is \epsilon has error bounded as

    ```undefined
    \max_{s,a} || P(\cdot|s,a) - \hat{P}(\cdot|s,a)||_1 \le (1-\gamma)^2\epsilon/2
    ```

*   Uniform value accuracy: For all policies π, ||Q^\pi - \hat Q^\pi||\_\infty \le \epsilon/2

### Matrix Expressions

*   Define P^\pi to be the transition matrix on state-action pairs with Q^\pi = r+\gamma PV^\pi ,     Q^\pi = r + \gamma P^\pi Q^\pi and that Q^\pi = (I - \gamma P^\pi)^{-1}r

### Simulation Lemma

*   For all \pi, we have

    ```undefined
    Q^\pi - \hat Q^\pi = \gamma(I-\gamma \hat P^\pi)^{-1}(P-\hat P)V^\pi
    ```

## Sublinear Sample complexity

### Crude Value Bound

*   Let \delta \ge 0. With probability greater than 1-\delta

    ```undefined
    ||Q^* - \hat Q^*||_\infty \le \frac{\gamma}{(1-\gamma)^2}\sqrt{\frac{2\log(2SA/\delta)}{N}} \\ ||Q^* - \hat Q^{\pi^*}||_\infty \le \frac{\gamma}{(1-\gamma)^2}\sqrt{\frac{2\log(2SA/\delta)}{N}} \\ ||Q^* - Q^{\hat\pi *}||_\infty \le \frac{\gamma}{(1-\gamma)^3}\sqrt{\frac{2\log(2SA/\delta)}{N}}
    ```

## Minimax optimal sample complexity

*   With probability greater than 1-\delta,

    ```undefined
    ||Q^* - \hat Q^*||_\infty \le \sqrt{\frac{c}{(1-\gamma)^3}{\frac{\log(cSA/\delta)}{N}}}+\frac{c}{(1-\gamma)^3}{\frac{\log(cSA/\delta)}{N}}
    ```

    where c is an absolute constant

*   For \epsilon < 1, provided N \ge \frac{c}{(1-\gamma)^3}{\frac{\log(cSA/\delta)}{\epsilon ^2}} then ||Q^*-\hat Q^*||\_\infty\le\epsilon with probability greater than 1-\delta

*   For \epsilon < \sqrt{1/(1-\gamma)}, provided N \ge \frac{c}{(1-\gamma)^3}{\frac{\log(cSA/\delta)}{\epsilon ^2}} then ||Q^*-Q^{\hat\pi*}||\_\infty\le\epsilon with probability greater than 1-\delta → lower bound!

## Bellman Equation for the variance

*   Variance \text{Var}*P(V)(s,a) := \text{Var}*{P(\cdot|s,a)}(V)

*   Component wise variance \text{Var}\_P(V):=P(V)^2 - (PV)^2

*   Define \Sigma\_M^\pi as the variance of discounted reward

    ```undefined
    \Sigma_M^\pi(s,a):= \mathbb{E} \left[\left( \sum_{t=0}^\infty \gamma^t r(s_t,a_t)-Q_M^\pi (s,a) \right)^2 | s_0=s, a_0=a \right]
    ```

*   Bellman equation for total variance

    ```undefined
    \Sigma_M^\pi = \gamma^2 \text{Var}_P(V_M^\pi)+\gamma^2 P^\pi \Sigma_M^\pi
    ```

*   Lemma: For any policy π and MDP M,

    ```undefined
    || (I-\gamma P^\pi)^{-1}\sqrt{\text{Var}_P(V_M^\pi)}||_\infty \le \sqrt{\frac{2}{(1-\gamma)^3}}
    ```

    *   Proof idea: convexity + Bellman equation for the variance
