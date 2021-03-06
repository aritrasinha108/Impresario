from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # path('',views.index,name="index"),
    path('userprofile/create_new_team/',views.create_new_team, name="new_team"),
    path('create_team/<int:par_id>', views.create_team, name="create_team"),
    path('team_request/<int:par_id>', views.team_request, name="team_request"),
    url(r'^ajax/approve_or_reject/$', views.ajax_change_status, name='ajax_change_status'),
    path('view_team/<int:team_id>', views.show_team,name = 'show_team'),
    path('<int:org_id>/add_event', views.add_event ,name = 'add_event'),
    path('edit_event/<int:event_id>', views.update_event ,name = 'edit_event'),
    path('view_event/<int:event_id>',views.view_event ,name = 'view_event'),
    path('calendar', views.view_calendar, name = "view_calendar")
]
