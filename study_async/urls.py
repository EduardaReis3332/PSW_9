from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('flashcard/', include('flashcard.urls')),
    path('apostilas/', include('apostilas.urls')),
    path('', lambda request: redirect('/flashcard/novo_flashcard'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
