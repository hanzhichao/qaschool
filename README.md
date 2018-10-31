# QA School v1.0
> 使用Django 2.1开发的一款简单的CMS

## 特性
- 模型结构为 栏目（Column）-》 课程（Course）-》 章节
- 后台使用django原生admin
- 集成Editor.md，使用Markdown编辑章节内容
- 可配置栏目是否显示在主导航中
- 栏目，课程，章节可配置是否显示（ToDo）
- 课程章节支持排序，查看时自动生成静态页面

## 使用方法
> 请提前安装Python3环境
- 克隆或下载项目代码，解压，cd进入项目中
- 安装依赖包 `pip install -r requirements.txt`
- 启动开发服务器 python3 manager.py runserver
- 访问 http://127.0.0.1:8000/
- 后台 http://127.0.0.1/admin/ （注意最后必须有'/'） 用户名：hanzhichao 密码 123456 


## 已知问题
- 初始为空时会报错

## ToDo
- 栏目，课程，章节可配置是否显示
- 标签及SEO
- 评论功能
- 点赞功能
- 分享
- 反馈 -》 WeChat
- 采集，html -> md
- 侧边TOC功能
- 代码高亮
- 搜索

2.0会开发独立admin并进行前后端分离

> 使用指导，建议，或bugs, 请微信联系lockingfree 