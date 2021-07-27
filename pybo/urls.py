from django.urls import path

from pybo.views import base_views, question_views, answer_views, comment_views, vote_views

app_name = 'pybo'
# url 별칭 -> 네임 스페이스

urlpatterns = [
    #base_views.py
    # 인데스 메인
    path('', base_views.index, name='index'),
    # 질문/답변 게시판
    path('board/', base_views.board, name='board'),
    # 나의 프로필
    path('profile/', base_views.profile, name='profile'),
    # 상세 페이지
    path('<int:question_id>/', base_views.detail, name='detail'),

    #question_views.py
    # 질문 등록
    path('question/create/', question_views.question_create,
         name='question_create'),
    # 질문 수정
    path('question/modify/<int:question_id>/', question_views.question_modify,
         name='question_modify'),
    # 질문 삭제
    path('question/delete/<int:question_id>/', question_views.question_delete,
         name='question_delete'),
    #answer_views.py
    # 답변 등록
    path('answer/create/<int:question_id>/', answer_views.answer_create,
         name='answer_create'),
    # 답변 수정
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify,
         name='answer_modify'),
    # 답변 삭제
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete,
         name='answer_delete'),

    #vote_views.py
    # 질문 추천
    path('vote/question/<int:question_id>/', vote_views.vote_question,
         name='vote_question'),

    #답변 추천
    path('vote/answer/<int:answer_id>/', vote_views.vote_answer,
         name='vote_answer'),

    #comment_views.py
    # 질문 댓글 등록
    path('comment/create/question/<int:question_id>', comment_views.comment_create_question,
         name='comment_create_question'),
    # 질문 댓글 수정
    path('comment/modify/question/<int:comment_id>', comment_views.comment_modify_question,
         name='comment_modify_question'),
    #질문 댓글 삭제
    path('comment/delete/question/<int:comment_id>', comment_views.comment_delete_question,
         name='comment_delete_question'),
    #답변 댓글 등록
    path('comment/create/answer/<int:answer_id>', comment_views.comment_create_answer,
         name='comment_create_answer'),
    #답변 댓글 수정
    path('comment/modify/answer/<int:comment_id>', comment_views.comment_modify_answer,
         name='comment_modify_answer'),
    #답변 댓글 삭제
    path('comment/delete/answer/<int:comment_id>', comment_views.comment_delete_answer,
         name='comment_delete_answer'),

]