"""
Created on Wed Oct 14 13:06:42 2020

@author: Bagavathi Priya
"""


import pymongo

client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')

#Creating database
mydb=client['Firstdb']

#Creating table employeeinfo in mydb
information=mydb.employeeinfo

record={
        'name':'priya',
        'interest':'Data science'
        }

information.insert_one(record)

record=[{
        'name':'Ani',
        'interest':'Data science I '
        },
        {
        'name':'Baggu',
        'interest':'Data science II'
        }]

information.insert_many(record)
