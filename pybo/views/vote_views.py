from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404

from pybo.models import Question, Answer


@login_required(login_url='common:login')
def vote_question(request, question_id):
    # 질문 추천
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:  #로그인한 사람 == 질문 글쓴이
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
    else:
        question.voter.add(request.user)
    return redirect('pybo:detail', question_id=question.id)


@login_required(login_url='comment:login')
def vote_answer(request, answer_id):
    #답변 추천 등록
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
    else:
        answer.voter.add(request.user)
    return redirect('pybo:detail', question_id=answer.question.id)