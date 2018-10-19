# sphinx-ext-napoleon-snakerpy
Sphinx odc SnakerPy docstring support by ext napoleon

napoleon是sphinx原生的版本（1.8.1），napoleon_snakerpy是扩展支持SnakerPy注释规范的插件



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



