## 58小区信息爬虫

<p>
<a href="#"><img src="https://img.shields.io/github/languages/top/tomhaoye/crawler.58" alt="lang"></a>
<a href="#"><img src="https://img.shields.io/badge/Python-3+-green.svg" alt="limit"></a>
<a href="#"><img src="https://img.shields.io/badge/MySQL-5.7-yellow.svg" alt="limit"></a>
<a href="#"><img src="https://img.shields.io/github/languages/code-size/tomhaoye/crawler.58" alt="size"></a>
<a href="#"><img src="https://img.shields.io/github/last-commit/tomhaoye/crawler.58" alt="last"></a>
<a href="#"><img src="https://img.shields.io/github/license/tomhaoye/crawler.58" alt="license"></a>
</p>

### 软件要求
 - Anaconda(可选)
 - python 3.6+
 - mysql 5.7
 
### 安装依赖
```pip install -r requirement```
 
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
 部分城市因为简称会重复所以具体的前缀请上58选择城市后使用二级域名例如```qingyuan.58.com```的```qingyuan```作为参数输入
 
### 配置说明
默认使用```config.example.json```作为配置文件使用，需要编辑对应的数据库信息后才可使用

### 数据库说明
需要先创建数据库，执行时会自动创建数据表

也可以手动建表，具体可见```58crawler.sql```文件

### 截图
![数据库截图](pic/1529899947.jpg)
