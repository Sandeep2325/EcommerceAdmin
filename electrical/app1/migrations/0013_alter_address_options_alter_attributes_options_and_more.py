# Generated by Django 4.0.2 on 2022-02-11 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_alter_address_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Address'},
        ),
        migrations.AlterModelOptions(
            name='attributes',
            options={'verbose_name_plural': 'Attributes'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Order'},
        ),
        migrations.AlterModelOptions(
            name='sales',
            options={'verbose_name_plural': 'Sales'},
        ),
    ]
