# Generated by Django 3.1.5 on 2022-02-04 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Branch', '0004_auto_20220202_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='branch_product',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
