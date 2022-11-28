from abc import ABC, abstractmethod
from flask import request
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

    # repository URLs class variables
    items_url = 'https://api.rollbar.com/api/1/items/' 
    item_url =  'https://api.rollbar.com/api/1/item' 
    reports_url = 'https://api.rollbar.com/api/1/reports/' 

    def list_items(self):
        params = request.args.to_dict()
        r = requests.get(
                        self.items_url,
                        headers = {'accept': 'application/json', 
                                    'X-Rollbar-Access-Token': Config.READ},
                        params = params
                    )
        print(f"Status code: {r.status_code}")
        return r.json()
    
    
    # It needs a refactorization
    def _create_dictionary(self) -> dict:

        params = request.get_json()
        print(params.items())
        message = {"body": params['message-body']}
        if params['route']:
            message["route"] = params['route']
        
        payload =  {"data": {
                            "environment": params['environment'],
                            "body": {
                                    "message": message
                                    }
                            }
                    }

        for i in ['level', 'title', 'user-id', 'status']:
            if params[i]:
                payload["data"][i] = params[i] 
        
        return payload


    def create_item(self):
        r = requests.post(
                        self.item_url,
                        headers = {'accept': 'application/json', 
                                    'content-type': 'application/json', 
                                    'X-Rollbar-Access-Token': Config.POST_SERVER_ITEM
                                },
                        json = self._create_dictionary()
                    )
        print(f"Status code: {r.status_code}")
        return r.json()
    

    def get_item(self, id: int):
        
        url_and_id = f"{self.item_url}/{id}" 
       
        r = requests.get(
                        url_and_id,
                        headers = {'accept': 'application/json', 
                                    'content-type': 'application/json', 
                                    'X-Rollbar-Access-Token': Config.READ},
                    )
        print(f"Status code: {r.status_code}")
        return r.json()
    

    def update_item(self, id: int):
        
        url_and_id = f"{self.item_url}/{id}" 
        data_dict =  request.get_json()
        
        print(data_dict)
        r = requests.patch(
                        url_and_id,
                        headers = {'accept': 'application/json', 
                                    'content-type': 'application/json', 
                                    'X-Rollbar-Access-Token': Config.WRITE},
                        json = data_dict
                    )
        print(f"Status code: {r.status_code}")
        return r.json()


    def delete_item(self, id: int):
        result = {"data": {"err": 1, "message": "Items can't be deleted."}}
        return json.dumps(result, indent=2)

    
    def top_active_items(self):
    
        full_url = f"{self.reports_url}top_active_items" 
        params = request.args.to_dict()
        r = requests.get(
                        full_url,
                        headers = {'accept': 'application/json', 
                                    'content-type': 'application/json', 
                                    'X-Rollbar-Access-Token': Config.READ},
                        params=params
                    )
        print(f"Status code: {r.status_code}")
        return r.json()
        