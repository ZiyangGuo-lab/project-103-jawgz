from django.test import TestCase
from login.models import User

class LoginTestCase(TestCase):

    newUser = User()

    def setUp(self):
        # create user
        self.newUser.name = "john doe"
        self.newUser.username = "username123"
        self.newUser.password = "password456"
        self.newUser.uid = hash(self.newUser.name + self.newUser.username + self.newUser.name[::-1])
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
        self.assertEqual(userQueried.uid, str(hash(userQueried.name + userQueried.username + userQueried.name[::-1])))

    def tearDown(self):
        query = User.objects.filter(username=self.newUser.username, password=self.newUser.password)
        query.delete()