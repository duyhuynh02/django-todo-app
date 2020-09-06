from django.urls import path 


from .views import HomePageView, WorkCreateView, WorkDetailView, WorkUpdateView, WorkDeleteView


urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('work/<int:pk>', WorkDetailView.as_view(), name='work_detail'),
	path('work/<int:pk>/edit/', WorkUpdateView.as_view(), name='work_edit'),
	path('work/<int:pk>delete/', WorkDeleteView.as_view(), name='work_delete'),
	path('new/', WorkCreateView.as_view(), name='work_new'),
]