from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page

from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView
from catalog.views import contacts, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    VersionCreateView, VersionUpdateView, ProductDeleteView
from send_emails import views
from send_emails.views import SmsLetterCreateView, SmsLetterUpdateView, SmsLetterDeleteView, \
    SmsLetterListView

app_name = 'catalog'

urlpatterns = [
                  path('create/', ProductCreateView.as_view(), name='create_product'),
                  path('update/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
                  path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
                  path('', cache_page(60)(ProductListView.as_view()), name='home'),
                  path('contacts/', contacts, name='contacts'),
                  path('view/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='goods'),
                  path('blog/', cache_page(60)(BlogListView.as_view()), name='list'),
                  path('create/', BlogCreateView.as_view(), name='create'),
                  path('view/<int:pk>', cache_page(60)(BlogDetailView.as_view()), name='view'),
                  path('edit/<int:pk>', BlogUpdateView.as_view(), name='edit'),
                  path('delete/<int:pk>', BlogDeleteView.as_view(), name='delete'),
                  path('create_version/', VersionCreateView.as_view(), name='create_version'),
                  path('catalog/<int:pk>/edit', VersionUpdateView.as_view(), name='edit_version'),
                  path('send_emails/', SmsLetterListView.as_view(), name='list_email'),
                  path("create/", SmsLetterCreateView.as_view(), name="create_send_email"),
                  path("edit/<int:pk>/", SmsLetterUpdateView.as_view(), name="update_send_email"),
                  path("delete/<int:pk>/", SmsLetterDeleteView.as_view(), name="delete_send_email"),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
