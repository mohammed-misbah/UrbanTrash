from django.urls import path
from .views import  ScrapCategoryAPIView, ScrapWastes, ScrapCategoryEditAPIVIEW, ScrapCategoryListAPIView, ScrapWasteListAPIView, ScrapWasteEditAPIView

urlpatterns = [
    path('scrapcategory/', ScrapCategoryAPIView.as_view(), name='waste-category-detail'),
    path('scrapcategoryedit/<int:id>/',ScrapCategoryEditAPIVIEW.as_view(),name='scrapcategory-edit'),
    path('scrapcategorylist/<int:id>/',ScrapCategoryListAPIView.as_view(), name='scrapcategory-list'),
    path('scrapwaste/', ScrapWastes.as_view(), name='scrapwaste'),
    path('scrapwastedit/<int:id>/',ScrapWasteEditAPIView.as_view(), name='scrapwaste-edit'),
    path('scrapwastelist/',ScrapWasteListAPIView.as_view(),name='scrapwaste-list'),
]



    # path('scrap-categories/', ScrapCategoryAPIView.as_view(), name='scrap-category-list'),
    # path('scrap-categories/<int:pk>/', ScrapCategoryDetailAPIView.as_view(), name='scrap-category-detail'),
    # path('scraps/', ScrapAPIView.as_view(), name='scrap-list'),
    # path('scrapss/<int:pk>/', ScrapDetailAPIView.as_view(), name='scrap-detail')