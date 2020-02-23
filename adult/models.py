from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Vendor(models.Model):
	name = models.CharField(max_length=500)
	uen = models.CharField(max_length=500, blank=True)
	phone_number = models.CharField(max_length=100, blank=True)
	email_address = models.CharField(max_length=100, blank=True)
	contact_person = models.CharField(max_length=100)
	billing_address = models.CharField(max_length=1000, blank=True)
	distribution_venue = models.CharField(max_length=500, blank=True)
	remarks = models.CharField(max_length=10000, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Table(models.Model):
	name = models.CharField(max_length=500)
	url_string = models.CharField(max_length=500, blank=True)
	database_table = models.CharField(max_length=500, blank=True)
	remarks = models.CharField(max_length=10000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	subsidiary_to = models.CharField(max_length=500, blank=True)

class Field(models.Model):
	label = models.CharField(max_length=500, blank=True)
	name = models.CharField(max_length=500)
	kind = models.CharField(max_length=100)
	table_index = models.IntegerField(blank=True, null=True)
	remarks = models.CharField(max_length=10000)
	dropdown = models.BooleanField(default=False)
	table = models.ForeignKey(Table, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class FieldValue(models.Model):
	name = models.CharField(max_length=500)
	kind = models.CharField(max_length=100)
	remarks = models.CharField(max_length=10000)
	field = models.ForeignKey(Field, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Role(models.Model):
	name = models.CharField(max_length=500)
	remarks = models.CharField(max_length=10000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alias = models.CharField(max_length=500)
    actual_name = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    nric = models.CharField(max_length=100)
    photo = models.CharField(max_length=500, blank=True)
    status = models.CharField(max_length=100)
    datetime_last_login = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, blank=True, null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Worker(models.Model):
	name = models.CharField(max_length=500) 
	fin_number = models.CharField(max_length=100, blank=True)
	fin_previous = models.CharField(max_length=100, blank=True)
	date_worker_registered = models.DateTimeField() 
	date_of_birth = models.DateTimeField() 
	when_first_arrive = models.CharField(max_length=100, blank=True)
	twid_string = models.CharField(max_length=100) 
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	created_for = models.CharField(max_length=100, blank=True)
	gender = models.CharField(max_length=100) 
	nationality = models.CharField(max_length=100) 
	nationality_more = models.CharField(max_length=100, blank=True)
	worker_flag = models.CharField(max_length=100, blank=True)
	path_current_facepic = models.CharField(max_length=100, blank=True)
	path_qr_code = models.CharField(max_length=100) 
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 

class PermissionPrivilege(models.Model):
	role = models.ForeignKey(Role, on_delete=models.CASCADE)
	field = models.ForeignKey(Field, on_delete=models.CASCADE)
	create = models.BooleanField()
	read = models.BooleanField()
	update = models.BooleanField()
	delete = models.BooleanField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Twid(models.Model):
	twid_card_type = models.CharField(max_length=100, blank=True)
	twid_card_serial_number = models.CharField(max_length=100, blank=True)
	date_twid_card_printed = models.DateTimeField() 
	twid_card_printed_by = models.CharField(max_length=100, blank=True)
	date_twid_card_issued = models.DateTimeField() 
	twid_card_issued_by = models.CharField(max_length=100, blank=True)
	date_twid_card_withdrawn = models.DateTimeField() 
	twid_card_withdrawn_by = models.CharField(max_length=100, blank=True)
	twid_card_remarks =  models.CharField(max_length=10000, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	worker = models.ForeignKey(Worker, on_delete=models.CASCADE, null=True) 
	table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True) 

class Nickname(models.Model):
	nickname = models.CharField(max_length=100, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	worker = models.ForeignKey(Worker, on_delete=models.CASCADE, null=True) 
	table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True) 