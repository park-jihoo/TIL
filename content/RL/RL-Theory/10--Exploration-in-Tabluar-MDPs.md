---
id: 094d8dc4-d1b8-4c66-8a63-e62ea362d2f7
title: 10. Exploration in Tabluar MDPs
created_time: 2023-07-10T05:54:00.000Z
last_edited_time: 2023-08-17T06:46:00.000Z
cover_image: https://www.notion.so/images/page-cover/met_william_morris_1877_willow.jpg
하위 항목: []
subclass: RL Theory
class: RL
작성일시: 2023-07-10T05:54:00.000Z
pdf: https://wensun.github.io/CS6789_data_fall_2021/UCBVI_annotated.pdf
상위 항목: []
_thumbnail: https://www.notion.so/images/page-cover/met_william_morris_1877_willow.jpg

---

> 💡 Finite horizon distrete mdp \mathscr{M}, only reset from \mu, and unknown transition P → exploration!

# Learning Procotol

*   Learner initializes a policy \pi^1

*   At episode n, learner executes \pi^n: \ {s\_h^n,a\_h^n,r\_h^n}*{h=0}^{H-1} with a\_h^n = \pi^n(s\_h^n),r\_h^n=r(s\_h^n,a\_h^n), s*{h+1}^n \sim P(\cdot|s\_h^n,a\_h^n)

*   Learner updates policy to \pi^{n+1} using all prior information

*   Performance measure : regret \mathbb{E} \left\[\sum\_{n=1}^N (V^\* - V^{\pi^n})\right] = \text{poly}(S,A,H)\sqrt{N}

# Convert MAB into Run UCB
