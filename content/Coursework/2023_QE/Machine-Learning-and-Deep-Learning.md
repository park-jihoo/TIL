---
id: bcab10cb-9cba-471e-bda4-771a583f9f1e
title: Machine Learning and Deep Learning
created_time: 2023-08-07T06:47:00.000Z
last_edited_time: 2023-08-30T13:49:00.000Z
하위 항목:
  - id: 3e9df96f-67fe-46ce-9ea1-126fdb9a9fc7
subclass: 2023_QE
class: Coursework
작성일시: 2023-08-07T06:47:00.000Z
상위 항목: []

---

# Linear Regression

    ## Simple Linear Regression with single predictor

    	- Assume a model

    		```undefined
    		Y = \beta_0 + \beta_1 X + \epsilon
    		```

    		where \beta_0 and \beta_1 are two unknown constants that represent the intercept and slope.

    	- Given some estimates \hat\beta_0 and \hat\beta_1 for the model coefficients, we predict

    		```undefined
    		\hat y = \hat\beta_0 + \hat\beta_1x
    		```

    	- The residual sum of square RSS = e_1^2 + e_2^2 + \cdots+e_n^2

    	- The least squares approach to choose \hat\beta_0 and \hat\beta_1 to minimize RSS

    		```undefined
    		\hat\beta_1 = \frac{\sum_{i=1}^n(x_i-\bar x)(y_i - \bar y)}{\sum_{i=1}^n(x_i-\bar x)^2}\\ \hat\beta_0 = \bar y - \hat\beta_1x
    		```

    	- Standard error of estimator reflects how it varies under repeated sampling

    		```undefined
    		SE(\hat\beta_1)^2 = \frac{\sigma^2}{\sum_{i=1}^n(x_i-\bar x)^2}, SE(\hat\beta_0)^2=\sigma^2\left[ \frac1n + \frac{\bar x^2}{\sum_{i=1}^n(x_i-\bar x)^2}\right]
    		```

    	- This standard error can be used to compute confidence intervals!

    ## Hypothesis Testing

    	- Null hypothesis H_0 means there is no relationship between X and Y

    	- Alternative hypothesis H_A means there is some relationship between X and Y

    	- In linear regression,

    		```undefined
    		H_0 : \beta_1 = 0 \text{ vs. } H_A: \beta_1\not=0
    		```

    	- To test null hypothesis, we compute t-statistics with n-2 degrees of freedom

    		```undefined
    		t = \frac{\hat\beta_1 - 0}{SE(\hat\beta_1)}
    		```

    	- Residual standard error RSE = \sqrt{\frac{RSS}{n-2}}

    	- R-squared R^2 = 1-\frac{RSS}{TSS}

    	- Correlation r = \frac{\sum_{i=1}^n(x_i-\bar x)(y_i - \bar y)}{\sqrt{\sum_{i=1}^n(x_i-\bar x)^2}\sqrt{\sum_{i=1}^n(y_i-\bar y)^2}}

    ## Multiple Linear Regression

    	- Model is

    		```undefined
    		Y = \beta_0 + \beta_1 X_1 + \beta_2X_2 +\cdots+\beta_pX_p+\epsilon
    		```

    	- The ideal scenario is when the predictors are uncorrelated because correlations amongst predictors cause problems

    	- We calculate RSS and \hat\beta like this

    		```undefined
    		\begin{aligned}RSS &= (y-X\hat\beta)^\top(y-X\hat\beta)\\\frac{\partial RSS}{\partial\hat\beta}&=-2X^\top y + 2X^\top X\hat\beta = 0\\\hat\beta &= (X^\top X)^{-1}X^\top y\end{aligned}
    		```

    	- If X^\top X is not invertible, that means columns are not independent, and it’s not full rank. This means xs are correlated.

    	- Is at least 1 predictor useful? We use F-statistic to check this

    		```undefined
    		F = \frac{(TSS-RSS)/p}{RSS/(n-p-1)}\sim F_{p,n-p-1}
    		```

    ## Deciding on the important variables

    	- Forward selection: begin with null model and fit p simple linear regression, then add to model with lowest RSS

    	- Backward selection: begin with full model, and remove the variable with largest p value

    	- How to choose optimal member? AIC, BIC, adjusted R-square, CV

# Classification: Logistic Regression

    > 📖 Logistic regression or Discriminant analysis is more appropriate than linear regression

    - Logistic regression uses the form

    	```undefined
    	p(X;\beta) = \frac{e^{\beta_0+\beta_1 X}}{1+e^{\beta_0+\beta_1 X}}
    	```

    - If we rearrange this, then

    	```undefined
    	\log\left(\frac{p(X;\beta)}{1-p(X;\beta)} \right) = \beta_0 + \beta_1 X
    	```

    	and this monotone transformation is called the log odds

    ## Maximum Likelihood Estimation

    	- We use maximum likelihood to estimate the parameters

    		```undefined
    		\mathcal{L}(\beta) = \mathcal{L}(\beta_0, \beta_1) = \prod_{i:y_i=1}p(x_i;\beta)\prod_{j:y_j=0}(1-p(x_j;\beta))
    		```

    	- This likelihood gives the probability of the observed zeros and ones in the data, and we pick \beta to maximize the likelihood of the observed data.

    	- Log make products to sums

    		```undefined
    		\log\mathcal{L}(\beta) = \sum_{i:y_i=1}\log p(x_i;\beta)+\sum_{j:y_j=0}\log(1-p(x_j;\beta))
    		```

    	- To maximize log likelihood, set its derivatives to zero, but this doesn’t have closed form

    ## Multiple Logistic Regression

    	- Confounding: Outcome에 영향을 미치는 것을 포함시키지 않으면 결과가 달라질 수 있는 것을 언급함 → 해결하기 위해서 Multiple Logistic Regression 이용

    	- For class k \in \{1,...,K\}

    		```undefined
    		\mathbb{P}(Y=k|X,\beta) = \frac{e^{\beta_{0k}+\beta_{1k}X_1+\cdots+\beta_{pk}X_p}}{\sum_{l=1}^Ke^{\beta_{0l}+\beta_{1l}X_1+\cdots+\beta_{pl}X_p}}
    		```

# Classification: Generative Models for Classification

    ## Linear Discriminant Analysis

    	- Use Bayes theorem slightly differently

    		```undefined
    		\mathbb{P}(Y=k|X=x) = \frac{\pi_kf_k(x)}{\sum_{l=1}^K\pi_lf_l(x)}
    		```

    	- When the classes are well separated, the parameter estimates for the logistic regression model are surprisingly unstable.

    	### LDA when p=1

    	- p_k(x) = \mathbb P(Y=k|X=x), and \delta_k(x) = \log p_k(x)

    	- k^* = \argmax_k p_k(x) = \argmax_k\delta_k(x) = x\frac{\mu_k}{\sigma^2}-\frac{\mu_k^2}{2\sigma^2}+\log(\pi_k)

    	- Then, \hat\mu_k = \frac 1{n_k} \sum_{i:y_i=k}x_i, \hat\sigma^2 = \sum_{k=1}^K\frac{n_k-1}{n-K}\hat\sigma_k^2, \hat\pi_k =\frac{n_k}n

    	### LDA when p>1

    	- Density

    		```undefined
    		f(x) = \frac1{(2\pi)^{p/2}|\Sigma|^{1/2}}e^{-\frac12(x-\mu)^\top\Sigma^{-1}(x-\mu)}
    		```

    	- Discriminant funciton \delta_k(x) = x^\top\Sigma^{-1}\mu_k - \frac 12 \mu_k^\top\Sigma^{-1}\mu_k + \log\pi_k

    	- Once we have estimated \hat\delta_k(x), then we can turn theses into estimates for class probabilities

    ## Types of errors

    	- False positive rate: The fraction of negative examples that are classified as positive

    	- False negative rate: The fraction of positive examples that are classified as negative

    	- In order to reduce the false negative rate, we may want to reduce threshold but it may increase the overall error rate

    ## Quadratic Discriminant Analysis

    	- With Gaussians but different \Sigma_k in each class, we get quadratic discriminant analysis

    	- \delta_k(x) = -\frac12(x-\mu_k)^\top \Sigma_k^{-1}(x-\mu_k)+\log\pi_k-\frac12\log|\Sigma_k|

    ## Naive Bayes

    	- Assume features are independent in each class

    	- Gaussian naive bayes assumes each \Sigma_k is diagonal

    		```undefined
    		\begin{aligned}\delta_k(x) &\propto\log\left[\pi_k\prod_{j=1}^pf_{kj}(x_j)\right]\\&=-\frac12\sum_{j=1}^p\left[ \frac{(x_j-\mu_{kj})^2}{\sigma_{kj}^2}+\log\sigma^2_{kj}\right]+\log\pi_k\end{aligned}
    		```

# Resampling Methods: Cross-Validation, Bootstrap

    ## Cross-Validation

    	### Validation-set approach

    		- We randomly divide the available set of samples into two parts: training and validation(hold-out)

    		- The learning method is fit on the training set, and its performance is evaluated on the validation set

    		- However, validation set error may tend to overestimate the test error for the model fit on the entire data set

    	### K-fold CV

    		- A set of n observations is randomly split into K non-overlapping groups of observations

    		- Each of these K groups acts as a validation set, and the remainder as a training set.

    		- LOOCV(Leave-one out CV): A training set contains all except one, and validation set is only one observation.

    			```undefined
    			CV_{(n)} = \frac1n\sum_{i=1}^n\left(\frac{y_i-\hat y_i}{1-h_i}\right)^2
    			```

    	### CV for classification

    		- Compute

    			```undefined
    			CV_k = \sum_{k=1}^K\frac{n_k}n\text{Err}_k
    			```

    		- The estimated standard deviation of CV_K is

    			```undefined
    			\hat{SE}(CV_k) = \sqrt{\frac1k\sum_{k=1}^K\frac{(\text{Err}_k-CV_k)^2}{K-1}}
    			```

    		- This is useful estimate but not quite valid

    ## Bootstrap

    	- The bootstrap is a flexible and powerful statistical tool that resamples a single dataset to create many simulated samples and can be used to quantify the uncertainty associated with a given estimator or ML method

    	- For example, we want to minimize \text{Var}(\alpha X+(1-\alpha)Y), and one saw

    		```undefined
    		\alpha=\frac{\sigma_Y^2-\sigma_{XY}}{\sigma_X^2+\sigma_Y^2-2\sigma_{XY}}
    		```

    		- To estimate standard deviation of \hat\alpha, repeat process of simulating 100 paired observations of X and Y and estimate \alpha 1000 times, then we will get \hat\alpha_1,...\hat\alpha_{1000}

    		- The mean over all 1000 estimates for \alpha is

    			```undefined
    			\bar\alpha=\frac 1{1000}\sum_{r=1}^{1000}\hat\alpha_r
    			```

    		- The standard deviation of the estimate is

    			```undefined
    			\sqrt{\frac1{1000-1}\sum_{r=1}^{1000}(\hat\sigma_r-\bar\sigma)^2}
    			```

    	- Each of the bootstrap data sets is created by sampling with replacement, and same size as original dataset.

    	- We estimate the standard error of these bootstrap estimates using the formula

    		```undefined
    		SE_B(\hat\alpha) = \sqrt{\frac{1}{B-1}\sum_{r=1}^B(\hat\alpha^{*r}-\bar{\hat\alpha}^*)^2}
    		```

    	- Bootstrap can be used to approximate confidence interval

    	- However, each bootstrap sample has significant overlap with the original data. About 2/3 of the original data points appear in each bootstrap sample

# Model Selection: Subset Selection

    ## Considerations

    	- Prediction accuracy: especially when p>n

    	- Model interpretability: by removing irrelevant features

    ## Best subset selection

    	- Let M_0 denote the null model, which contains no predictors. This model simply predicts the sample mean for each observations

    	- For k=1,2,…,p

    		- Fit all \begin{pmatrix}p\\k\end{pmatrix}=\frac{p!}{k!(p-k!)} models that contain exactly k predictors

    		- Pick the best among these models and call it M_k Here k best is defined as having the smallest RSS(or largest R-squared)

    	- Select a single best model among M_0,…,M_p using cross validated prediction error, C_p, AIC, BIC or adjusted R^2

    ## Stepwise selection

    	- There are a lot of kinds that can happen if p goes very large. It can also leads to overfitting, so suggest stepwise selection

    	### Forward stepwise selection

    	- Let M_0 denote the null model, with no predictors

    	- For k=0,…,p-1

    		- Consider all p-k models that augment the predictors in M_k with one additional predictor

    		- Choose the best among this p-k models, and call it M_{k+1}.

    	- Select a single best model from among M_0,…,M_p using cross validated prediction error, C_p, AIC, BIC, or adjusted R^2

    	### Backward stepwise selection

    	- Let M_p denote the full model, with all predictors

    	- For k=p,p-1,…,1

    		- Consider all k models that contain all but one of the predictors in M_k

    		- Choose the best among this k models and call it M_{k-1}

    	- Select a single best model from among M_0,…,M_p using cross-validated prediction error, C_p, AIC, BIC or adjusted R^2

    ## Estimating test error

    	- Directly estimate the test error with using either a validation set or cross validation approach

    	- Mallow’s C_p = \frac1n(RSS+2d\hat\sigma^2)

    	- The AIC = -2\log L + 2d

    	- BIC = \frac1n(RSS+\log(n)d\hat\sigma^2)

    	- Adjusted R^2 = 1-\frac{RSS/(n-d-1)}{TSS/(n-1)} → large value indicates a model with low test error 

# Model Selection: Shrinkage Methods

    ## Ridge Regression

    ## LASSO

# Tree Based Methods, Decision Trees, Bagging, Random forests, Boosting

# SVM

# Unsupervised Learning: PCA & Clustering

# Nearest Neighbor Classifiers

# Linear & Softmax Classifiers

# Neural Networks & Backpropagation

# Convolution Neural Networks

# Activation functions, data augmentation, weight initialization, learning rate

# Regularization, advanced optimization, batch norm

# Recurrent Neural Networks

# Attentions & Basics of Transformer
