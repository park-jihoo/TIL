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

# Set 09

# Set 10

# Set 11

# Set 13

# Set 14

# Set 15

# Set 16

# Set 17

# Set 19

# Set 20

# Set 21
