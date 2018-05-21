from django.conf.urls import url

from Api.common import *
from Api.resources import Register


api = Register()
api.regist(RegistCodeResource('regist_code'))
api.regist(UserResource('user'))
api.regist(SessionResource('session'))
