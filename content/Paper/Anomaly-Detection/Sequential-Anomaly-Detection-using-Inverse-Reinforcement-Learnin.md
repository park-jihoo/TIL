---
id: 01c90d03-68f0-470b-b9e3-d6c2834baad4
title: Sequential Anomaly Detection using Inverse Reinforcement Learning
created_time: 2024-01-17T04:52:00.000Z
last_edited_time: 2024-02-01T09:04:00.000Z
하위 항목: []
subclass: Anomaly Detection
class: Paper
작성일시: 2024-01-17T04:52:00.000Z
pdf: https://arxiv.org/pdf/2004.10398.pdf
상위 항목: []

---

# Introduction

*   Anomaly detection refers to identification of unforeseen or abnormal phenomena embedded in a large amount of normal data

*   One of the most interesting application scenarios in anomaly detection is when sequential datas are targeted → This is more complex then static anomalies

*   The main contribution of this paper is,

    *   First time to use inverse RL

    *   Incorporating model uncertainty in the IRL problem

    *   Incorporate trajectories with varying lengths

    *   Publicly available real-word data shows this method is effective

# Related work

*   There are a number of different methods available for outlier detection, including supervised approaches, distance-based, density-based, model-based and isolation-based methods

*   Sequential anomaly detection methods, which usually uses object trajectories of tracked things.

    *   One paper uses Gaussian Mixture Model to parametrize trajectories and an incremental one-class learning approach.

    *   Another paper introduces sparse reconstruction analysis that construct a normal dictionary set

    *   Another paper present a method for monotirong anomalies over continuous trajectory streams by using the local continuity characteristics of trajectories to cluster trajectories on a local level

*   However, many of the previous methods require **feature engineering** to perform analysis or preprocessing of the data

*   There are some methods that utilize clustering approaches, but that’s designed to be used in **batch-based** method, and cannot be used on online learning.

*   Artificial neural network and availability of larger dataset allowed the used of deep learning in the domain of anomaly detection.

    *   However, their evaluation uses either only univariate time series or time series with more regularity.

    *   Also, these methods typically requires the **fixed** length of sequences

*   There are also other work which uses forward RL to detect anomaly, but these methods require the **predefined notion of reward signals** whereas our approach is to infer such reward functions since it’s unknown.

# Preliminaries

## Forward and Inverse RL Basics

*   We assume the environment is modeled as a **Markov Decision Process** \braket{ S,A,T,R,\gamma,p\_0} where S is the finite set of states; A is the finite set of actions, T(s,a,s') is the state transition probability of changing to state s' from s when action a is taken; r(s,a) is the immediate reward of executing action a in state s; \gamma\in\[0,1) is the discount factor; p\_0(s) denotes the probability of starting in state s

*   In (forward) RL, \pi^\* is the policy to be learned, but in IRL reward function is not explicitly given. We need to learn r^\*(\cdot) such that

    ```undefined
    \mathbb E\left[\sum_{i=0}^\infty \gamma^t r^*(s_t,a_t)|\pi^*\right]\ge \mathbb E\left[\sum_{i=0}^\infty \gamma^t r^*(s_t,a_t)|\pi\right] ,\forall \pi
    ```

*   In IRL, not optimal policy is given but samples or demonstrations are given.

## Maximum Entropy IRL

*   Maximum Entropy IRL framework models the demonstrations using a Boltzmann distribution

    ```undefined
    p(\tau|\theta)=\frac1Z\exp(r(\tau|\theta))
    ```

*   The parameters \theta are chosen to maximize the likelihood of the deminstrated trajectories

    ```undefined
    \begin{aligned}\mathcal L(\theta) &= \frac 1M\sum_{m=1}^M\log p(\tau_m|\theta)\\&=\frac1M\sum_{m=1}^M R(\tau_m|\theta)-\log\sum_\tau\exp(R(\tau|\theta))\end{aligned}
    ```

## Bayesian Framework for IRL(BIRL)

> 💡 Use a prior to encode the reward preference and to formulate the compatibility with the demonstrator’s policy as likelihood

*   Prior is,

    ```undefined
    P(r)=\prod_{(s,a)\in\Tau} P(r(s,a))
    ```

*   The likelihood in BIRL is defined as independent exponential distribution analogus to the softmax function

    ```undefined
    \begin{aligned}P(r|\Tau)&=\prod_{\tau\in\Tau}\prod_{(s,a)\in\tau}P(a|s,r)\\&\propto P(\Tau|r)P(r)\end{aligned}
    ```

# Method

## Approximate Posterior Distribution

## Parameter Update

## Algorithm Overview

## Normality Score

## Incorporating Model Uncertainty when deciding an Anomaly

# Experiments

## Datasets

## Comparison with other methods

## Evaluation Metrics

## Results
