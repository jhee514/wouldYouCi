from rest_framework import status


class ErrorCollection(object):

    def __init__(self, code, status, message):
        self.code = code
        self.status = status
        self.message = message

    def as_md(self):
        return '```\n{\n\n\t"code": "%s"\n\n\t"message": "%s"\n\n}\n\n```' % \
               (self.code, self.message)


SERIALIZER_ERROR = ErrorCollection(
    code='SERIALIZER_ERROR',
    status=status.HTTP_400_BAD_REQUEST,
    message='필수 정보가 누락되었습니다.'
)
PERMISSION_DENIED = ErrorCollection(
    code='PERMISSION_DENIED',
    status=status.HTTP_403_FORBIDDEN,
    message='요청 권한이 없습니다.'
)


class SerializerErrorCollection(object):

    def __init__(self, arg, status, message, code):
        self.arg = arg
        self.status = status
        self.message = message
        self.code = code

    def as_md(self):
        return '\n\n> **%s**\n\n```\n{\n\n\t"message": {\n\n\t\t"%s": ["%s"]\n\n\t}\n\n}\n\n```' % \
               (self.code, self.arg, self.message)


ACCOUNTS_USERNAME = SerializerErrorCollection(
    arg='username',
    status=status.HTTP_400_BAD_REQUEST,
    message='user의 username은/는 이미 존재합니다.',
    code='유저네임 중복'
)


ACCOUNTS_EMAIL = SerializerErrorCollection(
    arg='email',
    status=status.HTTP_400_BAD_REQUEST,
    message='이 필드는 필수 항목입니다.',
    code='이메일 입력 안 함'
)


class SerializerErrorCollectionMulti(object):

    def __init__(self, arg, status, code, message, arg2, message2, arg3, message3):
        self.arg = arg
        self.status = status
        self.message = message
        self.arg2 = arg2
        self.message2 = message2
        self.code = code
        self.arg3 = arg3
        self.message3 = message3

    def as_md(self):
        return '\n\n> **%s**\n\n```\n{\n\n\t"message": {\n\n\t\t"%s": ["%s"],' \
               '\n\n\t\t"%s": ["%s"],\n\n\t\t"%s": ["%s"]\n\n\t}\n\n}\n\n```' % \
               (self.code, self.arg, self.message, self.arg2, self.message2, self.arg3, self.message3)


ACCOUNTS_MULTI = SerializerErrorCollectionMulti(
    arg='username',
    status=status.HTTP_400_BAD_REQUEST,
    code='유저네임 중복 + 패스워드 없음 + 이메일 형식 이상한 경우',
    message='user의 username은/는 이미 존재합니다.',
    arg2='password',
    message2='이 필드는 필수 항목입니다.',
    arg3='email',
    message3='유효한 이메일 주소를 입력하십시오.'
)