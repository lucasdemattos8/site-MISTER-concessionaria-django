from django.urls import path
from app_Concessionaria import views

from django.contrib import admin  # Adicione esta importação


from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('servicos/', views.servico, name='servicos'),
    path('quem_somos/', views.quemSomos, name='quemSomos'),
    path('compra/<uuid:carro_id>/', views.detalhe_carro, name='detalhe_carro'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
