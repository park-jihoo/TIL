---
id: 0cda2b1d-208b-4327-943a-03ae7d6997f3
title: Whose Opinions Do Language Models Reflect?
created_time: 2023-10-16T07:27:00.000Z
last_edited_time: 2023-10-23T13:54:00.000Z
하위 항목: []
subclass: NLP
class: Paper
작성일시: 2023-10-16T07:27:00.000Z
pdf: https://proceedings.mlr.press/v202/santurkar23a/santurkar23a.pdf
상위 항목: []

---

# Introduction

> 💡 Whose opinions (if any) do language models reflect?

*   A key evaluation for LMs in open-ended tasks will be not only to assess whether models are human-aligned broadly but also to identify whose opinions are reflected by LMs

## Contribution of this paper

*   A framework to study the opinions reflected by LMs and their alignment with different human populations

*   Build the OpinionQA dataset

*   Metrics

    *   Representativeness: How aligned is the default LM opinion distribution with the general US population(or a demographic group)?

    *   Steerability: Can an LM emulate the opinion distribution of a group when appropriately prompted?

    *   Consistency: Are the groups LMs align with consistent across the topic?

# The OpinionQA Dataset

*   Three challenges to tackle

    *   Identify topics where these opinions are relevant and curate pertinent questions for them

    *   The questions must be designed such that we can easilty extract LM opinions on them

    *   We need a reference distribution of human opinions from representative groups to compare LMs to

## The power of surveys

*   The primary approach for the latter currently is to use *public opinion surveys*

*   These surveys address the first of the tree challenges with the help of experts, who identify topics of public interest and carefully design questions to capture nuances of the topic

*   Finally, surveys determine humans’ opinion on these topic through extensive polling of the public a large

## Our Framework

*   Consider a survey with a set of question Q, where a question q has a set of possible answers A(q).

*   The question belong to topic T are denoted by Q\_T, and every individual h must select one answer F(h, q)

*   For a question, we can build distribution by aggregating the response

    ```undefined
    D_H(q) = \sum_{h\in H}w_h F(h,q)
    ```

## Instantiation OpinionQA

*   We apply this methodology to the annual “American Trends Panel”(ATP) polls conducted by Pew research to build the OpinionQA dataset.

*   This methodology is general, the OpinionQA dataset itself is English and US-centric. Thus, our subsequent analysis is limited to US populace.

# Measuring human-LM alignment

> 💡 Discuss how to probe language model opinions on questions from our OpinionQA dataset and compare them to the previously-obtained human opinion distributions

## Interfacing with models

### Prompting the model

*   Due to the multiple-choice nature of samples in our dataset, we can use the standard prompting approaches used for traditional question answering tasks

*   When evaluating representativeness, the goal is to understand the LM’s default opinion distribution, and we prompt the model using this standard QA template without any added context

*   Measuring steerability involves testing the model’s ability to adapt to a particular group.

*   We consider three approaches to supply this information to the LM

    *   QA: The group information is provided as a response to a previous multiple-choice survey question, using the phrasing used by Pew to collect this information.

    *   BIO: The group information is provided as a free-text response to a biographic question

    *   PORTRAY: The LM is instructed to pretend to be a member of said group, similar to the crowd-sourcing design.

### Extracting the output distribution

*   There’s no correct answer on our setting

*   For the model m, we are interested in the distribution of model opinions D\_m(q) for each question across the set of answer choices

*   We exponentiate and normalize the scores for all answer choices except refusal

*   We also measure the model’s refusal probability as the ratio of the exponentiated log probability of refusal vs. the exponentiated cumulative log probabilities for all choices

## Evaluating the model’s response

> 💡 We need similarity measure!

### Measuring opinion alignment

*   We define **alignment** between two opinion distiribution D\_1 and D\_2 on a set of questions Q as

    ```undefined
    \mathcal A (D_1, D_2;Q)=\frac1{|Q|}\sum_{q\in Q} 1 - \frac{\mathcal{WD}(D_1(q),D_2(q))}{N-1}
    ```

    where N is the number of answer choices and the normalization factor N-1 is the maximum \cal WD between any pair of distributions in this metric space

*   1-Wasserstein distance(\cal WD) is defined as the minimum cost for transforming D\_1 into D\_2

### On the use of the term alignment

*   We use theterm alignment of opinions and preferences between LMs and humans.

# Whose views do current LMs express?

> 💡 **Robustness**: We ensure that all our subsequent results are robust to such design choices by replicating our analysis with different prompt templates, and permuting the order in which answer choices are presented to the model

## Representativeness

### The Metric

*   We define the representativeness of an Lm with respect to the overall population as the average alignment between default opinion distribution and the overall population

    ```undefined
    \mathcal R_m^O(Q) = \mathcal A(D_m,D_O, Q)
    ```

### Are Current LMs representative?

*   Overall, we observe that none of the models are perfectly representative of the general populace.

*   Each of demographic groups is more representative of the overall populace than any of the LMs studied

*   \mathcal R\_m^O for most models is comparable to the opinion alignment of agnostic and orthodox people on abortion or democrats and republicans on climate change

### Group representativeness

*   The group representativeness scores for all the base LMs share striking similarities and thus mimic similar pools of human writers

*   The opinions reflected by these models align more with people who are liberal, high income, well-educated, and not religious or belong to religions other than Buddhists, Muslims and Hindus.

### Model representativeness

*   Human-feedback tuned models are less representative of overall opinions.

*   Specifically, it has an extremely sharp opinion distribution for most questions.

### Refusals

*   In our comparison of human and LM opinions so far, we omitted the “refusal” option for all question due to its non-ordinal nature.

## Steerability

> 💡 We now shift our focus from measuring the default aliginment of LM opinions with those of various demographics groups without prompting, to studying their steerability with group-specific prompting

### The Metric

### Steering doesn’t solve opinion misalignment

## Consistency

### Are LMs consistent?

### The Metric

# Related work

## Evaluating LM personas

## Subjectivity in evaluations

## Human-LM Alignment

## Bias, toxicity, and truthfulness

# Conclusions

## Limitations
