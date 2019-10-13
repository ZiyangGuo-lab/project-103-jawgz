from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    #the unique id of the user
    #created by hash(name + username + backwards(name))
    uid = models.CharField(max_length=200)

    #unlimited size field, comma seperated string of uids of postings created by this user
    postings = models.TextField(blank=True)

    def __str__(self):
        return self.name

    # def addListing(self, newListing):
    #     self.postings += "," + newListing
    #     self.save()