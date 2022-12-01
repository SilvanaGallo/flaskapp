import pytest
import json


class TestMainRoutes:

    def test_get_which_endpoint(client)-> None:
        response = client.get("/which")
        assert response.status_code == 200
        assert b"API under construction" in response.data

    def test_post_which_endpoint(client)-> None:
        response = client.post("/which")
        assert response.status_code == 405

    def test_get_check_ok_endpoint(client)-> None:
        response = client.get("/check")
        res = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 200
        assert res["err"] == 0
        assert res["status"] == "OK"

    def test_get_check_ko_endpoint(client)-> None: # change to database failure
        # response = client.get("/check")
        # res = json.loads(response.data.decode('utf-8'))

        # assert response.status_code == 200
        # assert res["err"] == 0
        # assert res["status"] == "KO"
        pass

    def test_post_check_endpoint(client)-> None:
        response = client.post("/check")
        assert response.status_code == 405

    

