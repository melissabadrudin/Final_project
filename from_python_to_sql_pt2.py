#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 14:14:27 2020

@author: melissabadrudin
"""


###### Import my csv file with the dataset

import pandas as pd

stand_virtual_dummies = pd.read_csv('df_dummie.csv',index_col=0 )
stand_virtual_


#import the module
from sqlalchemy import create_engine

# create sqlalchemy engine
engine =create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="descobri93",
                               db="stand_virtual"))

# pass the data in one line code to sql:
stand_virtual_dummies.to_sql('dataset_dummie', con = engine, if_exists = "append")


print("Done")

#it worked! 