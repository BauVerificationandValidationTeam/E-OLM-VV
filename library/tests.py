from django.test import TestCase

class SmokeTests(TestCase):
    def test_admin_login_page_loads(self):
        resp = self.client.get("/admin/login/")
        self.assertEqual(resp.status_code, 200)


