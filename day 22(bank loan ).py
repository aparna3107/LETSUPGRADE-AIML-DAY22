# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 15:41:40 2020

@author: Aparna s nair
"""
##BANKLOAN

import pandas as pd
import numpy as np
from sklearn import tree
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
dataset=pd.read_excel("Bank_Personal_Loan_Modelling.xlsx",sheet_name=1)
y=dataset.PersonalLoan
x=dataset[["Age","Experience","Income","Family","CCAvg","Education","Mortgage","Securities Account","CD Account","Online","CreditCard"]]
import statsmodels.api as sm
x1=sm.add_constant(x)
logistic=sm.Logit(y,x1)
result=logistic.fit()
print(result.summary())
print("INFERENCE : ")
print("1)All 11 factors have P value less than 0.5 so all are significant factors for loan approval.")
print("2)Factors such as INCOME, FAMILY,EDUCATION,CD ACCOUNT,ONLINE & CREDIT CARD have P value =0,so these factors are most significant.")
