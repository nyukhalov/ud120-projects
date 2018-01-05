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
import numpy as np

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print enron_data["SKILLING JEFFREY K"]

def poi_cnt():
    cnt = 0
    for person, features in enron_data.iteritems():
        if (features["poi"] == 1):
            cnt += 1
    return cnt

def james_prentice_stocks():
    return enron_data["PRENTICE JAMES"]["total_stock_value"]

def wesley_colwell_emails_to_poi():
    return enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

def jeffrey_k_skilling_stocks():
    return enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

def print_most_taken_money():
    skilling_tp = enron_data["SKILLING JEFFREY K"]["total_payments"]
    fastow_tp = enron_data["FASTOW ANDREW S"]["total_payments"]
    lay_tp = enron_data["LAY KENNETH L"]["total_payments"]
    print "Skilling:", skilling_tp
    print "Fastow:", fastow_tp
    print "Lay:", lay_tp
    return max(skilling_tp, 0, lay_tp)

def quantified_salaries_and_emails():
    salaries = 0
    emails = 0
    for person, features in enron_data.iteritems():
        if features["salary"] != 'NaN':
            salaries += 1
        if features["email_address"] != 'NaN':
            emails += 1
    return (salaries, emails)

print poi_cnt()      
print james_prentice_stocks()
print wesley_colwell_emails_to_poi()
print jeffrey_k_skilling_stocks()
print print_most_taken_money()
print quantified_salaries_and_emails()