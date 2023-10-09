---
id: d44a2a7c-6a63-40ec-8404-db80d8e6fd16
title: 07. LSVI in Offline RL
created_time: 2023-07-03T11:10:00.000Z
last_edited_time: 2023-08-17T06:46:00.000Z
cover_image: https://www.notion.so/images/page-cover/woodcuts_14.jpg
하위 항목: []
subclass: RL Theory
class: RL
작성일시: 2023-07-03T11:10:00.000Z
pdf: >-
  https://wensun.github.io/CS6789_data_fall_2021/linear_BC_continue_annotated.pdf
상위 항목: []
_thumbnail: https://www.notion.so/images/page-cover/woodcuts_14.jpg

---

# Offline Reinforcement Learning

*   Learner cannot interact with the environment, instead learner is given **static** datasets

    ```undefined
    \mathscr{D}_h = \{s,a,r,s'\}, s,a\sim\nu, r=r(s,a),s' \sim P_h(\cdot|s,a)
    ```

*   Offline RL is promising for safety critical applications

# LSVI Guarantees…

*   Recall \mathscr{D}\_h = {s,a,r,s'}, s,a\sim\nu, r=r(s,a),s' \sim P\_h(\cdot|s,a)

*   Assumptions

    *   Full offline data coverage: \sigma\_{\min}(\mathbb{E}\_{s,a\sim\nu}\phi(s,a)\phi(s,a)^\top)\ge \kappa

    *   Linear Bellman completion

*   Then, with probability at least 1-δ, LSVI return \hat\pi with V^\*-V^{\hat\pi} \le \epsilon, using at most \text{poly}(H,1/\epsilon,1/\kappa,d,\ln(1/\delta))

*   Proof: Linear Bellman completion + Linear Regression with full data coverage

    *   With N training samples where (s,a)\sim\nu, and r=r(s,a),s'\sim P\_h(\cdot|s,a)m we have

        ```undefined
        \mathbb{E}_{s,a\sim\nu}(\theta_h^\top\phi(s,a)-\mathscr{T}_h(\theta_{h+1})^\top\phi(s,a))^2\le \text{poly}(H,d,1/N)
        ```

        Then with Cauchy-Schwartz, we get

        ```undefined
        \forall s,a, \left|(\theta_h-\mathscr{T}_h(\theta_{h+1}))^\top \phi(s,a)\right| \le ||\theta_h - \mathscr{T}_h(\theta_{h+1})||_\Sigma||\phi(s,a)||_{\Sigma^{-1}}
        ```
