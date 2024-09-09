from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('academics/', views.academics, name='academics'),
    path('admission/', views.admission, name='admission'),
    path('gallery/', views.gallery, name='gallery'),
    path('calculator/', views.calculator, name='calculator'),
    path('markCalculator/', views.markCalculator, name='markCalculator'),
    path('form/', views.form_view, name='form'),
    # path('submitform/', views.submitform, name='submitform'),
    path('course/<str:course_name>/', views.course_detail, name='course_detail'),
    path('academics/arts_english.html', views.arts_english, name='arts_english'),
    path('academics/arts_sociology.html', views.arts_sociology, name='arts_sociology'),
    path('academics/cs.html', views.cs, name='cs'),
    path('academics/science_mathematics.html', views.science_mathematics, name='science_mathematics'),
    path('academics/commerce_accounting.html', views.commerce_accounting, name='commerce_accounting'),
    path('academics/commerce_economics.html', views.commerce_economics, name='commerce_economics'),
]
