# Restful Api文档


## 全部接口
+ POST /register       注册
+ POST /login          登陆
+ POST /flags           创建活动
+ GET /flags/<flag_id>   查看活动
+ GET /flags               查看活动列表
+ DELETE /flags/<flag_id>   删除活动
+ PATCH /flags/<flag_id>   更新活动




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

        { 
            "code":  0
        }

### 登陆
POST /login

1.参数
+ nickname  （Y） 用户名
+ phone     (Y) 手机号码
+ password  (Y) 密码

2. 返回值

        {
            "code":  0
        }
        
### 创建活动
POST /flags

1.参数
+ title (Y) 活动名称
+ content (Y) 活动地点

