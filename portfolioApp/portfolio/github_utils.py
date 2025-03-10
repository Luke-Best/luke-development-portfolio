import requests

def fetch_repos(username, token=None):
    url = f"https://api.github.com/users/{username}/repos"
    headers = {'Authorization': f'token {token}'} if token else {}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch repos: {response.status_code}")
        return []