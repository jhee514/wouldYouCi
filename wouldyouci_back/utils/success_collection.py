from rest_framework import status


class SuccessCollection(object):

    def __init__(self, status, message):
        self.status = status
        self.message = message

    def as_md(self):
        return '```\n{\n\n\t"message": "%s"\n\n}\n\n```' % self.message


ACCOUNTS_SUCCESS = SuccessCollection(
    status=status.HTTP_200_OK,
    message='회원가입 되었습니다.'
)
