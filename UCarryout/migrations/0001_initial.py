# Generated by Django 2.1.1 on 2018-09-09 21:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('price', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=255)),
                ('calories', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
                ('zip_code', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('food', models.ManyToManyField(related_name='menus', related_query_name='menu', to='UCarryout.Food')),
            ],
        ),
        migrations.CreateModel(
            name='MenuType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='OperationHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_hour', models.CharField(max_length=5)),
                ('close_hour', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='OrderHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PriceIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('average_price', models.CharField(max_length=50)),
                ('hours', models.CharField(max_length=50)),
                ('location', models.ManyToManyField(related_name='locations', related_query_name='location', to='UCarryout.Location')),
                ('menu', models.ManyToManyField(related_name='menus', related_query_name='menu', to='UCarryout.Menu')),
            ],
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='UCarryout.Restaurant'),
        ),
        migrations.AddField(
            model_name='menu',
            name='type',
            field=models.ManyToManyField(related_name='menus', related_query_name='menu', to='UCarryout.MenuType'),
        ),
        migrations.AddField(
            model_name='food',
            name='category',
            field=models.ManyToManyField(related_name='food_category', related_query_name='food_category', to='UCarryout.FoodCategory'),
        ),
        migrations.AddField(
            model_name='clientuser',
            name='order_history',
            field=models.ManyToManyField(to='UCarryout.OrderHistory'),
        ),
        migrations.AddField(
            model_name='clientuser',
            name='permission',
            field=models.ManyToManyField(to='auth.Permission'),
        ),
        migrations.AddField(
            model_name='clientuser',
            name='restaurant',
            field=models.ManyToManyField(to='UCarryout.Restaurant'),
        ),
        migrations.AddField(
            model_name='clientuser',
            name='user_auth',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
