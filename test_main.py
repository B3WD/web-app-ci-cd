from fastapi.testclient import TestClient
from main import app
from bs4 import BeautifulSoup

client = TestClient(app)


def test_read_main():
  response = client.get("/")
  assert response.status_code == 200

  # Parse the HTML content with BeautifulSoup
  soup = BeautifulSoup(response.content, 'html.parser')

  # Find the button element
  button = soup.find('button')

  # Assert the button text
  assert button.text == "Hello world!"
