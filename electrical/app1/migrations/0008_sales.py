# Generated by Django 3.2 on 2022-02-09 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_attributes'),
    ]

    operations = [
        migrations.CreateModel(
            name='sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign_name', models.CharField(max_length=200, null=True, verbose_name='Campaign name')),
                ('startdate', models.DateField(null=True, verbose_name='Start Date')),
                ('enddate', models.DateField(null=True, verbose_name='End Date')),
            ],
        ),
    ]
