# encoding: utf-8

from django.contrib import admin

from models import Rhythm, Level, DanceStep

admin.site.register([Rhythm, Level, DanceStep])