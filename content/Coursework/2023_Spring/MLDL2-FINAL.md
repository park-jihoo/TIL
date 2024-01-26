---
id: c2739906-38a1-4cbc-accb-4604cfa99402
title: MLDL2 FINAL
created_time: 2023-06-13T05:02:00.000Z
last_edited_time: 2023-10-07T16:40:00.000Z
cover_image: https://www.notion.so/images/page-cover/met_john_singer_sargent_morocco.jpg
icon_emoji: 💬
하위 항목: []
subclass: 2023_Spring
class: Coursework
작성일시: 2023-06-13T05:02:00.000Z
상위 항목: []
_thumbnail: https://www.notion.so/images/page-cover/met_john_singer_sargent_morocco.jpg

---

# Components of Learning

    - Task: the main goal of learning

    - Experience: a.k.a dataset

    - Performance Measure: evaluate the ability to perform the task

    ```undefined
    \theta_\tau^* \leftarrow A_\phi (D_\tau, P_\tau, L_\tau, f_\theta)
    ```

    - Empirical Risk

    ```undefined
    \frac 1 n \sum_{i=1}^n L_\tau(d^{(i)}, f_\theta)
    ```

# Optimization

    ### Expected Risk

    ```undefined
    R(f_\theta, \tau) = \int L_\tau(f_\theta(x), y)dP_\tau(x, y)
    ```

    - We need to approximate joint distribution by the empirical distribution

    - Empirical risk minimization(ERM)

    ```undefined
    \arg\min_\theta R(f_\theta, \tau) = \arg\min_\theta \frac 1 n \sum_{i=1}^n L_\tau(f_\theta(x_i), y_i)
    ```

    - It prones to overfitting, so need additional things to improve generalization

    ### Gradient Descent

    ```undefined
    \theta \leftarrow \theta - \alpha \nabla_\theta R(f_\theta, \tau)
    ```

    - A first-order iterative optimization algorithm for finding a local minimum of a differentiable function

    - However, there are local minimum or saddle points, so subsampling principle to gradient descent → Stochastic Gradient Descent

    - SGD has high variance, noisy gradient and it leads to slow convergence

    - Mini-batch SGD: use multiple data(not full) to estimate gradients

    	```undefined
    	\theta \leftarrow \theta - \alpha \nabla_\theta \frac 1 {|B_i|} \sum_{(x, y) \in B_i} L_\tau (f_\theta(x), y)
    	```

    - Larger LR for dimension with less curvature, smaller LR for dimension with more curvature

    ### Normalization

    - Input data normalization x \leftarrow \frac {x - \mu}{\sigma}

    - Batch normalization \hat{x_i} = \frac{x_i - \mu_B}{\sqrt{\sigma^2_B+\epsilon}}

    	- Adaptive reparameterization

    	- Internal covariate shift in DNN with SGD

    ### Gradient Momentum

    - Make step smaller when gradients reverse sign, and larger when gradients are consistent

    	```undefined
    	\theta_{t+1} \leftarrow \theta_t - \alpha \nabla_\theta R(\theta_t) + \gamma(\theta_t - \theta_{t-1})
    	```

    - Fix poor conditioning of Hessian matrix, and reduce variance in stochastic gradient

    ### Adaptive Learning Rates

    ```undefined
    \theta_{t+1} \leftarrow \theta_t - \alpha_t \cdot \nabla_\theta R(\theta_t)
    ```

    - Adagrad: accumulate second moment estimate r_j = r_j + g_j^2 for all i \in \{ 1,...,d\} 

    - Rmsprop: accumulate second moment estimate  r_j = \rho r_j + (1-\rho)g_j^2 for all i \in \{ 1,...,d\} 

    - Adam: accumulate first moment estimate, second moment estimate

    ### Others

    - Regularization: avoid overfitting / memorization

    - Gradient Clipping

# Data Augmentation

    - Many diverse samples give accurate approximation, so make virtual samples in training dataset, but not randomly!

    - Vicinal Risk Minimization(VRM)

    	```undefined
    	P_\tau (x, y) = \frac 1 n \sum_{i=1}^n v(x,y|x_i, y_i) = \frac 1 n \sum_{i=1}^n N(x-x_i, \sigma^2)\delta(y=y_i)
    	```

    - Label Invariant augmentation

    	```undefined
    	P_\tau (y|x) = P_\tau(y|\Tau_\gamma(x))
    	```

    	- Label invariant = same semantic meaning = content preserving

    	- Classifier to be invariant of it

    	- Transformation with parameter \gamma → randomly sample \gamma

    	- Use / combine many as possible

    	```python
    	transform_train = [transforms.resize(224, 224),
    	                   transforms.RandomHorizontalFlip(0.5)
    	                   transforms.RandomAffine(
    	                       degrees=15, translate=(0.2, 0.2),
    	                       shears=15, scale=(0.8, 1.2)),
    	                   transforms.ToTensor()]
    	transform_train = transforms.Compose(transform_train)
    	transform_valid = [transforms.resize(224, 224),
    	                  transforms.ToTensor()]
    	transform_valid = transforms.Compose(transform_valid)
    	```

    	- Casual interpretation → data augmentaiton as counterfactuals under soft style intervention

    - Mixup: mixing samples in training set(different labels)

    	```undefined
    	v(x, y|x_i,y_i) = \frac 1 n \sum_{j=1}^n \textbf{E}_\lambda [\delta (x=\lambda \cdot x_i + (1-\lambda) \cdot x_j, y = \lambda \cdot y_i + (1 - \lambda) \cdot y_j )] \\ \lambda \sim \text{Beta}(\alpha, \alpha) \text{  for  } \alpha \in (0, \inf)
    	```

    	- encourage model to behave linearly in-between samples, and gives smoother estimate

    - Label Smoothing \hat{y} = (1 - \alpha ) \cdot y + \frac \alpha K → to prevent overconfidence

    - Adversarial Training: make small pertubation to encourage smoothness

# Semi-supervised Learning

    ### Objectives

    - Main objective: task-oriented objective(use labeled data)

    - Auxiliary objective: regularizatoin, mainly use unlabeled data

    ### How

    - Consistency Regularization: model output remains unchanged when input is pertubed

    - Entropy Minimization: encourage model output to have low entropy(self-training/psuedo-labeling)

    ### Examples

    - Pseudo Labeling: Unlabeled data uses pseudo label as target data and make it highly confident

    - PI - model: consistent predictions between 2 different settings of same input

    	- Motivation: model ensembling is mostly better than a single model

    	- Temporal ensembling

    		```undefined
    		\tilde{z_i}^{(t)} = \frac {\alpha \tilde {z_i}^{(t-1)}+(1-\alpha) z_i}{1 - \alpha ^t}
    		```

    - Mean teacher → EMA model

    	```undefined
    	\theta_t' = \alpha \theta_{t-1}' + (1 - \alpha)\theta_t
    	```

    	- It looks similar to temporal ensembling but it is not a prediction, it’s model

    	- It’s a copy of model parameters

    - Virtural Adversarial Training

    	- Replate target by prediction, and it’s applicable to both labeled / unlabeled data

    - Mixmatch : Mixup을 통해 model ensembling을 하여 better estimation을 만든 뒤, sharpen하여 entropy minimization을 진행함

# Self-supervised Learning

    - Self supervised learning is constructing supervised learning tasks for unlabeled data

    - A special type of representation learning

    - Early  related work: Autoencoders, word2vec, autoregressive modeling, multiple instance

    ### How to define self-supervised learning tasks

    - Self-prediction: predict one part of the data given the other parts

    	- autoregressive generation: predict future behavior based on past behavior

    	- masked generation: predict missing portion given other information

    	- innate relationship prediction: predict relationship within data

    - Contrastive learning: given multiple data, predict relationship among them

    	- inner-sample classification: given an anchor data point, learn to identify(positive, negative candidates)

    	- feature clustering: use clustering algorithms to assign pseudo labels

    	- multi-view coding: use different views of input data as positive samples

    ### Examples of self-supervised learning tasks

    - Autoregressive Generation

    	- Image: pixelCNN, Row LSTM, Diagonal BiLSTM, ImageGPT

    	- Video: VideoGPT

    	- Language: GPT,

    - Masked Prediction

    	- Image: Denoising autoencoder, BERT+ViT, Masked AE

    	- Language: BERT

    	- Audio: Wav2Vec, HuBERT

    - Colorization

    - Innate Relationship prediction

    	- Vision: Repative position, Jigsaw puzzle, Temporal order, motion segmentation

    	- Language: ALBERT

    - Inter-Sample Classification

    	- Vision: similar than positive, dissimilar than negative/ Instance level, Momemtum contrastive, SimCLR

    	- Language: SimCSE

    	- Audio: COLA

    - Non-contrastive Learning: No Negative Sample

    	- BYOL, SimSiam

    ### Challenges in Self-supervised learning tasks

    - Positive Samples

    	- Data augmentation(label-invariant transformation)

    	- Different models(momentum/noise)

    - Negative Samples

    	- Hard Negative = different labels + similar context

    	- User some labels / sort samples by similarity

    	- use many negative samples

    - High-Quality Large Dataset

    	- Unbiased, diverse data

    	- more data then better performance

    - Pretext tasks

    	- How to design and combine data

    	- How to combine with supervised learning

# Transfer Learning

    > 💡 Transfer Learning is improving the learning of target(downstream) tasks

    ### Steps of Transfer Learning

    - Train a model with one or more large datasets

    - Apply obtained knowledge to learn a new target task(fine tuning)

    ### Difference between Semi-supervised learning and transfer learning

    - Transfer learning is two-step learning procedure

    - In transfer learning, pre-trained models are not designed for specific target tasks

    - Fine-tuning depends on pre training on semi-supervised learning

    ### Efficient Transfer Learning

    - Having multiple target tasks is not effective. Need to store multiple full models

    - Having one pre-trained model and use it as shared feature extractor

    - Residual Adapters: shared feature extractor + multiple adapters

    - Adapter BERT, Prefix-tuning

    ### Other case of Transfer Learning

    - Multi-task learning: source tasks = target tasks, use becauseeach task has a small dataset

    	- Challenges: cross-task interference

    	- Negative transfer can happen

    	- Balancing the learning of multiple tasks

    - Meta-learning: improve the learning of unseen task, and learnhow to learn

    - Continual Learning: Sequentially learn target tasks, and need to remember all previous tasks, but data of previous task is not available

# VAE & Diffusion

    - Why data distribution?

    	- Generate new samples

    	- Evaluate/ measure the likelihood

    - Latent Variable models

    	```undefined
    	\arg \min_\theta \prod_{x\in D} p_\theta (x) = \arg \min_\theta \sum_{x \in D} \log p_\theta(x)
    	```

    	- Unobserved latent variable z

    	- Instead of directly modeling p(x), use model joint distribution p(x, z)

    - ELBO(Evidence Lower Bound)

    	```undefined
    	\log p_\theta(x) \geq \int q(z)\log \left[ \frac {p_\theta(x, z)}{q_\phi(z)} \right]dz = \textbf{E}_{q_\phi(z)}\left[ \log \frac {p_\theta(x, z)}{q_\phi(z)} \right] = \log p_\theta(x) - D_{KL}(q_\phi(z) || p_\theta(z|x))
    	```

    	- Instead of directly optimizing the interactive evidence, ELBO is a proxy objective to be optimized

    	- EM algorithm→ make tight bound in expectation and improve bound in maximization

    	- However, there is no closed form of posterior distribution, so variational approximatiomn is appllied

    		```undefined
    		q_\phi(z) = N(z|\mu_z, \sigma_z^2I) \sim p_\theta(z|x)
    		```

    	- Reconstruct term is \textbf{E}_{q_\phi(z)}[\log p_\theta(x|z)], regularization term is D_{KL}(q_\phi(x)||p_\theta(z))

    - Variational Auto Encoder(VAE)

    	- optimize elbo, and use neural network for variational amortized inference

    		```undefined
    		q_\phi(z|x) = N(z|\mu_z(x), \sigma_z^2(x)I) \sim p_\theta(z|x)
    		```

    	- Each data x has its own variational parameter but it’s not scalable, so use encoder architecture

    	- Sample latent vector z through encoder and regenerate data x with latent vector z through decoder

    	- Reconstruct term \log p_\theta(x|z), Regularization KL divergence

    	- Hierarchical Variational Auto-Encoder(HVAE), Recurrent VAE exists as example

    	- Problem: inefficient to evaluate or measure the likelihood

    - Diffusion Model(VDM)

    	- Special case of VAE with three key restrictions

    		- Latent variable size = input data size

    		- encoder is not learned, use pre-defined linear Gaussian models

    		- Gaussian parameters vary over latent levels

    	- Encoding is noising and decoding is generation

    	```undefined
    	q(x_t|x_{t-1})= N(x_t ; \sqrt{\alpha_t}x_{t-1},(1-\alpha_t)I)\\p_\theta(x_{t-1}|x_t) = N(x_{t-1};\mu_\theta(x_t, t), \sigma^2_tI)
    	```

    	- There is reconstruction term, prior matching term(constant), consistency term

    	- Conditional Generation with VDM: generate data under some condition, but encoder is not conditioned

    	> Denoising diffusion model = mode coverage/diversity + High Quality Samples

# Graph Neural Networks

    - Graph Data: a set of objects and the connections between them

    - Task: graph-level, node-level, edge-level

    - Challenges of Using Graph Data

    	- Representing a graph’s connectivity: adjacency matrix or adjacency list

    - Graph Neural networks

    	- Transformation on all attributes of graph

    	- Preserve graph symmetries

    	- Message passing neural network framework

    - Simplest GNN: a separate multilayer perceptron on each component of a graph

    	- Node Prediction(for each node embedding, apply linear classifier, and no info then aggregate from edge)

    	- Edge Prediction(for each edge embeding, apply linear classifier, and no info then aggregate from node)

    	- Graph Prediction(for global-context embedding, apply a linear classifier and no info then aggregate node or edge)

    - GNN with Passing Messages

    	- Use pooling within each GNN layer

    	- Use message passing → Neighboring nodes or edges exchange information

    	- If aggregate neighboring nodes similar to convolution then **Graph Convolutional Network**

    	- Update x with node embedding not, and concatenate linear layers

    	- Graph Attention Network: get similarity as attention score

    	- GCN, GAT, and Transformer

    		![](https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/1bce0d94-57f1-481e-9e5f-803352158c2f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240126T004300Z&X-Amz-Expires=3600&X-Amz-Signature=0abd78a5ee99b3075fd89918860c2b3ba52ba56b5c0d9d70f7e9e9038b1a076d&X-Amz-SignedHeaders=host&x-id=GetObject)

# Transformers

    - CNN, RNN, GNN have inductive bias, so these model requires some type of architecture design and some initial assumptions about the data we want to analyze

    - Small dataset gives strong inductive bias, Large dataset gives weak inductive bias so we need large model

    - Self-Attention

    	- input → key / query / value

    	- key x query → attention score

    	- attention weight x value

    	- aggregate(update)

    	```undefined
    	\text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V=Z
    	```

    	- Self attention has adaptive parameters, so it doesn’t have restriction and changeover different input data

    	- Single head self-attention and multi-head self-attention exists

    - Positional Encoding

    	- Permutation equivariance of self-attention

    	- Same input data don’t lead to same results

    	- Use relative positional encoding and learn it

    - Transformer layer

    	```mermaid
    	graph LR
    		A[input] --> B[Multi-head self attention]
    		B --> C((+))
    		A -->|residual connection| C
    		C --> D[LayerNorm]
    		D --> E[MLP]
    		E --> F((+))
    		D --> |residual connection|F
    		F --> G[LayerNorm]
    		G --> H[output]
    	```

    	- Lack some inductive biases

    	- Need more data to learn related paramters → self-supervised learning

    - Attention is all you need

    	- Seq2Seq task model(encoder-decoder): use transformer with masked self-attention and encoder-decoder attention

    - BERT: masked prediction(encoder only)

    - GPT: autoregressive generation(decoder only)

    - ViT: Vision Transformer, image patch as token and classification with class token

    - Graph Transformers: attention over neighboring nodes, and use laplacian position eigenvectors

    - In-weights learning: standard setting for supervised learning

    - In-context learning: ability to generalize rapidly from few examples of a new concept

# Bayesian Neural Networks

    - Uncertainty: variance in regression, confidence in classification

    - Towards out-of-distribution leads to more uncertainty

    - More uncertainty gives low confidence, less uncertainty gives high confidence

    - Aleatoric uncertainty : data randomness

    	- Inherent uncertainty in the environment’s dynamics

    	- Homoscedastic: output noise is fixed

    	- Heteroscedastic: output noise can vary with input data(output is distribution)

    - Epistemic uncertainty: lack of knowledge

    	- Uncertainty about the model parameters

    - Calibration = |Confidence - Accuracy|

    	- Confidence: predicted probability of correctness

    	- Accuracy: observed frequency of correctness

    - Under-confident and over-confident

    - Expected calibration error

    	```undefined
    	\text{ECE} = \sum^B_{b=1} \frac {n_b}{N} |\text{acc}(b) - \text{conf}(b)|
    	```

    - Bayesian Neural Networks

    	- Maximum a posterior estimation

    		```undefined
    		\theta^* = \arg\max_\theta p(\theta|x,y) =^* \arg\min_\theta \sum_k y_k\log p_k + \lambda ||\theta||^2
    		```

    	- One model: one prediction per example

    	- Probabilistic approach: estimate full distribution

    	- Intuitive approach: ensemble approach

    		```undefined
    		p(y|x,D) = \int p(y|x,\theta)p(\theta|D)d\theta \sim  \frac 1 S \sum_{s=1}^S p(y|x,\theta^{(s)})
    		```
