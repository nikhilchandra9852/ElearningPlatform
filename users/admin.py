from django.contrib import admin
from .models import Users,Logins,Courses,Chat,QuizBranch,Quiz,evaluation
# Register your models here.

admin.site.register(Users)
admin.site.register(Logins)
admin.site.register(Courses)
admin.site.register(Chat)
admin.site.register(Quiz)
admin.site.register(QuizBranch)
admin.site.register(evaluation)


