---
id: edbf4616-f689-4977-ad1e-5b8ace47ea26
title: MLT Chapter 1,2,3
created_time: 2023-09-25T04:32:00.000Z
last_edited_time: 2023-09-27T08:23:00.000Z
하위 항목: []
subclass: Machine Learning Theory
class: RL
작성일시: 2023-09-25T04:32:00.000Z
상위 항목: []

---

# 1. Supervised Learning Formulations

## 1.1 Supervised Learning

*   Precisely, we seek to find a model h that minimizes what we call the expected loss

    ```undefined
    L(h) \triangleq \mathbb E_{(x, y)\sim p}[l(h(x), y)]
    ```

*   Hypothesis class: Given one particular function h \in \cal H, we define the excess risk of h with respect to \cal H as the difference between the population risk of h and best possible population risk inside \cal H:

    ```undefined
    E(h) \triangleq L(h) - \inf_{g\in\cal H}L(g)
    ```

## 1.2 Empirical risk minimization

*   We define the empirical risk of a model h as

    ```undefined
    \hat L(h_\theta) \triangleq \frac 1n \sum_{i=1}^n l\left(h_\theta(x^{(i)}), y^{(i)}\right) = l\left((x^{(i)}, y^{(i)}), \theta\right)
    ```

*   Empirical risk minimization is the method of finding the minimizer of \hat L, which we call \hat\theta

    ```undefined
    \hat\theta\triangleq\argmin_{\theta\in\Theta}\hat L(h_\theta)
    ```

*   Since we are assuming that our training examples are drawn from the same distributions as the whole population, we know that empirical risk and population risk are equal in expectation

    ```undefined
    \mathbb E_{(x^{(i)}, y^{(i)})\sim P} = L(h_\theta)
    ```

*   It is an unbiased estimator of the population risk

# 2. Asymptotic Analysis

## 2.1 Asymptotics of empirical risk minimization

> 📖 We want to prove

    ```undefined
    L(\hat\theta)-\inf_{\theta\in\Theta}L(\theta)\le \frac cn + o\left(\frac 1n\right)
    ```
