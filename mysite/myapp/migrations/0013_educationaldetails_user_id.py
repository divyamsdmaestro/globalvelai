# Generated by Django 3.2.12 on 2022-11-26 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_certificatedetails_educationaldetails_personaldetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationaldetails',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.personaldetails'),
        ),
    ]
