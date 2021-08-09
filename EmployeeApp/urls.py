from django.conf.urls import url
from EmployeeApp import views

urlpatterns = [
    url(r'^department$',views.departmentApi),
    url(r'^department/([0-9]+)$',views.departmentApi)
]

def miPruebaEnVim():
    print("Todo lo que quieras imprimir, sirvete papá")
