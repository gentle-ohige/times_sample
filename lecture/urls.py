from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('all/', all_lecture_view),
    path('', lecture_view),
    path('attendance/', AttendanceView.as_view()),
    path('teachers/', all_teacherview),
    path('teacher/', teacher_view),
    path('allAttendance/', AllAttendanceView.as_view()),
    # Task
    path('tasks/', tasks_view),
    path('task/', task_view),
    # Memo
    path('memos/', memos_view),
    path('memo/', memo_view),

    # Test
    path('test/', test_view),
]
