import subprocess
import re
import argparse
import sys

def get_memory_usage(limit):
    # 1. 使用 subprocess 执行 Linux 命令

    result = subprocess.run(["free", "-m"], capture_output=True, text=True)
    
    # 检查命令是否执行成功
    if result.returncode != 0:
        print("错误：无法获取内存信息")
        sys.exit(1)

    output = result.stdout
   
    match = re.search(r"Mem:\s+(\d+)\s+(\d+)", output)

    if match:
        total = int(match.group(1))
        used = int(match.group(2))
        
        # 3. 计算百分比
        usage_pct = (used / total) * 100

        print(f"--- 内存监控报告 ---")
        print(f"总量: {total}MB")
        print(f"已用: {used}MB")
        print(f"使用率: {usage_pct:.2f}%")

        # 4. 判断逻辑
        if usage_pct > limit:
            print(f"⚠️  警告：当前内存使用了 {usage_pct:.1f}%，已超过设定的阈值 {limit}%！")
        else:
            print(f"✅ 状态良好：使用率在安全范围内。")
    else:
        print("未能解析到内存数据。")

if __name__ == "__main__":
    # 5. 使用 argparse 包装成专业工具
    parser = argparse.ArgumentParser(description="Linux 内存预警脚本")
    # 添加 --limit 参数，默认 80
    parser.add_argument("--limit", type=int, default=80, help="设置报警阈值 (默认 80)")
    
    args = parser.parse_args()
    
    get_memory_usage(args.limit)