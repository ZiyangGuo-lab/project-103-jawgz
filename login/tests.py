
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

    def test_can_login(self):

        #query this user
        query = User.objects.filter(username=self.newUser.username, password=self.newUser.password)

        #confirm this is the user
        self.assertEqual(query.count(), 1)
        userQueried = query[0]
        self.assertEqual(userQueried.name, "john doe")
        self.assertEqual(userQueried.username, "username123")
        self.assertEqual(userQueried.password, "password456")

    def test_cannot_login(self):

        #query another user
        query = User.objects.filter(username="not a user", password="not the password")

        # confirm this does not exist
        self.assertEqual(query.count(), 0)

    def test_can_create_user(self):
        userCount = User.objects.all().count()

        # create user
        anotherUser = User()
        anotherUser.name = "new user"
        anotherUser.username = "newUser123"
        anotherUser.password = "newPassword456"
        anotherUser.save()  # save user
        newCount = User.objects.all().count()

        self.assertEquals(userCount+1, newCount)


    def tearDown(self):
        query = User.objects.filter(username=self.newUser.username, password=self.newUser.password)
        query.delete()