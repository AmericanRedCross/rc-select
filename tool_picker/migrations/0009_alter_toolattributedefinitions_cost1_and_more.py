# Generated by Django 5.0 on 2023-12-18 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool_picker', '0008_rename_cost_toolattributedefinitions_cost1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toolattributedefinitions',
            name='cost1',
            field=models.TextField(default='Not specified.', null=True),
        ),
        migrations.AlterField(
            model_name='toolattributedefinitions',
            name='cost2',
            field=models.TextField(default='Not specified.', null=True),
        ),
        migrations.AlterField(
            model_name='toolattributedefinitions',
            name='cost3',
            field=models.TextField(default='Not specified.', null=True),
        ),
        migrations.AlterField(
            model_name='toolattributedefinitions',
            name='cost4',
            field=models.TextField(default='Not specified.', null=True),
        ),
        migrations.AlterField(
            model_name='toolattributedefinitions',
            name='cost_def',
            field=models.TextField(default='Not specified.', null=True),
        ),
    ]