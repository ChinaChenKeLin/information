'''
1 创建app
2 定义配置类 添加配置类到app
3 创建db  添加相关配置类
4 创建redis   添加相关配置类
5 创建Session第三方工具 把session保存到服务器内存调整保存到redis库   添加相关配置类
6 创建csrf保护机制
7 创建数据库迁移对象
8 管理对象


单一思想    各司其职

抽取代码：
    配置类Config抽取出来单独一个文件专门配置     准备接口让外界调用

    1-6步抽取出来放init里面包装一个工厂函数 返回app   db对象需要延迟加载app   redis_obj也需要懒加载工外界调用

    数据库迁移和script启动页面

'''

from flask_wtf.csrf import CSRFProtect
from flask import session
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from info import create_app, db


app = create_app('developmentconfig')

CSRFProtect(app)
Migrate(app, db)
manage = Manager(app)
manage.add_command('db', MigrateCommand)



@app.route('/')
def index():
    session['user_name'] = 'zhangsan'
    return 'index'


if __name__ == '__main__':
    manage.run()