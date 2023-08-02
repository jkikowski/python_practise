import unittest
from python_repos import r

#asercja czy status_code == 200

class Status_codeTestCase(unittest.TestCase):
	"""Test dla programu python_repos.py"""

	def test_status_code(self):
		"""Czy status_code jest równy 200"""
		self.assertEqual(r.status_code,200)

if __name__ == '__main__':
	unittest.main()
