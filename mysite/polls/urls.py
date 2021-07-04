from django.urls import path

import polls.apps
from . import views
app_label = polls.apps.PollsConfig.name
urlpatterns = [path('', views.requestlist, name='requestlist'), ]
