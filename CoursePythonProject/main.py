from _typeshed import Self
import requests
import os
from NetologyOOP.CoursePythonProject.credentials import TOKEN_VK


class Vkapi:
    def __init__(self, profile_id):
        self.profile = profile_id
        self.token = TOKEN_VK
        