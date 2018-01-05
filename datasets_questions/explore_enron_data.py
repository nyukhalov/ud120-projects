#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

def poi_cnt():
    cnt = 0
    for person, features in enron_data.iteritems():
        if (features["poi"] == 1):
            cnt += 1
    return cnt

def james_prentice_stocks():
    return enron_data["PRENTICE JAMES"]["total_stock_value"]

print poi_cnt()      

print james_prentice_stocks()