import re
from rest_framework.serializers import ValidationError


class TitleValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        req = re.compile(r'^[а-яА-Яa-zA-Z0-9\.\-\ ]+$')
        print(req)
        tmp_val = dict(value).get(self.field)
        if not bool(req.match(tmp_val)):
            raise ValidationError('Title is not ok')
