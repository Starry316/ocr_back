import time
from enum import Enum


class Output(object):
    def __init__(self):
        pass

    @classmethod
    def output(cls, data, status, message):
        return {
            'responseTime': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            'success': True,
            'code': status.value,
            'status': status.name,
            'data': data,
            'message': message
        }

    @classmethod
    def success(cls, data):
        return cls.output(data, cls.Status.Success, "ok")

    @classmethod
    def error(cls, data):
        return cls.output(data, cls.Status.ServerError, "error")

    class Status(Enum):
        Success = 200
        NotLogin = 400
        ResourceExist = 401
        ResourceNotPermit = 403
        ServerError = 500
        ParameterError = 501
