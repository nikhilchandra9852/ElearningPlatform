from django.urls import path
from .forms import ChatForm
from users import views
from django.urls import path,include
from django.contrib.auth import views as auth_views

#from django.contrib.staticfiles.urls import staticfiles_urlspatterns

urlpatterns = [

	path('',views.homepage,name='homepage'),
	path('rgt/',views.register,name='register'),
	path('oauth/', include('social_django.urls', namespace='social')),
	path('lgn/',views.login,name='lgn'),
	path('fp/',views.forgotpassword,name='fg'),
	path('forgot/<str:id>',views.forgot,name ='forgot'),
	path('check/',views.check,name='check'),
	path('dashboard/<str:id>',views.dashboard,name='dashboard'),
	path('courses/<str:id>/<str:branch>',views.courses,name='courses'),
	path('pdf/<str:id>/<str:branch>/<str:course>',views.pdf,name='pdf'),
	path('profile/<str:id>',views.profile,name='profile'),
	path('quiz/<str:id>/',views.quiz,name='quiz'),
	path('exam/<str:id>/<str:branch>',views.exam,name='exam'),
	path('quizexam/<str:id>/<str:branch>',views.quizexam,name='quizexam'),
	path('passwordchange/<str:id>',views.passchange,name='passwordchange'),
	path('chat/<str:id>',views.chat,name='base'),
	path('result/<str:id>/<str:branch>/<int:marks>/<str:percentage>',views.result,name='result')
]