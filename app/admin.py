from django.contrib import admin
from .models import Profile, Work, Skill, Concept, Finaly, AboutMe, Footer

admin.site.register(Profile)
admin.site.register(Concept)
admin.site.register(Work)
admin.site.register(Skill)
admin.site.register(Finaly)
admin.site.register(AboutMe)
admin.site.register(Footer)