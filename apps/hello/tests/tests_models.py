# from django.test import TestCase

# from django.core.urlresolvers import reverse
# # from django.test import Client
# from django.test.client import RequestFactory

# from apps.hello.models import Person, RequestData
# from django.contrib.auth.models import User


# class PersonModelTestCase(TestCase):
#     """
#     test Person model
#     """
#     fixtures = ['test_data.json']

#     def test_person__str__(self):
#         """
#         test __str__ method returns first_name last_name
#         """

#         user = User.objects.get(username='admin')
#         person = Person(user=user)
#         self.assertEquals(person.__str__(), "Olexandr Lykhenko")

#     def test_person_properties_change_user(self):
#         """
#         test getter and setter for name, surname, email peroperties
#         test :model:`hello.Person` change affects :model:`auth.User` change
#         """
#         user = User.objects.get(username='admin')
#         person = Person(user=user)
#         self.assertEquals(person.name, "Olexandr")
#         self.assertEquals(person.surname, "Lykhenko")
#         self.assertEquals(person.email, "lykhenko.olexandr@gmail.com")
#         person.name = "Ololoshka"
#         person.surname = "Trololo"
#         person.email = "ololo@lol.lol"
#         self.assertEquals(person.name, "Ololoshka")
#         self.assertEquals(person.surname, "Trololo")
#         self.assertEquals(person.email, "ololo@lol.lol")

#         self.assertEquals(user.first_name, "Ololoshka")
#         self.assertEquals(user.last_name, "Trololo")
#         self.assertEquals(user.email, "ololo@lol.lol")


# class RequestDataTestCase(TestCase):
#     fixtures = ['test_data.json']
#     def test(self):
#         """
#         test __str__ outputs verbose object description
#         """
#         self.client.get(reverse('main'))
#         requestdata = RequestData.objects.latest('pub_date')
#         self.assertTrue("path:/ method:GET args:<QueryDict: {}> \
# username:AnonymusUser" in requestdata.__str__())





