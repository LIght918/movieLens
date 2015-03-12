# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 19:19:35 2015

@author: LIght
"""


##SVD 

smat_df = scipy.sparse.csc_matrix(user_item_matrix) # convert to sparse CSC format
ut, s, vt = sparsesvd(smat_df, 18) # do SVD, asking for 100 factors
movie_df = pd.DataFrame(vt).T
item_df = pd.read_csv(utility.CONST_PATH+'u.item', sep='\t', names=['movie'])
item_df = utility.Utility.prep_item_df(item_df)

test = pd.concat([movie_df,item_df],axis=1)
test = test.drop('moviename',axis=1)

test.corr()
