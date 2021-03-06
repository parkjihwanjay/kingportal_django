from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from .models import Chats, Nicks
from .forms import ChatsForm, NicksForm
# from django.views.decorators.csrf import ensure_csrf_cookie
# from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


def Main(request):
    return render(request, 'main.html')


@csrf_exempt
def Chat(request):
    # try:
    if request.method == 'POST':
        # print(request.POST)
        form = ChatsForm(request.POST)
        one_chat = form.save(commit=False)
        # one_chat.content = request.POST['content']
        one_chat.course = str(request.POST['course'])
        one_chat.author = str(request.POST['author'])
        one_chat.time = str(request.POST['time'])
        one_chat.save()
        return HttpResponse('글쓰기 완료', status=200)
    if request.method == 'GET':
        course_chats = Chats.objects.filter(
            course=request.GET['course_id'])
        json_course_chats = []
        for course_chat in course_chats:
            append_chat = {
                'content': course_chat.content,
                'author': course_chat.author,
                'time': course_chat.time,
                'course': course_chat.course
            }
            json_course_chats.append(append_chat)
        returnjson = json.dumps(json_course_chats)
        # return JsonResponse(returnjson, status=200)
        return HttpResponse(returnjson, content_type=u"application/json; charset=utf-8", status=200)
    # except:
    #     return HttpResponse('에러 발생', status=400)


@csrf_exempt
def Nick(request):
    # try:
    if request.method == 'POST':
        # duplicate check
        chat_nicks = Nicks.objects.filter(
            name=request.POST['name'])
        # print(chat_nicks)
        # print(len(chat_nicks))
        if len(chat_nicks) > 0:
            return HttpResponse('중복', status=200)
        form = NicksForm(request.POST)
        one_nick = form.save(commit=False)
        one_nick.sid = str(request.POST['sid'])
        one_nick.save()
        return HttpResponse('닉네임 완료', status=200)
    if request.method == 'GET':
        chat_nicks = Nicks.objects.filter(
            sid=request.GET['sid'])
        json_chat_nicks = []
        for chat_nick in chat_nicks:
            append_chat = {
                'name': chat_nick.name,
                'sid': chat_nick.sid,
            }
            json_chat_nicks.append(append_chat)
        returnjson = json.dumps(json_chat_nicks)
        return HttpResponse(returnjson, content_type=u"application/json; charset=utf-8", status=200)
    # except:
    #     return HttpResponse('에러 발생', status=400)
