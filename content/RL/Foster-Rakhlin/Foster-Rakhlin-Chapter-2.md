---
id: 3401832b-1c45-4b6e-969e-2a3045678a59
title: Foster&Rakhlin Chapter 2
created_time: 2023-10-15T07:25:00.000Z
last_edited_time: 2023-10-27T00:36:00.000Z
하위 항목: []
subclass: Foster&Rakhlin
class: RL
작성일시: 2023-10-15T07:25:00.000Z
pdf: >-
  https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/184eb728-0fe6-4cbc-bd94-9f27ef8f958a/Foster_Rakhlin_Notes.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20231028%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20231028T004025Z&X-Amz-Expires=3600&X-Amz-Signature=e621b64a23ab4302c0da30567246a77915b3773f17c4f5e6c921c9d83078bde7&X-Amz-SignedHeaders=host&x-id=GetObject
상위 항목: []
_thumbnail: >-
  https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/473a2256-19a8-4682-ac9e-0a814f88e374/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20231028%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20231028T004025Z&X-Amz-Expires=3600&X-Amz-Signature=f8d0f10e7a1e3e930cce1f016a33d44bd0c0e400324bf942c45e774d79834894&X-Amz-SignedHeaders=host&x-id=GetObject

---

# Multi-Armed Bandit

> 💡 Multi-Armed Bandit Protocol

    for t=1,…,T, do

    	Select decision \pi^t\in\Pi:=\{1,…,A\}

    	Observe reward r^t

*   \Pi: Decision space or action space, with A\in\N denoting the size of the space

*   Based on the decision \pi^t, the learner receives a reward r^t, and goal is to **maximize** the cumulative reward across all T rounds.

> Assumption 1 (Stochastic Rewards): Rewards are generated independently via

    ```undefined
    r^t\sim M^*(\cdot|\pi^t)
    ```

    where M^*(\cdot|\cdot) is the underlying model

*   We define f^*(\pi):=\mathbb E\[r|\pi] as the mean reward under r\sim M^*(\cdot|\pi) and are going to maximize \pi^*=\argmax\_{\pi\in\Pi}f^*(\pi)

## Regret

```undefined
\text{Reg}:= \sum_{t=1}^T f^*(\pi^*)-\sum_{t=1}^T \mathbb E_{\pi^t\sim p^t} f^*(\pi^*)
```

*   Measures how well the learner can identify an action with good reward, measures how well it can maximize reward as it goes

### Partial Feedback(or bandit feedback)

*   노트에서는 example로 의사가 치료법을 정할 때, 환자의 반응은 알 수 있지만 다른 치료법을 시도했을 때 환자가 어떤 반응을 보일지는 모른다고 이야기하는 예시를 들었음

*   Partial feedback은 **exploring** different action에 대한 필요성을 이야기함 → 2.1

*   In particular, information about one action doesn’t reveal information about other action.

*   In this section, regret that scales with \Omega(|\Pi|)=\Omega(A)

> Remark 8 (Other notions of regret)

    ```undefined
    \max_{\pi\in\Pi}\sum_{t=1}^Tr^t(\pi)-\sum_{t=1}^Tr^t(\pi^t)
    ```

    which is equivalent to definition up to O(\sqrt T) factors

*   Proof

    *   Hoeffding’s inequality

        ```undefined
        \mathbb P(\sum_{i=1}^T(X_i-\mathbb E[X_i])\ge t)) \le \exp(-\frac{2t^2}{\sum_{i=1}^T (b_i-a_i)^2})
        ```

# The Need For Exploration

*   First attempt is applying greedy principle

    ```undefined
    \hat f^t(\pi) =\frac1{n^t(\pi)}\sum_{s<t}r^s\mathbb I\{\pi^s=\pi\}
    ```

    where n^t(\pi) is the number of times \pi has been selected up to time t

*   Chosen greedy action is,

    ```undefined
    \pi^t = \argmax_{\pi\in\Pi}\hat f^t(\pi)
    ```

*   This has linear regret \Omega(T)

    > Example

          \Pi = \{1,2\}, and decision 1 has \frac12 reward almost surely, decision 2 has \text{Ber}(3/4) reward.

          Then, with probability 1/4, the greedy algorithm will get struct on action 1 although action 2’s reward(unseen) is optimal

*   We will consider algorithms that **explore** less visited actions to ensure that their estimated rewards are not misleading

# The \varepsilon-greedy Algorithm

> 💡 Let \varepsilon\in\[0,1] be the exploration parameter. At each time t\in\[T], the \varepsilon-greedy algorithm computes the estimated reward function \hat f^t. With probability 1-\varepsilon, the algorithm chooses the greedy decision

    ```undefined
    \hat\pi^t = \argmax_\pi \hat f^t(\pi)
    ```

     and with probability \varepsilon, it samples a uniform random action \pi^t\sim\text{unif}(\{1,…,A\})

*   \varepsilon-greedy action usually plays the greedy action, which is *exploit*

*   Uniform sampling ensures that the algorithm also *explore* unseen action.

> Proposition 4

    Assume that f^*(\pi)\in[0,1] and r^t is 1-sub-gaussian. Then for any T, by choosing \varepsilon appropriately, the \varepsilon-Greedy algorithm ensures that with probabilty at least 1-\delta,

    ```undefined
    \mathbb E[\text{Reg}] \lesssim A^{1/3}T^{2/3}\cdot\log ^{1/3}(AT/\delta)
    ```

*   Proof

> Remark 9 (Explore-then-commit)

    A relative of \varepsilon-Greedy is the explore-then-commit(ETC) algorithm, which uniformly explores actions for first N rounds then estimates rewards based on the data collected and commits to the greedy action for the remaining T-N rounds.

# The Upper Confidence Bound(UCB) Algorithm

*   UCB Algorithm attains a regret bound of the order \widetilde O(\sqrt{AT}), which improves regret bound comparing to \varepsilon-greedy, and is optimal up to logarithmic factors

*   The UCB algorithm is based on the notion of **optimism in the face of uncertainty.**

    *   At each time t, we should adopt the most optimistic perspective of the world possibled given the data collected so far, and then choose the decision \pi^t based on this perspective.

*   For each step t, we can construct **confidence intervals**

    ```undefined
    \underline f^t \bar f^t : \Pi\to\R
    ```

*   With probability at least 1-\delta,

    ```undefined
    \forall t\in[T],\pi\in\Pi,\ f^*(\pi)\in[\underline f^t(\pi), \bar f^t(\pi)]
    ```

![Illustration of the UCB Algorithm. \pi^t optimistically ensures that the suboptimality never greater exceeds the confidence width](https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/473a2256-19a8-4682-ac9e-0a814f88e374/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256\&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD\&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20231028%2Fus-west-2%2Fs3%2Faws4_request\&X-Amz-Date=20231028T004025Z\&X-Amz-Expires=3600\&X-Amz-Signature=f8d0f10e7a1e3e930cce1f016a33d44bd0c0e400324bf942c45e774d79834894\&X-Amz-SignedHeaders=host\&x-id=GetObject)

> Lemma 7

    Fix t, and suppose that f^*(\pi)\in[\underline f^t(\pi),\bar f^t(\pi)] for all \pi, Then the optimistic action

    ```undefined
    \pi^t=\argmax_{\pi\in\Pi}\bar f^t(\pi)
    ```

    has

    ```undefined
    f^*(\pi^*)-f^*(\pi^t)\le \bar f^t(\pi^t)-f^*(\pi^t)\le\bar f^t(\pi^t)-\underline f^t(\pi^t)
    ```

*   Proof

*   This lemma implies that as long as we can build **confidence intervals** for which the width shrinks, the regret for the UCB strategy will be small

*   As long as r^t\in\[0,1], a union bound gives that with probability at least 1-\delta, for all t\in \[T] and \pi\in\Pi,

    ```undefined
    |\hat f^t(\pi)-f^*(\pi)|\le \sqrt{\frac{2\log(2T^2A/\delta)}{n^t(\pi)}}
    ```

    where \hat f^t is the sample mean and n^t(\pi):=\sum\_{i\<t}\mathbb I {\pi^i=\pi}

*   For a given round t, one of these two things can happen

    *   The optimistic action has high reward, so the instantaneous regret is small

    *   The instantaneous regret is large(then confidence width is large and n^t(\pi^t) is small). This only happens in small n^t(\pi^t)

> Proposition 5

    Using the confidence bound [\bar f^t(\pi), \underline f^t(\pi)], the UCB algorithm insures that with a probability at least 1-\delta,

    ```undefined
    \text{Reg}\lesssim \sqrt{AT\log(AT/\delta)}
    ```

*   This result is optimal up to the \log(AT) factor

*   Proof

> Lemma 8 ( Confidence width potential lemma )

    We have

    ```undefined
    \sum_{t=1}^T\frac 1{\sqrt{n^t(\pi^t)}}\land 1\lesssim \sqrt{AT}
    ```
