from http.client import responses
from flask_testing import TestCase
from flask import current_app, url_for

from main import app

class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

        return app

    def test_app_exists(self):
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_index_redirects(self):
        response = self.client.get(url_for('index'))
        self.assertTrue(response.status_code == 302)

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)

    def test_home_post(self):
        response = self.client.post(
            url_for('home'),
            data={
                'username': 'Juan',
                'password': 'password'
            }
        )

        self.assertTrue(response.status_code == 405)

    def test_auth_blueprint_exist(self):
        self.assertIn('auth', self.app.blueprints)

    def test_auth_login__get(self):
        response = self.client.get(url_for('auth.login'))
        self.assert200(response)

    def test_auth_login_get(self):
        self.client.get(url_for('auth.login'))
        self.assertTemplateUsed('login.html')

    def test_auth_login_post(self):
        response = self.client.post(
            url_for('auth.login'),
            data={
                'username': 'Juan',
                'password': 'password'
            }
        )

        print(response)

        self.assertTrue(response.status_code == 302)
    