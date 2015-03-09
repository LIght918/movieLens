# -*- coding: utf-8 -*-
"""
Created on Wed Mar 04 15:31:20 2015

@author: LIght
"""

import feature_prep
import predict
import pandas as pd
import numpy as np
import scipy.sparse
from sparsesvd import sparsesvd
import re
import utility
import scipy





## import data
columns = ['userid','itemid','rating','timestamp']
df = pd.read_csv(utility.CONST_PATH + 'u.data', names=columns, sep='\t')

user_item_matrix, item_item_matrix = feature_prep.Feature.main(df)

df = predict.Predict.main(user_item_matrix, item_item_matrix, df)

print sum(abs(df.rating-df.score))/len(df)
print 'rmse: ',np.sqrt(sum((df.rating-df.score)**2)/len(df))


##SVD 

smat_df = scipy.sparse.csc_matrix(user_item_matrix) # convert to sparse CSC format
ut, s, vt = sparsesvd(smat_df, 18) # do SVD, asking for 100 factors
movie_df = pd.DataFrame(vt).T
item_df = pd.read_csv(utility.CONST_PATH+'u.item', sep='\t', names=['movie'])
item_df = utility.Utility.prep_item_df(item_df)

test = pd.concat([movie_df,item_df],axis=1)
test = test.drop('moviename',axis=1)

test.corr()
