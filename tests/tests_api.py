"""
Tests the api
"""

import unittest
import spacetrackapi


class TestAPI(unittest.TestCase):
    def setUp(self):
        """Retrieve an account credentials"""

        print('Please input your Space-Track credentials')
        self._identity = input('identity : ')
        self._password = input('password : ')

    def test_api(self):
        """Test a simple call to the API"""

        client = spacetrackapi.Client(
            self._identity,
            self._password
        )

        # Test authentication
        try:
            client.authenticate()
        except Exception as e:
            self.fail("Exception raised during authentication : " + str(e))

        # Test a call
        data = client.call('basicspacedata', 'query', 'satcat', {
                'LAUNCH': '>now-7',
                'CURRENT': 'Y',
                'orderby': 'LAUNCH DESC'
            }
        )
        self.assertIsInstance(data, list)
        self.assertIsInstance(data[0], dict)

        # Test logout
        try:
            client.logout()
        except Exception as e:
            self.fail("Exception raised during logout : " + str(e))


if __name__ == '__main__':
    unittest.main()
