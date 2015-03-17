# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:31:50 2015

@author: LIght
"""

from sklearn.decomposition import TruncatedSVD
import numpy as np
import pandas as pd
import scipy

class LSA:
    
    @staticmethod
    def groupMovieGenre(user_item_matrix,item_df):
        genre_num = 20
        user_item_matrix = scipy.sparse.csr_matrix(user_item_matrix.values)
        lsa_model = TruncatedSVD(n_components=genre_num, random_state=40)
        lsa_model.fit(user_item_matrix)
        
        ## decomposited user np array, W represent sementic user info
        W = lsa_model.fit_transform(user_item_matrix)
        ## decomposited item np array, H represent sementic item info
        H = lsa_model.components_
        
        movie_lsa = pd.DataFrame(H).T
        movie_lsa = pd.concat([movie_lsa,item_df],axis=1)
        movie_genre = ['Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
    
    ## return ret, 50 group related with movie genre
        ret_lsa = pd.DataFrame(movie_lsa[movie_lsa[0]>0.05][movie_genre].sum(axis=0))
        for i in range(genre_num):
            ret_lsa[str(i)] = pd.DataFrame(movie_lsa[movie_lsa[i]>0.05][movie_genre].sum(axis=0))
        return ret_lsa, movie_lsa
        