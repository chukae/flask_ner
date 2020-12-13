import unittest
import json
from flask import request

from app import app

class TestApi(unittest.TestCase):
    def test_ner_endpoint_given_json_body_returns_200(self):
        with app.test_client() as client:
            response = client.post('/ner', json={"sentence": "Stanford Research Institute is a top institution."})
            assert response._status_code == 200

    def test_ner_endpoint_given_json_body_with_known_entities_returns_entity_result_in_response(self):
        with app.test_client() as client:
            response = client.post('/ner', json={"sentence": "Jeffrey Epstein"})
            data = json.loads(response.get_data())
            print(data)
            assert len(data['entities']) > 0
            assert data['entities'][0]['ent'] == 'Jeffrey Epstein'
            assert data['entities'][0]['label'] == 'Person'