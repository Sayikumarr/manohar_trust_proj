# Generated by Django 4.0.2 on 2022-02-23 12:07

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('manohar_admin', '0004_rename_sponsers_event_vol_spon_count_sponsers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poster',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to=''),
        ),
    ]