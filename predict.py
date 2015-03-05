# -*- coding: utf-8 -*-
"""
Created on Wed Mar 04 17:02:20 2015

@author: LIght
"""

from sklearn import metrics
import math
import numpy as np

class Predict:
    
    @staticmethod
    def calculate_item_clicked_probability(user_item_matrix, item_item_matrix, userid, itemid):
        user_item_all = user_item_matrix.loc[userid,:]
        ## all the item that user has clicked
        user_clicked_item = list(user_item_all[user_item_all>0].index)
        user_item_rating = user_item_matrix.loc[userid,user_clicked_item].values
        ## get all items interact with itemid in item_item_matrix, and calculate prob
        all_related_item = item_item_matrix.loc[itemid,user_clicked_item].values
        
        related_item_vector = [(all_related_item > 0.35) & (all_related_item!=1)]
        
        ## for each clicked vector get a score
        user_item_rating = user_item_rating[related_item_vector]
        all_related_item = all_related_item[related_item_vector]
        
        #print user_item_rating
        #rint all_related_item
        
        all_related_item_positive_distance = np.dot(user_item_rating,all_related_item)*1.0/sum(all_related_item)
        return all_related_item_positive_distance 
    
    
    @staticmethod
    def main(user_item_matrix, item_item_matrix, test):
        test['score'] = test.apply(lambda x: Predict.calculate_item_clicked_probability(user_item_matrix, item_item_matrix, x['userid'],x['itemid']),axis=1)
        #test['score_norm'] = (test['score'] - test['score'].mean()) / (test['score'].max() - test['score'].min())
        #test['predict'] = test.apply(lambda x: 1 if x['score_norm']>0.2 else -1,axis=1)
        
        #print 'precision:', metrics.precision_score(test['result'], test['predict'], labels=[-1,1], pos_label=1)
        #print 'recall:', metrics.recall_score(test['result'], test['predict'], labels=[-1,1], pos_label=1)
        return test
