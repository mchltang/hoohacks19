# Generated by Django 2.1.7 on 2019-03-03 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naps', '0003_auto_20190303_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='spot',
            name='latitude',
            field=models.FloatField(default=38.033595),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spot',
            name='longtitude',
            field=models.FloatField(default=78.507976),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='noise',
            name='level',
            field=models.CharField(max_length=7),
        ),
    ]
