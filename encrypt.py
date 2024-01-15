import os
import sys
import re
import subprocess
import time
import tqdm

# 测试文件夹：D:\CZS4\1
# 错误码说明：负数表示出现了一个错误，正整数表示出现了一个异常，0表示正常退出。
# 错误码汇总:-1表示用户未输入正确的文件夹位置。-2 表示用户输入了错误的文本，强制退出。
# 1 表示由用户主动退出程序。0表示正常退出（无干预）

work_dir = input("请输入工作目录:")
"""
由用户输入新的工作目录，之后所有的项目都会在那里展开。
"""

# region 校对输入的文本。
# 判断用户输入的工作目录是否存在。
if (os.path.isdir(work_dir)):
    os.chdir(work_dir)
else:
    print("您输入了错误的文件夹路径，程序将终止！")
    sys.exit(-1)  # 错误码-1表示用户在初始化时未输入正确的文件夹位置。
# endregion

# 遍历目录里的所有文件。
"""
扫描工作目录，从中取得os.DirEntry对象的序列。
与os.DirEntry的条目相关的内容使用os.scandir()方法。
"""
fileobj = os.scandir(work_dir)

# region 获取工作区的文件列表，并决定是否继续加密流程。
# 将指定路径的所有文件存储到file_list列表中:
file_list = []
"""
供后续加密过程中处理文件。
"""
for entry in fileobj:
    if entry.is_file():
        file_list.append(entry.name)

# print(file_list,"\n",f"file_list的长度为:{len(file_list)}")  # 测试代码。

for a in file_list:
    print(a)
print("恭喜，已经找到了所有文件。请您再检查一次，确保没有不需要加密的文件后，输入ok。")
print("否则，请输入不需要加密的完整文件名（包括文件扩展名）。")
print("我们会将您输入的文件名添加到忽略列表中。")
print("输入exit表示放弃加密。输入continue表示继续。")
abort = input("是否继续？")  # 可能会出现意外输入的空格，可以自动忽略
if abort == "continue":
    pass
elif abort == "exit":
    print("请复制错误代码，联系作者。")
    sys.exit(1)  # 1 表示由用户主动退出程序。0表示正常退出（无干预）
else:
    print("请复制错误代码，联系作者。")
    sys.exit(-2)  # -2 表示用户输入了错误的文本，强制退出。

# endregion

# region 选择要忽略的文件。
ignoreList = []
"""
用于接收输入的信息，以此接收需要忽略的文件。
"""

doing = True
"""
决定while循环是否继续。
"""

# 下方的循环用于添加要忽略的文件到ignoreList[]（忽略文件列表）
while doing:
    f = input("请输入要忽略的文件。如果没有需要忽略的文件，请输入ok。输入cancel中止程序。文件名格式：文件名.后缀 \n")
    if f == "ok" or f == "":
        doing = False
    elif f == "cancel":
        sys.exit(1)  # 1 表示由用户主动退出程序。0表示正常退出（无干预）
    else:
        file_name = f
        # 最多三级嵌套。
        absolute_path = os.path.isfile(os.path.join(work_dir + os.sep + file_name))
        is_file = absolute_path
        if is_file and file_name not in ignoreList:
            ignoreList.append(file_name)
        else:
            print("输入的内容只能是文件，或者你输入了重复的内容。") # 仅列出警告，不必中止。因为此时并未添加任何错误信息。

# print(mp4file,"\n",f"mp4file的长度为:{len(mp4file)}")  # 测试代码
# print(ignoreList)  # 测试代码
# print(f"ignoreList的长度为：{len(ignoreList)}")  # 测试代码

def not_in_file_list(item, list_name):
    """
    判断item是否存在于list_name。
    :param item: 被检查的列表。
    :param list_name: 从属列表。
    :return: 如果item不在list_name中，返回True。否则，返回False。
    """
    if item not in list_name:  # 不在列表
        return True
    else:  # 在列表
        return False


readyToConvertList = list()
"""
最终用于转换的文件列表。
"""

for i, x in enumerate(file_list):
    if not_in_file_list(file_list[i], ignoreList):
        readyToConvertList.append(x)
# endregion

# print(readyToConvertList)  # 测试代码
# print(f"readyToConvertList的长度为:{len(readyToConvertList)}")  # 测试代码

# region 开始执行 openssl base64 命令，以此加密文件。
suffix = ".enc"
"""
指定加密后的文件后缀为".enc"。
"""
subArgs = ['openssl', 'base64', '-in', 'filename', '-out', 'outfilename']
encDir = input('请设置加密文件的存放位置:')
# 思路：先检查路径是否存在，再检查是否为文件夹。
if os.path.exists(encDir):
    if os.path.isdir(encDir):
        pass
    else:
        sys.exit(-1)
else:
    os.mkdir(encDir)

for file in tqdm.tqdm(readyToConvertList):
    # print(file + suffix)
    file_suf = file + suffix
    subArgs[3] = file
    subArgs[5] = encDir + os.sep + file_suf
    # print(subArgs)
    subprocess.Popen(subArgs, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


# endregion
