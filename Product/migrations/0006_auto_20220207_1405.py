# Generated by Django 3.1.5 on 2022-02-07 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0005_auto_20220204_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=150, verbose_name='size')),
                ('price', models.IntegerField(verbose_name='price')),
                ('description', models.CharField(max_length=150, verbose_name='size')),
            ],
            options={
                'verbose_name': 'Size',
                'verbose_name_plural': 'Sizes',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='null', max_length=150, verbose_name='description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(max_length=150, verbose_name='size'),
        ),
        migrations.AddField(
            model_name='product',
            name='multipleSIzes',
            field=models.ManyToManyField(blank=True, related_name='multiplesizes', to='Product.Size', verbose_name='multiplesizes'),
        ),
    ]
