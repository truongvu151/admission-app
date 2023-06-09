# Generated by Django 4.1.7 on 2023-04-27 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(null=True, upload_to='banners/%Y/%m/'),
        ),
    ]
