---
id: 3401832b-1c45-4b6e-969e-2a3045678a59
title: Foster&Rakhlin Chapter 2
created_time: 2023-10-15T07:25:00.000Z
last_edited_time: 2023-10-20T04:03:00.000Z
하위 항목: []
subclass: Foster&Rakhlin
class: RL
작성일시: 2023-10-15T07:25:00.000Z
pdf: >-
  https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/184eb728-0fe6-4cbc-bd94-9f27ef8f958a/Foster_Rakhlin_Notes.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20231024%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20231024T004159Z&X-Amz-Expires=3600&X-Amz-Signature=b7e68faf8946b854e6eab9025eae2d9e42b7cbf68b7ef03bcc5c7f6af0a76068&X-Amz-SignedHeaders=host&x-id=GetObject
상위 항목: []

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

    which is equivalent to definition

*   Proof

    *   Hoeffding’s inequality

        ```undefined
        \mathbb P(\sum_{i=1}^T(X_i-\mathbb E[X_i])\ge t)) \le \exp(-\frac{2t^2}{\sum_{i=1}^T (b_i-a_i)^2})
        ```
