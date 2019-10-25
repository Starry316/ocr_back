## 后端部分接口
#### 代码有点乱等待整理
#### 全局返回参数
```
  'responseTime': 服务器响应时间 %Y-%m-%d %H:%M:%S"
  'success': 调用是否成功 （True or False） 
  'code': 响应状态码 （见下）
  'status': 响应状态
  'data': 返回的数据
  'message': 相应信息

```

#### 相应状态码定义
```
    Success = 200
    NotLogin = 400
    ResourceExist = 401
    ResourceNotPermit = 403
    ServerError = 500
    ParameterError = 501
```

#### 上传文件
- Method : Post
- Request : 名称为 file 的图片文件
- Response : 
```
{
   image_url : str //图片在服务器上的路径 
}

```
#### 识别
- Method : Get
- Request : 
```
{
    image_url : str //图片在服务器上的路径
}
```
- Response : 
```
{
    text : str //识别结果
}
```