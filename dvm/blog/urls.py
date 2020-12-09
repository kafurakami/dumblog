from django.urls import path
from .views import homeview, detailview, addpostview, updatepostview, deletepostview, commentview

urlpatterns = [
    path('',homeview.as_view(), name = 'homepage'),
    path('article/<int:pk>',detailview.as_view(), name = 'detail'),
    path('add_post/', addpostview.as_view(), name = 'addpostpage'),
    path('update/<int:pk>', updatepostview.as_view(), name = 'updatepage'),
    path('article/<int:pk>/delete', deletepostview.as_view(), name = 'deletepage'),
    path('article/<int:pk>/comment', commentview.as_view(), name = 'commentpage')
]
