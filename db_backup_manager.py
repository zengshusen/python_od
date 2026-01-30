import subprocess
import os
import sys
import argparse
from datetime import datetime

def backup_database():
    # --- 1. 使用 argparse 设计专业的命令行接口 ---
    parser = argparse.ArgumentParser(description="MySQL 自动化备份工具")
    parser.add_argument("db_name", help="要备份的数据库名称")
    parser.add_argument("-u", "--user", default="rose", help="MySQL 用户名 (默认: rose)")
    parser.add_argument("-p", "--password", required=True, help="MySQL 密码")
    parser.add_argument("-o", "--output", default="./backups", help="备份文件存放目录 (默认: ./backups)")
    
    args = parser.parse_args()

  
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    backup_file = f"{args.db_name}_{timestamp}.sql"
    
    #  2. 使用 os 模块处理路径和文件夹 
    target_dir = os.path.abspath(args.output)
    
    # 如果文件夹不存在，自动创建 
    if not os.path.exists(target_dir):
        print(f"目录 {target_dir} 不存在，正在创建...")
        os.makedirs(target_dir, exist_ok=True)
    
    # 最终的 SQL 文件完整路径
    sql_path = os.path.join(target_dir, backup_file)
    tar_path = sql_path + ".tar.gz"

    print(f" 开始备份数据库: {args.db_name} ...")

    # --- 3. 使用 subprocess 调用 mysqldump 导出 ---
    try:
        #
        with open(sql_path, "w") as f:
            dump_process = subprocess.run(
                ["mysqldump", f"-u{args.user}", f"-p{args.password}", args.db_name],
                stdout=f,       # 将输出重定向到文件
                stderr=subprocess.PIPE,
                text=True
            )
        
        if dump_process.returncode != 0:
            print(f" 备份失败: {dump_process.stderr}")
            # --- 4. 使用 sys 报错退出 ---
            if os.path.exists(sql_path): os.remove(sql_path)
            sys.exit(1)

        print(f" SQL 导出成功: {sql_path}")

        #使用 subprocess 调用 tar 压缩文件 ---
        print(" 正在压缩备份文件...")
       
        compress_process = subprocess.run(
            ["tar", "-czf", tar_path, "-C", target_dir, backup_file],
            capture_output=True,
            text=True
        )

        if compress_process.returncode == 0:
            print(f" 最终备份包: {tar_path}")
            # 压缩成功后删除原始大的 .sql 文件
            os.remove(sql_path)
        else:
            print(f" 压缩失败: {compress_process.stderr}")

    except Exception as e:
        print(f" 发生致命错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    backup_database()