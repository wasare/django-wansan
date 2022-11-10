from django.urls import path

from blog.views import (
	index, ola, 
	post_detail, 
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView
  )  # Nesta linha importamos as views 


urlpatterns = [
	path('index/', index, name= "index"),
	path('ola-mundo/', ola, name="ola"),
	path('posts/all', ola, name="posts_list"), # a view responsável é ola()
	path('post/<int:post_id>/show', post_detail, name="show_post"),
	path('post-detail/<int:pk>', PostDetailView.as_view(), name="post_detail"),
	path('post/novo', PostCreateView.as_view(), name="post_add"),
	path('post/<int:pk>/edit', PostUpdateView.as_view(), name="post_edit"),
	path('post/<int:pk>/delete', PostDeleteView.as_view(), name="post_delete"),

]
