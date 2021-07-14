from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from django.utils import timezone

def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list' : question_list}
    return render(request, 'pybo/question_list.html' ,context)
    #return HttpResponse("Welcome!! pybo에 오신 것을 환영합니다.")
    #'-'기호는 내림차순 정렬

def detail(request, question_id):
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context ={'question' : question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'),
                               create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)