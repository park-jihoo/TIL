---
id: c5eb60ea-0987-4c58-8c72-c4b37b48a481
title: |-
  Toward Deep Supervised Anomaly Detection:
  Reinforcement Learning from Partially Labeled Anomaly Data
created_time: 2023-08-09T15:25:00.000Z
last_edited_time: 2023-08-17T06:45:00.000Z
cover_image: https://www.notion.so/images/page-cover/webb1.jpg
하위 항목: []
subclass: Anomaly Detection
class: Paper
작성일시: 2023-08-09T15:25:00.000Z
pdf: https://arxiv.org/pdf/2009.06847.pdf
상위 항목: []
_thumbnail: https://www.notion.so/images/page-cover/webb1.jpg

---

> 📖 This paper propose a deep reinforcement learning-based approach that enables end-to-end optimization of the detection of both labeled and unlabeled anomalies

# Related Work

## Anomaly Detection

*   Deep Learning has been explored to enhance the unsupervised approaches(autoencoder or GAN)

*   The most related studies are weakly-supervised anomaly detection methods

*   How to handle Positive-Unlabeled(PU) learning without human intervention?

## DRL-Driven Knowledge

*   Deep Reinforcement Learning(DRL) has demonstrated human level capability(Atari, etc.)

*   A related application used Inverse Reinforcement Learning in sequential anomaly detection

*   Another related application is that used DRL to perform neural architecture search for anomaly detection

# Proposed Approach

## Problem Statement

*   Given a training dataset \mathcal D={\mathcal D^a, \mathcal D^u} with \mathcal{D^a\cup D^u}=\empty composed by small labeled \mathcal D^a and large unlabeled \mathcal D^u. \mathcal D^u contains mostly normal data and a few anomalies from known and unknown anomaly class

*   Our goal is to learn anomaly scoring function \phi:\mathcal D\to\R that assigns anomaly scores to data instances so that \phi(s\_i)>\phi(s\_j) where s\_i,s\_j\in\mathcal D and s\_i can be either known or unknown anomaly and s\_j is a normal instance

## DRL Tailored for anomaly detection

### Foundation of the Proposed Approach

*   **Observation space** in the environment E is define upon the full training data \mathcal D, in which each data instances s\in\mathcal D is an observation

*   **Action space** is defined by {a^0,a^1} with a^0 as normal, a^1 as anomalous

*   **Agent** A is implemented by neural network to seek an optimal action out of two possible actions given an observation s

*   **Simulation Environment** E enable meaningful automatic interaction between our agent and environment. Paper define an anomaly-biased observation sampling function

    ```undefined
    g(s_{t+1}|s_t,a_t)
    ```

    in the environment, which responds differently to the agent with next observation dependent on the observation and the action at t

*   There are two **reward** function defined.

    *   External reward h(r\_t^e|s\_t,a\_t) is defined to provide high rewards for the agent when it’s able to correctly recognized a labeled anomaly observation

    *   Unsupervised intrinsic reward function f(s\_t) is defined to measure the novelty of an observation the agent perceives compared to other observation

*   A combined external and intrinsic reward is then defined c(r^e,r^i) to provide an overall reward

### Procedure of paper’s DRL-based Anomaly Detection

*   At each time stamp t, A receives observation s\_t by g and takes action a\_t to maximize reward.

*   The next observation sampling function g(s\_{t+1}|s\_t,a\_t) in the simulation environment E then responds the agent with a new observation s\_{t+1}. To effectively leverage both \mathcal D^u and \mathcal D^a, g is designed to return possible unlabeled anomalies as many as possible

*   The external reward function h(r\_t^e|s\_t,a\_t) further produces a positive reward r\_t^e for the agent if it correctly recognize the labeled anomaly observation s\_t \in \mathcal D^a. This enforces agent to learn the abnormality of the known anomalies

*   The intrinsic reward function f(s\_t) subsequently produces unsupervised reward r\_t^i for the agent, to make agent detect unlabeled anomalies

*   A receives combined reward r\_t=c(r\_t^e,r\_t^i)

# Proposed Model(DPLAN)

## DQN-based Anomaly Detection Agent A

*   The value function can be approximated as Q function

    ```undefined
    Q^*(s,a) = \max_\pi\mathbb E[r_t+\gamma r_{t+1}+\gamma^2 r_{t+2}+\cdots|s_t=s,a_t=a,\pi]
    ```

    which is the maximum expected return starting from s

*   DQN will be used, and it learns \theta=Q^\*(s,a). It minimizes

    ```undefined
    L_j(\theta_j)=\mathbb E_{(s,a,r,s')\sim U(\cal E)}\left[\left(r+\gamma \max_{\alpha'}Q(s',a';\theta_j^-)-Q(s,a;\theta_j)\right)\right]
    ```

    where \cal E is the set of agent’s learning experience and the loss is calculated using minibatch samples drawn uniformly

## Proximity-driven Observation Sampling g

*   g is composed by 2 functions g\_a and g\_u to balance exploration and exploitation of full data \cal D

*   g\_a uniformly samples s\_{t+1} from \cal D^a at random(s\_{t+1}\sim U(\cal D^a))

*   g\_u is a function that samples s\_{t+1} from \cal D^u based on the proximitiy of current observation.

    ```undefined
    g_u(s_{t+1}|s_t,a_t;\theta^e)=\begin{cases}\argmin_{s\in \cal S} d(s_t,s;\theta^e)&\text{if }a_t=a^1 \\\argmax_{s\in\cal S}d(s_t,s;\theta^e)&\text{if }a_t=a^0\end{cases}
    ```

    where \cal S \in D^u is a random subsample, \theta^e are the parameters of \psi(\cdot;\theta^e) that is a feature embedding function of last hidden layer of DQN

    *   g\_u returns the nearest neighbor of s\_t when the agent believes s\_t is an anomaly and takes a^1. If it believes s\_t a normal observation then returns farthest neighbor of s\_t and takes a^0

    *   The nearest and farthest neighbors are approximated on subsample \cal S for efficiency

*   With probability p the simulator performs g\_a and with probability 1-p the simulator performs g\_u. This way enables the agent to sufficiently exploit the small labeled anomaly data while exploring large unlabeled data.

## Combining external and Intrinsic rewards

### Labeled Anomaly Data-based External Reward Function h

```undefined
r_t^e=h(s_t,a_t)=\begin{cases}1&\text{if }a_t=a^1\text{ and }s_t\in\cal D^a\\0&\text{if }a_t=a^0\text{ and }s_t\in\cal D^u\\-1&\text{otherwise}\end{cases}
```

*   It indicates that the agent receives positive reward only when it correctly labels known anomaly as anomalous

*   It receives no reward if it correctly recognizes normal observations

*   It penalizes with a negative reward for either false negative or false positive detection

### Unsupervised Intrinsic Reward Function f

```undefined
r_t^i=f(s_t;\theta^e)=\text{iForest}(s_t;\theta^e)
```

*   Isolation is defined by the number of steps required to isolate an observation s from the observations in \cal D^u through half-space data partition. iForest is used for computationally efficient calculation.

*   f function also operates on the low dimensional \psi embedding space parametrized by \theta^e. That means both the training and inference are performed on the \psi-based projected Data

*   The output of iForest is rescaled to range\[0,1] and we accordingly have r\_t^i \in\[0,1]

*   The overall reward the agent receives at each step t is

    ```undefined
    r_t = r_t^e+r_t^i
    ```

## Theoretical Analysis

*   Let Q(s,a;\theta^*) be the Q network with the learned \theta^* after training, and Q(\hat s, a;\theta^*) outputs an estimated value of taking action a^0 or a^1 given a test observation \hat s. Q(\hat s,a^1;\theta^*) can be used as anomaly score

*   Let \pi be policy by Q, then

    ```undefined
    q_\pi(\hat s,a^1)=\mathbb E_\pi\left[\sum_{n=0}^\infty\gamma^nr_{t+n+1}|\hat s,a^1 \right]
    ```

*   Let \hat s^i,\hat s^j, \hat s^k be labeled anomaly, unlabeled anomaly and unlabeled normal observations. We have

    ```undefined
    h(\hat s^i,a^1)>h(\hat s^j,a^1)>h(\hat s^k,a^1).f(\hat s^i;\theta^e)\approx f(\hat s^j;\theta^e)>f(\hat s^i;\theta^e)
    ```

    also holds provided that f well captures the abnormality of the threee observations

*   Under the same policy \pi, this holds

    ```undefined
    q_\pi(\hat s^i,a^1)>q_\pi(\hat s^j,a^1)>q_\pi(\hat s^k,a^1)
    ```
