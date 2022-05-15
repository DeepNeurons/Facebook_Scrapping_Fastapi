from facebook_scraper import get_posts
from fastapi import FastAPI
import pymongo
## create mongodb to store scrapped data

app = FastAPI()
myclient = pymongo.MongoClient("mongodb://localhost:40759/") ## by default the port is 27017
mydb = myclient["fb_scrappingDB"]
my_collection = mydb["fb_scrappingCOLLECTION"]

def fb_scaper(word):
    """
        using the get_posts to extract posts and its dependencies from
        public facebook pages adn insert them one by one to the mongodb created above    
    """
    posts = get_posts(word, pages=1)
    for post in posts:
        my_collection.insert_one(post)
## app routing
@app.get("/")
def root():
    return fb_scaper("Google")  ## choose google as a parameter for scrap search


## rest to do throw data to mongoDB and dockerise app and mongodb an push it to github