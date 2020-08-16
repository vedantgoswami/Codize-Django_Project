from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns=[
	
	path('login',views.login,name="login"),
	path('register',views.register,name="register"),
	path('quizpage',views.quiz,name="quizpage"),
	path('selection',views.selection,name="selection"),
	path('logout',views.logout,name="logout"),
	path('get_data',views.get_data,name="get_data"),
	path('result',views.result,name="result"),
	path('logout',views.logout,name="logout")
]