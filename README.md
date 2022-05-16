# sphinx-ext-napoleon-snakerpy
Sphinx odc SnakerPy docstring support by ext napoleon

napoleon是sphinx原生的版本（1.8.1），napoleon_snakerpy是扩展支持SnakerPy注释规范的插件(1.8.1版本)


# 1.8.1版本的按照使用方法

## 安装

将napoleon_snakerpy复制到Sphinx扩展目录下，路径参考如下：

C:\Users\hi.li\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\sphinx\ext\



## 使用

修改配置文件增加插件参数：

```
# 增加'sphinx.ext.napoleon_snakerpy'插件支持
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon_snakerpy'
]

# 增加Napoleon配置
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_snakerpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_use_keyword = True
napoleon_custom_sections = None
```

# 4.5.0版本的安装使用方法

## 安装
将"4.5.0支持"目录下的"ext"目录整个复制到您要处理的docs目录下

## 使用
修改sphinx的source/conf.py文件，修改以下几个点:
1、增加snakerpy的注释类型支持插件搜索路径

```
# 增加snakerpy的注释类型支持插件搜索路径
sys.path.append(
    os.path.join(os.path.dirname(__file__), os.path.pardir, 'ext')
)
```

2、在extensions数组增加插件：

```
# 增加'napoleon_snakerpy'插件支持
extensions = [
    ...
    'napoleon_snakerpy'
]

# 在增加插件napoleon_snakerpy的配置
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_snakerpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_use_keyword = True
napoleon_custom_sections = None
```

