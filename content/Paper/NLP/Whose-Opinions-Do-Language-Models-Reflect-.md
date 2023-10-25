---
id: 0cda2b1d-208b-4327-943a-03ae7d6997f3
title: Whose Opinions Do Language Models Reflect?
created_time: 2023-10-16T07:27:00.000Z
last_edited_time: 2023-10-24T13:30:00.000Z
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

*   Concretely, we measure steerability as:

    ```undefined
    \mathcal S_m^G(Q) = \frac{1}{|Q|}\sum_{q\in Q}\max_{c_G\in[\text{QA,BIO,POR}]}\mathcal A(D_m(q;c_G),D_G(q))
    ```

    where D\_m(q;c\_G) denotes the LM opinion distribution.

*   Higher score indicates that the model is better aligned to the opinions of that group

### Steering doesn’t solve opinion misalignment

*   Most LMs do become somewhat more representative of subpopulation post steering.

*   However, none of the disparities in group opinion alignment of an LM disappear afterr steering.

## Consistency

> 💡 Are the views expressed by LMs consistent across the topics?

### Are LMs consistent?

*   The base model from both providers and RLHF trained text-davinci-003 from OpenAI seem to be most consistent

*   None of the models are perfectly consistent however.

### The Metric

*   Specifically, for a model, we first identify the group it best aligns across topics as

    ```undefined
    G_m^\text{best} :=\argmax_{G}\left(\frac 1T \sum_{T'}\mathcal R_M^G(Q_{T'})\right) 
    ```

*   Then, we define consistency as

    ```undefined
    \mathcal C_m :=\frac 1T\sum_T \mathbb{I}\left[\left(\argmax_{G}\mathcal R_M^G(Q_T)\right)=G_m^\text{best}\right]
    ```

*   Our metric \mathcal C\_m is bounnded between 0 and 1, and a higher score implies that the model agrees with the views of same subgroups across all topics.

# Related work

## Evaluating LM personas

*   By leveraging public opinion surveys, we are able to improve our understanding of LM steerability in three ways

    *   Breadth: Both in the range of different topics and steering groups

    *   Distributional View: Gauging whether LMs can match the spectrum of opinions of a group rather than its modal opinion

    *   Measurability: Using metrics grounded in human response distributions

*   Human feedback trained models often exhibit a left-leaning, pro-environmental stance.

## Subjectivity in evaluations

*   We approach the problem of evaluating opinions expressed by LMs through the use of surveys

## Human-LM Alignment

*   Asking who are the humans that we are/should be aligning the models to?

## Bias, toxicity, and truthfulness

*   Evaluating LMs on inherently subjective questions taken from Pew research

# Conclusions

## Limitations

### Alignment

*   We view our metrics as useful ways to understand the behavior of LMs, and not necessarily as benchmarks that should be blindly optimized

### ATP and surveys

*   Surveys in general may be sensitive to details such as question specificity, but our conclusions are only valid for the populations to US

### Multiple-choice format

*   We focus on probing LM behaviors using a multiple-choice prompts, which differs from the open-ended text generation setting in which LMs are being increasingly used.
