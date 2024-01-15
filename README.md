# openssl-base64 for python
&emsp;&emsp;这个项目用于实现base64位加密文件的工具。

## 安装方法:
*&emsp;&emsp;暂未发布至pip。
## 依赖库安装:
&emsp;&emsp;除了tqdm需要手动安装外，其他库均为内建标准库。
```bash
pip install tqdm
```

# 主要功能
&emsp;&emsp;执行openssl base64命令，实现base64加密。
```bash
openssl base64 -in filename -out filename
```

# 待实现的功能：
&emsp;&emsp;执行openssl base64命令，实现base64解密，
```bash
openssl base64 -in filename -out filename -d