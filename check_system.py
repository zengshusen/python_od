import subprocess
print("正在尝试创建文件夹。。")
result=subprocess.run(["mkdir","-p","learn_notes"])

if result.returncode==0:
    print("文件夹创建成功！")
else:
    print("创建失败。")
res=subprocess.run(["ls","-l"],capture_output=True,text=True)
print("当前目录内容:\n",res.stdout)