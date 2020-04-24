from django.urls import path
# from .views import BookmarkListView, BookmarkCreateView, BookmarkDetailView
from .views import *

urlpatterns = [
    # CBV 클래스 기반 뷰로 작성했기 때문에 .as_View()를 반드시 지정해야 함
    path('', BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),
]