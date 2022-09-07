## 简介
批量扫描目标url ssl证书名称、开始时间、过期时间

## 运行环境
linux_amd64，可选择编译版或源码版

## 使用方式
1. 把目标url写入txt文件中，每行一个url
2. 运行
```
源码版：python3 sslCAscan txt文件路径
编译版：./sslCAscan txt文件路径
```
```
示例：./sslCAscan url.txt
```
3. 运行结束后在执行路径下保存扫描结果为result.xlsx
