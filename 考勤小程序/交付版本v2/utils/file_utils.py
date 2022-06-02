import shutil
import os


def get_files(folder_path):
    """获取文件夹下的所有文件"""
    return os.listdir(folder_path)


def is_file_exist(file):
    """ 判断文件是否存在 """
    return os.path.exists(file)


def copy_file(source_file, to_file):
    """ 复制文件 """
    shutil.copy(source_file, to_file)


if __name__ == '__main__':
    path = "../1-学生名单表"
    print(get_files(path))
