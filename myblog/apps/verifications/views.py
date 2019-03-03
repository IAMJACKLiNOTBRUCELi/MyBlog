from django.shortcuts import render
from django.views import View
from django_redis import get_redis_connection
from django.http import HttpResponse

from utils.captcha.captcha import captcha
from . import constants
from user.models import Users


class ImageCode(View):
    """
    define image verifications view
    URL: /image_codes/uuid:image_code_id/
    """
    def get(self, request, image_code_id):
        # 通过captcha模块获取验证码的文本信息和二进制数据
        text, image = captcha.generate_captcha()

        # 获取redis的连接, alias通过别名选择settings中的配置.
        conn_redis = get_redis_connection(alias='verify_codes')
        img_key = "img_{}".format(image_code_id).encode('UTF-8')
        # 将key和文本信息写入到redis中, 并设置过期时间.
        conn_redis.setex(img_key, constants.IMAGE_CODE_REDIS_EXPIRES, text)
        
        return HttpResponse(content=image, content_type="image/png")

# Create your views here.
