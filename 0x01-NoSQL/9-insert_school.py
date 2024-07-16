#!/usr/bin/env python3
""" MongoDB operations with Python using pymongo"""

def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document using keywords"""
    return mongo_collection.insert(kwargs)
