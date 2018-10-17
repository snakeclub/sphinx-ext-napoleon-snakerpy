#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/'+'napoleon/'))
from docstring import SnakerPyDocstring, NumpyDocstring

module_str = u"""
国际化文本处理模块

@module simple_i18n
@file simple_i18n.py
@author <name> [<emailAddress>]
"""

fun_str = u"""
返回指定语言的文本

@param {string} msg_id - 要翻译的语言ID标识
@param {tuple} replace_para=() - 进行占位符替换的变量
@param {string} lang=None - 要翻译的语言，如果不指定则采用初始化对象的默认语言

@returns {string} - 国际化转换后的字符串

"""

if __name__ == '__main__':
    # 当程序自己独立运行时执行的操作
    print('module\r\n------\r\n"""' + module_str + '"""\r\n to ')
    SnakerPyDocstring(docstring=module_str, what='module')
    print('\r\n\r\n')

    print('function\r\n------\r\n"""' + fun_str + '"""\r\n to ')
    SnakerPyDocstring(docstring=fun_str, what='function')
