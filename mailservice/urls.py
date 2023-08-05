from django.urls import path, include

import send_emails
from send_emails import views
#from send_emails.apps import LatterConfig
from send_emails.views import SmsLetterDeleteView, SmsLetterUpdateView, SmsLetterCreateView, catalog, \
    smslatters, SmsLetterListView

app_name = send_emails

urlpatterns = [
    path('', SmsLetterListView.as_view(), name='list_email'),
    path("catalog/<int:pk>", catalog, name='catalog'),
    path("create_email/", SmsLetterCreateView.as_view(), name="create_email"),
    path("edit_email/<int:pk>/", SmsLetterUpdateView.as_view(), name="update_email"),
    path("delete_email/<int:pk>/", SmsLetterDeleteView.as_view(), name="delete_email"),
    path('send_email/', views.send_email, name='send_email'),
    path('index/', views.index, name='index'),
    ]