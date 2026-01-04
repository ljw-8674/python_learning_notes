import argparse

def main():
    # 定义ArgumentParser实例
    parser = argparse.ArgumentParser(
        prog='数据库备份程序',  # 程序名
        description='备份MySQL数据库',  # 描述
        epilog='这是一个假的数据库备份程序'  # 说明信息
    )

    # 关键字参数
    parser.add_argument('--host', default='localhost', help="主机名或IP地址")
    parser.add_argument('--port', default=3306, type=int, help="端口号")
    parser.add_argument('-u', '--user', required=True, help="用户名")
    parser.add_argument('-p', '--password', required=True, help="密码")
    parser.add_argument('--database', required=True, help="数据库名称")
    parser.add_argument('-gz', '--gzcompress', action='store_true', help='是否压缩备份文件 (.gz 格式)')

    # 位置参数
    parser.add_argument('outfile', help="备份文件保存路径")

    # 解析参数
    args = parser.parse_args()

    # 打印一下命令行里所输入的参数
    print('Parsed arguments:')
    print(f'host        = {args.host}')
    print(f'port        = {args.port}')
    print(f'user        = {args.user}')
    print(f'password    = {args.password}')
    print(f'database    = {args.database}')
    print(f'gzcompress  = {args.gzcompress}')
    print(f'outfile     = {args.outfile}')

    
if __name__ == '__main__':
    main()
