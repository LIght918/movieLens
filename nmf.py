# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 19:19:35 2015

@author: LIght
"""

from sklearn.decomposition import ProjectedGradientNMF
import utility
import numpy as np
import pandas as pd

##use of NMF
class NMF:
    
    @staticmethod
    def groupMovieGenre(user_item_matrix,item_df):
        genre_num = 50
        A = np.array(user_item_matrix)
        nmf_model = ProjectedGradientNMF(n_components = genre_num, init='random', random_state=0)
        nmf_model.fit(A)
        ## decomposited user np array, W represent sementic user info
        W = nmf_model.fit_transform(A)
        ## decomposited item np array, H represent sementic item info
        H = nmf_model.components_
        
    ## movie is df of each movie and it's probablity to each category
        movie = pd.DataFrame(H).T
        movie = pd.concat([movie,item_df],axis=1)
        movie_genre = ['Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
    
    ## return ret, 50 group related with movie genre
        ret = pd.DataFrame(movie[movie[0]>5][movie_genre].sum(axis=0))
        for i in range(genre_num):
            ret[str(i)] = pd.DataFrame(movie[movie[i]>5][movie_genre].sum(axis=0))
        return ret_nmf, movie_nmf
        
        
        
        
    