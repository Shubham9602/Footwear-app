# Generated by Django 4.2.6 on 2023-11-01 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footapp', '0003_alter_products_cat_alter_products_pdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='pimage',
            field=models.ImageField(default=0, upload_to='image'),
            preserve_default=False,
        ),
    ]
