from django.db import models

class Profile(models.Model):
    # null=True, blank=Trueを設定すると内容の入力が必須でなくなる。
    title = models.CharField('タイトル', max_length=100, null=True, blank=True)
    subtitle = models.CharField('サブタイトル', max_length=100, null=True, blank=True)
    name = models.CharField('名前', max_length=100)
    job = models.TextField('仕事')
    introduction = models.TextField('自己紹介')
    github = models.CharField('github', max_length=100, null=True, blank=True)
    twitter = models.CharField('twitter', max_length=100, null=True, blank=True)
    linkedin = models.CharField('linkedin', max_length=100, null=True, blank=True)
    facebook = models.CharField('facebook', max_length=100, null=True, blank=True)
    instagram = models.CharField('instagram', max_length=100, null=True, blank=True)
    topimage = models.ImageField(upload_to='images', verbose_name='トップ画像')
    subimage = models.ImageField(upload_to='images', verbose_name='サブ画像')

    def __str__(self):
        return self.name

class Concept(models.Model):
    title = models.CharField("タイトル", max_length=100)
    description = models.TextField("説明")

    def __str__(self):
        return self.title

class Work(models.Model):
    title = models.CharField("タイトル", max_length=100)
    image = models.ImageField(upload_to='images', verbose_name="イメージ画像")
    thumbnail = models.ImageField(upload_to="images", verbose_name="サムネイル", null=True, blank=True)
    skill = models.CharField("スキル", max_length=100)
    url = models.CharField("URL", max_length=100, null=True, blank=True)
    created = models.DateField("作成日時")
    description = models.TextField('説明')

    def __str__(self):
        return self.title


class Experience(models.Model):
    occupation = models.CharField('職業', max_length=100)
    company = models.CharField('会社', max_length=100)
    description = models.TextField('説明')
    place = models.CharField('場所', max_length=100)
    period = models.CharField('期間', max_length=100)

    def __str__(self):
        return self.occupation

class Education(models.Model):
    course = models.CharField('コース', max_length=100)
    school = models.CharField('学校', max_length=100)
    place = models.CharField('場所', max_length=100)
    period = models.CharField('期間', max_length=100)

    def __str__(self):
        return self.course

class Skill(models.Model):
    name = models.CharField("名前", max_length=100)
    level = models.IntegerField("スキルレベル")

    def __str__(self):
        return self.name

class Finaly(models.Model):
    thanks = models.TextField('お礼')
    final = models.CharField("最後の一文", max_length=100)

    def __str__(self):
        return self.final