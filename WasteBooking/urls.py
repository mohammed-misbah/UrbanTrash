from django.urls import path
from .views import WasteBookings, WasteOrderUpdatesAPI, WastePickupList,PickupListAPIView

urlpatterns = [ 
        path('waste_booking/', WasteBookings.as_view(), name='waste_booking'),
        path('pickup_detail/<int:id>',WastePickupList.as_view(),name='pickup-details'),
        path('pickup_detailist/', PickupListAPIView.as_view(), name='pick-details'),
        # path('order_detail/',WasteOrderDetailView.as_view(),name='order_detail'),
        path('pickup_update/<int:id>/',WasteOrderUpdatesAPI.as_view(),name='order-update'),
]

# class WasteOrderDetailView(APIView):
#     def post(self, request,order_detail_id):
#         try:
#             user = User.objects.get(id=order_detail_id)
#             orders = WasteOrderDetail.objects.filter(customer= user)
#             serializer = OrderDetailSerializer(orders, many=True)
#             return Response(serializer.data)
#         except APIException as e:
#             return Response({'Orderdetail': str(e)},
#                                 status=status.HTTP_400_BAD_REQUEST
#                         )
