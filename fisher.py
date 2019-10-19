from flask import  Flask
import config_hzw

__author__ = 'sirius'

app = Flask(__name__)


app.config.from_object('config_hzw')              # 导入配置，通过object  ?? pyinstaller打包后找不到config_hzw
# app.config.from_pyfile(filename='config_hzw.py')    # 导入配置，通过文件
# 配置文件key必须是大写字符，否则不会被载入

print(app.config['DEBUG'])

@app.route("/hello/")      # 装饰器里也是调用add_url_rule方法
def hello():
    return '''
    Hello sirius,
    this is my first Flask project
    '''

app.add_url_rule('/helloo',view_func=hello)

# app.run()
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=app.config.get('DEBUG',False)) # 调试模式，修改文件自动重启