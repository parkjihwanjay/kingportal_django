from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from .models import User, ApplyList
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
import time
import json
# apply_list = ApplyList.objects.create()
# apply_list.save()
# Create your views here.

@csrf_exempt
def hashing(request):
    try:
        # 우선 정보가 있는지 체크
        check_user = User.objects.get(student_id=request.POST['student_id'])
        # 정보가 있는데, 해시토큰이 없다면
        if 'hash_token' not in request.POST:
            # 해시토큰을 내려준다
            return HttpResponse(check_user.hash_token, status=404)
        # 정보가 있고, 해시 토큰이 있다면 체크한다
        if request.POST['hash_token'] != check_user.hash_token:
            return HttpResponse('요청 거부', status=404)
        return HttpResponse('인증 성공', status=200)
        # 진행
    except:
        # 정보가 없는데 해시토큰과 함께 리퀘스트가 오면 그냥 거부
        if 'hash_token' in request.POST:
            return HttpResponse('요청 거부', status=404)
        # 정보가 없이 sid만 리퀘스트로 오면 만들어서 내려줌
        user = User.objects.create(
            student_id=request.POST['student_id'],
            hash_token=make_password(time.time())
        )
        user.save()
        return HttpResponse(user.hash_token, status=200)

def convert_to_float(x):
    y = x.split(':')
    # print(float(y[0]))
    return float(y[0])


def only_analyze(entire_student_info, target_student_info):
    print('entire_student_info : ', entire_student_info)

    entire_student_list = entire_student_info.split(',')
    try:
        #    index = entire_student_list.index('')
        entire_student_list.remove('')
    except:
        pass
    print('entire_student_list: ', entire_student_list)

    entire_student_list = sorted(
        entire_student_list, reverse=True, key=convert_to_float)

    is_swapped = False
    index = 0
    count = 0
    gpa_sum = 0

    # entire_student_info = ','.join(entire_student_list)
    print('entire_student_list : ', entire_student_list)
    print('target_student_info : ', target_student_info)

    for i in range(len(entire_student_list)):
        entire_s_list = entire_student_list[i].split(':')
        target_s_info = target_student_info.split(':')
        current_gpa = float(entire_s_list[0])
        target_gpa = float(target_s_info[0])
        print(target_s_info)
        count += 1
        gpa_sum += current_gpa
        if current_gpa == target_gpa and entire_s_list[3] == target_s_info[-1].strip() and entire_s_list[1] == target_s_info[1]:
            index = count
        entire_student_list[i] = entire_student_list[i].split(':')
    print('entire_list : ', entire_student_list)

    data = {
        'index': index,
        'applicants_number': count,
        'average_gpa': round(gpa_sum / count, 2),
        'entire_student_list': entire_student_list,
    }
    print('data',  data)
    # print('entier_student_info :', entire_student_info)
    return data

@csrf_exempt
def getInfo(request):
    # print(request.POST)
    # print('student_id : ', student_id)
    student_id = request.POST['student_id'].strip()
    try:
        user = User.objects.get(student_id=student_id)
        # user = User.objects.get(student_id = '2008130419')
        # 진행
    except:
        # 회원가입 후 진행
        user = User(student_id=student_id)
        # user = User(student_id='2008130419')
        user.save()
    apply_major_list = user.apply_major_list.split(',')

    # 지원자 학점
    average_gpa = format(round(float(request.POST['average_gpa'].strip()), 2), '.2f')
    # average_gpa = '3.10'

    # 지원전공
    # apply_major = request.POST['apply_major']
    # apply_major = 'geographic_education'
    # apply_major_ko = request.POST['apply_major_ko']

    # user.apply_major_list = user.apply_major_list + f'apply_major_en:apply_major_ko'

    # 본 전공
    main_major = request.POST['main_major']
    # main_major = '심리학과'

    apply_list = ApplyList.objects.get()
    target_student_info = f'{average_gpa}:{student_id[:4]}:{main_major}'
    # target_student_info = f'{average_gpa}:{student_id[:4]}:{apply_major}:{main_major}'

    final_info_list = []
    for apply_major in apply_major_list:
        if apply_major == '':
            continue
        apply_major = apply_major.split(':')
        print(apply_major)
        entire_student_info = getattr(apply_list, apply_major[0])
        info = only_analyze(entire_student_info, target_student_info)
        info['apply_major'] = apply_major[1]

        final_info_list.append(info)

    print('final_data: ', final_info_list)

    data = {
        'info': final_info_list,
    }
    return JsonResponse(data, status=200, json_dumps_params={'ensure_ascii': False})


# 지원하기 눌렀을 때
@csrf_exempt
def Apply(request):
    print(request.POST)
    student_id = request.POST['student_id'].strip()
    user = User.objects.get(student_id=student_id)

    try:
        user = User.objects.get(student_id=student_id)
        # 진행
    except:
        # 회원가입 후 진행
        user = User(student_id=student_id)
        user.save()

    if(getattr(user, 'apply_count') >= 3):
        return HttpResponse('3번까지 지원하실 수 있습니다 ㅜ', status=400)

    # 지원자 학점
    average_gpa = format(round(float(request.POST['average_gpa'].strip()), 2), '.2f')

    # 지원전공
    apply_major = request.POST['apply_major']
    # apply_major = 'physics'

    apply_major_ko = request.POST['apply_major_ko']
    # apply_major_ko = '물리학'

    print('apply_list : ', user.apply_major_list)
    if user.apply_major_list.find(apply_major) > -1:
        return HttpResponse('이미 지원하신 전공입니다.', status=400)

    user.apply_major_list = user.apply_major_list + \
        f'{apply_major}:{apply_major_ko},'
    apply_major_list = user.apply_major_list.split(',')

    user.apply_count += 1

    # 본 전공
    main_major = request.POST['main_major'].strip()
    # main_major = '심리학과'

    apply_list = ApplyList.objects.get()
    print(apply_list)

    target_student_info = f'{average_gpa}:{student_id[:4]}:{apply_major}:{main_major}'
    entire_student_info = getattr(apply_list, apply_major)
    print('apply_major: ', apply_major)
    entire_student_list = entire_student_info.split(',')
    try:
        index = entire_student_list.index('')
        entire_student_list.remove('')
    except:
        pass
    entire_student_list.append(target_student_info)
    entire_student_info = ','.join(entire_student_list)
    setattr(apply_list, apply_major, entire_student_info)

    final_info_list = []
    for apply_major in apply_major_list:
        if apply_major == '':
            continue
        apply_major = apply_major.split(':')
        entire_student_info = getattr(apply_list, apply_major[0])
        info = only_analyze(entire_student_info, target_student_info)
        info['apply_major'] = apply_major[1]

        final_info_list.append(info)

    apply_list.save()
    user.save()

    data = {
        'info': final_info_list,
    }

    return JsonResponse(data, status=200, json_dumps_params={'ensure_ascii': False})
