from django.db.models import fields
from rest_framework import serializers
from .models import User, Tag, FileUpload, Country, State, Degree, Skills, YearsOfExp, Years, Industries, SalaryExp, TestModel, PersonalDetails, EducationalDetails, CertificateDetails, WorkDetails, EmploymentHistory, AwardsDetails, PreferencesDetails, Restaurants, Customers


def getGenericSerializer(model_arg):
    class GenericSerializer(serializers.ModelSerializer):
        class Meta:
            model = model_arg
            fields = '__all__'

    return GenericSerializer


class TagSerializer(getGenericSerializer(Tag)):
    """
    Tag model fields are automatically populated and validated.
    """

    


class UserModelSerializer(serializers.ModelSerializer):
    """
    User model fields are automatically populated and validated.
    """

    class Meta:
        model  = User
        fields = '__all__'

class TagLinktoUserModelSerializer(serializers.ModelSerializer):
    """
    Tag model used for tag linked to particular user.
    """
    class Meta:
        model = User
        fields = ['id', 'tag_id']

class FileUploadModelSerializer(serializers.ModelSerializer):
    """
    File Upload model fields are automatically populated and validated.
    """
    class Meta:
        model = FileUpload
        fields = ['file']
    
class CountryModelSerializer(getGenericSerializer(Country)):
    """
    Country model fields are automatically populated and validated.
    """
    # class Meta:
    #     model = Country
    #     fields = '__all__'

class StateModelSerializer(getGenericSerializer(State)):
    """
    State model fields are automatically populated and validated.
    """
    # class Meta:
    #     model = State
    #     fields = '__all__'

class DegreeModelSerializer(serializers.ModelSerializer):
    """
    Degree model fields are automatically populated and validated.
    """
    class Meta:
        model = Degree
        fields = '__all__'

class SkillsModelSerializer(serializers.ModelSerializer):
    """
    Skill Model fields are automatically populated and validated.
    """
    class Meta:
        model = Skills
        fields = '__all__'

class YearOfExpModelSerializer(serializers.ModelSerializer):
    """
    YearsOfExp Model fields are automatically populated and validated.
    """
    class Meta:
        model = YearsOfExp
        fields = '__all__'

class YearModelSerializer(serializers.ModelSerializer):
    """
    Year Model fields are automatically populated and validated.
    """
    class Meta:
        model = Years
        fields = '__all__'

class IndustriesModelSerializer(serializers.ModelSerializer):
    """
    Year Model fields are automatically populated and validated.
    """
    class Meta:
        model = Industries
        fields = '__all__'

class SalaryExpModelSerializer(serializers.ModelSerializer):
    """
    SalaryExp Model fields are automatically populated and validated.
    """
    class Meta:
        model = SalaryExp
        fields = '__all__'

class TestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = '__all__'



class PersonalDetailsModelSerializer(serializers.ModelSerializer):
    """
    PersonalDetails Model fields are automatically populated and validated.
    """
    class Meta:
        model = PersonalDetails
        fields = '__all__'

class EducationalDetailsModelSerializer(serializers.ModelSerializer):
    """
    EducationalDetails Model fields are automatically populated and validated.
    """
    # degree_name = serializers.SerializerMethodField()

    class Meta:
        model = EducationalDetails
        fields = ['yr_of_passing','school','created_at','user_id','degree']

    # def get_degree_name(self,obj):
    #     get_degree_name = Degree.objects.get(id=obj.degree_id)
    #     return get_degree_name.degree_name
        
class CertificateDetailsModelSerializer(serializers.ModelSerializer):
    """
    CertificateDetails Model fields are automatically populated and validated.
    """
    class Meta:
        model = CertificateDetails
        fields = '__all__'

class WorkDetailsModelSerializer(serializers.ModelSerializer):
    """
    WorkDetails Model fields are automatically populated and validated.
    """
    # skills_name = serializers.SerializerMethodField()
    experience_year = serializers.SerializerMethodField()

    class Meta:
        model = WorkDetails
        fields = ['id','user_id','skills_id','year_exp_id','experience_year']

    def get_experience_year(self,obj):
        get_exp_yr = YearsOfExp.objects.get(id=obj.year_exp_id_id)
        return get_exp_yr.year_of_exp
    # def get_skills_name(self,obj):
    #     get_skills_set_name = Skills.objects.filter(id=obj.skills_id_id).all()
    #     for skills in get_skills_set_name:

class EmployeeHistoryModelSerializer(serializers.ModelSerializer):
    """
    Employee Details Model fields are automatically populated and validated
    """
    state_name = serializers.SerializerMethodField()
    country_name = serializers.SerializerMethodField()
    fromYear = serializers.SerializerMethodField()
    to = serializers.SerializerMethodField()

    class Meta:
        model = EmploymentHistory
        fields = ['id','user_id','job_title','employer','city','state_id','state_name','country_id','country_name','from_id','fromYear','to_id','to','created_at']

    def get_state_name(self,obj):
        get_state_name = State.objects.get(id=obj.state_id_id)
        return get_state_name.state_name

    def get_country_name(self,obj):
        get_country_name = Country.objects.get(id=obj.country_id_id)
        return get_country_name.country_name
    
    def get_fromYear(self,obj):
        get_year = Years.objects.get(id=obj.from_id_id)
        return get_year.year
    
    def get_to(self,obj):
        get_to = Years.objects.get(id=obj.to_id_id)
        return get_to.year

class AwardDetailsModelSerializer(serializers.ModelSerializer):
    """
    Award Details Model fields are automatically populated and validated.
    """
    class Meta:
        model = AwardsDetails
        fields = '__all__'

class PreferencesDetailsModelSerializer(serializers.ModelSerializer):
    """
    Preference Details Model fields are automatically populated and validated.
    """
    industry = serializers.SerializerMethodField()
    country_name = serializers.SerializerMethodField()
    availableFrom = serializers.SerializerMethodField()
    Ispassport = serializers.SerializerMethodField()
    salaryExp = serializers.SerializerMethodField()

    class Meta:
        model = PreferencesDetails
        fields = ['id','user_id','country_id','country_name','industry_id','industry','position','available_from','availableFrom','has_passport','Ispassport','salary_exp','salaryExp','created_at']

    def get_industry(self,obj):
        get_industry_name = Industries.objects.get(id=obj.industry_id_id)
        return get_industry_name.industry_name
    
    def get_country_name(self,obj):
        get_country_name = Country.objects.get(id=obj.country_id_id)
        return get_country_name.country_name
    
    def get_availableFrom(self,obj):
        get_ava_from = Years.objects.get(id=obj.available_from_id)
        return get_ava_from.year

    def get_Ispassport(self,obj):
        if obj.has_passport ==1 :
            return True
        return False

    def get_salaryExp(self,obj):
        get_salary_exp = SalaryExp.objects.get(id=obj.salary_exp_id)
        return get_salary_exp.salary

class GetRegisterUsersDetailModelSerializer(serializers.ModelSerializer):
    """
    Get all register users details
    """
    educational = EducationalDetailsModelSerializer(many=True, read_only=True)
    certificate = CertificateDetailsModelSerializer(many=True, read_only=True)
    work        = WorkDetailsModelSerializer(many=True,read_only=True)
    employement = EmployeeHistoryModelSerializer(many=True, read_only=True)
    awards      = AwardDetailsModelSerializer(many=True, read_only=True)
    preference  = PreferencesDetailsModelSerializer(many=True,read_only=True)
    # state = serializers.SerializerMethodField()
    # country = serializers.SerializerMethodField()
    state = StateModelSerializer(read_only=True)
    country = CountryModelSerializer(read_only=True)
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = PersonalDetails
        fields = ['id','first_name', 'last_name', 'full_name','phone_number', 'email', 'city', 'state','country', 'educational', 'certificate', 'work', 'employement', 'awards', 'preference']

    # def get_state(self, obj):
    #     get_state_name = State.objects.get(id=obj.state_id)
    #     return get_state_name.state_name
    
    # def get_country(self, obj):
    #     get_country_name = Country.objects.get(id=obj.country_id)
    #     return get_country_name.country_name

    def get_full_name(self, obj):
        get_full_name = obj.first_name + '' + obj.last_name
        return get_full_name

class CommonSerializer(serializers.ModelSerializer):
    """Common fields that are shared among all serializers."""

    common_fields = ['created_at','updated_at']

class RestaurantsSerializer(CommonSerializer):
    """
    Get all Restaurants Details
    """
    class Meta:
        model = Restaurants
        fields = '__all__'

class CustomersSerializer(serializers.ModelSerializer):
    """
    Get all Customers Details
    """
    restaurants_id = RestaurantsSerializer(many=True,read_only=True)

    class Meta:
        model = Customers
        fields = ['customer_name','restaurants_id'] + CommonSerializer.common_fields