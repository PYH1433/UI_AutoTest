import os
from token import NAME
from faker import Faker


# 获取项目路径
PATH = os.path.dirname(__file__)

# 测试地址
BASE_URL = "http://121.43.169.97:8081"

# 测试数据
fk = Faker(locale='zh_CN')

# 姓名，手机号，身份证号
NAME = fk.name()
PHONE = fk.phone_number()
CARD = fk.ssn()

