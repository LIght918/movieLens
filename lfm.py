# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 19:15:08 2015

@author: LIght
"""

import numpy


class LFM:

    @staticmethod
    def matrix_factorization(R, P, Q, K, steps=1000, alpha=0.0002, beta=0.02):
        Q = Q.T
        for step in xrange(steps):
            print step            
            for i in xrange(len(R)):
                for j in xrange(len(R[i])):
                    if R[i][j] > 0:
                        eij = R[i][j] - numpy.dot(P[i,:],Q[:,j])
                        for k in xrange(K):
                            P[i][k] = P[i][k] + alpha * (2 * eij * Q[k][j] - beta * P[i][k])
                            Q[k][j] = Q[k][j] + alpha * (2 * eij * P[i][k] - beta * Q[k][j])
            #eR = numpy.dot(P,Q)
            e = 0
            for i in xrange(len(R)):
                for j in xrange(len(R[i])):
                    if R[i][j] > 0:
                        e = e + pow(R[i][j] - numpy.dot(P[i,:],Q[:,j]), 2)
                        for k in xrange(K):
                            e = e + (beta/2) * (pow(P[i][k],2) + pow(Q[k][j],2))
            if e < 0.001:
                break
        return P, Q.T
    
'''
example code, too slow for movielens matrix, optimize
R = np.array(user_item_matrix)
N = len(R)
M = len(R[0])
K = 5
 
P = np.random.rand(N,K)
Q = np.random.rand(M,K)
 
nP, nQ = lfm.LFM.matrix_factorization(R, P, Q, K)
nR = np.dot(nP, nQ.T)
'''