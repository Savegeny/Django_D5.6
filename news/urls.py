from django.urls import path
from .views import PostList, PostDetailView, PostAddView, PostUpdateView, PostDeleteView, PostSearch, IndexView, BaseRegisterView, upgrade_me
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', IndexView.as_view()),
    path('upgrade/', upgrade_me, name='upgrade'),

    path('news/', PostList.as_view()),
    path('news/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('news/add/', PostAddView.as_view(), name="post_add"),
    path('news/add/<int:pk>/', PostUpdateView.as_view(), name="post_update"),
    path('news/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('news/search/', PostSearch.as_view(), name="post_search"),

    path('about/', LoginView.as_view(template_name='flatpages/about_page.html'), name='about'),

    path('login/', LoginView.as_view(template_name='news_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='news_app/logout.html'), name='logout'),
    path('signup/', BaseRegisterView.as_view(template_name='news_app/signup.html'), name='signup')
]