from django.shortcuts import render

# Create your views here.
def list_courses(request):
    # This is a placeholder view. You can implement your logic here.
    return render(request, 'course/list_courses.html')

def course_detail(request, course_id):
    # This is a placeholder view. You can implement your logic here.
    return render(request, 'course/course_detail.html', {'course_id': course_id})

def create_course(request):
    # This is a placeholder view. You can implement your logic here.
    return render(request, 'course/create_course.html')

def update_course(request, course_id): 
    # This is a placeholder view. You can implement your logic here.
    return render(request, 'course/update_course.html', {'course_id': course_id})

def delete_course(request, course_id):
    # This is a placeholder view. You can implement your logic here.
    return render(request, 'course/delete_course.html', {'course_id': course_id})

def enroll_in_course(request, course_id):
    # This is a placeholder view. You can implement your logic here.
    return render(request, 'course/enroll_in_course.html', {'course_id': course_id})