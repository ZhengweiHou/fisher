from flask import  Flask,make_response
import config_hzw

__author__ = 'sirius'

app = Flask(__name__)


app.config.from_object('config_hzw')              # 导入配置，通过object  ?? pyinstaller打包后找不到config_hzw
# app.config.from_pyfile(filename='config_hzw.py')    # 导入配置，通过文件
# 配置文件key必须是大写字符，否则不会被载入

# =============配置路由===========
# 方式1 - 其本质上是方式2的语法糖
@app.route("/hello/")      # 装饰器里也是调用add_url_rule方法
def hello():
    return 'Hello sirius, this is my first Flask project！！！'

# 方式2
app.add_url_rule('/helloo',view_func=hello)


# =============Response===========
@app.route("/hello_resp")
def hello_resp():
    response = make_response('<html><h1>Hello sirius, this is my first Response</h1></html>')
    return response

# 重定向
# 重定向：当响应码为301时，浏览器会再次访问响应头location属性的路径
@app.route("/test301")
def response1():
    headers = {
        'content-type':'applicaton/json',
        'location':'http://www.bing.com'    # 重定向的位置
    }
    response = make_response('<html><h1>Hello sirius</h1></html>', 301) # 响应码301=重定向
    response.headers = headers    # 当响应码为301时，浏览器会再次访问响应头location属性的路径（重定向）
    return response



# app.run()
if __name__ == "__main__":
    app.run(
        host=app.config.get('HOST_IP','0.0.0.0'),
        port=app.config.get('HOST_PORT',5000),
        debug=app.config.get('DEBUG',False) # 调试模式，修改文件自动重
    )