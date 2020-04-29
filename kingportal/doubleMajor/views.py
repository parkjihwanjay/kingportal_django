from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from .models import User, ApplyList
from django.views.decorators.csrf import csrf_exempt
import json
# apply_list = ApplyList.objects.create()
# apply_list.save()
# Create your views here.

def convert_to_float(x):
    return float(x[:4])


def analyze(entire_student_info, target_student_info):
    entire_student_list = entire_student_info.split(',')
    try:
        index = entire_student_list.index('')
        entire_student_list.remove('')
    except:
        pass
    print('entire_student_list: ', entire_student_list)
    # entire_student_list.remove('')

    # entire_gpa_list = list(map(float, entire_gpa_list))
    entire_student_list.append(target_student_info)
    entire_student_list = sorted(
        entire_student_list, reverse=True, key=convert_to_float)

    is_swapped = False
    index = 0
    count = 0
    gpa_sum = 0

    # for i in range(len(entire_student_list)):
    #     if float(target_student_info[:4]) > float(entire_student_list[i][:4]) and is_swapped == False:
    #         is_swapped = True
    #         temp = entire_student_list[i]
    #         entire_student_list[i] = target_student_info
    #         entire_student_list.append(temp)

    #         index = count
    #         gpa_sum += float(entire_student_list[i][:4])

    #     count += 1

    # if is_swapped == False:
    #     entire_student_list.append(target_student_info)

    # gpa_sum += float(target_student_info[:4])
    # count += 1

    entire_student_info = ','.join(entire_student_list)

    for i in range(len(entire_student_list)):
        current_gpa = float(entire_student_list[i][:4])
        target_gpa = float(target_student_info[:4])

        count += 1
        gpa_sum += current_gpa
        if current_gpa == target_gpa:
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
    print('entier_student_info :', entire_student_info)
    return data, entire_student_info


def only_analyze(entire_student_info, target_student_info):
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

    for i in range(len(entire_student_list)):
        current_gpa = float(entire_student_list[i][:4])
        target_gpa = float(target_student_info[:4])

        count += 1
        gpa_sum += current_gpa
        if current_gpa == target_gpa:
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
def Login(request):
    # user = User(student_id=request.POST['kingBB'])
    # check_user = User.objects.filter(kingBB = request.POST['kingBB'])
    # check_user = User.objects.filter(kingBB = '/9j/4AAQSkZJRgABAAEAlgCWAAD//')

    try:
        check_user = User.objects.get(student_id=request.POST['student_id'])
        # 진행
    except:
        # 회원가입 후 진행
        user = User(student_id=request.POST['student_id'])
        user.save()

    try:
        user = User.objects.get(student_id=2012130419)

        if(getattr(user, 'apply_count') >= 3):
            return HttpResponse('3번까지 지원하실 수 있습니다 ㅜ', status=400)

        user.apply_count += 1

        average_gpa = request.POST['average_gpa']
        # average_gpa = '3.75'

        apply_major = request.POST['apply_major']
        # apply_major = 'philosophy'

        apply_list = ApplyList.objects.get()
        # print(apply_list)
        current_value = getattr(apply_list, apply_major)

        setattr(apply_list, apply_major, current_value + f'{average_gpa},')

        apply_list.save()
        user.save()

        entire_gpa = getattr(apply_list, apply_major)
        data = analyze(entire_gpa.strip(), average_gpa)
        return JsonResponse(data, status=200)
    except:
        return HttpResponse(status=400)


@csrf_exempt
def getInfo(request):
    print(request.POST)
    student_id = request.POST['student_id'].strip()
    print('student_id : ', student_id)
    user = User.objects.get(student_id=student_id)
    print('user :', user)
    # try:
    #     # user = User.objects.get(student_id = '2008130419')
    #     student_id = request.POST['student_id'].strip()
    #     print('student_id : ', student_id)
    #     user = User.objects.get(student_id = student_id)
    #     print('user :', user)
    # except:
    #     return JsonResponse({'info': []}, status=200)
    apply_major_list = user.apply_major_list.split(',')
    # "geographic_education, 지리교육과"
    if len(apply_major_list) == 0:
        return HttpResponse(status=200)
    # user = User.objects.get(request.POST['student_id'])

    # 지원자 학점
    average_gpa = request.POST['average_gpa']
    # average_gpa = '3.10'

    # 지원전공
    # apply_major = request.POST['apply_major']
    # apply_major = 'geographic_education'
    # apply_major_ko = request.POST['apply_major_ko']

    # user.apply_major_list = user.apply_major_list + f'apply_major_en:apply_major_ko'

    # 본 전공
    # main_major = request.POST['main_major']
    # main_major = '심리학과'

    # 학번
    # student_id = request.POST['student_id']
    # student_id = '2015130419'

    apply_list = ApplyList.objects.get()
    target_student_info = f'{average_gpa}'

    final_info_list = []

    for apply_major in apply_major_list:
        if apply_major == '':
            continue
        apply_major = apply_major.split(':')
        entire_student_info = getattr(apply_list, apply_major[0])
        info = only_analyze(entire_student_info, target_student_info)
        info['apply_major'] = apply_major[1]

        final_info_list.append(info)

    print('final_data: ', final_info_list)

    data = {
        'info': final_info_list,
    }
    return JsonResponse(data, status=200, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def Apply(request):
    print(request.POST)
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

    if(getattr(user, 'apply_count') >= 3):
        return HttpResponse('3번까지 지원하실 수 있습니다 ㅜ', status=400)

    # 지원자 학점
    average_gpa = request.POST['average_gpa'].strip()
    # average_gpa = '3.10'

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

    user.apply_count += 1

    # 본 전공
    main_major = request.POST['main_major']
    # main_major = '심리학과'

    # 학번
    # student_id = request.POST['student_id']
    # student_id = '2015130419'

    apply_list = ApplyList.objects.get()
    print(apply_list)
    # current_value = getattr(apply_list, apply_major)

    target_student_info = f'{average_gpa}:{student_id[:4]}:{apply_major}:{main_major}'
    entire_student_info = getattr(apply_list, apply_major)

    data, entire_student_info = analyze(
        entire_student_info, target_student_info)
    data['apply_major'] = apply_major_ko
    setattr(apply_list, apply_major, entire_student_info)

    apply_list.save()
    user.save()

    print('data: ', data)
    return JsonResponse(data, status=200, json_dumps_params={'ensure_ascii': False})
    # return HttpResponse(status=200)
