import requests

def test_scrape_page():
    response = requests.get("http://localhost:8000/scrape/155341306589")
    assert response.status_code == 200
    assert response.json() == {"message":"Scraping successful","page_id":"155341306589","page_name":"les trois teckto","page_about":"dance.tecktonik@hotmail.fr\ndance.hani@live.fr\ndance.oussama@hotmail.com"}