from flask import Flask
from flask_testing import TestCase
from app import db
from app import create_app

class Task(TestCase):

    def create_app(self):
        app = create_app("testing")
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def create_task(self):
        response = self.client.post('/task', json= {
            "name": "買晚餐"
        })
        return response

    def test_get_empty(self):
        response = self.client.get('/tasks')
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.json["result"])
    
    def test_get(self):
        response = self.create_task()
        get_response = self.client.get('/tasks')

        self.assertEqual(200, get_response.status_code)
        self.assertEqual(len(get_response.json["result"]), 1)
        self.assertEqual(get_response.json['result'][0]['name'], "買晚餐")
        self.assertEqual(get_response.json['result'][0]['status'], 0)
        self.assertEqual(get_response.json['result'][0]['id'], 1)

    def test_post(self):
        response = self.create_task()
        self.assertEqual(201, response.status_code)
        self.assertEqual(response.json['result']['name'], "買晚餐")
        self.assertEqual(response.json['result']['status'], 0)


    def test_put(self):
        response = self.create_task()
        id = response.json['result']['id']
        put_response = self.client.put('/task/' + str(id), json= {
            "name": "買宵夜",
            "status": 1
        })
        self.assertEqual(200, put_response.status_code)
        self.assertEqual(put_response.json['name'], "買宵夜")
        self.assertEqual(put_response.json['status'], 1)


    def test_delete(self):
        response = self.create_task()
        id = response.json['result']['id']
        put_response = self.client.delete('/task/' + str(id))

        self.assertEqual(200, put_response.status_code)