from django.test import TestCase, Client

class BlogTestCase(TestCase):
    def setUp(self):
        self.c = Client()

    def test_index_access(self):
        res = self.c.get('')
        self.assertEqual(200, res.status_code)
