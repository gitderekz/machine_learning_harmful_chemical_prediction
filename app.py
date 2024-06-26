import os

# import packages
import numpy as np
from flask import Flask,request,jsonify,render_template
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle as pk

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [str(x) for x in request.form.values()]
    # payload = [np.array(int_features)]
    print('Payload: ',int_features)
    phone = [int_features[0]]
    message = [int_features[1]]

    # Use stored model
    if os.path.exists('toxicity_model.pkl'):
        with open('toxicity_model.pkl', 'rb') as model_file:
            model, cv = pk.load(model_file)

    message = cv.transform(message)
    print('message: ',message)
    prediction = model.predict(message)
    print('prediction: ',prediction)

    output = prediction[0].upper()
    # if output == 1:
    #     output = 'UNSAFE'
    # else:
    #     output = "SAFE"

    # return render_template('index.html',prediction_text='RESULT = []'.format(output))
    return render_template('index.html',prediction_text='THIS IS {}'.format(output))
    # return {"result":'{}'.format(output)}

# if __name__ == '__main__':
#     app.run(debug=True)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Bind to all interfaces