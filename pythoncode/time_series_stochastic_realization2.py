# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 08:41:01 2023

@author: MarcosFerreira
"""
import pandas as pd
from pandas import to_datetime
# define the period for which we want a prediction
future = list()
for i in range(1, 13):
 date = '1968-%02d' % i
 future.append([date])
future = pd.DataFrame(future)
future.columns = ['ds']
future['ds']= to_datetime(future['ds'])
print(future)

train = future.drop(future.index[-6:])

print(train)
