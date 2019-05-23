from socket import *


# 具体功能
class FtpClient:
    pass


# 发起请求
def request(sockfd):
    while True:
        print("\n=======命令选项========")
        print("******** list ********")
        print("****** get file ******")
        print("****** put file ******")
        print("******** quit ********")
        print("=======================")

        cmd = input("输入命令:")
        if cmd == 'list':
            sockfd.send(cmd.encode())


# 网络链接
def main():
    # 服务器地址
    ADDR = ('127.0.0.1', 8080)
    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print("链接服务器失败")
        return
    else:
        print("""******************************************
                    Data          File          Image
                 ******************************************
        """)
        cls = input("请输入想要文件类别: ")
        if cls not in ['Data', 'File', 'Image']:
            print("Sorry input Error!!")
            return
        else:
            sockfd.send(cls.encode())
            request(sockfd)


if __name__ == '__main__':
    main()
