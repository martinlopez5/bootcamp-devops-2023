# tests/test_app.py
import unittest
from app import app, db, Transaction

class TestApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_calculate_route(self):
        response = self.app.post('/calculate', data=dict(total_amount=100, num_people=5))
        self.assertEqual(response.status_code, 200)
        # Aquí puedes agregar más aserciones para verificar el comportamiento esperado

if __name__ == '__main__':
    unittest.main()
