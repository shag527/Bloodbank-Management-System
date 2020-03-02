from django.db import models
class BRequests(models.Model):
  status_choices=(
    (0,'pending'),
    (1,'approve'),
    (2,'done'),
    )
  blood_choices=(
    ("O Positive","O Positive"),
    ("O Negative","O Negative"),
    ("A Positive","A Positive"),
    ("A Negative","A Negative"),
    ("B Positive","B Positive"),
    ("B Negative","B Negative"),
    ("AB Positive","AB Positive"),
    ("AB Negative","AB Negative"),
    )
  patient_name=models.CharField(max_length=100)
  attendant_name=models.CharField(max_length=100)
  contact_number=models.CharField(max_length=15)
  blood_group=models.CharField(max_length=50,choices=blood_choices)
  quantity=models.IntegerField()
  hospital_name=models.CharField(max_length=100)
  deadline=models.DateField()
  status=models.IntegerField(choices=status_choices)
  the_donors=models.TextField(max_length=700,default="none")


  def __str__(self):
    return self.patient_name
  

class Donors(models.Model):
  gender_choices=(
    ("Male","Male"),
    ("Female","Female"),
    ("Other","Other"),
    )
  name=models.CharField(max_length=100)
  gender=models.CharField(max_length=10,choices=gender_choices)
  age=models.IntegerField()
  email=models.CharField(max_length=100)
  district=models.CharField(max_length=100)
  pincode=models.IntegerField()
  address=models.TextField()
  contact_number=models.CharField(max_length=15)
  blood_group=models.CharField(max_length=30)
  last_donated_date=models.CharField(max_length=30)
  major_illness=models.CharField(max_length=200)
  the_link=models.IntegerField(default=0)
  b_request_id=models.ForeignKey(BRequests,null=True,on_delete=models.SET_NULL,blank=True)

  def __str__(self):
    return self.name

class Contact_Us(models.Model):
  firstname=models.CharField(max_length=100)
  lastname=models.CharField(max_length=100)
  state=models.CharField(max_length=100)
  subject=models.TextField()

  def __str__(self):
    return self.firstname



