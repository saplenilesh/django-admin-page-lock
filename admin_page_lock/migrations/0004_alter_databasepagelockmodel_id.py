# Generated by Django 4.0.4 on 2022-05-24 11:10

from django.db import migrations
import hashid_field.field


class Migration(migrations.Migration):

    dependencies = [
        ('admin_page_lock', '0003_databasepagelockmodel_tab_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='databasepagelockmodel',
            name='id',
            field=hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', auto_created=True, min_length=7, prefix='', primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
