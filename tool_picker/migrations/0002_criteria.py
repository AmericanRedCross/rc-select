# Generated by Django 5.0 on 2023-12-11 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool_picker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Criteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('case_management', models.BooleanField()),
                ('fsp_integration', models.BooleanField()),
                ('sms', models.BooleanField()),
                ('biometrics', models.BooleanField()),
                ('customized_workflows', models.BooleanField()),
                ('setup_speed', models.IntegerField()),
                ('setup_complexity', models.IntegerField()),
                ('maintenance_complexity', models.IntegerField()),
                ('training_and_support', models.IntegerField()),
                ('transition', models.IntegerField()),
                ('performance', models.IntegerField()),
                ('connectivity', models.IntegerField()),
                ('data_cleaning', models.IntegerField()),
                ('data_viz', models.IntegerField()),
                ('data_management_policies', models.IntegerField()),
                ('interoperability', models.IntegerField()),
                ('localization', models.IntegerField()),
                ('data_security', models.IntegerField()),
            ],
        ),
    ]