# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 21:31:46 2023

@author: bedir
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

data=pd.read_csv("C:/Users/bedir/Downloads/veriler.csv")
data_eksik=pd.read_csv("C:/Users/bedir/Downloads/eksikveriler.csv")
boykilo=data[["boy","kilo"]]
print(data_eksik)

imputer =SimpleImputer(missing_values=np.nan,strategy="mean")
yas=data_eksik.iloc[:,1:4].values
print(yas)
imputer=imputer.fit(yas[:,1:4])
yas[:,1:4]=imputer.transform(yas[:,1:4])
print(yas)