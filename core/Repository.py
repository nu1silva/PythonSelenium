import uuid

import pymongo

dbClient = pymongo.MongoClient("mongodb://localhost:27017/")
db = dbClient["autom"]

data = {"elementId": str(uuid.uuid4()),
        "locators": [
            {"locatorId": str(uuid.uuid4()),
             "locator": "xpath",
             "rating": 0.99},
            {"locatorId": str(uuid.uuid4()),
             "locator": "xpath",
             "rating": 0.75}
        ]}

# def captureElementLocators():
db.element_locators.insert_one(data)
