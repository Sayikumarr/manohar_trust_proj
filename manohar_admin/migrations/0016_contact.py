# Generated by Django 4.0.2 on 2022-02-24 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manohar_admin', '0015_mediapost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Name', max_length=20)),
                ('email', models.CharField(default='Email', max_length=50)),
                ('message', models.CharField(default='message', max_length=500)),
            ],
        ),
    ]