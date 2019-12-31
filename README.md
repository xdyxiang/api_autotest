#### 技术栈：
* python3   pytest
* ssh mysql
* requests


#### 项目文件说明
- api_request api ：接口封装
- common ：公共文件
- test_case ：测试文件入口
- datafile ：测试数据存放
- verify_response ：检验接口返回结果方法

#### 安装教程
- 安装python3
- 工作目录建立虚拟目录  python -m venv venv
- 激活虚拟环境 ./venv/Scripts/activate
- 安装python包 pip install -r requirements.txt

### 运行用例
- 增加环境变量--env： ```pytest ./test_case  --env dev --html ./report/report.html```
- 1.```pytest ./test_case  -q --html ./report/report.html```
- 2.```pytest ./test_case --verbose --junit-xml ./report/results.xml  --html ./report/report.html```  

#### pytest 参数说明
    
    * -v 用于显示每个测试函数的执行结果
    * -q 只显示整体测试结果
    * -s 用于显示测试函数中print()函数输出
    * -x, --exitfirst, exit instantly on first error or failed test
    * -h 帮助

#### pip备份包到文件
    
    * pip备份包：pip freeze > requirements.txt
    * pip安装包：pip install -r requirements.txt


#### 若有缓存pyc删除： find . -name *.pyc -delete
