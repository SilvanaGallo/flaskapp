import pytest
import json
import requests
#import requests_mock


class TestItemsRoutes:

    API_RESPONSE = '''
    {
  "err": 0,
  "result": [
    {
      "counts": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        3,
        0,
        0
      ],
      "item": {
        "counter": 11,
        "environment": "development",
        "framework": 0,
        "group_status": 1,
        "id": 1350424236,
        "last_occurrence_timestamp": 1669884940,
        "level": 40,
        "occurrences": 3,
        "project_id": 604161,
        "title": "Message from CLI 12",
        "unique_occurrences": null
      }
    },
    {
      "counts": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        3,
        0,
        0
      ],
      "item": {
        "counter": 12,
        "environment": "unknown",
        "framework": 0,
        "group_status": 1,
        "id": 1350427779,
        "last_occurrence_timestamp": 1669884889,
        "level": 40,
        "occurrences": 3,
        "project_id": 604161,
        "title": "Message from CLI 13",
        "unique_occurrences": null
      }
    },
    {
      "counts": [0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        2,
        0,
        0
      ],
      "item": {
        "counter": 10,
        "environment": "production",
        "framework": 0,
        "group_status": 1,
        "id": 1350423454,
        "last_occurrence_timestamp": 1669883677,
        "level": 40,
        "occurrences": 2,
        "project_id": 604161,
        "title": "Updated title",
        "unique_occurrences": null
      }
    },
    {
      "counts": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        0
      ],
      "item": {
        "counter": 13,
        "environment": "unknown",
        "framework": 0,
        "group_status": 1,
        "id": 1350428891,
        "last_occurrence_timestamp": 1669884686,
        "level": 40,
        "occurrences": 1,
        "project_id": 604161,
        "title": "Hello, world!",
        "unique_occurrences": null
      }
    }
  ]
}

    '''
    
    # @request_mock.Mocker() # I need to learn more about it 
    # I found it in the LMS but I didn't have time to do it
    # def test_get_items_endpoint(m)-> None:
    #     m.get('http://httpbin.org/test', text=self.API_RESPONSE)
    #     resp = request.get('http://httpbin.org/test')

    #     assert resp.text == API_RESPONSE

    def test_get_items_endpoint_without_params(client)-> None:
        response = client.get("/items")
        res = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 200
        assert res["err"] == 0
        assert type(res["result"]["items"]) is list


    def test_get_items_endpoint_with_params(client)-> None:
        response = client.get("/items", params={"environment": "production"})
        res = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 200
        assert res["err"] == 0
        assert type(res["result"]["items"]) is list
        for item in res["result"]["items"]:
            assert item["environment"] == "production"


    def test_post_items_endpoint_without_params(client)-> None:
        response = client.post("/items")
        res = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 200
        assert res["err"] == 1
        assert res["message"] == "Invalid format. data.body.message.body is a required property."


    def test_post_items_endpoint_with_params(client)-> None:
        payload = { 'route': "route", 
                    'environment': "development", 
                    'message-body': "A body message"
                }
        response = client.post("/items",json=payload)
        res = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 200
        assert res["err"] == 0
        assert "uuid" in res["result"]


    def test_delete_items_endpoint(client)-> None:
        response = client.delete("/items")
        res = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 200
        assert res["err"] == 1
        assert res["message"] == "Items can't be deleted."


    def test_get_item_endpoint_without_id(client)-> None:
        response = client.get("/items/")
        res = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 404


    def test_get_item_endpoint_with_id(client)-> None: # see how to pass id
        id: int = 1234 
        response = client.get(f"/items/{id}")
        res = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 200
        assert res["err"] == 0
        assert res["result"]["id"] == id


    def test_get_item_endpoint_with_existent_id(client)-> None: # see how to pass id
        id: int = 1234 
        response = client.get(f"/items/{id}")
        res = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 200
        assert res["err"] == 0
        assert res["result"]["id"] == id


    def test_get_item_endpoint_with_inexistent_id(client)-> None: 
        id: int = 1234 
        response = client.get(f"/items/{id}")
        res = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 200
        assert res["err"] == 1
        assert res["message"] == "Item not found in this project."


    def test_update_item_endpoint_inexistent_id(client)-> None: 
        id: int = 1234 
        response = client.get(f"/items/{id}")
        res = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 200
        assert res["err"] == 1
        assert res["message"] == "Item not found in this project."

