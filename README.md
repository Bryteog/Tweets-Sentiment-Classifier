#### Overview

Built a model to predict the sentiment behind a tweet. The sentiment labelled as "Polarity" in the dataset is has two classes, "Positive" and "Negative". The dataset is obtained from [kaggle](https://www.kaggle.com/datasets/kazanova/sentiment140). The data directory contains a single csv file made up of 1,600,000 tweets, user account name, date of tweet and a unique id.


#### Model

Four separate versions of the model each a bit different from the other are made.

##### Version 1
Text preprocessing is done to remove punctuation signs and assign embeddings to text with the Keras library.
The data is divided into three parts, training, testing and validating sets. A bidirectional LSTM with tahn activation is used along with a couple of dense layers. The last layer has a single with sigmoid activation. The model is trainined for 10 epochs and reaches a loss of 0.2905 and 0.2604 on the training and validation set, respectively.

##### Version 2
Text preprocessing is done using the nltk, sklearn-text and keras libraries. The @ sign in user names, various, url formats, punctuations and stop words are all removed from the tweets. The remaining text are then converted to sequences and padded. Training and testing splits are made using the sklearn library. A bidirectional LSTM with tahn activation is used along with a couple of dense layers with the last layer having a single with sigmoid activation. The model is trainined for 15 epochs but stops at the end of the 4th epoch due to overfitting. 

##### Version 3&4
Preprocessing and modelling is as was done in the 2nd version, further processing using text vectorising, tokenizing and sequence padding with sklearn and keras. The difference is how the processed data was made available for training.

Version 3 uses a 2-d array of shape (100000, 1) for the y vector, this is then fed as sliced tensors (along with the X vector) and then trained and evaluated. After 15 epochs the training and validation losses were 0.2413, and 0.2087 and accuracy was 89.33 and 90.9, all respectively.

Version 4 uses a 1-d array of shape (100000,) for the y vector, which is in turn fed as sliced tensors (along with the X vector) and then trained and evaluated. After 15 epochs the training and validation losses were 0.2413, and 0.2087 and accuracy was 89.74 and 91.3, all respectively.