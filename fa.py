# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 15:44:54 2015

@author: LIght
"""

from sklearn.decomposition import FactorAnalysis
import pandas as pd


class FactAnalysis:
    
    @staticmethod
    def groupMovieGenre(user_item_matrix,item_df):
        genre_num = 5
        fa_model = FactorAnalysis(n_components=genre_num)
        fa_model.fit(user_item_matrix)
        
        ## decomposited user np array, W represent sementic user info
        W = fa_model.fit_transform(user_item_matrix)
        ## decomposited item np array, H represent sementic item info
        H = fa_model.components_
        
        movie_fa = pd.DataFrame(H).T
        movie_fa = pd.concat([movie_fa,item_df],axis=1)
        movie_genre = ['Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
    
    ## return ret, 50 group related with movie genre
        ret_fa = pd.DataFrame(movie_fa[movie_fa[0]>0.05][movie_genre].sum(axis=0))
        for i in range(genre_num):
            ret_fa[str(i)] = pd.DataFrame(movie_fa[movie_fa[i]>0.05][movie_genre].sum(axis=0))
        return ret_fa, movie_fa
        
