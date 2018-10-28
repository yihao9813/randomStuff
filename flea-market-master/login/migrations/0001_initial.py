# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsissueGoods',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, blank=True)),
                ('size', models.FloatField(blank=True, null=True)),
                ('material', models.CharField(max_length=255, blank=True)),
                ('introduction', models.CharField(max_length=255, blank=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('imagefile', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'goodsissue_goods',
            },
        ),
        migrations.CreateModel(
            name='GoodsissueIssuer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('issuedate', models.DateTimeField(blank=True, null=True, db_column='issueDate')),
                ('goods', models.ForeignKey(blank=True, null=True, to='login.GoodsissueGoods')),
            ],
            options={
                'db_table': 'goodsissue_issuer',
            },
        ),
        migrations.CreateModel(
            name='GoodsissueSaler',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('goods_id', models.IntegerField(blank=True, null=True)),
                ('tradedate', models.DateTimeField(blank=True, null=True, db_column='tradeDate')),
            ],
            options={
                'db_table': 'goodsissue_saler',
            },
        ),
        migrations.CreateModel(
            name='LoginUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=255, blank=True)),
                ('passwd', models.CharField(max_length=255, blank=True)),
                ('name', models.CharField(max_length=255, blank=True)),
                ('phone', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'login_user',
            },
        ),
        migrations.AddField(
            model_name='goodsissuesaler',
            name='buyer',
            field=models.ForeignKey(blank=True, null=True, to='login.LoginUser'),
        ),
        migrations.AddField(
            model_name='goodsissueissuer',
            name='uid',
            field=models.ForeignKey(blank=True, null=True, db_column='uid', to='login.LoginUser'),
        ),
        migrations.AddField(
            model_name='goodsissuegoods',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, to='login.LoginUser'),
        ),
    ]
