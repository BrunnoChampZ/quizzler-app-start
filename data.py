import requests

url = "https://opentdb.com/api.php?amount=10&type=boolean"
amount = 10
type = "boolean"

params = {
    "amount": amount,
    "type": type
}

response = requests.get(url=url, params=params)
data = response.json()

question_data = data["results"]