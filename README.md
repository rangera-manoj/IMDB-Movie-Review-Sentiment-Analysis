# IMDB-Movie-Review-Sentiment-Analysis
Basic EDA and Sentiment-Analysis-on-IMDB-Dataset.

Natural Language Processing

This is a basic form of Natural Language Processing (NLP) called Sentiment Analysis in which we will try and classify a movie review as either positive or negative.

## Sentiment Analysis

Sentiment analysis studies the subjective information in an expression, that is, the opinions, appraisals, emotions, or attitudes towards a topic, person or entity. Expressions can be classified as positive, negative, or neutral. For example: “I really like the new design of your website!” → Positive.

In clean_function.py, i define a cleaning function to clean our reviews.

## 1. IMDB Sentiment Analysis using Bag of Words
IMDB Movie review sentiment analysis using bag of words by MultinomialNB.

### Bag of Words

A bag-of-words model, or BoW for short, is a way of extracting features from text for use in modeling, such as with machine learning algorithms.A bag-of-words is a representation of text that describes the occurrence of words within a document. It involves two things:

a) A vocabulary of known words.
b) A measure of the presence of known words.

It is called a “bag” of words, because any information about the order or structure of words in the document is discarded. The model is only concerned with whether known words occur in the document, not where in the document.

### Result 
#### Confusion matrix
array([[4236    703]

       [816    4162]])
 
#### Classification report 
              precision    recall  f1-score   support

           0       0.84      0.86      0.85      4939
           1       0.86      0.84      0.85      4978

    accuracy                           0.85      9917
 

## 2. IMDB Sentiment Analysis using TF-IDF
IMDB Movie review sentiment analysis using TF-IDF by MultinomialNB.

### TF-IDF
A problem with scoring word frequency is that highly frequent words start to dominate in the document (e.g. larger score), but may not contain as much “informational content” to the model as rarer but perhaps domain specific words.

One approach is to rescale the frequency of words by how often they appear in all documents, so that the scores for frequent words like “the” that are also frequent across all documents are penalized.

This approach to scoring is called Term Frequency – Inverse Document Frequency, or TF-IDF for short, where:

* Term Frequency: is a scoring of the frequency of the word in the current document.
* Inverse Document Frequency: is a scoring of how rare the word is across documents.
* 
The scores are a weighting where not all words are equally as important or interesting.The scores have the effect of highlighting words that are distinct (contain useful information) in a given document.

### Result
#### Confusion matrix
array([[4225    714]

       [711    4267]])

#### Classification report 
              precision    recall  f1-score   support

           0       0.86      0.86      0.86      4939
           1       0.86      0.86      0.86      4978

    accuracy                           0.86      9917


## 3. IMDB Sentiment Analysis using LSTM-Deep Learning(word embedding)
IMDB Movie review sentiment analysis using LSTM-Depp learning.

### Word embedding
A word embedding is a learned representation for text where words that have the same meaning have a similar representation.

Word embeddings are in fact a class of techniques where individual words are represented as real-valued vectors in a predefined vector space. Each word is mapped to one vector and the vector values are learned in a way that resembles a neural network, and hence the technique is often lumped into the field of deep learning.

Each word is represented by a real-valued vector, often tens or hundreds of dimensions. This is contrasted to the thousands or millions of dimensions required for sparse word representations, such as a one-hot encoding.

### Plot
#### Losses plot
![imdb loss](https://user-images.githubusercontent.com/88196035/134050897-c9b29f4f-1c94-4606-814b-cdc0ebc6b4de.png)

#### Accuracy plot
![imdb accu](https://user-images.githubusercontent.com/88196035/134050907-d4654746-8fee-4dad-9d77-6139e9024eb2.png)


## Dataset

This is a dataset for binary sentiment classification containing substantially more data than previous benchmark datasets. We provide a set of 25,000 highly polar movie reviews for training, and 25,000 for testing.

The dataset can be downloaded here: https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews
