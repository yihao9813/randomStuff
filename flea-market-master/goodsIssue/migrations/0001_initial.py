# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsissueGoods',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, blank=True)),
                ('introduction', models.CharField(max_length=255, blank=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('imagefile', models.CharField(max_length=255, blank=True)),
                ('owner', models.ForeignKey(blank=True, null=True, to='login.LoginUser')),
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
                ('goods', models.ForeignKey(blank=True, null=True, to='goodsIssue.GoodsissueGoods')),
                ('uid', models.ForeignKey(blank=True, null=True, db_column='uid', to='login.LoginUser')),
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
                ('buyer', models.ForeignKey(blank=True, null=True, to='login.LoginUser')),
            ],
            options={
                'db_table': 'goodsissue_saler',
            },
        ),
    ]
