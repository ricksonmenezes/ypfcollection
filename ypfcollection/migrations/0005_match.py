# Generated by Django 2.0 on 2018-03-20 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ypfcollection', '0004_auto_20180319_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('match_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
