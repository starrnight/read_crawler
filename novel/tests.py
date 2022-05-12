import json

from django.test import TestCase

# Create your tests here.
from crawler.crawler import Crawler


class CrawlerTest(TestCase):

    def json_post(self, path, data=None):
        """Request a response from the server using POST."""
        resp = self.client.post(path, data, content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        resp.context = json.loads(resp.content)
        return resp

    def test_crawler(self):
        obj = Crawler()
        # obj.start()
