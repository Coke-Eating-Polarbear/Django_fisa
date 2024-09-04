from .models import Comment
from django import forms

# 커스텀한 폼을 사용하기 위한 클래스
class CommentForm(forms.ModelForm):
    class Meta:  # 추가적인 정보들을 달아서 보낼 때 사용하는 클래스
        model = Comment
        fields = ['content']