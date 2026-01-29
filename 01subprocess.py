import subprocess
import os

#subprocess模块 能够连接Linux操作系统管理
response=subprocess.Popen(
    "ls",
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)
# print(response)
# print(response.stdout)
print(response.stdout.read())#已经read以后，下面的代码将读取不到，因为管道中的数据被取走了
print(response.stdout.read().decode('gbk'))#mac0S默认是utf8

print(response.stderr)
print(response.stderr.read().decode("gbk"))
print("#"*30)
base_dir=os.path.dirname(__file__)
print(base_dir)
response=subprocess.run(
    ["ls",base_dir],
    shell=True,
    # stdout=subprocess.PIPE,
    # stderr=subprocess.PIPE,
    capture_output=True#加了capture_output就不需要stdout和stderr
)
# print(response)
# print(response.returncode)
# print(response.stdout.decode("gbk"))

print("#"*30)
def run_commend(commend_list):



    response=subprocess.run(
        commend_list,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="gbk"
    )
    if response.returncode == 0:
        return response.stdout
    else:
        return response.stderr
base_dir = os.path.dirname(__file__)
result=run_commend(["ls",base_dir])
print(result)

subprocess.call(["python","--version"])

