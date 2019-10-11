from django.urls import path

from apps.base import views as base_views

urlpatterns = [
    # role
    path('role/', base_views.RoleView.as_view(), name="role_list"),
    path('role/<id>/', base_views.RoleView.as_view(), name="role_list"),
    # menu
    path('menu/', base_views.MenuView.as_view(), name="menu_list"),
    path('menu/<id>/', base_views.MenuView.as_view(), name="menu_list"),
    # user
    path('user/', base_views.UserView.as_view(), name="user_list"),
    path('user/<id>/', base_views.UserView.as_view(), name="user_list"),
    # userRole
    path('user_role/', base_views.UserRoleView.as_view(), name="user_role"),
    path('user_role/<user_id>/', base_views.UserRoleView.as_view(), name="user_role"),
    # roleMenu
    path('role_menu/', base_views.RoleMenuView.as_view(), name="role_menu"),
    path('role_menu/<role_id>/', base_views.RoleMenuView.as_view(), name="role_menu"),

    # userMenu
    path('user_menu/', base_views.UserMenuView.as_view(), name="user_menu"),

]
