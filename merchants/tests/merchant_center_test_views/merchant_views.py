from django.test import TestCase, Client
from django.urls import reverse
from merchants.models import *
from users.models import UserGender
from datetime import datetime

class TestMCMerchantViewSet(TestCase):
    
    def setUp(self):
        self.client = Client(enforce_csrf_checks=True)
        date_time_str = '12/31/1990'
        self.date_time_obj = datetime.strptime(date_time_str, '%m/%d/%Y')
        self.client.get(reverse('x-fct-list'))
        self.csrftoken = self.client.cookies['csrftoken'].value
        self.user_gender = UserGender.objects.create(gender = 'male')
        self.user_gender.save()

        #User Sign up
        user_sign_up_data = {
            'first_name': "Desmond",
            'last_name': 'Fox',
            'email': 'fox@foxbecoding.com',
            'password': '123456',
            'confirm_password': '123456',
            'date_of_birth': self.date_time_obj.date(),
            'agreed_to_toa': True,
            'gender': self.user_gender.pk
        }

        self.client.post(
            reverse('account-sign-up-list'), 
            user_sign_up_data, 
            **{'HTTP_X_CSRFTOKEN': self.csrftoken}
        )

        #User Login
        login_credentials = {
            'email': 'fox@foxbecoding.com',
            'password': '123456'
        }
    
        #Get response data
        res = self.client.post(
            reverse('account-log-in-list'), 
            login_credentials, 
            **{'HTTP_X_CSRFTOKEN': self.csrftoken}
        )
        self.user = res.data
        self.csrftoken = self.client.cookies['csrftoken'].value

    def test_mc_merchant_create(self):
        res = self.client.post(
            reverse('mc-merchant-list'),
            data = {'title': 'Fenty Beauty'},
            **{'HTTP_X_CSRFTOKEN': self.csrftoken}
        )
        self.assertEqual(res.data['title'], 'Fenty Beauty')
        self.assertEqual(res.status_code, 201)
    
    def test_mc_merchant_create_error(self):
        res = self.client.post(
            reverse('mc-merchant-list'),
            data = {},
            **{'HTTP_X_CSRFTOKEN': self.csrftoken}
        )
        self.assertEqual(res.status_code, 400)

    def test_mc_merchant_retrieve(self):
        create_merchant_res = self.client.post(
            reverse('mc-merchant-list'),
            data = {'title': 'Fenty Beauty'},
            **{'HTTP_X_CSRFTOKEN': self.csrftoken}
        )
        
        res = self.client.get(
            reverse('mc-merchant-detail', kwargs={ 'pk': create_merchant_res.data['pk'] })
        )
  
        self.assertEqual(res.data['title'], 'Fenty Beauty')
        self.assertEqual(res.status_code, 200)
    
    def test_mc_merchant_retrieve_permissions_failed(self):
        self.client.post(
            reverse('mc-merchant-list'),
            data = {'title': 'Fenty Beauty'},
            **{'HTTP_X_CSRFTOKEN': self.csrftoken}
        )
        res = self.client.get(
            reverse('mc-merchant-detail', kwargs={ 'pk': 1558 })
        )
        self.assertEqual(res.status_code, 403)
