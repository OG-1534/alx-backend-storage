#!/usr/bin/env python3
""" MongoDB operations in Python using pymongo"""

def update_topics(mongo_collection, name, topics):
    """ Changes all topics of a school document basedd on the name"""
    query = {"name": name}
    new_value = {"$set": {"topics": topics}}
    
    mongo_collection.update_many(query, new_value)
