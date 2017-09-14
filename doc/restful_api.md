# Restful Api文档


## 全部接口
+ POST /register       注册
+ POST /login          登陆


## 业务码
+ 0     成功
+ 1     失败


## 接口详情

参数部分，括号()中，Y表示必须的参数

### 注册
POST /register

1.参数
+ nickname  （Y） 用户名
+ phone     (Y) 手机号码
+ password  (Y) 密码

2. 返回值

        { "code":  0 }

### 登陆
POST /login

1.参数
+ nickname  （Y） 用户名
+ phone     (Y) 手机号码
+ password  (Y) 密码

2. 返回值

        { "code":  0 }

