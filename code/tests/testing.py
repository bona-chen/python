import unittest
from tests import saving
from tests.saving import get_new_username


class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_new_username("janis", "joplin")
        self.assertEqual(formatted_name, "Janis Joplin")


unittest.main()
