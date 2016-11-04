# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students_app', '0002_group_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='head',
            field=models.ForeignKey(verbose_name='head', blank=True, to='students_app.Student', null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='card_number',
            field=models.CharField(max_length=9, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='student_group',
            field=models.ForeignKey(verbose_name='student_group', blank=True, to='students_app.Group', null=True),
        ),
    ]
