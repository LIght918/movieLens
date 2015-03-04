# -*- coding: utf-8 -*-
"""
Created on Wed Mar 04 15:31:20 2015

@author: LIght
"""

import feature_prep
import predict
import pandas as pd

PATH = '.\\..\\data\\'


## import data
columns = ['userid','itemid','rating','timestamp']
df = pd.read_csv(PATH + 'u.data', names=columns, sep='\t')

user_item_matrix, item_item_matrix = feature_prep.Feature.main(df)

df = predict.Predict.main(user_item_matrix, item_item_matrix, df)

user_item_all = user_item_matrix.loc[2,:]
## all the item that user has clicked
user_clicked_item = list(user_item_all[user_item_all>0].index)
user_item_rating = list(user_item_matrix.loc[userid,user_clicked_item])
## get all items interact with itemid in item_item_matrix, and calculate prob
all_related_item = list(item_item_matrix.loc[itemid,user_clicked_item])

## for each clicked vector get a score
all_related_item_positive_distance = np.dot(user_item_rating,all_related_item)*1.0/sum(all_related_item)
return all_related_item_positive_distance   