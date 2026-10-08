from django.test import TestCase


class PollsPageTest(TestCase):

    def test_polls_page(self):
        response = self.client.get('/polls/')
        self.assertEqual(response.status_code, 200)