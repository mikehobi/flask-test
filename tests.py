from app import app
import unittest

class FlaskTestCase(unittest.TestCase):
	# flask loads correctly
	def test_index(self):
		tester = app.test_client()
		response = tester.get('/login', content_type='html/text')
		self.assertEqual(response.status_code, 200)
	# login page loads correctly
	def test_login_page_loads(self):
		tester = app.test_client()
		response = tester.get('/login', content_type='html/text')
		self.assertTrue(b'Login dude' in response.data)

	# login credentials testing
	def test_correct_login(self):
		tester = app.test_client()
		response = tester.post('/login', data=dict(user="admin", password="admin"), follow_redirects = True)
		self.assertIn(b'You just logged in', response.data)

	def test_incorrect_login(self):
		tester = app.test_client()
		response = tester.post('/login', data=dict(user="wrong", password="admin"), follow_redirects = True)
		self.assertIn(b'Oops. That username or password is incorrect.', response.data)

	# logout behaviour works
	def test_correct_logout(self):
		tester = app.test_client()
		tester.post('/login', data=dict(user="admin", password="admin"), follow_redirects = True)
		response =  tester.get('/logout', follow_redirects = True)
		self.assertIn(b'You just logged out', response.data)

	# ensure main page requires login
	def test_require_login_index(self):
		tester = app.test_client()
		response =  tester.get('/', follow_redirects = True)
		self.assertIn(b'You need to login first.', response.data)

	# ensure logout page requires login
	def test_require_login_logout(self):
		tester = app.test_client()
		response =  tester.get('/logout', follow_redirects = True)
		self.assertIn(b'You need to login first.', response.data)

	# index shows posts
	def test_posts_on_index(self):
		tester = app.test_client()
		response = tester.post('/login', data=dict(user="admin", password="admin"), follow_redirects = True)
		self.assertIn(b'niceeeeeee', response.data)


if __name__ == '__main__':
	unittest.main()