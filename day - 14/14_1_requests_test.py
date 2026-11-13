import requests
response = requests.get("https://api.github.com")
response1 = requests.get("https://api.github.com/users/SaiMoon67")
print(response.status_code)
print(response.json()["current_user_url"])
print(response.json())
print(response1.status_code)
print(response1.json())