from django.test import SimpleTestCase
from django.urls import reverse, resolve

class TestMPAUserUrls(SimpleTestCase):

    def test_mpa_user_detail_url_resolves(self):
        url = reverse('mpa-user-detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).view_name, 'mpa-user-detail')

class TestMPAUserProfileUrls(SimpleTestCase):

    def test_mpa_user_profile_list_url_resolves(self):
        url = reverse('mpa-user-profile-list')
        self.assertEqual(resolve(url).view_name, 'mpa-user-profile-list')
    
    def test_mpa_user_profile_detail_url_resolves(self):
        url = reverse('mpa-user-profile-detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).view_name, 'mpa-user-profile-detail')

class TestMPAUserProfileImageUrls(SimpleTestCase):

    def test_mpa_user_profile_image_list_url_resolves(self):
        url = reverse('mpa-user-profile-image-list')
        self.assertEqual(resolve(url).view_name, 'mpa-user-profile-image-list')

class TestMPAUserAdressUrls(SimpleTestCase):

    def test_mpa_user_address_list_url_resolves(self):
        url = reverse('mpa-user-address-list')
        self.assertEqual(resolve(url).view_name, 'mpa-user-address-list')
    
    def test_mpa_user_address_detail_url_resolves(self):
        url = reverse('mpa-user-address-detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).view_name, 'mpa-user-address-detail')