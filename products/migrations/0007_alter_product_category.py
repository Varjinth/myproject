# Generated by Django 4.1.6 on 2023-02-03 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_category_category_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='unknown', on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
    ]