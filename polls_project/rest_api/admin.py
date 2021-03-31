from django.contrib import admin
from rest_api.models import Question, Choice, Poll, AnonymousUser, Answer


admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Poll)
admin.site.register(AnonymousUser)
admin.site.register(Answer)
# Register your models here.
