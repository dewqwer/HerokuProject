from django.contrib import admin
from backend.models import CountRealTime, Faculty, GraduationDetail, Major, FacultyNewLogic, GraduationDetailNewLogic, MajorNewLogic, CountRealTimeNewLogic

# Register your models here.

admin.site.register(CountRealTime)
admin.site.register(Faculty)
admin.site.register(GraduationDetail)
admin.site.register(Major)

admin.site.register(FacultyNewLogic)
admin.site.register(GraduationDetailNewLogic)
admin.site.register(MajorNewLogic)
admin.site.register(CountRealTimeNewLogic)
