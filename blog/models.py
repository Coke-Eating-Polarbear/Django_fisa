from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

# Tag table 작성 - pk는 자동 생성됨
class Tag(models.Model):
    tag_name = models.CharField(max_length=30, unique=True)
    # 짧은 라벨로서, 문자, 숫자, 밑줄 또는 하이픈만을 포함. 일반적으로 URL에 사용.  
    slug = models.SlugField(max_length=30, unique=True, allow_unicode=True)

    def __str__(self):
        return self.tag_name
    
    def get_absolute_url(self): 
        return f'/blog/tag/{self.slug}'


# Create your models here.
# models모듈의 Model 클래스를 상속받는 자식클래스 생성
# 게시글에 필요한 필드는 무엇무엇일까요
class Post(models.Model): 
    title = models.CharField(max_length=50)
    content = models.TextField()
		
	# django model 이 최초 저장(insert) 시에만 현재날짜(date.today()) 를 적용
    # 아예 값 자체가 지금 시간으로 입력되어 들어감(우리가 변경할 필요 없음)
    created_at = models.DateTimeField(auto_now_add=True) # now()
	# django model 이 save 될 때마다 현재날짜(date.today()) 로 갱신됨
    updated_at = models.DateTimeField(auto_now=True) 

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    
    # 외래키와 프라이머리키의 관계
    # CASCADE - User가 삭제되면 관련있는 Post 테이블의 모든 글이 삭제
    # SET_NULL - User가 삭제되면 관련있는 Post 테이블의 모든 글에 author 항목은 NULL로 바뀜
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(Tag)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'[[{self.pk}] {self.title}]'
		
    def get_absolute_url(self): 
        return f'/blog/{self.pk}'

    def get_file_extension(self):
        return f'{self.file_upload}'.split('.')[-1]



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # 하나의 포스트에 여러개의 댓글 관계
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 여러 사람이 하나의 댓글창에 댓글 구현 가능
    content = models.TextField()
    
    # 아예 값 자체가 지금 시간으로 입력되어 들어감(우리가 변경할 필요 없음)
    created_at = models.DateTimeField(auto_now_add=True) # now()
	# django model 이 save 될 때마다 현재날짜(date.today()) 로 갱신됨
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f'[[{self.pk}] {self.content}]'
		
    def get_absolute_url(self): 
        return f'{self.post.get_absolute_url()}#comment-{self.pk}' # #을 단 이유 : html에서 ID 