import requests

ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
USER_ID = 'YOUR_USER_ID'

def get_following(user_id, access_token):
    url = f'https://graph.instagram.com/{user_id}/following?access_token={access_token}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['data']
    else:
        return []

def get_followers(user_id, access_token):
    url = f'https://graph.instagram.com/{user_id}/followers?access_token={access_token}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['data']
    else:
        return []

def check_follow_back(following, followers):
    following_ids = {user['id'] for user in following}
    followers_ids = {user['id'] for user in followers}
    not_following_back = following_ids - followers_ids
    return not_following_back

following = get_following(USER_ID, ACCESS_TOKEN)
followers = get_followers(USER_ID, ACCESS_TOKEN)
not_following_back = check_follow_back(following, followers)

print("Accounts not following back:")
for user_id in not_following_back:
    print(user_id)
