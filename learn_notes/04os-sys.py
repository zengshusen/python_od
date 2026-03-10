import os
import sys
import subprocess
def monitor_log(dir_name):
    base_dir=os.path.dirname(os.path.abspath(__file__))
    target_path=os.path.join(base_dir,dir_name)
    if not os.path.exists(target_path):
        print(f"错误：目标目录{target_path}不存在")
        sys.exit(1)
    print(f"正在分析目录:{target_path}")
    try:
        result=subprocess.run(
            ["du","-sh",target_path],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"目录统计信息:{result.stdout.strip()}")
    except subprocess.CalledProcessError:
        print("执行du命令失败")
if __name__ == "__main__":
    folder=sys.argv[1] if len(sys.argv) > 1 else "03re.py"
    monitor_log(folder)