from django.contrib import admin
from django.urls import path,include
from Todo import views

#####################
#django admin customization
#
# django admin heder  costumization
admin.site.site_header = "SAI-Tasks"
admin.site.site_title = "Tasks-dashboard"
admin.site.index_title = "patience and focus leads to sucsses"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('list/', views.todoList, name='about')
]