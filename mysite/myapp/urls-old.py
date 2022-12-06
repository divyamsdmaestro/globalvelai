from django.urls import include, path

from .views import (
    UserCreateView, CreateUserView, AddUser, UpdateUserView, ListUserView, DeleteUserView, UpdateUserView, DetailUserView, CreateTag, LinkUsertoTag, CreateUserModelViewset,
)

urlpatterns = [

    path('usercreate/', UserCreateView.as_view(), name='usercreate'),
    path('usercreatetest/', CreateUserView.as_view(), name='usercreatetest'),
    # path('useradd/', AddUser.as_view(), name='useradd'),
    path('userupdatetest/<int:id>/', UpdateUserView.as_view(), name='userupdatetest'),
    path('userlisttest/', ListUserView.as_view(), name='userlisttest'),
    path('userdeletetest/<int:id>/', DeleteUserView.as_view(), name='userdeletetest'),
    path('userdetailstest/<int:id>/', DetailUserView.as_view(), name='userdetailstest'),
    path('createtag/', CreateTag.as_view(), name='createtag'),
    path('linkusertotag/<int:id>/', LinkUsertoTag.as_view(), name='linkusertotag'),
    path('createmodeluser/', CreateUserModelViewset.as_view({'get': 'list'}), name='createmodeluser'),
    path('retrievemodeluser/<pk>/', CreateUserModelViewset.as_view({'get': 'retrieve'}), name='retrievemodeluser'),
    path('listcreatemodeluser/', CreateUserModelViewset.as_view({'get': 'create'}), name='listcreatemodeluser'),
    path('deletemodeluser/<pk>/', CreateUserModelViewset.as_view({'get': 'destroy'}), name='deletemodeluser'),
    # path('updatemodeluser/<pk>/', CreateUserModelViewset.as_view({'get': 'update'}), name='updatemodeluser'),
]
