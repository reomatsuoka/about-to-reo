from django.contrib import admin
from .models import Profile, Work, Experience, Education, Skill, Concept, Finaly

admin.site.register(Profile)
admin.site.register(Concept)
admin.site.register(Work)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Finaly)