# Generated by Django 5.0.2 on 2024-03-23 09:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField(null=True)),
                ('status', models.CharField(choices=[('In Stock', 'In Stock'), ('Out Stock', 'Out Stock')], max_length=100)),
                ('stock_count', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='products/')),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('trending', models.BooleanField(default=False)),
                ('product_details', models.TextField(blank=True, null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Brand_name', to='category.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_name', to='category.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='additional_images', to='products.products')),
            ],
        ),
        migrations.CreateModel(
            name='product_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1)),
                ('Title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='products.products')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(null=True)),
                ('stock_count', models.IntegerField(default=0)),
                ('size', models.CharField(blank=True, max_length=50, null=True)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_variants', to='products.products')),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='variants',
            field=models.ManyToManyField(blank=True, related_name='products', to='products.productvariant'),
        ),
        migrations.CreateModel(
            name='VariantImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='variant_images')),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='products.productvariant')),
            ],
        ),
    ]