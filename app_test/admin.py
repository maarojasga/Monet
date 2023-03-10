from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student, Test, Question, Answer

# Permitir que un estudiante ingrese a Django Admin a ver sólo sus propias respuestas
class StudentAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=request.user)

class AnswerAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(student=request.user)
        



admin.site.register(Answer, AnswerAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Test)
admin.site.register(Question)

