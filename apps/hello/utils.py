from django.contrib.auth import authenticate
from django.contrib import auth

from apps.hello.models import Person






def get_person_or_admin(request):
    """
    get Person object for current User if authenticated
    or
    login as admin and then get Person object for admin 
    """
    user = request.user
    if not user.is_authenticated():
        user = authenticate(username='admin', password='admin')
        auth.login(request, user)

    return Person.objects.get(user__username=user.username)

    # try:
    #     
    # except User.DoesNotExist:
    #     print "Handling unauthorized user", User.DoesNotExist
    #     
           
    #     
    # finally:
    #     return u

# def get_or_create_user_profile(request):
#     profile = None
#     user = get_user_or_auth_and_get_admin(request)
#     try:
#         profile = user.userprofile
#     except UserProfile.DoesNotExist:
#         profile = UserProfile(user=user)
#         profile.save()
#     return profile




