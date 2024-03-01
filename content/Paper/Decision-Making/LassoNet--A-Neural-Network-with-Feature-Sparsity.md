---
id: 42f801c9-5acd-4b25-a258-a51414b4cdc3
title: 'LassoNet: A Neural Network with Feature Sparsity'
created_time: 2023-11-22T03:43:00.000Z
last_edited_time: 2023-11-30T11:18:00.000Z
하위 항목: []
subclass: Decision Making
class: Paper
작성일시: 2023-11-22T03:43:00.000Z
pdf: https://arxiv.org/pdf/1907.12207.pdf
상위 항목: []
_thumbnail: >-
  https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/c08d75eb-1723-4523-b630-4165a0571849/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240301T004648Z&X-Amz-Expires=3600&X-Amz-Signature=0ac16eb686b7bf31388ab8f40906e4211cd6b946548a4efb7b992b45d33e26a2&X-Amz-SignedHeaders=host&x-id=GetObject

---

> 💡 We introduce LassoNet, a neural network framework with global feature selection. LassoNet uses projected proximal gradient descent, and generalizes directly to deep networks

# Introduction

## Background

*   We discuss related work on feature selection

*   Section 2 formulates the problem from a non-parametric model selection perspective

*   Section 3 introduces our main proposal, and optimization is presented in Section 4

*   In Section 5, we conduct an experiments with several real-world datasets

*   Section 6 and 7 offer extension of LassoNet to the unsupervised learning setting and to the matrix completion problem

*   Section 8 discusses other possible extensions

## Related Works

*   Filter methods operate independently of the choice of the predictor by selecting individual features that maximize the desired criteria

*   Wrapper methods use learning algorithms to evaluate subsets of features based on their predictive power

*   Embedded methods use specific predictors to select features, and are generally able to detect interactions and redundancies among features

## Proposed Method

*   Our procedure uses an input-to-output-skip-layer connection that allows a feature to have non-zero weights in a hidden unit only if its skip-layer connection is active

# Problem Formulation

*   We assume a data-generating mode p(x,y) over a d-dimensional space, where x\in\R^d is the covariate and y is the response, such as class labels.

*   We seek to minimize the empirical reconstruction error

    ```undefined
    \min_{\cal f \in F,S}\hat{\mathbb E}\left[l(f(x_S), y)\right]
    ```

    where S\sube {1,2,...,d} is a subset of features and l is a loss function specified by the user.

# Our proposal: LassoNet

## Background and notation

*   Here we choose \cal F to be the class of residual feed-forward neural networks:

    ```undefined
    \mathcal F = \{f\equiv f_{\theta,W}:x \to \theta^\top x+g_W(x)\}
    ```

    where the width and depth of the network are arbitrary.

*   Throughout the paper,

    *   n denotes the total number of training observations

    *   d denotes the data dimension

    *   g\_W denotes a feed-forward network with weights W

    *   K denotes the number of units in the first hidden layer

    *   W^{(1)}\in\R^{d\times K} denotes the weights in the first hidden layer, and \theta\in\R^d denotes the weights in the residual layer

    *   L(\theta, W)=\frac 1n \sum\_{i=1}^n l(f\_{\theta, W}(x\_i), y\_i) is the empirical loss on the training data set

    *   \mathcal S\_\lambda(x)=\text{sign}(x)\cdot\max{|x|-\lambda, 0} is the soft-thresholding operator

*   LassoNet consists of two main ingredients

    *   A **penalty** is introduced to the original empirical risk minimization that encourages features parsity.

    *   A **proximal** **algorithm** is applied in a mathematically elegant way, so that it admits a simple and efficient implementation on top of back-propagation

## Formulation

*   Objective function is

    ```undefined
    \begin{aligned}\text{minimize}_{\theta, W} &&L(\theta, W)+\lambda ||\theta||_1\\\text{subject to} &&\left\|W_j^{(1)}\right\|_\infty\le M|\theta_j|, j=1,...,d\end{aligned}
    ```

*   The key idea is the constraint

    ```undefined
    |W_{jk}^{(1)}|\le M\cdot |\theta_j|, k=1,...,K
    ```

*   This formulation has several benefits

    *   It promotes the linear component of the signal above the nonlinear one and uses it to guide feature sparsity.

    *   The linear and non-linear components are fitted simultaneously, allowing the network to capture the arbitrary nonlinearity in the data

    *   The LassoNet regularization path can be trained at a cost that is essentially that of training a single model

## Hyper-parameter tuning

*   The l\_1 penalty coefficient, \lambda controls the complexity of fitted model

*   The hierarchy coefficient M, controls the relative strength of the linear and nonlinear components

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/c08d75eb-1723-4523-b630-4165a0571849/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256\&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD\&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240301%2Fus-west-2%2Fs3%2Faws4_request\&X-Amz-Date=20240301T004648Z\&X-Amz-Expires=3600\&X-Amz-Signature=0ac16eb686b7bf31388ab8f40906e4211cd6b946548a4efb7b992b45d33e26a2\&X-Amz-SignedHeaders=host\&x-id=GetObject)

# Optimization

## Warm starts: a path from dense to sparse

*   To optimize LassoNet we find that a dense-to-sparse warm start approach is far more effective than a sparse-to-dense approach.

## Hierarchical proximal optimization

*   The objective is optimized using proximal gradient descent. The key novelty is a numerically efficient algorithm for the proximal inner loop

    ```undefined
    \begin{aligned}\text{minimize}_{b\in\R,W\in\R^k}&&\frac 12(v-b)^2+\frac 12\|u-W\|^2_2+\lambda|b|\\\text{subject to}&& \|W\|_\infty\le M|b|\end{aligned}
    ```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/1597b596-d420-42c6-a83a-633202774eb0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256\&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD\&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240301%2Fus-west-2%2Fs3%2Faws4_request\&X-Amz-Date=20240301T004648Z\&X-Amz-Expires=3600\&X-Amz-Signature=28f781beac5923196f4fcd0d99a8e6587104d9f4f1627fd0508854d1b33ded46\&X-Amz-SignedHeaders=host\&x-id=GetObject)

## Computational Complexity

*   The bulk of the computational cost occurs when training the dense network

*   Subsequently, trianing over the \lambda path is computationally cheap

## Bias due to regularization

*   If the goal is to perform feature selection, this has no consequence on the training of LassoNet.

*   If the goal is to get optimal predictive performance, it can be helpful to debias LassoNet

# Experiments

## Data Sets

*   Mice Protein, MNIST, MNIST-Fashion, ISOLET, COIL-20, Smartphone Activity

## Methodology

*   Benchmarked each feature selection method with varying number of features

## Results

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/7922b0df-8bc6-44c3-8397-9cffb4ec004c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256\&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD\&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240301%2Fus-west-2%2Fs3%2Faws4_request\&X-Amz-Date=20240301T004648Z\&X-Amz-Expires=3600\&X-Amz-Signature=1349233f90f7a288ed7e5c3c2d08252eaca9dfa48bdb797560457420b4fa6c77\&X-Amz-SignedHeaders=host\&x-id=GetObject)

# Extension to Unsupervised Feature Selection

## Background

*   An unsupervised approach becomes relevant in order to identify the most important features in the dataset, and whether there are redundant features that do not need to be mearused

## Training

*   We consider the reconstruction loss L(\theta, W)=\left|f\_{\theta,W}(X)-X\right|^2\_F, where |\cdot|\_F denotes the Frobenius matrix norm

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/ed7fd0bc-5b40-4c40-8d01-07293e99e353/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256\&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD\&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240301%2Fus-west-2%2Fs3%2Faws4_request\&X-Amz-Date=20240301T004648Z\&X-Amz-Expires=3600\&X-Amz-Signature=c3cb36f17cdc2c13a2da32b0941c4d9dd2ccf14791645baca774bc67c4ce0585\&X-Amz-SignedHeaders=host\&x-id=GetObject)

## Selected Digits for Single Classes in MNIST

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/5a911a15-325c-42c9-8bca-ec42c9296c4e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256\&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD\&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240301%2Fus-west-2%2Fs3%2Faws4_request\&X-Amz-Date=20240301T004648Z\&X-Amz-Expires=3600\&X-Amz-Signature=8df402439f8e2f3a6e626b55ab40d892cd93ff50c63f7fc6a1e94fe5e90d972d\&X-Amz-SignedHeaders=host\&x-id=GetObject)

# Extension to Matrix Completion

> 💡 What if the observed data are in the form of a large sparse matrix, Z\_{ij},(i,j)\in\Omega where \Omega \sub{1,...,m}\times{1,...,n}

*   First, it trains a feed-forward neural network on the imputation task

*   Once the dense model has been trained, the method performs feature selection using the GROUP-HIER-PROX operator

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/8049d151-4542-47d5-907c-86f6b10e65bb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256\&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD\&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240301%2Fus-west-2%2Fs3%2Faws4_request\&X-Amz-Date=20240301T004648Z\&X-Amz-Expires=3600\&X-Amz-Signature=99c19f55ba3f7a448ff0101038e2488eedb3ca96ea189fdad408867e7720fcd0\&X-Amz-SignedHeaders=host\&x-id=GetObject)
