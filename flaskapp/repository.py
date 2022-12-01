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
        return r.json()
    
    
    # It needs a refactorization
    def _create_dictionary(self) -> dict:

        message: dict = {}
        params = request.get_json()
                
        message = {"body": params['message-body']} if "message-body" in params else {}
        message["route"] = params['route'] if "route" in params else ''
        
        payload =  {"data": {
                            "body": {
                                    "message": message
                                    }
                            }
                    }

        for i in ['level', 'title', 'user-id', 'status', 'environment']:
            if i in params:
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
        return r.json()
    

    def get_item(self, id: int):
        
        url_and_id = f"{self.item_url}/{id}" 
       
        r = requests.get(
                        url_and_id,
                        headers = {'accept': 'application/json', 
                                    'content-type': 'application/json', 
                                    'X-Rollbar-Access-Token': Config.READ},
                    )
        return r.json()
    

    def update_item(self, id: int):
        
        url_and_id = f"{self.item_url}/{id}" 
        data_dict =  request.get_json()
        
        r = requests.patch(
                        url_and_id,
                        headers = {'accept': 'application/json', 
                                    'content-type': 'application/json', 
                                    'X-Rollbar-Access-Token': Config.WRITE},
                        json = data_dict
                    )
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
        return r.json()
        