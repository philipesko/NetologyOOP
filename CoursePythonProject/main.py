import requests
import os
import time
from tqdm import tqdm


from credentials import TOKEN_VK



class Vkapi:
    def __init__(self, profile_id):
        self.profile = profile_id
        self.token = TOKEN_VK
        
    def result(self):
        return self.token



if __name__ == "__main__":
    vkapi = Vkapi('Test')
    pbar = tqdm(total=3, desc="VKAPI")
    pbar.update(1)
    time.sleep(1)
    vkapi.result()
    pbar.update(1)
    time.sleep(1)
    #print(vkapi.result())
    time.sleep(1)
    pbar.update(1)
        
    
    
