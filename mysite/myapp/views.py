from django.conf import settings
from django.shortcuts import get_object_or_404, render
from html5lib import serialize
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView
from .serializers import TagSerializer, UserModelSerializer, TagLinktoUserModelSerializer, FileUploadModelSerializer, CountryModelSerializer, StateModelSerializer, DegreeModelSerializer, SkillsModelSerializer, YearOfExpModelSerializer, YearModelSerializer, IndustriesModelSerializer, SalaryExpModelSerializer, TestModelSerializer, PersonalDetailsModelSerializer, EducationalDetailsModelSerializer, CertificateDetailsModelSerializer, WorkDetailsModelSerializer, EmployeeHistoryModelSerializer, AwardDetailsModelSerializer, PreferencesDetailsModelSerializer, RestaurantsSerializer, CustomersSerializer, getGenericSerializer
from .models import User, Tag, FileUpload, Country, State, Degree, Skills, YearsOfExp, Years, Industries, SalaryExp, TestModel, PersonalDetails, Restaurants, Customers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser, FileUploadParser, MultiPartParser, FormParser
from rest_framework.decorators import parser_classes
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend

def getGenericModelViewset(model_arg):

    class GenericModelViewset(viewsets.ModelViewSet):
        queryset = model_arg.objects.all()
        serializer_class = getGenericSerializer(model_arg)
         
    return GenericModelViewset

class TagModelViewset(getGenericModelViewset(Tag)):
    """
    Viewset to handle CRUD opetations for the `Tag` model.
    The viewsets provides the create(),update(),list(), destroy(), and retrive() actions.
        create() - POST methods
        update() - PATCH methods
        destroy() - DELETE methods
        list(),retrieve() - GET methods
    """

    pass
    
    # queryset = Tag.objects.all()
    # serializer_class = TagSerializer

class UserModelViewset(viewsets.ModelViewSet):
    """
        Viewset to handle CRUD opetations for the `User` model.
        The viewsets provides the create(),update(),list(), destroy(), and retrive() actions.
        create() - POST methods
        update() - PATCH methods
        destroy() - DELETE methods
        list(),retrieve() - GET methods
    """
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'email_address', 'tag_id']

    @action(detail=True, methods=['get'])
    def add_tag(self, request, pk=None):
        user = User.objects.get(id=pk)
        # print(request.data)
        # breakpoint()
        serializer = TagLinktoUserModelSerializer(user,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})


class FileUploadViewsets(viewsets.ModelViewSet):
    # print(settings.TEMP_ROOT)
    """
        Viewset to handle CRUD opetations for the `FileUpload` model.
        The viewsets provides the create(),update(),list(), destroy(), and retrive() actions.
        create() - POST methods
    """
    # media_type = 'multipart/form-data'
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadModelSerializer
    parser_classes = [MultiPartParser]

class CountryViewsets(viewsets.ModelViewSet):
    """
    Viewset to handle CRUD opetations for the `Country` model.
    The viewsets provides the create(),update(),list(), destroy(), and retrive() actions.
        create() - POST methods
        update() - PATCH methods
        destroy() - DELETE methods
        list(),retrieve() - GET methods
    """
    
    queryset = Country.objects.all()
    serializer_class = CountryModelSerializer

class StateViewsets(viewsets.ModelViewSet):
    """
    Viewset to handle CRUD opetations for the `State` model.
    The viewsets provides the create(),update(),list(), destroy(), and retrive() actions.
        create() - POST methods
        update() - PATCH methods
        destroy() - DELETE methods
        list(),retrieve() - GET methods
    """
    
    queryset = State.objects.all()
    serializer_class = StateModelSerializer

class DegreeViewsets(viewsets.ModelViewSet):
    """
    Viewset to handle CRUD opetations for the `Degree` model.
    The viewsets provides the create(),update(),list(), destroy(), and retrive() actions.
        create() - POST methods
        update() - PATCH methods
        destroy() - DELETE methods
        list(),retrieve() - GET methods
    """
    
    queryset = Degree.objects.all()
    serializer_class = DegreeModelSerializer

class SkillsViewsets(viewsets.ModelViewSet):
    """
    Viewset to handle CRUD opetations for the `Skills` model.
    The viewsets provides the create(),update(),list(), destroy(), and retrive() actions.
        create() - POST methods
        update() - PATCH methods
        destroy() - DELETE methods
        list(),retrieve() - GET methods
    """
    
    queryset = Skills.objects.all()
    serializer_class = SkillsModelSerializer

class YearOfExpViewsets(viewsets.ModelViewSet):
    """
    Viewset to handle CRUD opetations for the `Yearofexp` model.
    The viewsets provides the create(),update(),list(), destroy(), and retrive() actions.
        create() - POST methods
        update() - PATCH methods
        destroy() - DELETE methods
        list(),retrieve() - GET methods
    """
    
    queryset = YearsOfExp.objects.all()
    serializer_class = YearOfExpModelSerializer

class YearViewsets(viewsets.ModelViewSet):
    """
    Viewset to handle CRUD opetations for the `Year` model.
    The viewsets provides the create(),update(),list(), destroy(), and retrive() actions.
        create() - POST methods
        update() - PATCH methods
        destroy() - DELETE methods
        list(),retrieve() - GET methods
    """
    
    queryset = Years.objects.all()
    serializer_class = YearModelSerializer

class IndustriesViewsets(viewsets.ModelViewSet):
    """
    Viewset to handle CRUD opetations for the `Industries` model.
    The viewsets provides the create(),update(),list(), destroy(), and retrive() actions.
        create() - POST methods
        update() - PATCH methods
        destroy() - DELETE methods
        list(),retrieve() - GET methods
    """
    
    queryset = Industries.objects.all()
    serializer_class = IndustriesModelSerializer

class SalaryExpViewsets(viewsets.ModelViewSet):
    """
    Viewset to handle CRUD opetations for the `SalaryExp` model.
    The viewsets provides the create(),update(),list(), destroy(), and retrive() actions.
        create() - POST methods
        update() - PATCH methods
        destroy() - DELETE methods
        list(),retrieve() - GET methods
    """
    
    queryset = SalaryExp.objects.all()
    serializer_class = SalaryExpModelSerializer

class RegisterUserDetailsViewsets(viewsets.ModelViewSet):
    """
    Viewset to handle CRUD opetations for the `RegisterUser` Details.
    The viewsets provides the create(),update(),list(), destroy(), and retrive() actions.
        list(),retrieve() - GET methods
    """
    queryset = PersonalDetails.objects.all()
    serializer_class = PersonalDetailsModelSerializer

    @action(detail=False, methods=['post'])
    def add_user_register_details(self, request, pk=None):
        # print(request.data['data'])
        # breakpoint()
        personal_serializer = PersonalDetailsModelSerializer(data=request.data['personal_details'])
        educational_serializer = EducationalDetailsModelSerializer(data=request.data['educational_details'],many=True)
        certificate_serializer = CertificateDetailsModelSerializer(data=request.data['certificate_details'], many=True)
        work_serializer = WorkDetailsModelSerializer(data=request.data['work_details'])
        employee_history_serializer = EmployeeHistoryModelSerializer(data=request.data['employee_history_details'], many=True)
        awards_serializer = AwardDetailsModelSerializer(data=request.data['awards_details'], many=True)
        preference_serializer = PreferencesDetailsModelSerializer(data=request.data['preference_details'])

        if personal_serializer.is_valid() and educational_serializer.is_valid() and certificate_serializer.is_valid() and work_serializer.is_valid() and employee_history_serializer.is_valid() and awards_serializer.is_valid() and preference_serializer.is_valid():
            personal_serializer.save()
            educational_serializer.save()
            certificate_serializer.save()
            work_serializer.save()
            employee_history_serializer.save()
            awards_serializer.save()
            preference_serializer.save()

            return Response({"status": "success", 'personal_details':personal_serializer.data, 'educational_details':educational_serializer.data, 'certificate_details':certificate_serializer.data, 'work_details':work_serializer.data, 'employee_history_details':employee_history_serializer.data, 'awards_details':awards_serializer.data, 'preference_details':preference_serializer.data})
        # return Response({'status':'error', 'personal_details':personal_serializer.errors, 'educational_details':educational_serializer.errors, 'certificate_details':certificate_serializer.errors})
        return Response({'status':'error', 'personal_details':personal_serializer.errors})


class RestaurantsViewsets(viewsets.ModelViewSet):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantsSerializer

class TagRestaurantToCustomersViewsets(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer

class TestModelViewsets(viewsets.ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer

    @action(detail=False, methods=['post'])
    def add_test(self, request, pk=None):
        # print(request.data['data'])
        # breakpoint()
        serializer = TestModelSerializer(data=request.data['data'],many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success"})
        return Response({'status':'error'})
