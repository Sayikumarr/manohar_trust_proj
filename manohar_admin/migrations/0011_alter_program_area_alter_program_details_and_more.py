# Generated by Django 4.0.2 on 2022-02-23 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manohar_admin', '0010_rename_programs_program'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='area',
            field=models.CharField(default='Program Area', max_length=50),
        ),
        migrations.AlterField(
            model_name='program',
            name='details',
            field=models.CharField(default='Program Details', max_length=500),
        ),
        migrations.AlterField(
            model_name='program',
            name='title',
            field=models.CharField(default='Program Title', max_length=50),
        ),
    ]
