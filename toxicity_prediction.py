# import packages
import os

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle as pk

# import data
spam_df = pd.read_csv('ingredients.csv',sep=",") #spam dataframe

# # inspect data
# spam_df.groupby('Category').describe

# create new column spam(vectorize ham/spam to numerical data)
spam_df['Unsafe'] = spam_df['Classification'].apply(lambda x: 1 if x=='Unsafe' else 0)

# create train/test split
# x = email content(features), y = (label)
x_train, x_test, y_train, y_test = train_test_split(spam_df.Ingredients,spam_df.Classification,test_size = 0.25)

# find word count in mesage
cv = CountVectorizer()
# make it to matrix
x_train_count = cv.fit_transform(x_train.values)
x_train_count.toarray()

# train model
model = MultinomialNB()
model.fit(x_train_count, y_train)

# # Save model and vectorizer
# with open('toxicity_model.pkl', 'wb') as model_file:
#     pk.dump((model, cv), model_file)

# Use stored model
if os.path.exists('toxicity_model.pkl'):
    with open('toxicity_model.pkl', 'rb') as model_file:
        model, cv = pk.load(model_file)

# pre-test
valid_email = ['benzyl']
valid_email_count = cv.transform(valid_email)
print('message: ',valid_email_count)
result = model.predict(valid_email_count)
print('result1',result)
invalid_email = ['water']
invalid_email_count = cv.transform(invalid_email)
print('message: ',valid_email_count)
result = model.predict(invalid_email_count)
print('result2',result)

# test model
x_test_count = cv.transform(x_test)
test_result = model.score(x_test_count, y_test)
print(test_result)
