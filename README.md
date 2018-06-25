## 58小区信息爬虫

### 软件要求
 - Anaconda(可选)
 - python 3.6+
 - mysql 5.7
 
### 目录结构
 - app
   - model
   - util
 - main.py
 - list.py
 - detail.py

### 使用说明
 1. 抓取区域信息 ```python main.py gz```
 2. 抓取列表信息 ```python list.py gz```
 3. 抓取详情数据 ```python detail.py gz```
 
 >参数```gz```为广州的拼音首字母相加，其他城市以此类推。若不输入参数则默认使用广州。
