
from django.contrib import admin
from django.urls import path
from deals.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('categories/', CategoryView, name="categories-list"),
    path('categories-create/', CategoryCreate, name="categories-create"),

    
    path('subcategories/', SubcategoryView, name="sub-categories-list"),
    path('subcategories-create/', SubcategoryCreate, name="sub-categories-create"),

    
    path('companies/', CompanyView, name="companies-list"),
    path('companies-create/', CompanyCreate, name="companies-create"),



    path('broadband/', BroadbandView, name="broadband-list"),
]



if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)