from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as _UserManager


class UserManager(_UserManager):
    """
    DOC
    """
    def create_superuser(self, username, password, email=None, **extra_fields):
        super(UserManager, self).create_superuser(
            username=username,
            password=password,
            email=email,
            **extra_fields
        )


class Users(AbstractUser):
    """
    add mobile, email_active field.

    """
    # 定义创建用户时, 需要输入的字段值.
    REQUIRED_FIELDS = ['mobile']

    objects = UserManager()

    mobile = models.CharField(
        max_length=11,
        unique=True,
        help_text="手机号",
        verbose_name="verbose_手机号",
        error_messages={
            'unique': "该手机号已被注册.",
        }
    )

    email_active = models.BooleanField(default=False, verbose_name="verbose_邮箱状态.")

    class Meta:
        """
        元数据.
        """
        db_table = 'tb_users'
        verbose_name = "verbose_用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        # inherit from `AbstractUser`.
        return self.username

# Create your models here.
