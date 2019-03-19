# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from djang.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.core.urlresolvers import reverse
from django.views import generic
from groups.models import Group,GroupMember
# Create your views here.

class CreateGroup(LoginRequiredMixin,generic.CreateView):
    fields = ('name','description')
    models = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group




