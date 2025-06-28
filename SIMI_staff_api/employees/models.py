from django.db import models
from django.contrib.auth.models import AbstractUser

'''
super user name: Chidi
email: fleektyre@gmail.com
password: 1910theguy
'''
class Address(models.Model):
    street_address1 = models.CharField(max_length=255)
    street_address2 = models.CharField(max_length=255)
    street_address3 = models.CharField(max_length=255)

    house_number = models.CharField(max_length=50 )
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

class StaffBase(AbstractUser):
    company_role = models.CharField(max_length=100)

    def get_role(self):
        return self.company_role

class Manager(StaffBase):
    department = models.CharField(max_length=10)
    has_company_card = models.BooleanField(default=True)
    address = models.ForeignKey("Address", related_name="address_manager", on_delete=models.CASCADE)

class Intern(StaffBase):
    mentor = models.ForeignKey("Manager", related_name="interns", on_delete=models.CASCADE)
    internship_end = models.DateTimeField(auto_now_add=True)
    address = models.ForeignKey("Address", related_name="address_intern", on_delete=models.CASCADE)

