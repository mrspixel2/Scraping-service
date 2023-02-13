from fastapi import FastAPI
import facebook
import pymongo

app = FastAPI()

graph = facebook.GraphAPI(access_token='EAAItZAgQ5EmsBAHaTD4Bj7OhnUZA9ZAkFPYBmKUrfEk3YspS79U2a80g2mOkvRvLlX1NzqVW5PjUgX6qU5WRqUEj6y3GvCkJ9KkNZArb43ezMzztKNwnan98BJgwbbF0wn0kpRUpNXdInhoeHZAelYFqyOXpJpdNHV9enW3IRTWYIwSgw2OCKuLJpfQ9MOb0zBK4LhzWc1cdmwoBpJ1L', version='3.1')

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["facebook_scraping"]
collection = db["pages"]

@app.get("/scrape/{page_id}")
def scrape_page(page_id: str):
    
    page = graph.get_object(page_id, fields="id, name, about")

    collection.insert_one(page)
    return {"message": "Scraping successful", "page_id": page_id, "page_name": page["name"], "page_about": page["about"]}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
