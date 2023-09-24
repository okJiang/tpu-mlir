import re
import sys
import os
from setuptools import setup, find_packages
from glob import glob
import subprocess

def collect_caffe_dependence():

    cur_dir=os.system("pwd")
    print(cur_dir)

    os.system("cp /usr/lib/x86_64-linux-gnu/libpython3.10.so.1.0 /workspace/tpu-mlir/install/lib")
    os.system("cp /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.74.0 /workspace/tpu-mlir/install/lib")
    os.system("cp /usr/lib/x86_64-linux-gnu/libboost_filesystem.so.1.74.0 /workspace/tpu-mlir/install/lib")
    os.system("cp /usr/lib/x86_64-linux-gnu/libboost_regex.so.1.74.0 /workspace/tpu-mlir/install/lib")
    os.system("cp /usr/lib/x86_64-linux-gnu/libglog.so.0 /workspace/tpu-mlir/install/lib")
    os.system("cp /usr/lib/x86_64-linux-gnu/libgflags.so.2.2 /workspace/tpu-mlir/install/lib")
    os.system("cp /usr/lib/x86_64-linux-gnu/libprotobuf.so.23 /workspace/tpu-mlir/install/lib")
    os.system("cp /usr/lib/x86_64-linux-gnu/libm.so.6 /workspace/tpu-mlir/install/lib")
    os.system("cp /usr/lib/x86_64-linux-gnu/libboost_python310.so.1.74.0 /workspace/tpu-mlir/install/lib")
    os.system("cp /usr/lib/x86_64-linux-gnu/libstdc++.so.6 /workspace/tpu-mlir/install/lib")
    os.system("cp /usr/lib/x86_64-linux-gnu/libgomp.so.1 /workspace/tpu-mlir/install/lib")
    os.system("cp /usr/lib/x86_64-linux-gnu/libz.so.1 /workspace/tpu-mlir/install/lib")
    os.system("cp /usr/lib/x86_64-linux-gnu/libicui18n.so.70 /workspace/tpu-mlir/install/lib")
    os.system("cp /usr/lib/x86_64-linux-gnu/libicuuc.so.70 /workspace/tpu-mlir/install/lib")
    os.system("cp /usr/lib/x86_64-linux-gnu/libunwind.so.8 /workspace/tpu-mlir/install/lib")
    os.system("cp /usr/lib/x86_64-linux-gnu/libpthread.so.0  /workspace/tpu-mlir/install/lib")
    os.system("cp /usr/lib/x86_64-linux-gnu/libgfortran.so.5  /workspace/tpu-mlir/install/lib")
    os.system("cp /usr/lib/x86_64-linux-gnu/liblzma.so.5 /workspace/tpu-mlir/install/lib")
    os.system("cp /usr/lib/x86_64-linux-gnu/libquadmath.so.0 /workspace/tpu-mlir/install/lib")
    os.system("cp /usr/lib/x86_64-linux-gnu/libopenblas.so.0  /workspace/tpu-mlir/install/lib")
    os.system("cp /usr/lib/x86_64-linux-gnu/libgcc_s.so.1  /workspace/tpu-mlir/install/lib")
    os.system("cp /usr/lib/x86_64-linux-gnu/libicudata.so.70  /workspace/tpu-mlir/install/lib")
    os.system("cp /usr/lib/x86_64-linux-gnu/libc.so.6 /workspace/tpu-mlir/install/lib")
    os.system("cp -r /usr/local/python_packages/caffe  /workspace/tpu-mlir/install/lib")
    print("cllect Done")

def release_packages_merge():

    os.system("cp -r /workspace/tpu-mlir/install/lib  /workspace/tpu-mlir/tpu_mlir/")
    os.system("cp -r /workspace/tpu-mlir/install/python  /workspace/tpu-mlir/tpu_mlir/")
    os.system("cp -r /workspace/tpu-mlir/install/docs  /workspace/tpu-mlir/tpu_mlir/")
    os.system("cp -r /workspace/tpu-mlir/install/src   /workspace/tpu-mlir/tpu_mlir/")
    os.system("cp -r /workspace/tpu-mlir/install/bin  /workspace/tpu-mlir/tpu_mlir/")
    os.system("cp -r /workspace/tpu-mlir/regression  /workspace/tpu-mlir/tpu_mlir/")


def iter_shared_objects():
    cur_dir = os.path.abspath(os.path.dirname(sys.argv[0]) or '.')
    for dirpath, dirnames, filenames in os.walk(cur_dir):
        for fn in filenames:
            if fn.endswith('.so'):
                yield os.path.join(dirpath, fn)

#packages = ['tpu_perf']
so_list = list(iter_shared_objects())


def search_files(dir_path):
    """
    获取所有文件
    :param dir_path:文件夹路径
    :return: 该文件夹下的所有文件的列表
    """
    result = []
    file_list = os.listdir(dir_path)  # 获取当前文件夹下的所有文件
    for file_name in file_list:
        complete_file_name = os.path.join(dir_path, file_name)  # 获取包含路径的文件名
        if os.path.isdir(complete_file_name):  # 如果是文件夹
            result.extend(search_files(complete_file_name)) # 文件夹递归
        if os.path.isfile(complete_file_name):  # 文件名判断是否为文件
            result.append(complete_file_name)   # 添加文件路径到结果列表里
            print(complete_file_name)           # 输出找到的文件的路径
    return result

#list1 = list(search_files("/workspace/tpu-mlir/python"))
#list2 = list(search_files("/workspace/tpu-mlir/regression"))
list3 = list(search_files("/workspace/tpu-mlir/tpu_mlir/lib"))

collect_caffe_dependence()
release_packages_merge()
setup(
    name='tpu_mlir',
    version='1.3',
    author='sophgo',
    description='tpu-mlir release pip',
    author_email='dev@sophgo.com',
    license='Apache',



    platforms = 'any',
    url='https://www.sophgo.com/',
   # install_requires=['numpy'],
    #packages=['tpu_mlir_release'],

    include_package_data=True,
    packages=find_packages(),

  #  package_data={'regression': list2},
     package_data={'': list3},
   # py_modules=['__init__'],
   # package_dir={"lib": "tpu_mlir_release"},
     long_description_content_type="text/markdown",



)
