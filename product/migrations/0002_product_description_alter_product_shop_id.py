# Generated by Django 4.1 on 2022-08-15 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='shop_id',
            field=models.IntegerField(null=True),
        ),
    ]
