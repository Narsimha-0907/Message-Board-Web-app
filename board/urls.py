from django.urls import path
from .views import (
    MessageListView,
    MessageDetailView,
    MessageCreateView,
    MessageUpdateView,
    MessageDeleteView
)

urlpatterns = [
    path('', MessageListView.as_view(), name='message_list'),
    path('<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('new/', MessageCreateView.as_view(), name='message_create'),
    path('<int:pk>/edit/', MessageUpdateView.as_view(), name='message_update'),
    path('<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),
]