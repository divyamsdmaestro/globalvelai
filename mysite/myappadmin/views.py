import json
from rest_framework import viewsets
from myapp.models import AwardsDetails, CertificateDetails, EmploymentHistory, PersonalDetails, PreferencesDetails, WorkDetails, EducationalDetails
from myapp.serializers import PersonalDetailsModelSerializer, StateModelSerializer, WorkDetailsModelSerializer, GetRegisterUsersDetailModelSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from .filters import RegisterUserFilter
from fpdf import FPDF
import reportlab
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django import template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import django_filters
from django.db.models import Prefetch

class RegisterUserDetailsViewsets(viewsets.ModelViewSet):
    """
    Viewset to handle CRUD opetations for the `RegisterUser` Details.
    The viewsets provides the create(),update(),list(), destroy(), and retrive() actions.
        list(),retrieve() - GET methods
    """
    
    queryset = PersonalDetails.objects.prefetch_related('educational','certificate','work','employement','awards','preference').all()
    serializer_class = GetRegisterUsersDetailModelSerializer
    statename = StateModelSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_class    = RegisterUserFilter
    filterset_fields = ['state','first_name','last_name','work__year_exp_id_id','work__skills_id_id','preference__has_passport','preference__created_at']

    # def list(self, request):
    #     return Response({'register_users_list': GetRegisterUsersDetailModelSerializer(self.get_queryset(), many=True).data})
        

    @action(detail=True, methods=['get'])
    def generate_register_user_pdf(self, request, pk=None):
        # queryset = PersonalDetails.objects.select_related('state').prefetch_related('educational','certificate','work','employement','awards','preference').get(id=pk)
        # serializer_class = GetRegisterUsersDetailModelSerializer(queryset).data
        # content = serializer_class
        queryset = PersonalDetails.objects.select_related('state','country').prefetch_related(Prefetch('educational',queryset=EducationalDetails.objects.select_related('degree'), to_attr='educational_details')).prefetch_related(Prefetch('certificate',queryset=CertificateDetails.objects.select_related('user_id'), to_attr='certificate_details')).prefetch_related(Prefetch('work',queryset=WorkDetails.objects.select_related('user_id','skills_id','year_exp_id'), to_attr='work_details')).prefetch_related(Prefetch('employement',queryset=EmploymentHistory.objects.select_related('user_id','state_id','country_id','from_id','to_id'), to_attr='employement_details')).prefetch_related(Prefetch('awards',queryset=AwardsDetails.objects.select_related('user_id'), to_attr='awards_details')).prefetch_related(Prefetch('preference',queryset=PreferencesDetails.objects.select_related('user_id','country_id','industry_id','available_from','salary_exp'), to_attr='preference_details')).get(id=pk)
        content = queryset
       
        template_path = 'users/generate_pdf.html'
        context = {'register_user_details': content}

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="register_users_details.pdf"'
        template = get_template(template_path)
        html = template.render(context)
        # create a pdf
        pisa_status = pisa.CreatePDF(
            html, dest=response)
        # if error then show some funy view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response

