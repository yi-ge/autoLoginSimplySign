import pyotp


def get_password(args):
    # 配置
    secret_key = ''
    algorithm = 'sha256'
    digits = 6
    interval = 30  # 有效期

    # 创建 TOTP 对象
    totp = pyotp.TOTP(secret_key, digits=digits,
                      interval=interval, digest=algorithm)

    # 生成一次性密码
    return totp.now()
