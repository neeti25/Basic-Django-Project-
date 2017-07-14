# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class InfoConfig(AppConfig):
    name = 'info'
    def ready(self):
        UserInfo = self.get_model('UserInfo')
        algoliasearch.register(UserInfo)
