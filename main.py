# -*- coding: utf-8 -*-
"""
Created on Wed Mar 04 15:31:20 2015

@author: LIght
"""

import feature_prep
import lfm
import predict
import pandas as pd
import numpy as np
import scipy.sparse
from sparsesvd import sparsesvd
import re
import utility
import scipy
from sklearn.decomposition import ProjectedGradientNMF




## import data
columns = ['userid','itemid','rating','timestamp']
df = pd.read_csv(utility.CONST_PATH + 'u.data', names=columns, sep='\t')

user_item_matrix, item_item_matrix = feature_prep.Feature.main(df)

df = predict.Predict.main(user_item_matrix, item_item_matrix, df)

print sum(abs(df.rating-df.score))/len(df)
print 'rmse: ',np.sqrt(sum((df.rating-df.score)**2)/len(df))

item_df = pd.read_csv(utility.CONST_PATH + 'u.item', names=['movie'],sep='\t')
item_df = utility.Utility.prep_item_df(item_df)


genre_num = 50
A = np.array(user_item_matrix)
nmf_model = ProjectedGradientNMF(n_components = genre_num, init='random', random_state=0)
nmf_model.fit(A)
## decomposited user np array
W = nmf_model.fit_transform(A)

## decomposited item np array
H = nmf_model.components_

movie = pd.DataFrame(H).T
movie = pd.concat([movie,item_df],axis=1)

movie_genre = ['Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']


ret = pd.DataFrame(movie[movie[0]>5][movie_genre].sum(axis=0))
for i in range(genre_num):
    ret[str(i)] = pd.DataFrame(movie[movie[i]>5][movie_genre].sum(axis=0))