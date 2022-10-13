# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 15:33:35 2022

@author: ramazanolcay
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.types import *
from  sqlalchemy.sql.expression import func
import numpy as np
from faker import Faker
myfake = Faker()

engine = create_engine("postgresql://postgres:k7147bdz0.@localhost:5432/postgres")

session =sessionmaker(bind=engine)()

base = declarative_base()

class Fakerr(base):
    
    __tablename__ = 'Faker_table'
    
    id = Column(Integer, primary_key = True)
    mail = Column(String(50))
    password = Column(String(50))
 
class Findings(base):
    __tablename__ = 'Findings'
    
    id = Column(Integer, primary_key = True)
    mail = Column(String(50))
    password = Column(String(50))
    
base.metadata.create_all(engine)
#%%

myarray = np.zeros((10000,2),dtype="U50")
for i in range(10000):
    myarray[i,0] = myfake.email()
    myarray[i,1] = myfake.password()
    
print(len(np.unique(myarray[:,0]))) # It means that faker could
print(len(np.unique(myarray[:,1]))) #create same emails

#%%

for i in range(10000):
    diff_array = Fakerr(mail=myarray[i,0],password = myarray[i,1])
    session.add(diff_array)
    
session.commit()
    
#%%

myquery = session.query(Fakerr).order_by(func.random()).limit(1000)
myarray_mail_bin = list()
myarray_password_bin = list()
for query in myquery:
    myarray_mail_bin.append(query.mail)
    myarray_password_bin.append(query.password)
    
#%%
for i in range(1000,10000):
    myarray_mail_bin.append(myfake.email())
    myarray_password_bin.append(myfake.password())
#%%

query_array = np.array([myarray_mail_bin,myarray_password_bin]).transpose()

my_dict = dict()

for key in myarray_mail_bin:
    for value in myarray_password_bin:
        my_dict[key] = value
        myarray_password_bin.remove(value)
        break

import pandas as pd
query_pd = pd.DataFrame(data=query_array, columns = ["mail","password"])

#%%
last_query = session.query(Fakerr).all()
last_query_array = np.full((10000,1),False)


import time
start_time=time.time()

for query , i in zip(last_query,range(10000)):
    last_query_array[i] = ((query.mail in query_array[:,0]) and (query.password in query_array[:,1]))

end_time=time.time()
print("Query Time of Numpy Array = ",end_time-start_time)    
#Query Time of Numpy Array =  0.9043641090393066

#%%
last_query_dict = np.full((10000,1),False)
start_time=time.time()

for query , i in zip(last_query,range(10000)):
    last_query_dict[i] = ((my_dict.get(query.mail) == query.password))

end_time=time.time()
print("Query Time of Dictionary = ",end_time-start_time)  
#Query Time of Dictionary =  0.015306472778320312

#%%
last_query_pd = np.full((10000,1),False)

start_time=time.time()

for query , i in zip(last_query,range(10000)):
    last_query_pd[i] = ((query.mail in query_pd["mail"].unique()) and (query.password in query_pd["password"].unique()))

end_time=time.time()
print("Query Time of Pandas DataFrame = ",end_time-start_time)  

#Query Time of Pandas DataFrame =  13.100891828536987
# Dictionary gives best results.
    
#%%

k=-1

for i,j in my_dict.items():    
    k +=1
    if last_query_dict[k] == True:
        diff_array = Findings(mail=i,password = j)
        session.add(diff_array) #ad_all
    else:
        continue
    
session.commit()
