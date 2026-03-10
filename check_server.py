import subprocess
import re
import sys
import argparse
import os

def check_memory(threshold):
    """
    执行 free -m 命令并解析内存百分比
    """
    try:
        # --- 1. 使用 subprocess 执行 Linux 命令 ---
       
        result = subprocess.run(["free", "-m"], capture_output=True, text=True, check=True)
        
        # --- 2. 使用 re 解析输出结果 ---
       
        match = re.search(r"Mem:\s+(\d+)\s+(\d+)", result.stdout)
        
        if match:
            total = int(match.group(1))
            used = int(match.group(2))
            
            # 计算百分比
            usage_pct = int((used / total) * 100)
            
            # --- 3. 核心逻辑输出 ---
    
            print(f"当前内存使用了 {usage_pct}%", end="")
            
            if usage_pct >= threshold:
                print("，警告！")
    
                sys.exit(1)
            else:
                print("，状态正常。")
                sys.exit(0)
        else:
            print("错误：解析内存数据失败。")
            sys.exit(1)

    except subprocess.CalledProcessError as e:
        print(f"执行命令失败: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"发生未知错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # --- 4. 使用 argparse 像命令一样接受参数 ---
    parser = argparse.ArgumentParser(description="Linux 服务器内存预警工具")
    

    parser.add_argument(
        "--limit", 
        type=int, 
        default=80, 
        help="设置内存报警阈值 (百分比)，默认为 80"
    )
    
    args = parser.parse_args()
    
    # 运行检查
    check_memory(args.limit)