# -*- encoding: utf-8 -*-
"""
This module contains the models for NXT LVL
"""
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import FieldError
from django.db import models
from django.utils.translation import ugettext_lazy as _

from students.settings import AUTH_USER_MODEL


# import logging


class UserNxtlvl(AbstractUser):

    def save(self, *args, **kwargs):
        if self.email and self.id is None:
            if get_user_model().objects.filter(email=self.email).count() > 0:
                raise FieldError('User %s already exists' % self.email)
        if self.email and self.id is not None:
            if get_user_model().objects.filter(email=self.email).exclude(id=self.id):
                raise FieldError('User email %s already exists' % self.email)
        return super(UserNxtlvl, self).save(*args, **kwargs)


class CreatedAbstract(models.Model):
    created_at = models.DateTimeField(verbose_name=_(u"created at"), auto_now_add=True)
    created_by = models.ForeignKey(AUTH_USER_MODEL, verbose_name=_(u"created by"),
                                   related_name='%(class)s_created_by', blank=True,
                                   null=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True


class UpdatedAbstract(models.Model):
    updated_at = models.DateTimeField(verbose_name=_(u"updated at"), auto_now=True)
    updated_by = models.ForeignKey(AUTH_USER_MODEL, verbose_name=_(u"updated by"),
                                   related_name='%(class)s_updated_by', blank=True,
                                   null=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True


class Employee(CreatedAbstract, UpdatedAbstract):
    """
    Employee in a company
    """
    user = models.OneToOneField(AUTH_USER_MODEL, related_name='employee_user', verbose_name=_("user"))
    phone = models.CharField(verbose_name=_(u"phone"), max_length=40, default='')
    notes = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return u'<{} (id: {})>'.format(self.user.username, self.id)

    class Meta:
        verbose_name = _(u'employee')
        verbose_name_plural = _(u'employees')


class EmployeeMailReminder(CreatedAbstract, UpdatedAbstract):
    """
    MailReminder for yourself
    """
    title = models.TextField(verbose_name=_(u"mail reminder title"), null=True)
    description = models.TextField(verbose_name=_(u"description"), default='')
    employee = models.ForeignKey(Employee, verbose_name=_(u"employee"))
    reminder_date = models.DateTimeField(verbose_name=_(u"reminder date"), auto_now=False)
    # employee = models.ForeignKey(Employee, related_name="goals")
    is_achieved = models.BooleanField(default=False)

    def __unicode__(self):
        return u'<{} (id: {})>'.format(self.title, self.id)

    class Meta:
        verbose_name = _(u'employee mail reminder')
        verbose_name_plural = _(u'employee mail reminders')