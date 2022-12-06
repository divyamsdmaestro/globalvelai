from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
# Create your models here.

class Tag(models.Model):
    tag_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)


class User(models.Model):
    first_name = models.CharField(max_length=30)
    email_address = models.EmailField(unique=True, max_length=254)
    tag_id  =  models.ForeignKey(Tag, null=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)


class FileUpload(models.Model):
    """
    This model contains file upload details.
    """
    file = models.FileField(upload_to='myapp/uploads/', validators=[FileExtensionValidator( ['pdf','csv','jpg','png', 'xls'] ) ])
    uploaded_at = models.DateTimeField(default=timezone.now)







class Country(models.Model):
    """
    This model contains Country Details
    """
    country_name = models.CharField(max_length=75)
    created_at = models.DateTimeField(default=timezone.now)

class State(models.Model):
    """
    This model Contains State Details
    """
    country_id = models.ForeignKey(Country,on_delete=models.CASCADE)
    state_name = models.CharField(max_length=75)
    created_at = models.DateTimeField(default=timezone.now)

class Degree(models.Model):
    """
    This model Contains Degree Details
    """
    degree_name = models.CharField(max_length=75)
    created_at = models.DateTimeField(default=timezone.now)

class Skills(models.Model):
    """
    This model Contains Skills Details
    """
    skills_name = models.CharField(max_length=100)
    created_at  = models.DateTimeField(default=timezone.now)

class YearsOfExp(models.Model):
    """
    This model Contains YearsOfExp Details
    """
    year_of_exp = models.IntegerField()
    created_at  = models.DateTimeField(default=timezone.now)

class Years(models.Model):
    """
    This model Contains Year Details
    """
    year = models.IntegerField()
    created_at  = models.DateTimeField(default=timezone.now)

class Industries(models.Model):
    """
    This model Contains Industries Details
    """
    industry_name = models.CharField(max_length=75)
    created_at  = models.DateTimeField(default=timezone.now)

class SalaryExp(models.Model):
    """
    This model Contains SalaryExp Details
    """
    salary = models.CharField(max_length=75)
    created_at  = models.DateTimeField(default=timezone.now)

class TestModel(models.Model):

    name = models.CharField(max_length=75)
    email = models.CharField(max_length=30,unique=True)

class PersonalDetails(models.Model):
    """
    This model Contains Users Personal Details
    """
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    phone_number = models.CharField(unique=True, max_length=10)
    email = models.EmailField(unique=True, max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=75)
    pincode = models.CharField(max_length=30)
    state = models.ForeignKey(State,null=True,on_delete=models.SET_NULL)
    country = models.ForeignKey(Country,null=True,on_delete=models.SET_NULL)
    created_at  = models.DateTimeField(default=timezone.now)


class EducationalDetails(models.Model):
    """
    This model Contains Users Educational Details
    """
    def fetch_userid():
        user_id = PersonalDetails.objects.latest('id')
        return user_id.id

    user_id = models.ForeignKey(PersonalDetails,default=fetch_userid,related_name='educational',on_delete=models.SET_DEFAULT)
    degree = models.ForeignKey(Degree,null=True,on_delete=models.SET_NULL)
    yr_of_passing = models.CharField(max_length=20)
    school = models.CharField(max_length=100)
    created_at  = models.DateTimeField(default=timezone.now)

class CertificateDetails(models.Model):
    """
    This model Contains Users Certificate Details
    """
    def fetch_userid():
        user_id = PersonalDetails.objects.latest('id')
        return user_id.id

    user_id = models.ForeignKey(PersonalDetails,default=fetch_userid,related_name='certificate',on_delete=models.SET_DEFAULT)
    certificate_name = models.CharField(max_length=75)
    yr_of_certificate = models.CharField(max_length=20)
    created_at  = models.DateTimeField(default=timezone.now)

class WorkDetails(models.Model):
    """
    This model Contains user Work Experience Details
    """
    def fetch_userid():
        user_id = PersonalDetails.objects.latest('id')
        return user_id.id

    user_id = models.ForeignKey(PersonalDetails,default=fetch_userid,related_name='work',on_delete=models.SET_DEFAULT)
    skills_id = models.ForeignKey(Skills,null=True,on_delete=models.SET_NULL)
    year_exp_id = models.ForeignKey(YearsOfExp,null=True,on_delete=models.SET_NULL)
    created_at  = models.DateTimeField(default=timezone.now)


class EmploymentHistory(models.Model):
    """
    This model Contains Employment History Details
    """
    def fetch_userid():
        user_id = PersonalDetails.objects.latest('id')
        return user_id.id

    user_id = models.ForeignKey(PersonalDetails,default=fetch_userid,related_name='employement',on_delete=models.SET_DEFAULT)
    job_title = models.CharField(max_length=80)
    employer  = models.CharField(max_length=80)
    city      = models.CharField(max_length=80)
    state_id = models.ForeignKey(State,null=True,on_delete=models.SET_NULL)
    country_id = models.ForeignKey(Country,null=True,on_delete=models.SET_NULL)
    from_id = models.ForeignKey(Years,null=True,on_delete=models.SET_NULL)
    to_id   = models.ForeignKey(Years,related_name='to',null=True,on_delete=models.SET_NULL)
    created_at  = models.DateTimeField(default=timezone.now)

class AwardsDetails(models.Model):
    """
    This model Contains user awards Details
    """
    def fetch_userid():
        user_id = PersonalDetails.objects.latest('id')
        return user_id.id

    user_id = models.ForeignKey(PersonalDetails,default=fetch_userid,related_name='awards',on_delete=models.SET_DEFAULT)
    award_name = models.CharField(max_length=255)
    award_org  = models.CharField(max_length=255)
    created_at  = models.DateTimeField(default=timezone.now)


class PreferencesDetails(models.Model):
    """
    This model Contains user preference Details
    """
    def fetch_userid():
        user_id = PersonalDetails.objects.latest('id')
        return user_id.id

    user_id = models.ForeignKey(PersonalDetails,default=fetch_userid,related_name='preference',on_delete=models.SET_DEFAULT)
    country_id = models.ForeignKey(Country,null=True,on_delete=models.SET_NULL)
    industry_id  = models.ForeignKey(Industries,null=True,on_delete=models.SET_NULL)
    position  = models.CharField(null=True,max_length=80)
    available_from = models.ForeignKey(Years,null=True,on_delete=models.SET_NULL)
    has_passport = models.BooleanField(default=0)
    salary_exp = models.ForeignKey(SalaryExp,null=True,on_delete=models.SET_NULL)
    created_at  = models.DateTimeField(default=timezone.now)

class CommonModel(models.Model):
    """Common fields that are shared among all models."""

    created_at = models.DateTimeField(auto_now_add=True,
                                      editable=False)
    updated_at = models.DateTimeField(auto_now=True,
                                      editable=False)

class Restaurants(CommonModel):
    """
    This model Contains user Restaurants Details
    """
    restaurants_name = models.CharField(max_length=100)

class Customers(CommonModel):
    """
    This model Contains Customers Details
    """
    customer_name = models.CharField(max_length=100)
    restaurants_id = models.ManyToManyField(Restaurants,related_name='restaurants')