
import requests
import re
resp = requests.get("https://www.bilibili.com/video/BV1MDx6eHE5Q/?spm_id_from=333.1007.tianma.1-1-1.click&vd_source=0f67a74f9c63001c28aebb7539deb0ba")
obj = re.compile(f'"aid":(?P<id>.*?),"bvid":"BV1MDx6eHE5Q"')  # 在网页源代码里可以找到id，用正则获取到
oid = obj.search(resp.text).group('id')
print('oid是' + oid)  # 在程序运行时告诉我们已经获取到了参数oid