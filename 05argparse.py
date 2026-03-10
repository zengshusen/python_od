import argparse
import sys
import subprocess


def main():
    #1.配置解析器
    parser=argparse.ArgumentParser(
        description="简单的MySQL状态检查工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="示例：python3 mysql_check.py localhost -u root --threshold 100"
    )
    #2.定义参数
    parser.add_argument("host",help="数据库主机地址")
    parser.add_argument("-u","--user",default="root",help="用户名 (默认：root)")
    parser.add_argument("-p","--port",type=int,default=3306,help="端口 (默认：3306)")
    parser.add_argument("-t","--threshold",type=int,default=50,help="连接数报警阈值")
    parser.add_argument("--debug",action="store_true",help="开启调试模式")
    #3.获取参数
    args=parser.parse_args()
    #4.模拟逻辑
    print(f"---- 正在检查数据库{args.host}:{args.port} ---")
    cmd=["pgrep","mysql"]
    res=subprocess.run(cmd,capture_output=True,text=True)

    if res.returncode!=0:
        print("错误：MySQL服务未运行！")
        sys.exit(1)
    if args.debug:
        print(f"[DEBUG] 当前配置用户:{args.user},报警阈值:{args.threshold}")
    print("数据库状态正常。")
    
if __name__ == "__main__":
        main()

