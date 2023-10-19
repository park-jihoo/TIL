---
id: 3401832b-1c45-4b6e-969e-2a3045678a59
title: Foster&Rakhlin Chapter 2
created_time: 2023-10-15T07:25:00.000Z
last_edited_time: 2023-10-17T15:29:00.000Z
하위 항목: []
subclass: Foster&Rakhlin
class: RL
작성일시: 2023-10-15T07:25:00.000Z
pdf: >-
  https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/184eb728-0fe6-4cbc-bd94-9f27ef8f958a/Foster_Rakhlin_Notes.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20231019%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20231019T004205Z&X-Amz-Expires=3600&X-Amz-Signature=6e5f3160e068883bff0c038af01f6dc766c52cb0c5eca8a6ebc40889fd4474bc&X-Amz-SignedHeaders=host&x-id=GetObject
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

## Regret
