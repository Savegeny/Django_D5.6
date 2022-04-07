from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models import Sum
from django.contrib.auth.forms import UserCreationForm
from django import forms
from allauth.account.forms import SignupForm


class Author(models.Model):
    rating_A = models.IntegerField(default=0)
    author_U = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self):
        upd_rat = self.post_set.aggregate(ratingPost=Sum('rating_post'))
        uRat = 0
        uRat += upd_rat.get('ratingPost')

        upd_com = self.author_U.comment_set.aggregate(commPost=Sum('rating_com'))
        uComm = 0
        uComm += upd_com.get('commPost')

        self.rating_A = uRat * 3 + uComm
        self.save()


class Category(models.Model):
    post_cat = models.CharField(max_length=64, unique=True)


class Post(models.Model):
    author_post = models.ForeignKey(Author, on_delete=models.CASCADE)
    authorname = author_post.name

    NEWS = 'NW'
    POST = 'PS'
    CATEGORY_CHOISE = (
        (NEWS, 'Новость'),
        (POST, 'Статья')
    )
    type = models.CharField(max_length=2, choices=CATEGORY_CHOISE, default=POST)
    date_create = models.DateTimeField(auto_now_add=True)
    category_post = models.ManyToManyField(Category, through='PostCategory')
    head_post = models.CharField(max_length=128)
    text_post = models.TextField()
    rating_post = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.head_post}{self.date_create}"

    def get_absolut_url(self):
        return f"/news/{self.id}"

    def like(self):
        self.rating_post += 1
        self.save()

    def dislike(self):
        self.rating_post -= 1
        self.save()

    def preview(self):
        return self.text_post[0:123] + '...'


class PostCategory(models.Model):
    post_pc = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_pc = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post_c = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_c = models.ForeignKey(User, on_delete=models.CASCADE)
    text_com = models.TextField()
    datein_com = models.DateTimeField(auto_now_add=True)
    rating_com = models.IntegerField(default=0)

    def like(self):
        self.rating_com += 1
        self.save()

    def dislike(self):
        self.rating_com -= 1
        self.save()


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user