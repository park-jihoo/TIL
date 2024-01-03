---
id: 3e9df96f-67fe-46ce-9ea1-126fdb9a9fc7
title: ML Multiple choices
created_time: 2023-08-30T13:49:00.000Z
last_edited_time: 2023-09-16T05:27:00.000Z
하위 항목: []
subclass: 2023_QE
class: Coursework
작성일시: 2023-08-30T13:49:00.000Z
상위 항목:
  - id: bcab10cb-9cba-471e-bda4-771a583f9f1e

---

# Set 01

    - High entropy means that the partitions in classification are

    	- Pure

    	- Not pure

    	- Useful

    	- Useless

    	Answer

    		(b) Not Pure

    - A machine learning problem involves four attributes plus a class. The attributes have 3, 2, 2, and 2 possible values each. The class has 3 possible values. How many maximum possible different examples are there?

    	- 12

    	- 24

    	- 48

    	- 72

    	Answer

    		(d) 72

    - Which of the following is NOT supervised leraning

    	- PCA

    	- Decision Tree

    	- Linear Regression

    	- Naive Bayesian

    	Answer

    		(a) PCA

    - Which of the following statements about Naive Bayes is incorrect?

    	- Attributes are equally important.

    	- Attributes are statistically dependent of one other given the class value.

    	- Attributes are statistically independent of one other given the class value

    	- Attributes can be nominal or numeric

    	Answer

    		(b) Attributes are statically dependent of one other given the class value

    - Suppose we would like to perform clustering on spatial data such as the geometrical locations of houses. We wish to produce clusters of many different sizes and shapes. Which of the following methods is the most appropriate?

    	- Decision Trees

    	- Density-based clustering

    	- Model-based clustering

    	- K-means Clustering

    	Answer

    		Density-based clustering

# Set 02

    - Which of the following are the spatial clustering algorithms?

    	- Partitioning based clustering

    	- K-means clustering

    	- Grid based clustering

    	- All of the above

    	Answer

    		(d) All of the above

    - Which of the following tasks can be best solved using Clustering?

    	- Predicting the amount of rainfall based on various cues

    	- Detecting fradulent credit card transactions

    	- Training a robot to solve a maze

    	- All of the above

    	Answer

    		(b) Detecting fraudulent credit card transactions

    - Choose the correct option from the following

    	- When working with a small dataset, one should prefer low bias/high variance classifiers over high bias/low variance classifiers.

    	- When working with a small dataset, one should prefer high bias/low variance classifiers over low bias/high variance classifiers.

    	- When working with a large dataset, one should prefer high bias/low variance classifiers over low bias/high variance classifiers.

    	- When working with a large dataset, one should prefer low bias/high variance classifiers over high bias/low variance classifiers.

    	Answer

    		(b) and (d)

# Set 03

    - Predicting the amount of rainfall in a region based on various cues is a __________ problem.

    	- Supervised Learning

    	- Unsupervised Learning

    	- Clustering

    	- None of the above

    	Answer

    		(a) Supervised Learning

    - A and B are two events. If P(A, B) decreases while P(A) increases, which of the following is true?

    	- P(A|B) decreases

    	- P(B|A) decreases

    	- P(B) decreases

    	- All of above

    	Answer

    		(b)

    - In building a linear regression model for a particular data set, you observe the coefficient of one of the features having a relatively high negative value. This suggests that

    	- This feature has a strong effect on the model (should be retained)

    	- This feature does not have a strong effect on the model (should be ignored)

    	- It is not possible to comment on the importance of this feature without additional information

    	- Nothing can be determined.

    	Answer

    		(c) It is not possible to comment on the importance of this feature without additional information

    - After applying a regularization penalty in linear regression, you find that some of the coefficients of w are zeroed out. Which of the following penalties might have been used?

    	- L_0 Norm

    	- L_1 Norm

    	- L_2 Norm

    	- either a or b

    	Answer

    		(d) either a or b

    - MLE Estimators are often undesirable because

    	- They are biased

    	- They have high variance

    	- They are not consistent estimators

    	- None of the above

    	Answer

    		(b) They have high variance

# Set 04

    - As the number of training examples goes to infinity, your model trained on that data will have

    	- Lower variance

    	- Higher variance

    	- Same variance

    	- None of the above

    	Answer

    		(a) Lower variance

    - Which of the following is/are true regarding an SVM?

    	- For two dimensional data points, the separating hyperplane learnt by a linear SVM will be a straight line.

    	- In theory, a Gaussian kernel SVM cannot model any complex separating hyperplane.

    	- For every kernel function used in a SVM, one can obtain an equivalent closed form basis expansion.

    	- Overfitting in an SVM is not a function of number of support vectors.

    	Answer

    		(a) For two dimensional data points, the separating hyperplane learnt by a linear svm will be a straight line

# Set 05

    - The model obtained by applying linear regression on the identified subset of features may differ from the model obtained at the end of the process of identifying the subset during

    	- Best-subset selection

    	- Forward stepwise selection

    	- Forward stage wise selection

    	- All of the above

    	Answer

    		(c) Forward stage wise selection

    - You trained a binary classifier model which gives very high accuracy on the training data, but much lower accuracy on validation data. Which of the following may be true?

    	- This is an instance of overfitting

    	- This is an instance of underfitting

    	- The training is not well regularized

    	- The training and testing examples are sampled from different distributions

    	Answer

    		(a), (c), (d)

    - What are support vectors?

    	- The examples farthest from the decision boundary

    	- The only example necessary to compute f(x) in a SVM

    	- The class centroids

    	- All of the examples that have a non-zero weight \alpha_k in a SVM

    	Answer

    		(b), (d)

# Set 06

    - You’ve just finished training a decision tree for spam classification, and it is getting abnormally bad performance on both your training and test sets. You know that your implementation has no bugs, so what could be causing the problem?

    	- Your decision trees are too shallow

    	- You need to increase the learning rate

    	- You are overfitting

    	- None of the above

    	Answer

    		(a) Your decision trees are too shallow

    - ___________  refers to a model that can neither model the training data nor generalize to new data

    	- good fitting

    	- overfitting

    	- underfitting

    	- all of the above

    	Answer

    		(c) underfitting

# Set 07

    - Which of the following can only be used when training data are linearly separable?

    	- Linear hard-margin SVM

    	- Linear Logistic Regression

    	- Linear Soft margin SVM

    	- The centroid method

    	Answer

    		(a) Linear hard-margin SVM

    - The K-means algorithm

    	- Requires the dimension of the feature space to be no bigger than the number of samples

    	- Has the smallest value of objective function when K=1

    	- Minimizes the within class variance for given number of clusters

    	- Converges to the global optimum if and only if the initial means are chosen as some of the samples themselves

    	Answer

    		(c) Minimizes the within class variance for a given number of clusters

    - For polynomial regression, which one of these structural assumptions is the one that most affects the trade-off between underfitting and overfitting:

    	- The polynomial degree

    	- Whether we learn the weights by matrix inversion or gradient descent

    	- The assumed variance of the Gaussian noise

    	- The use of a constant-term unit input

    	Answer

    		(a) the polynomial degree

# Set 08

    - Which among the following prevents overfitting when we perform bagging?

    	- The use of sampling with replacement as the sampling technique

    	- The use of weak classifiers

    	- The use of classification algorithms which are not prone to overfitting

    	- The practice of validation performed on every classifier trained

    	Answer

    		(b) The use of weak classifier

    - Averaging the output of multiple decision trees helps _________.

    	- Increase bias

    	- Decrease bias

    	- Increase variance

    	- Decrease variance

    	Answer

    		(d) Decrease variance

    - If N is the number of instances in the training dataset, nearest neighbors has a classification run time of

    	- O(1)

    	- O( N )

    	- O(\log N )

    	- O( N^2 )

    	Answer

    		(b) O(N)

    - Which among the following is/are some of the assumptions made by the k-means algorithms(assuming euclidean distance measure)?

    	- Clusters are spherical in shape

    	- Clusters are of similar sizes

    	- Data points in one cluster are well separated from data points of other clusters

    	- There is no wide variation in density among the data points

    	Answer

    		(a) and (b)

    - Which of the following is more appropriate to do feature selection?

    	- Ridge

    	- Lasso

    	- Both (a) and (b)

    	- Neither (a) nor (b)

    	Answer

    		(b) Lasso

# Set 09

    - The number of test examples needed to get statistically significant results should be _________

    	- Larger if the error rate is larger

    	- Larger if the error rate is smaller

    	- Smaller if the error rate is smaller

    	- It doesn’t matter

    	Answer

    		(b) Larger if the error rate is smaller

    - Which of the following is the main reason for pruning a decision tree?

    	- To save computing time during testing

    	- To save space for storing the Decision Tree

    	- To make the training set error smaller

    	- To avoid overfitting the training set

    	Answer

    		(d) To avoid overfitting the training set

# Set 10

    - What would you do in PCA to get same projection as SVD?

    	- Transform data to zero mean

    	- Transform data to zero median

    	- Not possible

    	- None of these

    	Answer

    		(a) transform data to zero mean

    - Regarding bias and variance, which of the following statements are true?

    	- Models which overfit have a high bias

    	- Models which overfit have a low bias

    	- Models which underfit have a high variance

    	- Models which underfit have a low variance

    	Answer

    		(b) and (d)

    - Given a large dataset of medical records from patients suffering from heart disease, try to learn whether there might be different clusters of such patients for which we might tailor separate treatments. What kind of learning problem is this?

    	- Supervised learning

    	- Unsupervised learning

    	- Both (a) and (b)

    	- Neither (a) nor (b)

    	Answer

    		(b) Unsupervised Learning

    - Predicting on whether will it rain or not tomorrow evening at particular time is a type of _______ problem

    	- Classification

    	- Regression

    	- Unsupervised Learning

    	- All of the above

    	Answer

    		(a) Classification

# Set 11

    - For a gaussian bayes classifier, which one of these structural assumptions is the one that most affects the trade-off between underfitting and overfitting?

    	- Whether we learn the class centers by maximum likelihood or gradient descent

    	- Whether we assume full class covariance matrices or diagonal class covariance matrices

    	- Whether we have equal class priors or priors estimated from the data

    	- Whether we allow classes to have different mean vectors or we force them to share the same mean vector

    	Answer

    		(b) Whether we assume full class covariance matrices or diagonal class covariance matrices

# Set 13

    - Which of the following methods can achieve zero training error on any linearly separable dataset?

    	- Decision Tree

    	- 15 Nearest Neighbors

    	- Perceptrons

    	- Logistic Regression

    	Answer

    		(a) (b)

    - Consider a point that is correctly classified and distant from the decision boundary. Which of the following methods will be unaffected by this point?

    	- Nearest neighbor

    	- SVM

    	- Logistic regression

    	- Linear regression

    	Answer

    		(b) SVM

    - Suppose your model is overfitting. Which of the following is NOT a valid way to try and reduce the overfitting?

    	- Increase the amount of training data

    	- Improve the optimization algorithm being used for error minimization

    	- Decrease the model complexity

    	- Reduce the noise in the training data

# Set 14

    - You are given a labeled binary classification data set with N data points and D features. Suppose that N<D In training an SVM on this data set, which of the following kernels is likely to be most appropriate?

    	- Linear Kernel

    	- Quadratic Kernel

    	- Higher-order polynomial kernel

    	- RBF kernel

# Set 15

    - In the general case, imagine that we have d binary features, and we want to count the number of features with value 1. How many leaf nodes would a decision tree need to represent this funciton?

    	- 2^1 leaf nodes

    	- 2^d leaf nodes

    	- 2^{d-1} leaf nodes

    	- 2^d-1 leaf nodes

    	Answer

    		(b) 2^d leaf nodes

    - The measures developed for selecting the best split are often based on the degree of impurity of the child nodes. Which of the following is NOT an impurity measure

    	- Gini

    	- Entropy

    	- Pruning

    	- Classification error

    	Answer

    		(c) Pruning

    - We are dealing with samples x where x is a single value. We would like to test two alternative regression models

    	```undefined
    	\begin{aligned}y&=ax+e\\y&=ax+bx^2+e\end{aligned}
    	```

    	Which of the two models are more likely to fit the test data better?

    	- model 1

    	- Model 2

    	- both will equally fit

    	- impossible to decide

    	Answer

    		(d) impossible to decide

    - What is the biggest weakness of decision trees compared to logistic regression classifiers?

    	- Decision trees are more likely to overfit the data

    	- Decision trees are more likely to underfit the data

    	- Decision trees do not assume independence of the input features

    	- None of the mentioned

    	Answer

    		(a) Decision trees are more likely to overfit the data

    - Which of the following classifiers can generate linear decision boundary?

    	- Linear SVM

    	- Random forest

    	- Logistic Regression

    	- kNN

    	Answer

    		(a) and (c)

# Set 16

    - If we increase the k value in kNN, the model will _________ the bias and __________ the variance

    	- Decrease, Decrease

    	- Increase, Decrease

    	- Decrease, Increasae

    	- Increase, Increase

    	Answer

    		(b) Increase, Decrease

    - For a large k value the kNN model becomes ________ and _______

    	- Complex model, Overfit

    	- Complex model, Underfit

    	- Simple model, Underfit

    	- Simple model, Overfit

    	Answer

    		(c) Simple model, Underfit

    - When we have a real-valued input attribute during decision-tree learning, what would be the impact multi-way split with one branch for each of the distinct values of the attribute?

    	- It’s too computationally expensive

    	- It would probably result in a decision tree that scores badly on the training set and a test set

    	- It would probably result in a decision tree that scores well on the training set but badly on a test set

    	- It would probably result in a decision tree that scores well on a test set but badly on a training set

    	Answer

    		(c) It would probably result in a decision tree that scores well on the training set but badly on a test set

# Set 17

    - The partitions in a classification are __________ if the entropy is high

    	- Pure

    	- Not pure

    	- Useless

    	- Low noise

    	Answer

    		(b) Not pure

    - A measure of goodness of fit for the estimated regression equation is the

    	- Multiple coefficient of determination

    	- Mean square due to error

    	- Mean square due to regression

    	- All of the above

    	Answer

    		(c) Mean square due to regression

    - A regression model in which more than one independent variable is used to predict the dependent variable is called

    	- Simple linear regression model

    	- Multiple regression model

    	- Independent model

    	- None of the above

    	Answer

    		(b) Multiple Regression Model

# Set 19

    - Which of the following cross validation versions may not be suitable for very large datasets with hundreds of thousands of samples?

    	- k-fold CV

    	- LOOCV

    	- Holdout method

    	- All of the above

    	Answer

    		(b) Leave-one-out CV

    - Which of the following cross validation version is suitable quicker CV for very large datasets with hundreds of thousands of samples?

    	- k-fold CV

    	- LOOCV

    	- Holdout method

    	- All of the above

    	Answer

    		(c) Holdout method

    - Which of the following is a disadvantage of k-fold CV method?

    	- The variance of resulting estimate is reduced as k is increased

    	- This usually doesn’t take longer time to compute

    	- Reduced bias

    	- The training algorithm has to rerun from scratch k times

    	Answer

    		(d) The training algorithm has to rerun from scratch k times

    - Consider that you are analyzing a large collection of fraudulent credit card transactions to discover if there are sub-types of these transactions. Which of the following learning methods best describes the given learning problem?

    	- Reinforcement Learning

    	- Supervised Learning

    	- Unsupervised Learning

    	- Semi-supervised Learning

    	Answer

    		(c) Unsupervised Learning

# Set 20

    - Which of the following clustering algorithm requires the number of clusters to be pre-specified?

    	- hierarchical clustering

    	- k-means clustering

    	- DBSCAN

    	- Markov clustering algorithm

    	Answer

    		(b) k-means clustering

    - Identify the best method that is used for finding optimal clusters in k-means algorithm

    	- Euclidean method

    	- Manhattan method

    	- Elbow method

    	- Silhouette method

    	Answer

    		(c) Elbow method

    - If we would like to produce learning rules that are easily interpreted by humans, which of the following machine learning task would we use?

    	- Logistic Regression

    	- Nearest Neighbor

    	- Decision tree learning

    	- SVM

    	Answer

    		(c) Decision tree learning

# Set 21

    - In terms of the bias-variance trade-off, which of the following is substantially more harmful to the test error than the training error?

    	- Bias

    	- Loss

    	- Variance

    	- Risk

    	Answer

    		(c) Variance

    - Which of the following learning algorithm will return a classifier if the training data is not linearly separable?

    	- Hard margin SVM

    	- Soft margin SVM

    	- Perceptron

    	- Naive bayes

    	Answer

    		(b) Soft margin SVM

    - Modeling a classification rule directly from the input data like in logistic regression fits which of the following classification methods?

    	- Discriminative classification

    	- Generative classification

    	- Probabilistic classification

    	- All of the above

    	Answer

    		(a) Discriminative classification
