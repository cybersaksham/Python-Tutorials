import requests

r = requests.get("https://www.google.com")
print(r.text)  # Printing all text in request
print(r.status_code)  # Printing status code of request

# How to use post request
url = "https://www.google.com"
data = {
    "p1": 4,
    "p2": 5
}
r2 = requests.post(url=url, data=data)
