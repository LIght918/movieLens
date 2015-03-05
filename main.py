# -*- coding: utf-8 -*-
"""
Created on Wed Mar 04 15:31:20 2015

@author: LIght
"""

import feature_prep
import predict
import pandas as pd
from numpy import linalg as la  

PATH = '.\\..\\data\\'


## import data
columns = ['userid','itemid','rating','timestamp']
df = pd.read_csv(PATH + 'u.data', names=columns, sep='\t')

user_item_matrix, item_item_matrix = feature_prep.Feature.main(df)

df = predict.Predict.main(user_item_matrix, item_item_matrix, df)

print sum(abs(df.rating-df.score))/len(df)

##SVD 

U,sigma,VT=la.svd(user_item_matrix) 