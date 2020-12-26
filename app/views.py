from django.views.generic import View
from django.shortcuts import render, redirect
from .models import Profile, Work, Skill, Concept, Finaly, AboutMe, Footer
import json
from django.conf import settings
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse
import textwrap
from .forms import ContactForm

class IndexView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by("-id")[0]
        concept_data = Concept.objects.all()
        if concept_data.exists():
            concept_data = Concept.objects.order_by("-id")[0]
        aboutme_data = AboutMe.objects.all()
        if aboutme_data.exists():
            aboutme_data = AboutMe.objects.order_by("-id")[0]
        finaly_data = Finaly.objects.all()
        if finaly_data.exists():
            finaly_data = Finaly.objects.order_by("-id")[0]
        work_data = Work.objects.order_by("-id")
        skill_master_data = Skill.objects.all()
        skill_name = []
        skill_level = []
        for skill in skill_master_data:
            skill_name.append(skill.name)
            skill_level.append(skill.level)
        skill_data = {
            "name": skill_name,
            "level": skill_level
        }
        footer_data = Footer.objects.all()
        if footer_data.exists():
            footer_data = footer_data.order_by("-id")[0]
            
        return render(request, 'app/index.html', {
            'profile_data': profile_data,
            'concept_data': concept_data,
            'aboutme_data': aboutme_data,
            'work_data': work_data,
            'skill_data': json.dumps(skill_data),
            'finaly_data': finaly_data,
            'footer_data': footer_data,
        })

class DetailView(View):
    def get(self, request, *args, **kwargs):
        work_data = Work.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/detail.html',{
            'work_data': work_data,
        })

class ContactView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm(request.POST or None)

        return render(request, 'app/contact.html',{
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST or None)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = 'お問い合わせありがとうございます。'
            content = textwrap.dedent('''
            ※このメールはシステムからの自動返信です。
                
                {name} 様
                
                お問い合わせありがとうございました。
                以下の内容でお問い合わせを受け付けいたしました。
                内容を確認させていただき、ご返信させて頂きますので、少々お待ちください。
                
                --------------------
                ■お名前
                {name}
                
                ■メールアドレス
                {email}
                
                ■メッセージ
                {message}
                --------------------
                ''').format(
                    name=name,
                    email=email,
                    message=message
                )

            to_list = [email]
            bcc_list = [settings.EMAIL_HOST_USER]

            try:
                message = EmailMessage(subject=subject, body=content, to=to_list, bcc=bcc_list)
                message.send()
            except BadHeaderError:
                return HttpResponse('無効なヘッダが検出されました。')

            return redirect('thanks')

        return render(request, 'app/contact.html', {
            'form': form
        })

class ThanksView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/thanks.html')