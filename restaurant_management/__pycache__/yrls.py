from django.conf import settings
from django.conf.urls.static imoprt static

urlpatters=[

path('menu/',menu_view,name='menu'),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)