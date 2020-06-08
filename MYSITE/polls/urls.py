from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
	path('', views.index, name='index'),
	path('question/', views.IndexView.as_view(), name='index'),
	path('question/<int:pk>', views.DetailView.as_view(), name='detail'),
	path('question/<int:pk>/result/', views.ResultView.as_view(), name='result'),
	path('question/<int:question_id>/vote/', views.vote, name='vote'),
]

"""
 urlpatterns = [
	path('', views.index, name='index'),
	path('<int:question_id>', views.detail, name='detail'),
	path('<int:question_id>/result/', views.result, name='result'),
	path('<int:question_id>/vote/', views.vote, name='vote'),
] 
"""