from rest_framework import serializers
from merchants.models import *
from utils.helpers import create_uid
from PIL import Image
import stripe

class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = [
            'pk',
            'uid',
            'title'
        ]

class CreateMerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = [
            'user',
            'uid',
            'title'
        ]
    
    def validate(self, attrs):
        Merchant_Instance = Merchant.objects.create(
            user = self.context['user'],
            uid = create_uid('m-'),
            title = attrs.get('title'),
        )
        Merchant_Instance.save()
        attrs['merchant'] = Merchant_Instance
        return attrs 

