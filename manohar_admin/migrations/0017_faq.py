# Generated by Django 4.0.2 on 2022-02-25 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manohar_admin', '0016_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(default='Question', max_length=100)),
                ('answer', models.CharField(default='Answer', max_length=500)),
            ],
        ),
    ]