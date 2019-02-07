import unittest
from flask import json
from app import create_app
from app.api.v1.models.user_model import users


class TestUsers(unittest.TestCase):
    

    def setUp(self):

        """ Initialize app instance and testclient """
        self.app = create_app('testing')
        self.client = self.app.test_client()
       
    
    def tearDown(self):
        """runs after every testcase"""

        self.app = None
        users.clear()


    def test_signup_without_data(self):
        """ Test sign up with no data sent """
        response = self.client.post('/api/v1/signup')
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'No Sign up data provided')
    
    def test_signup_wth_empty_data(self):
        """ Test sign up with empty data sent """
        user = {}

        response = self.client.post('/api/v1/signup', json=json.dumps(user), headers={'Content-Type': 'application/json'})
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'Invalid data. Please fill all the required fields')

    def test_signup_when_there_are_missing_fields(self):
        """ Test signup with missing fields in data sent """
        user = {
            'firstname' : 'hassan',
            'lastname' : 'joho',
            'password' : 'mombasa@county#01'
        }

        response = self.client.post('/api/v1/signup', json=user, headers={'Content-Type': 'application/json'})
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'Invalid data. Please fill all the required fields')
    
    def test_signup_invalid_password_provided(self):
        """ Test signup with invalid password """

        user = {
            'firstname' : 'hassan',
            'lastname' : 'joho',
            'username' : 'sheikh',
            'email' : 'hjoho@gmail.com',
            'password' : 'mombasa@county',
            'phone_number' : '0704895360'
        }

        response = self.client.post('/api/v1/signup', json=user, headers={'Content-Type': 'application/json'})
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'Invalid data. Please fill all the required fields')

    def test_signup_invalid_email(self):
        """ Test sign up with invalid email """
        
        user = {
            'firstname' : 'hassan',
            'lastname' : 'joho',
            'username' : 'sheikh',
            'email' : 'hjoho',
            'password' : 'mombasa@county#01',
            'phone_number' : '0704895360'
        }

       
        response = self.client.post('/api/v1/signup', json=user, headers={'Content-Type': 'application/json'})
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'Invalid data. Please fill all the required fields')
    
    def test_signup(self):
        """ Test sign up with correct data """
        
        user = {
            'firstname' : 'hassan',
            'lastname' : 'joho',
            'username' : 'sheikh',
            'email' : 'hjoho@gmail.com',
            'password' : 'Calebmbugua1#',
            'phone_number' : '0704699193'
        }
        

        response = self.client.post('/api/v1/signup', json=user, headers={'Content-Type': 'application/json'})
        data = response.get_json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['status'], 201)
        self.assertEqual(data['message'], 'User created successfully')
        self.assertEqual(data['data']['username'], user['username'])


    def test_user_login_when_no_data_provided(self):

        """ Test login with no data has been provided """

        response= self.client.post('/api/v1/signin')
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['message'], 'No data has provided! Please put your login credentials')

   
    def test_login_for_unregistered_user(self):
        """ Test login with an un unregistered user credentials """
        user = {
            'username' : 'samboja',
            'password' : '#grunts'
        }

        response = self.client.post('/api/v1/login', json=user, headers={'Content-Type': 'application/json'})
        data = response.get_json()

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], 404)
        #self.assertEqual(data['message'], 'User not found')

    def test_login_success(self):
        """ Test successfull login """
        # Register user

        
        user = {
            "firstname":"hassan",
	        "lastname":"joho",
	        "username":"sheikh",
	        "email":"hjoho@gmail.com",
	        "password":"mombasa@county#01",
	        "phone_number":"0704895360"
	
        }


        res_1 = self.client.post('/api/v1/signup', json=user, headers={'Content-Type': 'application/json'})
        data_1 = res_1.get_json()

        self.assertEqual(res_1.status_code, 200)
        self.assertEqual(data_1['status'], 201)

        # Login user
        res_2 = self.client.post('/api/v1/signin', json={'username': 'sheikh', 'password': 'mombasa@county#01'}, headers={'Content-Type': 'application/json'})
        data_2 = res_2.get_json()

        self.assertEqual(res_2.status_code, 200)
        self.assertEqual(data_2['status'], 200)
        self.assertEqual(data_2['message'], 'User logged in successfully')

        # Login user
        res_2 = self.client.post('/api/v1/signin', json={'username': 'sheikh', 'password': 'mombasa@county#01'}, headers={'Content-Type': 'application/json'})
        data_2 = res_2.get_json()

        self.assertEqual(res_2.status_code, 200)
        self.assertEqual(data_2['status'], 200)
        self.assertEqual(data_2['message'], 'logg in successfully')

    def test_login_when_no_username_provided(self):
        """ Test login with no username provided """
        # Register user


        
        user = {
            "firstname":"hassan",
	        "lastname":"joho",
	        "username":"sheikh",
	        "email":"hjoho@gmail.com",
	        "password":"mombasa@county#01",
	        "phone_number":"0704895360"
	
        }

        res_1 = self.client.post('/api/v1/signin', json=user, headers={'Content-Type': 'application/json'})
        data_1 = res_1.get_json()

        #self.assertEqual(res_1.status_code, 201)
        #self.assertEqual(data_1['status'], 201)

        # Login user
        res_2 = self.client.post('/api/v1/signin', json={'password': 'mombasa@county#01'}, headers={'Content-Type': 'application/json'})
        data_2 = res_2.get_json()

        self.assertEqual(res_2.status_code, 400)
        self.assertEqual(data_2['status'], 400)
        self.assertEqual(data_2['message'], 'Invalid data. Make sure you fill all required fields')

  