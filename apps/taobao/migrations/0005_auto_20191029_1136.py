# Generated by Django 2.0.12 on 2019-10-29 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taobao', '0004_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='pid',
            field=models.CharField(max_length=100, verbose_name='活动id'),
        ),
    ]