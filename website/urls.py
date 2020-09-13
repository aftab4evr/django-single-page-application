from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from .views import *


urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'^delete-record/(?P<uuid>[0-9A-Za-z_\-]+)$', DeleteRecordView.as_view()),
    url(r'^get-record', GetRecordView.as_view()),
    url(r'^get-add-record', GetAddRecordPage.as_view()),
    url(r'^get-edit-record/(?P<uuid>[0-9A-Za-z_\-]+)', GetEditRecordPage.as_view()),
    url(r'^get-view-record/(?P<uuid>[0-9A-Za-z_\-]+)', GetViewRecordView.as_view()),


    url(r'^add-record', AddRecordView.as_view()),
    url(r'^edit-record', EditRecordView.as_view()),

    url(r'^.*',HandelAnyUrl.as_view()),





]