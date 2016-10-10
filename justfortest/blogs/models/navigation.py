# -*- coding: utf-8 -*-2
from django.db import models
from django.contrib import admin


class Navigation(models.Model):
    title = models.CharField(max_length=320)
    href = models.CharField(max_length=320)

    @classmethod
    def create(cls, title, href):
        navigation = cls(
            title=title, href=href
        )
        return navigation

    class Meta:
        db_table='navigation'

Navigation.create('Домой','/')
Navigation.create('Посты','/posts/')

class NavigationAdmin(admin.ModelAdmin):
    list_display = ('title','href')