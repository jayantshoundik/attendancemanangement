# Generated by Django 3.0.5 on 2020-05-02 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0006_auto_20200502_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='leaveend',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='leave',
            name='leavestart',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
