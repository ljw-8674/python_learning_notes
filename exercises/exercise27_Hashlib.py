import hashlib, hmac

# MD5算法
# 基本使用
md5 = hashlib.md5()
md5.update('123456ok'.encode('utf-8'))
print(md5.hexdigest())	# fb95629e097482282808236504e8f623

# 分块多次调用
md5 = hashlib.md5()
md5.update('123456'.encode('utf-8'))
md5.update('ok'.encode('utf-8'))
print(md5.hexdigest())  # fb95629e097482282808236504e8f623

# SHA1算法
sha1 = hashlib.sha1()
sha1.update('123456ok'.encode('utf-8'))
print(sha1.hexdigest())	# d515531e48597d6a76e002cfd199959007379f1f

# HMAC算法
message = b'Hello, world!'
key = b'secret'

h = hmac.new(key, message, digestmod='MD5')
print(h.hexdigest())  # fa4ee7d173f2d97ee79022d1a7355bcf
