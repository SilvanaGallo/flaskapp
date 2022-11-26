from abc import ABC, abstractmethod
import requests
import json

from flaskapp import Config

class Repository(ABC):

    @abstractmethod
    def list_items():
        return

    @abstractmethod
    def create_item():
        return
    
    @abstractmethod
    def get_item(id: int):
        return
    
    @abstractmethod
    def update_item(id: int):
        return

    @abstractmethod
    def delete_item(id: int):
        return

class RollbarRepository(Repository):
 
    items_url = 'https://api.rollbar.com/api/1/items/' # repository url class variable
    

    def list_items(self):
        api_key = Config.READ
            
        r = requests.get(
                        self.items_url,
                        headers = {'accept': 'application/json', 'X-Rollbar-Access-Token': api_key},
                        params = {'status': 'all'}
                    )
        print(f"Status code: {r.status_code}")
        return r.json()
    
    def create_item(self):
        api_key = Config.POST_SERVER_ITEM
            
        payload =  {"data": {"environment": "production","body": {"message": {"body": "Message 4"}}}}
        r = requests.post(
                        self.items_url,
                        headers = {'accept': 'application/json', 
                                    'content-type': 'application/json', 
                                    'X-Rollbar-Access-Token': api_key
                                },
                        json = payload
                    )
        print(f"Status code: {r.status_code}")
        return r.json()
    
    def get_item(self, id: int):
        api_key = Config.READ
        
        url_and_id = f"{self.items_url}{id}" 
       
        r = requests.get(
                        url_and_id,
                        headers = {'accept': 'application/json', 'content-type': 'application/json', 'X-Rollbar-Access-Token': api_key},
                    )
        print(f"Status code: {r.status_code}")
        return r.json()
    
    def update_item(self, id: int):
        api_key = Config.WRITE
        url_and_id = f"{self.items_url}/{id}" 
        # armar bien el data con status title resolved_in_version, level, assigned_user_id    
        # data_dict =  {'environment': 'production', 'body': { 'message': {'body': 'Hello, world!'}}}
        
        r = requests.patch(
                        url_and_id,
                        headers = {'accept': 'application/json', 'content-type': 'application/json', 'X-Rollbar-Access-Token': api_key},
                        #json = data_dict
                    )
        print(f"Status code: {r.status_code}")
        return r.json()

    def delete_item(self, id: int):
        result = {"data": {"err": 1, "message": "Items can't be deleted."}}
        return json.dumps(result, indent=2)