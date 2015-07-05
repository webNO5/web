这是python flask框架及SocialForum项目的所有文件，内含测试服务器和SQLite数据库

——————————————————————————————————————————————————————————————————————
windows环境运行说明：

若要启动服务器，请先将本文件夹内所有文件拷贝到本地的某个目录下（如：D:\SocialForum_V2）

将flask文件夹重新命名（如 flask01）

安装Python解释器并配置环境变量，本项目开发所用的python解释器版本为2.7.6  64位

在命令行内进入含有该项目的路径下（如：D:\SocialForum_V2）

执行>python virtualenv.py flask

用原flask\Lib\site-packages文件夹替换掉当前的flask\Lib\site-packages文件夹（如：用flask01\Lib\site-packages替换掉flask\Lib\site-packages）

执行>flask\Scripts\python run.py  (为保证网站功能，建议在有网络连接的环境下运行)

在浏览器中访问http://localhost:5000

——————————————————————————————————————————————————————————————————————

Linux自带python解释器

运行指令相似
