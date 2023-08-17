from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from usuario.router import router as usuario_router
from django.conf import settings
from django.conf.urls.static import static
from uploader.router import router as uploader_router

from garagem.views import (
    AcessorioViewSet,
    CategoriaViewSet,
    CorViewSet,
    MarcaViewSet,
    VeiculoViewSet,
    ModeloViewSet,
)

router = DefaultRouter()
router.register(r"acessorios", AcessorioViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"cors", CorViewSet)
router.register(r"modelos", ModeloViewSet)
router.register(r"marcas", MarcaViewSet)
router.register(r"veiculos", VeiculoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/usuario", include(usuario_router.urls)),
    path("api/media/", include(uploader_router.urls)),

]
