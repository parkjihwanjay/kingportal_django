from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from .models import Chats
from .forms import ChatsForm
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
