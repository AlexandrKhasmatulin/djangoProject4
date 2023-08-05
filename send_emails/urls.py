from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import send_emails
from send_emails import views
from send_emails.apps import Send_EmailsConfig
from send_emails.views import SmsLetterDeleteView, SmsLetterUpdateView, SmsLetterCreateView, \
    SmsLetterListView, catalog

app_name = send_emails

urlpatterns = [
    path('', SmsLetterListView.as_view(), name='list_email'),
    path("catalog/<int:pk>", catalog, name='catalog'),
    path("create/", SmsLetterCreateView.as_view(), name="create_send_email"),
    path("edit/<int:pk>/", SmsLetterUpdateView.as_view(), name="update_send_email"),
    path("delete/<int:pk>/", SmsLetterDeleteView.as_view(), name="delete_send_email"),
    path('send_email/', views.send_email, name='send_email'),
    path('index/', views.index, name='index'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)