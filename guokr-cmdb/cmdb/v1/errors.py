# -*- coding: utf-8 -*-

from werkzeug.exceptions import HTTPException
from flask import Response


def abort(error_code=None, http_status_code=400, message='', errors=None):
    m = ''
    if error_code and ERRORS.get(error_code):
        http_status_code, m = ERRORS[error_code]

    message = m or message

    raise JSONError(http_status_code, error_code, message, errors)


class JSONError(HTTPException):

    def __init__(self, http_status_code=400,
                 error_code=None, message=None, errors=None):
        super(JSONError, self).__init__(message, None)
        self.status = self.code = http_status_code
        self.error_code = error_code
        self.message = message
        self.errors = errors
        self.data = {
            'status': self.status,
            'error_code': self.error_code,
            'message': self.message,
            'errors': errors,
        }

    def get_response(self):
        return Response(
            self.data, status=self.status, headers=None,
            mimetype=None, content_type='application/json')


def json_error_handler(error):
    return error.get_response()

ERRORS = {
        'ec2_not_found': (404, u'ec2不存在！'),
        'elasticache_not_found': (404, u'elasticache不存在！'),
        'elb_not_found': (404, u'elb不存在！'),
        'rds_not_found': (404, u'rds不存在！'),
        'vpc_not_found': (404, u'vpc不存在！'),
        's3_not_found': (404, u's3不存在！'),
        'iam_not_found': (404, u'iam不存在！'),
        'volume_not_found': (404, u'volume不存在！'),
        'period_not_right': (400, u'时间间隔必须为60整倍数'),
        'time_not_right': (400, u'时间参数格式必须为"%Y.%m.%d %H:%M:%S"'),
        'add_config_error': (500, u'账号信息写入数据库失败'),
        'cmdb_user_not_found': (404, u'用户账号不存在'),
        'cmdb_user_secret_error': (403, u'用户密码错误'),
        'error_access_token': (407, u'非法登录！'),
        'unauthorized': (401, u'token失效'),
        'secret_not_mate': (401, u'两次密码不一致'),
        'cmdb_user_exited': (402, u'账号已存在'),
        'host is unreach': (404, u'主机不可达')
}
