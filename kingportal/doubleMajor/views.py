from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from .models import User, ApplyList
# apply_list = ApplyList.objects.create()
# apply_list.save()
# Create your views here.
def analyze(entire_gpa, target_gpa):
    entire_gpa_list = entire_gpa.split(',')
    print(entire_gpa_list)
    entire_gpa_list.remove('')
    entire_gpa_list = list(map(float, entire_gpa_list))
    entire_gpa_list.sort()
    print(entire_gpa_list)
    print('entire : ', entire_gpa, 'target:', target_gpa)
    
    data = {
        'index' : entire_gpa_list.index(float(target_gpa)) + 1,
        'applicants_number' : len(entire_gpa_list),
        'average_gpa' : sum(entire_gpa_list, 0.0) / len(entire_gpa_list)
    }
    return data

def Login(request):
    # user = User(student_id=request.Post['kingBB'])
    # check_user = User.objects.filter(kingBB = request.Post['kingBB'])
    # check_user = User.objects.filter(kingBB = '/9j/4AAQSkZJRgABAAEAlgCWAAD//')
    
    try:
        check_user = User.objects.get(student_id = request.Post['student_id'])
        # 진행
    except:
        # 회원가입 후 진행
        user = User(student_id=request.Post['student_id'])
        user.save()

    try:
        user = User.objects.get(student_id = 2012130419)

        if(getattr(user, 'apply_count')>=3):
            return HttpResponse('3번까지 지원하실 수 있습니다 ㅜ', status=400)

        user.apply_count += 1

        # average_gpa = request.Post['average_gpa']
        average_gpa = '3.75'

        # apply_major = request.Post['apply_major']
        apply_major = 'philosophy'

        apply_list = ApplyList.objects.get()
        current_value = getattr(apply_list, apply_major)
        setattr(apply_list, apply_major, current_value + f'{average_gpa},')

        apply_list.save()
        user.save()

        entire_gpa = getattr(apply_list, apply_major)
        data = analyze(entire_gpa.strip(), average_gpa)
        return JsonResponse(data, status=200)
    except:
        return HttpResponse(status=400)    




def Apply(request):
    # try:
    #     user = User.objects.get(student_id = 2012130419)

    #     if(getattr(user, 'apply_count')>=3):
    #         return HttpResponse(status=400, message='3번까지 지원하실 수 있습니다 ㅜ')

    #     user.apply_count += 1

    #     # average_gpa = request.Post['average_gpa']
    #     average_gpa = '3.75'

    #     # apply_major = request.Post['apply_major']
    #     apply_major = 'psychology'

    #     apply_list = ApplyList.objects.get()
    #     current_value = getattr(apply_list, apply_major)
    #     setattr(apply_list, apply_major, current_value + f'{average_gpa},')

    #     apply_list.save()
    #     user.save()

    #     # getattr(apply_list, apply_major), average_gpa
    #     entire_gpa = getattr(apply_list, apply_major)
    #     index = analyze(entire_gpa, average_gpa)

    #     return HttpResponse(status=200)
    # except:
    #     return HttpResponse(status=400)    

    user = User.objects.get(student_id = 2012130419)

    if(getattr(user, 'apply_count')>=10):
        return HttpResponse('3번까지 지원하실 수 있습니다 ㅜ', status=400)

    user.apply_count += 1

    # average_gpa = request.Post['average_gpa']
    average_gpa = '3.75'

    # apply_major = request.Post['apply_major']
    apply_major = 'philosophy'

    apply_list = ApplyList.objects.get()
    current_value = getattr(apply_list, apply_major)
    setattr(apply_list, apply_major, current_value + f'{average_gpa},')

    apply_list.save()
    user.save()

    entire_gpa = getattr(apply_list, apply_major)
    index = analyze(entire_gpa.strip(), average_gpa)
    data = {
        'index' : index,
    }
    return JsonResponse(data, status=200)




    



    
