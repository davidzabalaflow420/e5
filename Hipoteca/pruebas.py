import unittest
from flask import Flask
from flask_testing import TestCase
from src.controller.Controller import main
import psycopg2
from unittest.mock import patch, Mock

class TestController(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.register_blueprint(main)
        return app

    @patch('src.controller.Controller.psycopg2.connect')
    def test_index(self, mock_connect):
        mock_connect.return_value = Mock()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('index.html')

    @patch('src.controller.Controller.psycopg2.connect')
    def test_calcular_temporal(self, mock_connect):
        mock_connect.return_value = Mock()
        response = self.client.post('/calcular', data={
            'valor_vivienda': '300000',
            'edad': '65',
            'interes_anual': '4.5',
            'renta_mensual': '1000',
            'tipo': 'temporal',
            'años': '10'
        })
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('resultado.html')

    @patch('src.controller.Controller.psycopg2.connect')
    def test_calcular_vitalicia(self, mock_connect):
        mock_connect.return_value = Mock()
        response = self.client.post('/calcular', data={
            'valor_vivienda': '300000',
            'edad': '65',
            'interes_anual': '4.5',
            'renta_mensual': '1000',
            'tipo': 'vitalicia',
            'esperanza_vida': '20'
        })
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('resultado.html')

    @patch('src.controller.Controller.psycopg2.connect')
    def test_calcular_unica(self, mock_connect):
        mock_connect.return_value = Mock()
        response = self.client.post('/calcular', data={
            'valor_vivienda': '300000',
            'edad': '65',
            'interes_anual': '4.5',
            'renta_mensual': '1000',
            'tipo': 'unica'
        })
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('resultado.html')

    @patch('src.controller.Controller.psycopg2.connect')
    def test_shutdown(self, mock_connect):
        mock_connect.return_value = Mock()
        response = self.client.get('/shutdown')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Conexi\xc3\xb3n cerrada', response.data)

if __name__ == '__main__':
    unittest.main()
