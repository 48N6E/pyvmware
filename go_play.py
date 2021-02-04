import ssl
import re
import time
from pysphere import VIServer,VIProperty



host_ip = "10.10.10.123"
username = "administrator@vcsq.nite"
passwd = "1qaz@WSX#$*&"
server_obj = VIServer()

server_obj.connect(host=host_ip, user=username, password=passwd)
# 可以连接esxi主机，也可以连接vcenter

# 获取连接的对象类型
print(server_obj.get_server_type())

# 获取esxi的版本信息
print(server_obj.get_api_version())