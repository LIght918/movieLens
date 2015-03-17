# -*- coding: utf-8 -*-
"""
Created on Mon Mar 09 13:42:14 2015

@author: LIght
"""

import pandas as pd 
import numpy as np
import copy

CONST_PATH = '.\\..\\data\\'

class Utility:
    
    @staticmethod
## convert the format of movie item dataframe, put each tab into each columns    
    def prep_item_df(item_df):

    ## sec columns is movie names, fields[5-23] is the movie genre        
        item_df['moviename'] = item_df.apply(lambda x: x['movie'].split('|')[1], axis=1)
        item_df['Action'] = item_df.apply(lambda x: x['movie'].split('|')[6], axis=1)
        item_df['Adventure'] = item_df.apply(lambda x: x['movie'].split('|')[7], axis=1)
        item_df['Animation'] = item_df.apply(lambda x: x['movie'].split('|')[8], axis=1)
        item_df['Children'] = item_df.apply(lambda x: x['movie'].split('|')[9], axis=1)
        item_df['Comedy'] = item_df.apply(lambda x: x['movie'].split('|')[10], axis=1)
        item_df['Crime'] = item_df.apply(lambda x: x['movie'].split('|')[11], axis=1)
        item_df['Documentary'] = item_df.apply(lambda x: x['movie'].split('|')[12], axis=1)
        item_df['Drama'] = item_df.apply(lambda x: x['movie'].split('|')[13], axis=1)
        item_df['Fantasy'] = item_df.apply(lambda x: x['movie'].split('|')[14], axis=1)
        item_df['Film-Noir'] = item_df.apply(lambda x: x['movie'].split('|')[15], axis=1)
        item_df['Horror'] = item_df.apply(lambda x: x['movie'].split('|')[16], axis=1)
        item_df['Musical'] = item_df.apply(lambda x: x['movie'].split('|')[17], axis=1)
        item_df['Mystery'] = item_df.apply(lambda x: x['movie'].split('|')[18], axis=1)
        item_df['Romance'] = item_df.apply(lambda x: x['movie'].split('|')[19], axis=1)
        item_df['Sci-Fi'] = item_df.apply(lambda x: x['movie'].split('|')[20], axis=1)
        item_df['Thriller'] = item_df.apply(lambda x: x['movie'].split('|')[21], axis=1)
        item_df['War'] = item_df.apply(lambda x: x['movie'].split('|')[22], axis=1)
        item_df['Western'] = item_df.apply(lambda x: x['movie'].split('|')[23], axis=1)
        
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
    
    @staticmethod       
    def prep_item_df_large(item_df):
        item_df['movie'] = item_df.apply(lambda x: Utility.covnert_string_format(x['movie_tmp']) ,axis=1)
        item_df = item_df.drop('movie_tmp',axis=1)
        return item_df
        
    @staticmethod       
    def covnert_string_format(string):
        fields = string.split('::')
        movieid = fields[0]
        moviename = fields[1]        
        genres_fields = fields[2]         
        outstr_dic = { 'movieid':0, 'moviename':0, 'releasedate':0,'releasedate2':0, 'URL':'empty', 'unknown':0 \
                 ,'Action':0,'Adventure':0,'Animation':0,'Children':0,'Comedy':0,'Crime':0,'Documentary':0,'Drama':0,'Fantasy':0 \
                 ,'Film-Noir':0,'Horror':0,'Musical':0,'Mystery':0,'Romance':0,'Sci-Fi':0,'Thriller':0,'War':0,'Western':0}
        outstr_dic['moviename'] = moviename
        outstr_dic['movieid'] = movieid
        genres = genres_fields.split('|')
        for genre in genres:
            if outstr_dic.has_key(genre):
                outstr_dic[genre] = 1
        outstr = ''
        outstr = outstr + str(outstr_dic['movieid']) + '|'
        outstr = outstr + str(outstr_dic['moviename']) + '|'
        outstr = outstr + str(outstr_dic['releasedate']) + '|'
        outstr = outstr + str(outstr_dic['releasedate2']) + '|'
        outstr = outstr + str(outstr_dic['URL']) + '|'
        outstr = outstr + str(outstr_dic['unknown']) + '|'
        outstr = outstr + str(outstr_dic['Action']) + '|'
        outstr = outstr + str(outstr_dic['Adventure']) + '|'
        outstr = outstr + str(outstr_dic['Animation']) + '|'
        outstr = outstr + str(outstr_dic['Children']) + '|'
        outstr = outstr + str(outstr_dic['Comedy']) + '|'
        outstr = outstr + str(outstr_dic['Crime']) + '|'
        outstr = outstr + str(outstr_dic['Documentary']) + '|'
        outstr = outstr + str(outstr_dic['Drama']) + '|'
        outstr = outstr + str(outstr_dic['Fantasy']) + '|'
        outstr = outstr + str(outstr_dic['Film-Noir']) + '|'
        outstr = outstr + str(outstr_dic['Horror']) + '|'
        outstr = outstr + str(outstr_dic['Musical']) + '|'
        outstr = outstr + str(outstr_dic['Mystery']) + '|'
        outstr = outstr + str(outstr_dic['Romance']) + '|'
        outstr = outstr + str(outstr_dic['Sci-Fi']) + '|'
        outstr = outstr + str(outstr_dic['Thriller']) + '|'
        outstr = outstr + str(outstr_dic['War']) + '|'
        outstr = outstr + str(outstr_dic['Western'])
        return outstr

             