---
id: c4fe8e99-0760-4c24-b152-66e376d28bc5
title: MLDL1 FINAL
created_time: 2022-12-07T09:47:00.000Z
last_edited_time: 2023-10-07T16:40:00.000Z
cover_image: https://www.notion.so/images/page-cover/gradients_11.jpg
icon_emoji: 🐾
하위 항목: []
subclass: 2022_Fall
class: Coursework
작성일시: 2022-12-07T09:47:00.000Z
상위 항목: []
_thumbnail: https://www.notion.so/images/page-cover/gradients_11.jpg

---

# Nearest Neighbor Classifiers

    - Nearest Neighbor으로 classification할 시의 단점: O(1) for training but O(N) for testing

    - L_1 (A,B) = \sum_{\substack {i,j}}|A_{i,j}-B_{i,j}|, L_2(A,B) = {\sqrt{(A_{i,j}-B_{i,j})^2}}

    - However, nearest neighbors with pixel distance are never used

    - Curse of dimensionality : need exponentially increasing number of examples for higher dimensional data

***

# Linear Softmax Classifier

    - Linear Classifier: weighted sum of input pixels

    - f({\textsf x}, W) = {\textsf y} = Wx+b = \begin{bmatrix} W & b \end{bmatrix} \begin{bmatrix}x \\ 1\end{bmatrix} = W^{'}x^{'}

    - b라는 variable이 필요한 이유: affecting the output without interacting with data {\textsf x}

    - Limations of linear classifier: unbounded and it’s hard to interpret → probability로 만들기

    - Sigmoid function \sigma(s) = \frac 1 {1+e^{-s}}

    - Sigmoid를 n으로 확장하면 softmax이고, p(y=c_i |x) = \frac {e^{s_i}}{\sum_j {e^{s_j}}}

    - We can update the parameters based on Loss functions

    - Loss function의 종류: Margin-based(0-1, log loss, exponential loss, hinge loss)

    	- hinge loss and log loss are widely used, but we can’t differentiate hinge loss at 1 and log loss is more interpretable

    - Cross Entropy: {\cal L} = - \frac 1 N  \sum_{i=1}^N \sum_{k=1}^K y_{ik} \log(\hat{y}_{ik}) = -\frac 1 N \sum_{i=1}^{N} \log(\hat{y}_i T_i)

    - Kullback-Leibler divergence D_{KL}(P||Q) = \sum_i P(i) \log \frac {P(i)} {Q(i)}

    - How to follow the slope? Calculate gradient descent \theta _i^{new} = \theta _i^{old}-\alpha \frac {\partial}{\partial \theta_i^{old}} J(\Theta)

    	- Problems: Surface may not be convex and works if and only if the cost function is differentiable

    	- Stochastic Gradient Descent: compute gradients for only on a randomly sampled subset

***

# Neural Networks and Backpropagation

    - Issues with linear classifiers: learn one template and only works if inputs are linearly separable

    - Perceptron: Takes input value and each of them is multiplied with a weight y = \operatorname f(w_1x_1+w_2x_2) and multiple perceptron에서는 이게 여러 번 이루어짐

    - Multilayer Perceptrion x \in \reals^d   W_1 \in \reals ^{h \times d}   W_2 \in \reals ^{c \times h}      s \in \reals ^c

    - How Can we add nonlinearity? Activation functions! f(x) = a_2 (W_2a_1(W_1x))

    - Activation Functions: sigmoid, tanh(\tanh (x)), ReLU(\max (0,x))

    - For Backpropagation, we compute gradient of loss \frac {\partial \cal {L}}{\partial \hat W_2} = \frac {\partial \cal {L}}{\partial \hat y} \frac {\partial \hat y}{\partial W_2}, \frac {\partial \cal {L}}{\partial W_1} = \frac {\partial \cal {L}}{\partial \hat y}\frac {\partial \hat {y}}{\partial h}\frac {\partial h}{\partial W_1}

    ```python
    import torch.nn as nn
    import torch.nn.functional as F
    import torch.optim as optim

    class Net(nn.Module):
    		def __init__(self):
            super(Net, self).__init__()
            self.fc1 = nn.Linear(784, 128)
            self.fc2 = nn.Linear(128, 64)
            self.classifier = nn.Linear(64, 10)
        
        def forward(self, x):
            x = x.reshape(-1, 784)
            x = F.relu(self.fc1(x))
            x = F.relu(self.fc2(x))
            x = self.classifier(x)
            return x

    network = Net()
    ```

***

# Convolution Neural Networks

    - Fully Connected Layer이 가지는 문제: models relationships from every input value to every output value, so no spatial locality and positional invariance → CNN!

    - Convolutional Layer 

    	> Slide over the image spatially, computing dot products

    - Why Nested Conv Layer? Get Low, Mid, High Level Features

    - Stride: How much pixels to slide, output size \frac {(N-F)}{\mathsf {stride}}+1

    - Padding: zero pad the border, output size \frac {(N-F+2P)}{\mathsf {stride}}+1

    - Given an input volume W \times H\times C, filters K, stride S, zero padding P will produce an output of size W'\times H' \times K where W' = (W-F+2P)/S + 1, H' = (H-F+2P)/S+1, numbers of parameters K(F^2C+1)

    - Pooling: for downsampling and denoising to control overfit. Max pool에서는 filter의 max값을 고르고, average pooling에서는 filter의 average값을 구한다.

***

# Training Neural Networks

    - Activation Functions

    	- Sigmoid Function: Kill the gradients, outputs are not zero-centered, computationally expensive

    	- Not zero-centered output이 문제인 이유: sigmoid node doesn’t change the sign of the upstream gradient for all w_i

    	- Tanh function: zero-centered이긴 하지만, killing gradient에 대한 문제는 가지고 있음

    	- ReLU: Not zero centered, anad not differentiable when x=0, if an initial output is inegative, it’s never updated

    - Why zero-centering? Classification becomes less sensitive and easy to optimize

    - Why normalize? Each axis has the same importance

    ```python
    X -= np.mean(X, axis=0) #zero-centering
    X /= np.std(X, axis=0) #Normalizing
    ```

    - Data augmentation: slightly modifying each datum without affecting its semantics

    	- Horizontal flips, Random crops, Scaling, Color jitter 등이 있음

    - Weight Initialization

    	- Gaussian Random의 문제점: gradient가 zero가 되어 learning이 진행되지 않음

    	- Xavier Initialization: Var[W_{ij}] = 1/d_{in} 으로 맞추어 input variance와 output variance를 동일하도록 만드는 방법

    	```python
    	W = np.random.randn(d_in, d_out) / np.sqrt(d_in)
    	```

    - Learning Rate Scheduling: 너무 높으면 explode, 너무 낮으면 천천히 learning함. 그렇기 떄문에 처음에는 높였다가 그 다음에는 낮추는 decay 형식을 진행하려고 함

    - Regularization: adding an additional penalty term in the objective function, for example Ridge or Lasso

    	- In a neural network, there is weight decay.\Omega(W) = \sum_i \sum_j W_{i,j}^2 or \Omega(W) = \sum_i \sum_j |W_{i,j}| 

    - Early Stopping: validation loss가 최소가 나온 지 꽤 되었다면, 빠르게 stop하는 방식임

    - Dropout: forward 과정에서 randomly set some neurons to zero, but test시에는 모든 neuron을 활성화해야 함

    - Optimization

    	- Stochastic Gradient Descent의 문제점: progress slow, saddle point, may not be accurate because of mini-batch

    	- SGD+Momentum(관성) v_{t+1} = \rho v_t - \alpha \nabla f(x_t), x_{t+1} = x_t + v_{t+1}

    	- Adagrad, RmsProp: learning rate를 dimension vector에 대해 조절하는 것이며, Rmsprop는 여기에 decaying을 추가한 것

    	```python
    	grad_squared = 0.0
    	while True:
    		dx = compute_gradient(x)
    		if adagrad = True:
    			grad_squared += dx*dx
    		elif rmsprop = True:
    			grad_squared = dr * grad_squared + (1-dr)* dx*dx
    		divider = np.sqrt(grad_squared) + 1e-7
    		x -= learning_rate * dx / divider
    	```

    	- ADAM: Rmsprop에 SGD+Momentum 기법을 둘 다 활용하는 것

    	- Second-order Optimization: Use gradient and Hessian to form quadratic approximation, \theta^* = \theta_0 - H^{-1} \nabla_\theta J(\theta_0) where J(\theta) \approx J(\theta_0) + (\theta - \theta_0)^{\intercal}\nabla_\theta J(\theta_0) + \frac 1 2 (\theta - \theta_0)^{\intercal} H(\theta - \theta_0) → takes too long time to calculate

     

    - Batch normalization: In some hidden layers, we can make each dimension have a zero-mean unit variance: \hat x^{(k)} = \frac {x^{(k)} - {\mathbb E}[x^{(k)}]} {\sqrt {Var[x^{(k)}]}}

    - Collate_function: converts PIL images, labels to pytorch tensors

    	```python
    	def collate_fn(data_samples):
    	    batch_x, batch_y = [], []
    	    for x, y in data_samples:
    	      x = transforms.ToTensor()(x)
    	      y = torch.Tensor([y])
    	      batch_x.append(x)
    	      batch_y.append(y)
    	    batch_x = torch.stack(batch_x).float()
    	    batch_y = torch.cat(batch_y).long()
    	    return (batch_x, batch_y)
    	```

***

# Sequential Data & RNN

    - Problem types: one-to-one, many-to-one, many-to-many, one-to-many

    - Word embeddings: change the word as a vector to reflect its semantics. They’re fitted to maximize the likelihood L(\theta) = \displaystyle{\prod_{{i=1}}^N \prod_{ -m \le j \le m, j \not = 0 }} p(w_{t+j}|w_t;\theta)

    - CNN이 sequential data에서 활용하기 어려운 이유: Sentences have variable length 😨

    - Encoder: input as entire sequence, and embeds entire sequence preserving its overall semantics and it will make them arbitrary length

    ```python
    MAX_LEN = 32
    #collate_batch를 통해 sentence length를 MAX_LEN으로 맞출 수 있음
    def collate_batch(batch):
        label_list, text_list = [], []
        for (_label, _text) in batch:
          label_list.append(label_pipeline(_label))
          processed_text = torch.tensor(text_pipeline(_text), dtype=torch.int64)
          if processed_text.size(0) > MAX_LEN:
            processed_text = processed_text[:MAX_LEN]
          else:
            processed_text = torch.cat([processed_text, torch.zeros(MAX_LEN-processed_text.size(0))])
          text_list.append(processed_text)
        label_list = torch.tensor(label_list, dtype=torch.int64)
        text_list= torch.stack(text_list).long()
        return label_list.to(DEVICE), text_list.to(DEVICE)
    ```

    - Recurrent Neural Network: They maintain an internal state, so the new internal state is determined by its old state as well as the input. h_t = f_W(h_{t-1},x_t) = tanh(W_{hh}h_{t-1}+W_{xh}x_t)

    	- Forward pass: all parameters are fixed and they are used to compute \hat y

    	- Backpropagation: from the  loss(diff(\hat y, y)), parameters are updated

    - Language model: probability for a sequence of words, traditionally used Markov assumptions

    - RNNs calculate the likelihood of each word appearing in the next position. 이 때 cross entropy loss(J^{(t)}(\theta) = - \displaystyle{\sum ^{|V|}_{j=1}}y_{t, j} \log \hat y_{t,j})가 주로 이용됨

    - RNN의 장점: input sentence를 조절할 수 있으며, model size가 커지지 않는다. 하지만 vanishing gradient 문제로 long-range에서 정확도가 떨어진다.

    - Gradient flow in RNN: \frac{\partial h_t}{\partial h_{t-1}} = \tanh'(W_{hh}h_{t-1}+W_{xh}x_{t})W_{hh}로 이걸 계속 반복하게 되면 |W_{hh}| 가 계속 곱해지게 되는데 얘가 0에 수렴하거나 발산한다면 learning이 제대로 되지 않을 것

    - LSTM: Long Short Term Memory

    	- cell state(c_{t-1}) : new set of hidden state로, detouring FC layer

    	- forget gate: 얼마나 기억해낼지를 control하는 gate

    	- input gate: 방금 입력된 데이터가 기억할 가치가 있는지를 control

    	- output gate: 단기기억으로 넣어줘야 하는게 있는지를 확인함

    	```undefined
    	f_t = \sigma (W_fx_t + U_f h_{t-1} + b_f)\\i_t = \sigma (W_ix_t + U_i h_{t-1} + b_i)\\o_t = \sigma (W_ox_t + U_o h_{t-1} + b_o)\\c_t = f_t \circ c_{t-1} + i_t \circ \tanh (W_cx_t + U_c h_{t-1} + b_c)\\h_t = o_t \circ \tanh (c_t)
    	```

    - GRU has fewer parameters and no additional cell state. They use a convex combination of the previous hidden state and the new one computed from the input.

    	```undefined
    	r_t = \sigma (W_rx_t + U_r h_{t-1} + b_r)\\z_t = \sigma (W_zx_t + U_z h_{t-1} + b_z)\\h_t = (1-z_t) \circ h_{t-1} + z_t \circ \tanh (W_hx_t + U_h(r_t \circ h_{t-1}) + b_h)
    	```

    - Machine Transform problems에서 RNN을 사용할 수 없는 이유: 문장의 길이와 어순이 다르기 때문

    - Encoder-Decoder Structure: By encoder, make an embedding containing semantics of the entire input sequence, then auto-regressive decoder을 만듦

    	- <SOS>: A special token indicating the first time step

    	- At training, we use ground truth y_{t-1} as input, but at inference, we actually feed previous output

    	```python
    	from torchtext.vocab import build_vocab_from_iterator
    	
    	def tokens(data_iter):
    	    for _, text in data_iter:
    	        yield tokenizer(text)
    	
    	train_iterator = tokens(train_data)
    	encoder = build_vocab_from_iterator(train_iterator, specials=[""])
    	encoder.set_default_index(encoder[""])
    	
    	encoder(tokenizer("Hello World!"))
    	```

***

# Attention Mechanism & Transformers

    - Limitations of RNN-based models: information loss is unavoidable for long sequences

    - Attention function: Attention(Q, K,V) = value

    - Q, K는 comparable해야 하며, V와 attention value는 같은 dimensionality여야 한다. 많은 예시에서 4개 모두가 같은 dimension을 가짐

    - Seq2Seq model과 비교하면 Q는 decoder hidden state, K는 encoder hidden state, V는 encoder hidden state

    - Dot-Product Attention

    	- encoder hidden state h_1, ...,h_T \in \reals ^h, decoder state at t is s_t \in \reals ^h

    	- Attention score e_t = \begin{bmatrix}s_t^\top h_1 &,..., & s_t^\top h_T \end{bmatrix} \in \reals^T가 됨

    	- 여기에 softmax를 적용해 만든 attention coefficient를 encodere hidden state에 넣으면 a_t = \sum_{i=1}^T [\alpha_t]_ih_i \in \reals^h이고 이를 decoder hidden state와 concat해서 리턴함

    - Transformer: Attention is what you all need.

    	- Encoder

    		- Input is sequence of tokens

    		- Contextulixing the word embedding by self attention, calculate {softmax} {(\frac {Q \times K^\top}{\sqrt{d_k}})}V = Z를 multi-head에 대해 한 후 concatenate함

    		- Goes through an additional FC layer. FFN(x) = \max (0, xW_1+b_1)W_2+b_2로 output is still same size contextualized token embedding. 이제 self-attention block이 stack되어버림, 이 때 positional encoding을 추가해 주어 단어의 위치를 파악시킴

    	- Decoder

    		- Input: given Z = \begin{Bmatrix} z_1, &..., &z_n \end{Bmatrix}, generate auto-regressively

    		- Masked Multi-head self attention: input sequence is fed into multi-head self attention layer as the encoder, and they are masked out.

    		- Encoder-decoder attention: encoder output을 가지고 오며, Q is the query from decoder, K, V is the key and value form encoder임 이 때 masking은 없음

    		- Feed forward layer → Linear layer → softmax layer

    - BERT: Bidirectional Encoder Representations from Transformers로, transformer을 이용한 언어 모델이다. 2개의 문장이 들어가고 얘네가 연결될 때 sep 토큰, 첫 문장의 시작에는 CLS 토큰이 들어감

    	- example: Masked Language Modeling, Next sentence prediction
