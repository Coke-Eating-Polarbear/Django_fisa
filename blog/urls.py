from django.urls import path
from . import views

# 앞으로 현재 프로젝트 내에서 blog/ 안에 있는 경로는 모두 blog_app
app_name= 'blog_app'  # blog_app:blog  -> localhost:8000/blog/post-list
# url 'blog_app:about_me'  localhost:8000/blog/about-me 
urlpatterns = [
    # blog 앱 내부의 경로를 지정할 부분
    # path('', views.index), # localhost:8000/blog 경로, 경로를 호출하면 실행할 함수의 위치
    path('post-list/', views.PostList.as_view(paginate_by=5), name='post_list'), #  name= 개발자가 이 주소를 부를 이름
    path('', views.about_me, name='about_me'), # blog_app:about_me     blog/
    path('<int:pk>/', views.PostDetail.as_view()), # <자료형:필드명> 
    path('create-post/', views.PostCreate.as_view(), name="create"),  # blog_app:create
    # update, delete는 이미 있는 글을 수정/삭제하므로 글번호가 필요합니다. 
    path('edit-post/<int:pk>', views.PostUpdate.as_view(), name='update'),
    path('delete-post/<int:pk>', views.PostDelete.as_view(), name='delete'),



    path('user-delete/', views.user_delete, name='user_delete'), # blog_app:user_delete
    # 같은 tag를 가진 글끼리 게시판에 보여주기
    path('tag/<str:slug>/', views.tag_posts, name="tag"), # <자료형:필드명> 

    # 댓글은 글에 딸려있습니다.
    # 댓글 조회 -> post-detail.html 안에서 동작하도록
    # 댓글 작성 - 글의 번호 blog/30/
    path('<int:pk>/create-comment', views.create_comment, name='create_comment'),
    # 댓글 수정 - 댓글의 번호
    path('update-comment/<int:pk>', views.CommentUpdate.as_view(), name='update_comment'),
    # 댓글 삭제
    path('delete-comment/<int:pk>',  views.delete_comment, name='delete_comment'),

    # 검색을 위한 주소
    path("search/<str:q>/", views.PostSearch.as_view(), name="post_search"),
]