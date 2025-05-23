from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, nickname, social_provider, full_name, age, salary, **extra_fields):
        if not email:
            raise ValueError('이메일 필쑤')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            nickname=nickname,
            social_provider=social_provider,
            full_name=full_name,
            age=age,
            salary=salary,
            **extra_fields
        )
        user.set_unusable_password()
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, nickname, social_provider, full_name, age, salary, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if password:
            user = self.model(
                email=email,
                nickname=nickname,
                social_provider=social_provider,
                full_name=full_name,
                age=age,
                salary=salary,
                **extra_fields
            )
            user.set_password(password)
        else:
            user = self.create_user(email, nickname, social_provider, full_name, age, salary, **extra_fields)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=254)
    nickname = models.CharField(max_length=30, unique=True)
    social_pervider = models.CharField(max_length=30)
    pull_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=150)
    profile_url = models.URLField(blank=True, null=True)

    # 기본 정보
    inclination = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()
    salary = models.IntegerField()

    # 추가 필드
    favorite_bank = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    occupation = models.CharField(max_length=50, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname', 'social_provider', 'full_name', 'age', 'salary']

    objects = UserManager()

    def __str__(self):
        return self.nickname
