"""
UrlBuilder module tests
"""

import unittest
from collections import OrderedDict
from spacetrackapi import urlbuilder


build_parameters = {
    'controller': 'basicspacedata',
    'action': 'query',
    'request_class': 'satcat',
    'predicates': OrderedDict([
        ('LAUNCH', '>now-7'),
        ('CURRENT', 'Y'),
        ('orderby', 'LAUNCH DESC'),
        ('format', 'json')
    ])
}
"""
Default parameters for urlbuilder.build()
Should create the url below.
Uses an OrderedDict because otherwise the query's parameters
would be ordered randomly.
"""

correct_url = 'https://www.space-track.org/basicspacedata/query/class/satcat/LAUNCH/%3Enow-7/CURRENT/Y/orderby/LAUNCH%20DESC/format/json'
"""Url that should be created with the parameters above"""


class TestUrlBuilder(unittest.TestCase):
    def test_url(self):
        """Tests if the urlbuilder builds the correct url"""

        self.assertEqual(
            urlbuilder.build(**build_parameters),
            correct_url
        )

    def test_exceptions(self):
        """Tests if the builder throws the correct exceptions"""

        parameters = build_parameters.copy()
        parameters['controller'] = 'incorrect'
        with self.assertRaises(ValueError):
            urlbuilder.build(**parameters)

        parameters = build_parameters.copy()
        parameters['action'] = 'incorrect'
        with self.assertRaises(ValueError):
            urlbuilder.build(**parameters)

if __name__ == '__main__':
    unittest.main()
