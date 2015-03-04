# -*- coding: utf-8 -*-
"""
Created on Wed Mar 04 15:30:30 2015

@author: LIght
"""

import pandas as pd
import copy
from sklearn import metrics

class Feature:

## get all the item that showed up in user_item record
    @staticmethod    
    def get_itemList(data_df):
        itemlist_tmp = list(set(data_df.itemid))
        itemdict = {item:0 for item in itemlist_tmp}
        return itemdict        
        
## get user item dictionary
    @staticmethod
    def get_user_item_matrix(data_df, itemdict):
        user_item_dict = {}     
    ## group items that each user has rated
        item_groupby_user = data_df.groupby(by='userid')
    ## get item list groupby users
        user_item_tuple_list = [item for item in item_groupby_user.itemid]
        user_rating_tuple_list = [rating for rating in item_groupby_user.rating]        

        for i in range(len(user_item_tuple_list)):
    ## calculate each item vector, assign item vector of if item exists in itemlist to each user
            user_item_tuple = user_item_tuple_list[i]
            user_rating_tuple = user_rating_tuple_list[i]
            item_vector = copy.deepcopy(itemdict)
            user = user_item_tuple[0]            
            for j in range(len(user_item_tuple[1])):
                #item_vector[item] = item_vector[item] + 1
                item = list(user_item_tuple[1])[j]
                rating = list(user_rating_tuple[1])[j]                                
                item_vector[item] = item_vector[item] + rating
            user_item_dict[user_item_tuple[0]] = item_vector
        user_item_matrix = pd.DataFrame(user_item_dict.values())
        user_item_matrix.index = user_item_dict.keys()
        return user_item_matrix

    @staticmethod
    def item_similarity(user_item_matrix):
    ## calculate item pairwise similarity        
        item_item_matrix = pd.DataFrame(1-metrics.pairwise.pairwise_distances(user_item_matrix.T ,metric='cosine'))
        item_item_matrix.columns = user_item_matrix.columns
        item_item_matrix.index = user_item_matrix.columns   
        item_item_matrix = item_item_matrix.fillna(0)        
        return item_item_matrix
        
        
        
        
    @staticmethod        
    def main(data_df):
    ## get all the item         
        itemdict = Feature.get_itemList(data_df)
    ## get user_item matrix, u1,item1 is u1's rating for item1        
        user_item_matrix = Feature.get_user_item_matrix(data_df, itemdict)
    ## get item_item_matrix        
        item_item_matrix = Feature.item_similarity(user_item_matrix)
        return user_item_matrix, item_item_matrix








