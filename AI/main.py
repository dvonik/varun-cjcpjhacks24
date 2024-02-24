import pandas as pd
import numpy as np
import pytesseract
import easyocr
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import requests

#Step 1: Reprocess the Data through OCR requests
# Extract all relevant information from the receipt

receipts = ['image.jpg']
amounts = []
merchants = []
reader = easyocr.Reader(['en'])
for receipt in receipts:
    img = Image.open(receipt)
    text = reader.readText(img)
    
    
# Extract bank account balance and recent transactions
# will be accessed through users bank account and the back end

bank_account = {'balance' : 0, 'recent-transcations' : []};


# Step 2: Clean and preprocess the data

# Remove outliers from the amounts
amounts = [a for a in amounts if a < 1000]

# Handle missing values in the bank account data
bank_account['transactions'].remove(1000)

# Normalize the data
amounts = [a / np.mean(amounts) for a in amounts]
bank_account['balance'] = bank_account['balance'] / np.mean(bank_account['balance'])
bank_account['transactions'] = [t / np.mean(bank_account['transactions']) for t in bank_account['transactions']]

# Step 3: Train the machine learning model

# Combine the receipt and bank account data
data = pd.DataFrame({'amount': amounts, 'merchant': merchants, 'balance': bank_account['balance'], 'transaction': bank_account['transactions']})

# Encode the categorical variables
data = pd.get_dummies(data, columns=['merchant'])

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(data.drop('amount', axis=1), data['amount'], test_size=0.2, random_state=42)

# Train the machine learning model
model = RandomForestClassifier()