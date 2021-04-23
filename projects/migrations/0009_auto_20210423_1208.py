# Generated by Django 3.1.6 on 2021-04-23 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20210423_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='latitude',
            field=models.DecimalField(decimal_places=16, max_digits=22, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='longitude',
            field=models.DecimalField(decimal_places=16, max_digits=22, null=True),
        ),
    ]
