import os.path
import sys

sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath('./考勤程序'))
sys.path.append(os.path.abspath('./考勤程序/utils'))
from 考勤程序 import server, service
from 考勤程序.utils import setting_utils, file_utils

settings = setting_utils.read_settings()
TO_FILE = "考勤总表.xlsx"


def init():
    """
    初始化：
    复制文件
    """
    source_file = service.get_read_file()
    to_file = settings['save_folder'] + "/" + TO_FILE
    file_utils.copy_file(source_file, to_file)


if __name__ == '__main__':
    init()
    server.app.run(debug=True)
