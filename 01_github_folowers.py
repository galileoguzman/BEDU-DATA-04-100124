import requests

BASE_URL = 'https://api.github.com/'

def get_github_user(username):
    url = f'{BASE_URL}users/{username}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    return None


print(get_github_user('Darriecha'))