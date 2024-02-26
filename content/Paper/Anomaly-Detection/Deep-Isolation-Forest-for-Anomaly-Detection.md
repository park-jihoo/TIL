---
id: 3a3827fa-1b06-4903-b065-5a291992fd93
title: Deep Isolation Forest for Anomaly Detection
created_time: 2023-08-13T06:02:00.000Z
last_edited_time: 2023-12-01T06:03:00.000Z
하위 항목: []
subclass: Anomaly Detection
class: Paper
작성일시: 2023-08-13T06:02:00.000Z
pdf: https://arxiv.org/pdf/2206.06602.pdf
상위 항목: []
_thumbnail: >-
  https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/a1f92f77-f6dd-4dec-9c54-592da138bb34/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240226T004306Z&X-Amz-Expires=3600&X-Amz-Signature=84eab443711a323736033ae456d71b2a7eff3ae8fb88204ff378981a3cc0ab7e&X-Amz-SignedHeaders=host&x-id=GetObject

---

> 💡 This paper introduce a new representation scheme that utilizes casually initialized neural networks to map original data into random representation ensembles, where random axis-parallel cuts are subsequently applied to perform the data partition

# Introduction

*   An explicit major issue is that iForest cannot handle hard anomalies because it treats all features separately and considers only one feature per isolation operations

*   Another inherent imperfection of iForest is that it assigns unexpectedly low anomaly scores to artifacts introduced by the algorithm itself.

*   This paper proposes a novel extension of iForest named Deep Isolation Forest(DIF). The key idea in DIF is to harness the strong representation power of neural networks to map the original data into a group of new data spaces, and non-linear isolation can be easily achieved by performing simple axis-parallel partitions upon these newly created data spaces.

# Related Work

## Anomaly Detection

*   Recent studies devise deep anomaly detection models based on representation learning.

*   Also, some practical anomaly detection tools, are developed to facilitate the use of anomaly detection models in real-world applications

## Isolation Forest and Its Extensions

*   The mainstream of these extension focuses on devising more effective isolation methods

    *   The major problem is that they still rely on linear isolation operations

    *   Distance-based methods introduce an extra assumption that anomalies are far from other data objects. However this doesn’t always hold

*   Another angle is to enhance the scoring method.

    *   Similarly, these extensions are still vulnerable due to their linear isolation methods

## Deep Ensembles

*   Deep ensemble, a simple framework that combines prediction results of a group of independently trained networks together.

# Problem Statement and notations

*   Let \mathcal D = {o\_1,…,o\_N} be a dataset with N data objects, anomaly detection is to give a scoring function f:\mathcal D \to \R^N that estimates the abnormality of each data object

    | Format                 | Notations  | Descriptions                         |                           |
    | ---------------------- | ---------- | ------------------------------------ | ------------------------- |
    | Caligraphic Fonts      | \cal D     | Datasets                             |                           |
    | Caligraphic Fonts      | \cal X     | Representations                      |                           |
    | Caligraphic Fonts      | \cal T     | the set of iTrees                    |                           |
    | Caligraphic Fonts      | \cal P     | data pools in iTree nodes            |                           |
    | Script typeface        | \mathscr F | anomaly scoring functions            |                           |
    | Script typeface        | \mathscr G | representation function              |                           |
    | Bold lowercase letters | o          | original data objects                |                           |
    | Bold lowercase letters | x          | representation vectors               |                           |
    | Bold lowercase letters | p,q        | random vectors used in CERE          |                           |
    | Bold uppercase letters | W          | weight matrices of neural networks   |                           |
    | Bold uppercase letters | P,Q        | matrices used in CERE                |                           |
    | others                 | r          | number of representations            |                           |
    | others                 | t          | number of iTrees per representations |                           |
    | others                 | T          | total number of iTrees               |                           |
    | others                 | p(\cdot    | \cdot)                               | traversed node path       |
    | others                 | g(\cdot    | \cdot)                               | averaged deviation degree |

# Preliminaries: Isolation Forest

*   iTree \tau is essentially a binary tree and each node in the tree corresponds to a pool of data objects

*   A subset containing n data objects is used as the data pool of the root node, which is randomly subsampled from the whole dataset

*   iForest constructs a forest of T trees \mathcal T={\tau\_i}\_{i=1}^T

*   The anomaly score of data object o is calculated based on its averaged path length \mathbb E\_{\tau\_i\in T}(|p(o|\tau\_i)|) over all of the iTrees in the forest \cal T

    ```undefined
    \mathscr F_{\text{iForest}}(o|\mathcal T)=2^{-\mathbb E_{\tau_i\in\mathcal T}\frac{|p(o|\tau_i)|}{C(T)}}
    ```

*   Only **linear partition is admitted**

# Deep Isolation Forest(DIF)

## Formulation of DIF

```undefined
\mathscr G(\mathcal D)=\{\mathcal X_u\sub\R^d|\mathcal X_u=\phi_u(\mathcal D;\theta_u)\}_{u=1}^r
```

where r is the ensemble size, \phi\_u:\mathcal D\to\R^d is the network that maps original data into new d-dimensional spaces, and the network weights in \theta\_u are randomly initialized.

*   The scoring function is defined as

    ```undefined
    \mathscr F(o|\mathcal T)=\Omega_{\tau_i\sim\mathcal T}I(o|\tau_i)
    ```

## Implementation of DIF

### CERE: Computation-efficient Deep Representation Ensemble Method

*   Let W\in\R^{m\times n} be a weight matrix of neural network, and we use tuple of small random vectors p\_i\in\R^m, q\_i\in\R^n to yield a rank-one matrix via multiplication

    ```undefined
    W_i = W_0\circ(p_iq_i)^\top
    ```

    where \circ denotes the hadamard product

*   The mapping process of incoming neurons x\in\R^m and the weight W\_i can be further derived as:

    ```undefined
    \begin{aligned}W_i^\top x&=(W_0\circ p_iq_i^\top)^\top x\\&=W_0^\top(x\circ p_i)\circ q_i\end{aligned}
    ```

*   Let \Phi be the L-layer neural network using the neuly defined feed forward step. The ensemble of representations can be directly generated as

    ```undefined
    \mathscr G_\text{CERE}(\mathcal D)=\Phi(\mathcal D;\Theta)=\{\mathcal X_i\sub\R^d\}_{i=1}^r
    ```

    where \Theta=\left{W\_l,{p\_{(l,i)}}*{i=1}^r.{q*{(l, i)}}*{i=1}^r\right}*{i=1}^L

### DEAS: Deviation-enhanced Anomaly Scoring Function

*   We utilize the deviation degree of the feature value to the branching threshold as additional weighting information to further improve the measurement of isolation difficulty

*   We define the averaged deviation degree of x\_u in \tau\_i as

    ```undefined
    g(x_u|\tau_i)=\frac1{|p(x_u|\tau_i)|}\sum_{k\in p(x_u|\tau_i)}\left|x_u^{j_k}-\eta_k\right|
    ```

*   Combine path length as in iForest and the deviation measure then our function is

    ```undefined
    \mathscr F_\text{DEAS}(o|\mathcal T)=2^{-\mathbb E_{\tau_i\in\mathcal T}\frac{|p(x_u|\tau_i)|}{C(T)}}\times\mathbb E_{\tau_i\in\mathcal T}\left(g(x_u|\tau_i)\right)
    ```

## Algorithm of DIF

*   Algorithm 1 presents the procedure of the construction of deep isolation trees

    ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/a1f92f77-f6dd-4dec-9c54-592da138bb34/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256\&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD\&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240226%2Fus-west-2%2Fs3%2Faws4_request\&X-Amz-Date=20240226T004306Z\&X-Amz-Expires=3600\&X-Amz-Signature=84eab443711a323736033ae456d71b2a7eff3ae8fb88204ff378981a3cc0ab7e\&X-Amz-SignedHeaders=host\&x-id=GetObject)

*   Algorithm 2 is about anomaly scoring procedure

    ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/2a3aa3e8-6a78-4503-8752-fa92bff625d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256\&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD\&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240226%2Fus-west-2%2Fs3%2Faws4_request\&X-Amz-Date=20240226T004307Z\&X-Amz-Expires=3600\&X-Amz-Signature=fffd8336b9c044d9050d582331172286aa3e35719336d2f21015e636a75594c9\&X-Amz-SignedHeaders=host\&x-id=GetObject)

## Theoretical Analysis

### Time Complexity Analysis

*   We use CERE to implement the ensemble with r members within each mini-batch, and thus the whole feed-forward computation induces O(r\times N\times(Dd\_1+d\_ld+\sum\_{l=1}^{L-1}d\_ld\_{l+1}))

*   In terms of subsequent process of the iTree construction, it induces O(2^{J-1}\times n\times r\times t)

*   Overall time complexity of DIF is O(ND(r\times t))

### DIF as a Generalization of iForest and EIF

*   Let o\in\R^D be a vectorized data object and branching criterion is \phi(o)^{(j)}\le\eta

*   iForest splits the node by the criterion o^{(j)}\le\eta, while DIF degrades to iForest if the weight matrix is wet as an identity matrix

*   EIF uses a slicing hyperplane for each node branching, and the slope of its hyperplane is a normal vector k\in\R^D, and k^{(i)}\sim\mathcal N(0,1). The branching criterion is (o-p)\cdot k\le 0

*   We can fulfill exactly the same operation in DIF when the weight matrix satisfies W\in\R^{D\times 1}

## Discussions

### Representation Ability of Neural Networks

*   Non linear activation functions can effectively tweak and fold partition bounds to embed non-linearity into the isolation process

### Optimized vs Casually initialized Representations

*   Instead of using optimized representations, DIF uses the casually initialized representations.

    *   These loss functions are not versatile

    *   The downstream data partition might be strongly controlled by the optimization process

### Synergy between Random Representations and Random Partition-based isolation

*   The parameters of these networks can be initialized by randomly sampling from widely-used initialization distributions.

*   Given a sufficiently large set of such random representations, we can largely boost the isolation power in the random data partition

# Experiments

## Experimental Setup

### Datasets

*   Tabular: Analysis, Backdoor, DoS, and Exploits

*   Graph: Tox21

*   Time-series: Mars, Gait, ECG

### Competing methods

*   iForest and its extensions

*   Ensemble of Deep Anomaly Detectors → Different SOTA deep anomaly detection methods

### Parameter Settings and Implementations

*   DIF uses 50 representations and 6 isolation trees per representation with 256 as subsampling size for each iTree

*   All the IF-based competing methods use 300 trees

### Evaluation Metrics and Computing Infrastructure

*   We introduce a new metric called Anomaly Isoability Index(AII) to measure the quality of representations

    ```undefined
    AII=P_{a\sim\mathcal A}\left(\text{median}_{n_i\in\mathcal N}\left\{\frac1{|\mathcal C|}\sum_{n_j\in\mathcal C}(\omega(a|n_i,n_j))\right\}>0\right)
    ```

    where \omega(a|n\_i,n\_j)=d(a,n\_i)-d(n\_j,n\_j) renotes the difference between the Euclidean distances of the two pairs

## Effectiveness in Reducing False Negatives

### Tabluar Data

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/5f64a9e8-3dc0-481b-b415-1c43f3241c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256\&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD\&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240226%2Fus-west-2%2Fs3%2Faws4_request\&X-Amz-Date=20240226T004304Z\&X-Amz-Expires=3600\&X-Amz-Signature=18460d3040641363b3652f56090003ec1d837a99b932292a62521de11a270990\&X-Amz-SignedHeaders=host\&x-id=GetObject)

### Graph Data and Time Series

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/8b05b4a0-0641-4ad6-b467-796ce86eb9aa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256\&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD\&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240226%2Fus-west-2%2Fs3%2Faws4_request\&X-Amz-Date=20240226T004304Z\&X-Amz-Expires=3600\&X-Amz-Signature=4d030447cf4a67dc9a2e31cb896ebb2547e94d520ba95fe3b5e0474fd5ae6b9e\&X-Amz-SignedHeaders=host\&x-id=GetObject)

## Scalability to High-dimensional, Large-scale Data

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/a22a0b6d-9ef6-44b5-9238-640c8588c6f9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256\&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD\&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240226%2Fus-west-2%2Fs3%2Faws4_request\&X-Amz-Date=20240226T004304Z\&X-Amz-Expires=3600\&X-Amz-Signature=2873fba7186225b465c5776e56cfc8b92cc9ab07ef5e5b2e9274d96b35c36fc4\&X-Amz-SignedHeaders=host\&x-id=GetObject)

## Robustness w\.r.t Anomaly Contamination

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/c7293ce1-d752-47b3-9ff7-14aa62e38528/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256\&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD\&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240226%2Fus-west-2%2Fs3%2Faws4_request\&X-Amz-Date=20240226T004304Z\&X-Amz-Expires=3600\&X-Amz-Signature=2fae94ea76532b97fe8dd9f73c60f6843d20a8299a58d915016be6f4ac546e16\&X-Amz-SignedHeaders=host\&x-id=GetObject)

*   Generally, the performance of all the anomaly detectors downgrades with the increasing contamination ratio.

*   Nevertheless, DIF has relatively clear superiority and stronger robustness in most of the datasets

## Significance of the Synergy between Random Representations and Random Partition-based Isolation

### Representation Scheme

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/ee69e784-dfed-47aa-b170-c30f638da57a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256\&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD\&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240226%2Fus-west-2%2Fs3%2Faws4_request\&X-Amz-Date=20240226T004304Z\&X-Amz-Expires=3600\&X-Amz-Signature=582ee6f2b524c0aecb0fb3fd055650f7dbb0b518b7c353399afcf605c7689a00\&X-Amz-SignedHeaders=host\&x-id=GetObject)

*   Our representation scheme achieves desired diversity and randomness, while simultaneously maintaining stable expressiveness in each representation, enabling excellent synergy with the downstream isolation-based anomaly scoring mechanism

*   Optimized representations can be with consistently good quality on some datasets, whereas the lack of diversity in representations downgrades the efficacy of this ensemble framework

*   Optimization may even lead to worse representations on some datasets

### Scoring Strategy

*   These competing scoring methods can produce markedly better individual scoring results than our isolation-based scoring. However it’s less effective or slightly better.

*   By contrast, DIF combines data representation and anomaly scoring in a successful unified ensemble learning framework

*   DIF is inferior to its variants. It might be because anomalies in this dataset can be more easily identified by using the prior concepts used in this competing scoring methods.

## Ablation Study in CERE and DEAS

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/a9d5a398-7cb7-47b1-b131-e02f6b11ea7e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256\&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD\&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240226%2Fus-west-2%2Fs3%2Faws4_request\&X-Amz-Date=20240226T004304Z\&X-Amz-Expires=3600\&X-Amz-Signature=077f00df052049cfb1bcb03a1d857904186d49db482ff67523b9233a3a205d27\&X-Amz-SignedHeaders=host\&x-id=GetObject)

# Conclusions

*   The anomaly scoring can be facilitated by the synergy between random representations and random partition-based isolation

*   This enables DIF to fulfill

    *   More effective isolation of anomalies, especially hard anomalies in data with intractable sparsity and nonlinearity

    *   Liberation of isolation process from existing constraints to tackle the artefact problem

    *   Versatile ability to handle different data types
