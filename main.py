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
import nmf
import lsa
import fa



## import data
columns = ['userid','itemid','rating','timestamp']
#df_small = pd.read_csv(utility.CONST_PATH + 'u.data', names=columns, sep='\t')
#ser_item_matrix, item_item_matrix = feature_prep.Feature.main(df_small)
#df_small = predict.Predict.main(user_item_matrix, item_item_matrix, df_small)
#item_df = pd.read_csv(utility.CONST_PATH + 'u.item', names=['movie'],sep='\t')
#item_df = utility.Utility.prep_item_df(item_df)

#print sum(abs(df_small.rating-df_small.score))/len(df_small)
#print 'rmse: ',np.sqrt(sum((df_small.rating-df_small.score)**2)/len(df_small))

#df_10m = pd.read_csv(utility.CONST_PATH + 'ratings.dat', names=columns, sep='::')
#user_item_matrix, item_item_matrix = feature_prep.Feature.main(df_10m)
item_df_10m = pd.read_csv(utility.CONST_PATH + 'movies.dat', names=['movie_tmp'],sep='\t')
item_df_10m = utility.Utility.prep_item_df_large(item_df_10m)
item_df_10m = utility.Utility.prep_item_df(item_df_10m)
print 'item_matrix loaded...'

df_1m = pd.read_csv(utility.CONST_PATH + 'out.movielens-1m', names=columns, skiprows=1,sep=' ')
user_item_matrix, item_item_matrix = feature_prep.Feature.main(df_1m)

ret, movie = fa.FactAnalysis.groupMovieGenre(user_item_matrix,item_df_10m)  ## fact analysis

#ret, movie = lsa.LSA.groupMovieGenre(user_item_matrix,item_df_10m)  ## LSA



## ret['0'].plot(kind='bar')  / sample code to plot genre
## movie[movie[18]>5]['moviename']  /sample code to plot movie belong to that category
## movie[[0,'moviename']].sort([0], ascending=False).head(10) select top 10 movie from categ


