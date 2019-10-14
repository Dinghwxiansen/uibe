# uibe
对外经贸
2.任意项目内根目录输入pip3 install pipenv

          注意：安装的可能比较慢，整个电脑环境此步骤只需要执行一次，并不是每个项目都需要执行
3.绑定项目的pipenv环境，在项目根目录下输入pipenv install，如图所示会自动创建一个虚拟环境
4.根据提示激活虚拟并进入环境输入 pipenv shell
5.根据提示激活虚拟并进入环境输入 pipenv shell
6.常用操作介绍

    pipenv install flask---安装flask库

    pipenv uninstall flask---删除flask库

    pipenv shell ---进入虚拟环境

    exit---推出虚拟环境

   pipenv graph---查看依赖关系

    pipenv --venv---查看虚拟环境名称




WSGI_APPLICATION = 'myweb.wsgi.application'

ROOT_URLCONF = 'myweb.urls'

STATIC_URL = '/static/'
python版本：3.7
django版本：


pip install：
    pymysql
    djangorestframework
    markdown
    django-filter
    coreapi             drf的文档支持
    django-guardian     drf对象级别的权限支持

pip install django-cors-headers   后端跨域

Django REST Framework extensions 配合redis进行缓存
pip install drf-extensions
pip install django-redis
pip install django-redis-cache
https://blog.csdn.net/ros_donggua/article/details/81007919


supervisorctl -c ~/etc/supervisord.conf restart uibe