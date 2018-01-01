#!/usr/bin/env python
from pymongo import MongoClient
import pprint
import json

class MongoStorage:

    def __init__(self, db_host, db_port, db_name, db_user, db_pass) :
	# Connect to mongo server
        self.client = MongoClient('mongodb://'+db_user+':'+db_pass+'@'+db_host+':'+db_port)
	# Select database
        self.db=self.client[db_name]

    def insert(self, json_data) :
        cashReceipts = self.db.cashReceipts
        cashReceipts.insert_one(json_data).inserted_id
    
    def select(self) :
        cashReceipts = self.db.cashReceipts
        for cashReceipt in cashReceipts.find() :
    	    pprint.pprint(cashReceipt)

    def selectByAgentID(self, agentID) :
        cashReceipts = self.db.cashReceipts
        cashReceipts_filtred = cashReceipts.find({"agentID": agentID})
        for cashReceipt in cashReceipts_filtred :
            pprint.pprint(cashReceipt)

    def selectByCashReceiptID(self, cashReceiptID) :
        cashReceipts = self.db.cashReceipts
        cashReceipts_filtred = cashReceipts.find({"cashReceiptID": cashReceiptID})
        for cashReceipt in cashReceipts_filtred :
            pprint.pprint(cashReceipt)
