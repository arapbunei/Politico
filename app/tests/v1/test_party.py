import unittest
from flask import json
from app import create_app
from ..models.party_model import Party


class TestParty(unittest.TestCase):
    

    def setUp(self):

        """ Initialize app instance and testclient """
        self.app = create_app('testing')
        self.client = self.app.test_client()
       
    
    def tearDown(self):
        """runs after every testcase"""

        self.app = None
        Party.clear()
       

    """Test cases """

    def test_create_party_no_data(self):

        """ Testing while there is no data sent when creating meetup """
        response = self.client.post('/api/v1/party')
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['error'], 'No data provided')


    def test_create_party_empty_data(self):

        """ Test while there is no data sent """
        party = {}

        response = self.client.post('/api/v1/party', json=json.dumps(party), content_type="application/json")
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['error'], 'Invalid data. Please fill all required fields')


    def test_create_party_missing_fields(self):

     
        party = {

            'name' : 'Republican',
            'hqaddress' : 'sameer park',
            
        }

        response = self.client.post('/api/v1/party', json=party, content_type="application/json")
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['error'], 'Invalid data. Please fill all required fields')

    def test_create_party(self):

        """ Test create party """

        party = {

            'name' : 'Republican',
            'hqaddress' : 'sameer',
            'logourl' : 'desktop'
           
        }

        res = self.client.post('/api/v1/party', json=party, content_type="application/json")
        data = res.get_json()
        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['status'], 201)
        self.assertEqual(data['message'], 'party created successfully')


    def test_fetch_specific_party(self):
       
        party = {

            'name' : 'Republican',
            'hqaddress' : 'sameer',
            'logourl' : 'desktop'
            
            
        }

        party2 = {
            'name' : 'Democrats',
            'hqaddress' : 'washington',
            'logourl' : 'home',
            
        }
        self.client.post('/api/v1/party', json=party, content_type="application/json")
        self.client.post('/api/v1/party', json=party2, content_type="application/json")

        res = self.client.get('/api/v1/party/1')
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status'], 200)
        self.assertEqual(data['data'][0]['id'], 1)

    def test_fetch_non_existent_party(self):

        """ Test for  a existent meetup """
        response = self.client.get('/api/v1/party/10')
        data = response.get_json()

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(data['error'], 'party not found')

    def test_fetch_all_parties(self):
        

        party = {

            'name' : 'Republican',
            'hqaddress' : 'sameer',
            'logourl' : 'desktop'
            
            
        }

        party2 = {
            'name' : 'Democrats',
            'hqaddress' : 'washington',
            'logourl' : 'home',
            
        }
        
        self.client.post('/api/v1/party', json=party, content_type="application/json")
        self.client.post('/api/v1/party', json=party2, content_type="application/json")

        res = self.client.get('/api/v1/parties')
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status'], 200)