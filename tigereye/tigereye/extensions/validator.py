import functools
from flask import request, jsonify
from tigereye.helper.code import Code


class Validator():
    # 接口参数验证器

    def __init__(self, **params_template):
        # 接收参数的模板，并存放至成员属性
        self.pt = params_template

    def __call__(self, f):
        # 实际实现参数过滤的装饰器函数
        @functools.wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                request.params = {}
                for k, v in self.pt.items():
                    request.params[k] = v(request.values[k])
            except Exception:
                response = jsonify(
                    rc=Code.required_parameter_missing.value,
                    msg=Code.required_parameter_missing.name,
                    data={
                        "required_param": k,
                        'you_passed':request.values.get(k),
                    }
                )
                # 设置response的http响应吗
                response.staus_code = 400
                # 返回response对象
                return response
            # 执行被装饰的接口方法,并返回结果
            return f(*args, **kwargs)
        # 返回装饰器函数
        return decorated_function


class ValidationError(Exception):
    # 自定义异常，当验证出错时抛出此异常
    def __init__(self, message, values):
        super(ValidationError,self).__init__(message)
        self.values = values


def multi_int(values, sperator=','):
    # 验证多个数字 类似于1,3,5这种形式 并返回一个列表
    return  [int(i) for i in values.split(sperator)]


def complex_int(values,sperator = '-'):
    # 验证多个数字 类似1-2-3 并返回一个元祖
    digits = values.split(sperator)
    result = []
    for digit in digits:
        if not digit.isdigit():
            raise ValidationError('complex int error: %s' % values, values)
        result.append(int(digit))
    return tuple(result)


def multi_complex_int(values, sperator= ','):
    # 验证多组数字 类似于1-2-3,4-5-6,7-8-9 最后返回一个列表包含N个元祖
    return [complex_int(i) for i in values.split(sperator)]