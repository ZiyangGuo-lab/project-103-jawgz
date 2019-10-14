<<<<<<< HEAD
from django.test import TestCase

# Create your tests here.
=======

# Create your tests here.
from django.test import TestCase
from login.models import User
#
class LoginTestCase(TestCase):

    newUser = User()

    def setUp(self):
        # create user
        self.newUser.name = "john doe"
        self.newUser.username = "username123"
        self.newUser.password = "password456"
        self.newUser.save()  # save user

    def test_can_create_users(self):

        #query this user
        query = User.objects.filter(username=self.newUser.username, password=self.newUser.password)

        #confirm this is the user
        self.assertEqual(query.count(), 1)
        userQueried = query[0]
        self.assertEqual(userQueried.name, "john doe")
        self.assertEqual(userQueried.username, "username123")
        self.assertEqual(userQueried.password, "password456")


    def tearDown(self):
        query = User.objects.filter(username=self.newUser.username, password=self.newUser.password)
        query.delete()
>>>>>>> 6f91319546b813bd00251c2cac2a9cdfd98975e9
