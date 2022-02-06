# Generated by Django 3.1.5 on 2022-02-04 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_auto_20220203_1002'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bad_product',
            options={'ordering': ['-date'], 'verbose_name': 'Bad_Product', 'verbose_name_plural': 'Bad_Products'},
        ),
        migrations.AlterField(
            model_name='bad_product',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product_type',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='returned_product',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
