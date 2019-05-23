"""
    ftp 文件服务器
    并发网络功能训练
"""
import sys
from socket import *
from threading import Thread

# 全局变量
HOST = '0.0.0.0'
PORT = 8080
ADDR = (HOST, PORT)
FTP = "/home/tarena/concurrent/FTP"  # 文件库路径


# 将客户端请求功能封装为类
class FtpServer:
    def __init__(self):
        pass


def handle(connfd):
    """
        客户端请求处理函数
    :return:
    """
    cls = connfd.recv(1024).decode()
    FTP_PATH = FTP + cls + '/'
    while True:
        data = connfd.recv(1024).decode()
        print(FTP_PATH, data)


def main():
    """
        网络搭建
    :return:
    """
    # 创建套接字
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(ADDR)
    sockfd.listen(5)
    print("Listen the port 8080...")
    # 循环等待接收客户端链接
    while True:
        try:
            connfd, addr = sockfd.accept()
        except KeyboardInterrupt:
            print("服务器退出")
            return
        except Exception as e:
            print(e)
            continue
        print("链接的客户端: ", addr)
        # 创建新的线程处理客户端请求

        client = Thread(target=handle, args=(connfd,))
        client.setDaemon(True)  # 主线程退出,分支线程一并退出
        client.start()


if __name__ == '__main__':
    main()
