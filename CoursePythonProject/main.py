import requests
import os
import time
import vk
import pprint
from tqdm import tqdm


from credentials import TOKEN_VK



class Vkapi:
    def __init__(self, profile_id='https://vk.com/begemot_korovin'):
        self.profile = profile_id
        self.token = TOKEN_VK
        
    def result(self):
        #user_info = vk.method('users.get', {'slug': 'begemot_korovin',
                  #'fields': 'nickname', 'name_case': 'nom'})

        user_info = requests.get(
            f'https://api.vk.com/method/users.get?slug=begemot_korovin&fields=bdate&access_token={self.token}&v=5.131').json()
        return user_info['response'][0]['id']



if __name__ == "__main__":
    vkapi = Vkapi('Test')
    pbar = tqdm(total=3, desc="VKAPI")
    pbar.update(1)
    time.sleep(1)
    print(vkapi.result())
    pbar.update(1)
    time.sleep(1)
    time.sleep(1)
    pbar.update(1)
        
    
    
