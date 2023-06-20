from django.urls import path
from .views import BioWastes, WasteCategoryAPIVIEW, WasteCategoryEditAPIVIEW, BioWasteEditAPIVIEW, WasteCategoryListAPIView, BioWasteListAPIView

urlpatterns = [
    path('wastecategory/', WasteCategoryAPIVIEW.as_view(), name='waste-category-detail'),
    path('wastecategorylist/<int:id>/', WasteCategoryListAPIView.as_view(), name='waste-category-list'),
    path('wastecatedit/<int:id>/',WasteCategoryEditAPIVIEW.as_view(), name='waste-category-edit'),
    path('biowaste/',BioWastes.as_view(), name='biowaste-list'),
    path('biowastedit/<int:id>/',BioWasteEditAPIVIEW.as_view(),name='biowaste-edit'),
    path('biowastelist/',BioWasteListAPIView.as_view(),name='biowaste-list')
]   
