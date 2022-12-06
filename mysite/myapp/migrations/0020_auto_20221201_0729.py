# Generated by Django 3.2.12 on 2022-12-01 07:29

from django.db import migrations, models
import django.db.models.deletion
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_auto_20221128_0930'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='awardsdetails',
            name='user_id',
            field=models.ForeignKey(default=myapp.models.AwardsDetails.fetch_userid, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='awards', to='myapp.personaldetails'),
        ),
        migrations.AlterField(
            model_name='certificatedetails',
            name='user_id',
            field=models.ForeignKey(default=myapp.models.CertificateDetails.fetch_userid, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='certificate', to='myapp.personaldetails'),
        ),
        migrations.AlterField(
            model_name='educationaldetails',
            name='user_id',
            field=models.ForeignKey(default=myapp.models.EducationalDetails.fetch_userid, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='educational', to='myapp.personaldetails'),
        ),
        migrations.AlterField(
            model_name='employmenthistory',
            name='user_id',
            field=models.ForeignKey(default=myapp.models.EmploymentHistory.fetch_userid, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='employement', to='myapp.personaldetails'),
        ),
        migrations.AlterField(
            model_name='preferencesdetails',
            name='has_passport',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='preferencesdetails',
            name='position',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='preferencesdetails',
            name='user_id',
            field=models.ForeignKey(default=myapp.models.PreferencesDetails.fetch_userid, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='preference', to='myapp.personaldetails'),
        ),
        migrations.AlterField(
            model_name='workdetails',
            name='user_id',
            field=models.ForeignKey(default=myapp.models.WorkDetails.fetch_userid, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='work', to='myapp.personaldetails'),
        ),
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('commonmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.commonmodel')),
                ('restaurants_name', models.CharField(max_length=100, null=True)),
            ],
            bases=('myapp.commonmodel',),
        ),
    ]