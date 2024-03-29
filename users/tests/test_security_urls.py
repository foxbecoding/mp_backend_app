from django.test import SimpleTestCase
from django.urls import reverse, resolve

class TestSecurityUrls(SimpleTestCase):
    
    def test_security_list_url_resolves(self):
        url = reverse('x-fct-list')
        self.assertEqual(resolve(url).view_name, 'x-fct-list')

    # def test_user_sign_up_detail_url_resolves(self):
    #     url = reverse('user-sign-up-detail', kwargs={'pk': 1})
    #     self.assertEqual(resolve(url).view_name, 'user-sign-up-detail')
