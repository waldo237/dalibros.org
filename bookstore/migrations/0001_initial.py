# Generated by Django 3.2 on 2021-04-29 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('pub_date', models.DateTimeField(verbose_name='date it was published')),
                ('condition', models.IntegerField()),
                ('reason_for_donation', models.CharField(max_length=400)),
                ('photo_url', models.CharField(max_length=100)),
                ('author', models.ManyToManyField(to='bookstore.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('rating', models.IntegerField()),
                ('province', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('joining_date', models.DateTimeField()),
                ('red_flag', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('rating', models.IntegerField()),
                ('province', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('joining_date', models.DateTimeField()),
                ('red_flag', models.IntegerField()),
                ('story', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.book')),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.donor')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.receiver')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genders',
            field=models.ManyToManyField(to='bookstore.Gender'),
        ),
    ]
