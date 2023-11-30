---
id: 42f801c9-5acd-4b25-a258-a51414b4cdc3
title: 'LassoNet: A Neural Network with Feature Sparsity'
created_time: 2023-11-22T03:43:00.000Z
last_edited_time: 2023-11-29T10:49:00.000Z
하위 항목: []
subclass: Decision Making
class: Paper
작성일시: 2023-11-22T03:43:00.000Z
pdf: https://arxiv.org/pdf/1907.12207.pdf
상위 항목: []

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

## Formulation

## Hyper-parameter tuning

# Optimization

## Warm starts: a path from dense to sparse

## Hierarchical proximal optimization

## Computational Complexity

## Bias due to regularization

# Experiments

## Data Sets

## Methodology

## Results

# Extension to Unsupervised Feature Selection

## Background

## Training

## Selected Digits for Single Classes in MNIST

# Extension to Matrix Completion

# Sparsity in Learned Features
