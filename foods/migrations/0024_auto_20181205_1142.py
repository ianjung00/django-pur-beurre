# Generated by Django 2.1.2 on 2018-12-05 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0023_auto_20181205_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='countries_fr',
            field=models.CharField(max_length=255, null=True),
        ),
    ]