# Generated by Django 2.1.7 on 2019-03-03 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('naps', '0004_auto_20190303_0203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spot',
            name='pub_date',
        ),
    ]