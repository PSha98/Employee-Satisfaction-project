#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import GridSearchCV
import pandas as pd
import numpy as np

def RFtune(depth = None, split = 2, leaf = 1, estimators = 100, df, y, seed = 20, testsz = .1, feature = 9):
    X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=testsz, random_state=seed)
    paramF = dict(n_estimators = estimators, max_depth = depth,  
              min_samples_split = split, 
             min_samples_leaf = leaf)
    forest = RandomForestClassifier(max_features=feature, random_state=seed)
    gridF = GridSearchCV(forest, paramF, cv = 3, verbose = 1, 
                      n_jobs = -1)
    return gridF.fit(X_train, y_train), X_test, y_test

    

