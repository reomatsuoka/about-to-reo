from django.db import models

class Profile(models.Model):
    # null=True, blank=Trueを設定すると内容の入力が必須でなくなる。
    title = models.CharField('タイトル', max_length=100, null=True, blank=True)
    subtitle = models.CharField('サブタイトル', max_length=100, null=True, blank=True)
    name = models.CharField('名前', max_length=100)
    job = models.TextField('仕事')
    introduction = models.TextField('自己紹介')
    character1 = models.ImageField(upload_to='images', verbose_name='性格１')
    character2 = models.ImageField(upload_to='images', verbose_name='性格２')
    character3 = models.ImageField(upload_to='images', verbose_name='性格３')
    github = models.CharField('github', max_length=100, null=True, blank=True)
    twitter = models.CharField('twitter', max_length=100, null=True, blank=True)
    linkedin = models.CharField('linkedin', max_length=100, null=True, blank=True)
    facebook = models.CharField('facebook', max_length=100, null=True, blank=True)
    instagram = models.CharField('instagram', max_length=100, null=True, blank=True)
    topimage1 = models.ImageField(upload_to='images', verbose_name='トップ画像1')
    topimage2 = models.ImageField(upload_to='images', verbose_name='トップ画像2')
    topimage3 = models.ImageField(upload_to='images', verbose_name='トップ画像３')
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

class AboutMe(models.Model):
    description = models.TextField('説明')
    school = models.CharField('学校', max_length=100)
    start = models.CharField('入学', max_length=100)
    graduate = models.CharField('卒業', max_length=100)
    occupation = models.CharField('職業', max_length=100)
    job_place = models.CharField('職場', max_length=100)
    job_period = models.CharField('入社', max_length=100)

    def __str__(self):
        return self.school

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

class Footer(models.Model):
    tel = models.CharField("電話番号", max_length=100)
    mail = models.EmailField(max_length=100)
    address = models.CharField("住所", max_length=100)
    hour1 = models.CharField("営業時間１", max_length=100)
    hour2 = models.CharField("営業時間２", max_length=100)
    hour3 = models.CharField("営業時間３", max_length=100)

    def __str__(self):
        return self.tel