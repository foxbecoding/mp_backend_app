from django.test import SimpleTestCase
from django.urls import reverse, resolve

class TestMPACategoryUrls(SimpleTestCase):

    def test_mpa_category_list_url_resolves(self):
        url = reverse('mpa-category-list')
        self.assertEqual(resolve(url).view_name, 'mpa-category-list')
    
    def test_mpa_category_detail_url_resolves(self):
        url = reverse('mpa-category-detail', kwargs={'uid': 'cat-IH4io44f'})
        self.assertEqual(resolve(url).view_name, 'mpa-category-detail')