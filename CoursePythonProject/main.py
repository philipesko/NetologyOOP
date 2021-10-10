import requests
import os
import time
import vk
from pprint import pprint
from tqdm import tqdm


from credentials import TOKEN_VK



class Vkapi:
    def __init__(self, profile_name='https://vk.com/begemot_korovin'):
        self.profile = profile_name
        self.token = TOKEN_VK
        
    def result(self):
        user_info = requests.get(
            f'https://api.vk.com/method/users.get?slug=begemot_korovin&fields=bdate&access_token={self.token}&v=5.131').json()
        return user_info['response'][0]['id']

    def get_photos(self, user_id):
        photos = requests.get(
            f'https://api.vk.com/method/photos.get?owner_id={user_id}&album_id=profile&extended=1&access_token={self.token}&count=10&v=5.131').json()
        
        for items in photos['response']['items']:
            pprint(items)
        return photos

    def get_photos(self, user_id, count=5):
        playload = {
            'owner_id': user_id, 
            'album_id': 'profile',
            'extended': 1,
            'access_token': self.token,
            'count': count,
            'v': 5.131,
            'photo_sizes': 1
            }
        get_photos = requests.get('https://api.vk.com/method/photos.get', params=playload).json()
        return get_photos

if __name__ == "__main__":
    vkapi = Vkapi('Test')
    pbar = tqdm(total=3, desc="VKAPI")
    pbar.update(1)
    time.sleep(1)
    result = vkapi.result()
    print(result)
    pbar.update(1)
    time.sleep(1)
    pprint(vkapi.get_photos(result, 1))
    pbar.update(1)
        
    
    
