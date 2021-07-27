from .models import Question, Answer, Comment
from django import forms

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question   # 폼 클래스의 객체
        fields = ['subject', 'content']
        labels = { # 레이블을 한글로 변경
            'subject' : '제목',
            'content' : '내용'
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels ={
            'content': '답변내용'
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용'
        }