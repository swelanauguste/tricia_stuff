# Generated by Django 4.1.2 on 2022-10-04 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contracts", "0005_alter_contract_options_contract_contract_ended"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contract",
            name="contract_ended",
        ),
    ]
