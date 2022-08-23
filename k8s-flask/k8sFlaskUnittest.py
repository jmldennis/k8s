import unittest
import k8sflask

class TestFlask(unittest.TestCase):

    def setUp(self):
        k8sflask.app.testing = True
        self.app = k8sflask.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertIn(bytearray("local port", 'utf-8'), rv.data)

if __name__ == '__main__':
    unittest.main()