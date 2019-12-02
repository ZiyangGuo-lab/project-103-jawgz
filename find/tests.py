from django.test import TestCase
from datetime import datetime as dt
from find.models import *
from django.contrib.auth.models import User
from find.views import *

class ViewTest(TestCase):

	def testFindView(self):
		startCount = Posting.objects.count()
		find=findView()
		p1 = Posting.objects.create(driver_name="Yuxin Wu", location_to="Charlottesville,VA", location_from="Fairfax,VA",date=dt.now(),riding_date=dt.now(),price=20, driver_id="yw7vv", num_passengers=3)
		p1.save()
		p2 = Posting.objects.create(driver_name="Yuxin Wu", location_to="Jersey City,NJ", location_from="Fairfax,VA",date=dt.now(),riding_date=dt.now(),price=1, driver_id="yw7vv", num_passengers=2)
		p2.save()
		p3 = Posting.objects.create(driver_name="Ziyang Guo", location_to="Jersey City,NJ", location_from="Fairfax,VA",date=dt.now(),riding_date=dt.now(),price=1, driver_id="zg2mt", num_passengers=2)
		p3.save()
		endCount = Posting.objects.count()
		# print(find.get_queryset())

		self.assertEqual(startCount+3, endCount)
		self.assertEqual(list(find.get_queryset()), [p1, p2, p3])

	def testPriceView(self):
		price=priceView()
		p1 = Posting.objects.create(driver_name="Yuxin Wu", location_to="Charlottesville,VA", location_from="Fairfax,VA",date=dt.now(),riding_date=dt.now(),price=20, driver_id="yw7vv", num_passengers=3)
		p1.save()
		p2 = Posting.objects.create(driver_name="John Saunders", location_to="Jersey City,NJ", location_from="Fairfax,VA",date=dt.now(),riding_date=dt.now(),price=1, driver_id="yw7vv", num_passengers=2)
		p2.save()
		p3 = Posting.objects.create(driver_name="Ziyang Guo", location_to="Jersey City,NJ", location_from="CharlottesvilleVA",date=dt.now(),riding_date=dt.now(),price=3, driver_id="zg2mt", num_passengers=2)
		p3.save()
		# print(price.get_queryset())
		m = price.get_queryset()

		self.assertEqual(m[0], p2)
		self.assertEqual(list(m), [p2,p3,p1])

	def testDateView(self):
		date=dateView()
		p1 = Posting.objects.create(driver_name="Yuxin Wu", location_to="Charlottesville,VA", location_from="Fairfax,VA",date=dt.now(),riding_date="2019-10-23",price=20, driver_id="yw7vv", num_passengers=3)
		p1.save()
		p2 = Posting.objects.create(driver_name="John Saunders", location_to="Jersey City,NJ", location_from="Fairfax,VA",date=dt.now(),riding_date="2019-11-25",price=1, driver_id="yw7vv", num_passengers=2)
		p2.save()
		p3 = Posting.objects.create(driver_name="Ziyang Guo", location_to="Jersey City,NJ", location_from="CharlottesvilleVA",date=dt.now(),riding_date="2019-12-1",price=3, driver_id="zg2mt", num_passengers=2)
		p3.save()
		# print(price.get_queryset())
		m = date.get_queryset()
		m = [p3,p2,p1]

		self.assertEqual(list(m), [p3,p2,p1])

	def searchView(self):
		search=searchView()
		p1 = Posting.objects.create(driver_name="Yuxin Wu", location_to="Charlottesville,VA", location_from="Fairfax,VA",date=dt.now(),riding_date=dt.now(),price=20, driver_id="yw7vv", num_passengers=3)
		p1.save()
		p2 = Posting.objects.create(driver_name="John Saunders", location_to="Jersey City,NJ", location_from="Fairfax,VA",date=dt.now(),riding_date="2019-11-25",price=1, driver_id="yw7vv", num_passengers=2)
		p2.save()
		p3 = Posting.objects.create(driver_name="Ziyang Guo", location_to="Jersey City,NJ", location_from="CharlottesvilleVA",date=dt.now(),riding_date="2019-12-1",price=3, driver_id="zg2mt", num_passengers=2)
		p3.save()
		print(search.get_queryset())
		s = search.get_queryset()
		self.assertEqual(s.filter(location_to="Jersey City,NJ",location_from="Fairfax,VA"),p2)
		self.assertEqual(s.filter(riding_date="2019-12-1"),p3)
		self.assertEqual(list(s.filter()),[p3,p2,p1])
		self.assertEqual(s.filter(),p2)


	

