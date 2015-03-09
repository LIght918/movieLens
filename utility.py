# -*- coding: utf-8 -*-
"""
Created on Mon Mar 09 13:42:14 2015

@author: LIght
"""

import pandas as pd 
import numpy as np

CONST_PATH = '.\\..\\data\\'

class Utility:
    
    @staticmethod
## convert the format of movie item dataframe, put each tab into each columns    
    def prep_item_df(item_df):

    ## sec columns is movie names, fields[5-23] is the movie genre        
        item_df['moviename'] = item_df.apply(lambda x: x['movie'].split('|')[1], axis=1)
        item_df['Action'] = item_df.apply(lambda x: x['movie'].split('|')[5], axis=1)
        item_df['Adventure'] = item_df.apply(lambda x: x['movie'].split('|')[6], axis=1)
        item_df['Animation'] = item_df.apply(lambda x: x['movie'].split('|')[7], axis=1)
        item_df['Children'] = item_df.apply(lambda x: x['movie'].split('|')[8], axis=1)
        item_df['Comedy'] = item_df.apply(lambda x: x['movie'].split('|')[9], axis=1)
        item_df['Crime'] = item_df.apply(lambda x: x['movie'].split('|')[10], axis=1)
        item_df['Documentary'] = item_df.apply(lambda x: x['movie'].split('|')[11], axis=1)
        item_df['Drama'] = item_df.apply(lambda x: x['movie'].split('|')[12], axis=1)
        item_df['Fantasy'] = item_df.apply(lambda x: x['movie'].split('|')[13], axis=1)
        item_df['Film-Noir'] = item_df.apply(lambda x: x['movie'].split('|')[14], axis=1)
        item_df['Horror'] = item_df.apply(lambda x: x['movie'].split('|')[15], axis=1)
        item_df['Musical'] = item_df.apply(lambda x: x['movie'].split('|')[16], axis=1)
        item_df['Mystery'] = item_df.apply(lambda x: x['movie'].split('|')[17], axis=1)
        item_df['Romance'] = item_df.apply(lambda x: x['movie'].split('|')[18], axis=1)
        item_df['Sci-Fi'] = item_df.apply(lambda x: x['movie'].split('|')[19], axis=1)
        item_df['Thriller'] = item_df.apply(lambda x: x['movie'].split('|')[20], axis=1)
        item_df['War'] = item_df.apply(lambda x: x['movie'].split('|')[21], axis=1)
        item_df['Western'] = item_df.apply(lambda x: x['movie'].split('|')[22], axis=1)
        
        item_df['Action'] = item_df['Action'].astype(int)
        item_df['Adventure'] = item_df['Adventure'].astype(int)
        item_df['Animation'] = item_df['Animation'].astype(int)
        item_df['Children'] = item_df['Children'].astype(int)
        item_df['Comedy'] = item_df['Comedy'].astype(int)
        item_df['Crime'] = item_df['Crime'].astype(int)
        item_df['Documentary'] = item_df['Documentary'].astype(int)
        item_df['Drama'] = item_df['Drama'].astype(int)
        item_df['Fantasy'] = item_df['Fantasy'].astype(int)
        item_df['Film-Noir'] = item_df['Film-Noir'].astype(int)
        item_df['Horror'] = item_df['Horror'].astype(int)
        item_df['Musical'] = item_df['Musical'].astype(int)
        item_df['Mystery'] = item_df['Mystery'].astype(int)
        item_df['Romance'] = item_df['Romance'].astype(int)
        item_df['Sci-Fi'] = item_df['Sci-Fi'].astype(int)
        item_df['Thriller'] = item_df['Thriller'].astype(int)
        item_df['War'] = item_df['War'].astype(int)
        item_df['Western'] = item_df['Western'].astype(int)
        print type(item_df['Action'][1])
        item_df = item_df.drop('movie',axis=1)
        return item_df