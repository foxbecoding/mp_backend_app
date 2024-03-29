from users.serializers import *
from users.models import UserProfile

def Prepare_User_Data(User_Instance):
    User_Serializer = UserSerializer(User_Instance)
    User_Data = User_Serializer.data
    User_Login_Instances = UserLogin.objects.filter(pk__in=User_Data['logins'])
    User_Account_Login_Serializer = UserLoginSerializer(User_Login_Instances, many=True)
    
    user_logins = [
        {
            'pk': login['pk'],
            'logged_in_date': login['created']
        }
        for login in User_Account_Login_Serializer.data
    ]
    
    User_Profile_Instance = UserProfile.objects.filter(pk__in=User_Data['profiles'])
    User_Profile_Serializer = UserProfileSerializer(User_Profile_Instance, many=True)
    user_profiles = [
        { 
            'pk': profile['pk'], 
            'name': profile['name'], 
            'is_account_holder': profile['is_account_holder']
        }
        for profile in User_Profile_Serializer.data
    ]

    for profile in user_profiles:
        if UserProfileImage.objects.filter(user_profile=profile['pk']).exists():
            User_Profile_Image_Instance = UserProfileImage.objects.get(user_profile=profile['pk'])
            User_Profile_Image_Serializer = UserProfileImageSerializer(User_Profile_Image_Instance)
            profile['image'] = {
                'pk': User_Profile_Image_Serializer.data['pk'],
                'path': User_Profile_Image_Serializer.data['image']
            }
        else:
            profile['image'] = None

    User_Address_Instance = UserAddress.objects.filter(pk__in=User_Data['addresses'])
    User_Address_Serializer = UserAddressSerializer(User_Address_Instance, many=True)

    data = {
        'pk': User_Data['pk'],
        'uid': User_Data['uid'],
        'first_name': User_Data['first_name'],
        'last_name': User_Data['last_name'],
        'email': User_Data['email'],
        'logins': user_logins,
        'profiles': user_profiles,
        'addresses': User_Address_Serializer.data
    }
    
    return data