from django.urls import path
from lab_clg import views
 
urlpatterns = [
    path("",views.signaction,name="signaction"),
    path("loginaction/",views.loginaction,name="loginaction"),
    path("addbook/",views.addbook,name="addbook"),
    path("dashborad/",views.dashborad,name="dashborad"),
    path("updatedetails/",views.updatedetails,name="updatedetails"),
    path("deletebook/",views.deletebook,name="deletebook"),
    path('editbookdetails/<int:id>',views.editbookdetails,name='editbookdetails'),

]