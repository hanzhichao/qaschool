import requests
from tomd import Tomd
from urllib import request
headers = {'user-agent': 'PostmanRuntime/7.3.0'}
# html = requests.get('https://www.jianshu.com/p/4b374b4556c5').text

# with request.urlopen('https://www.jianshu.com/p/4b374b4556c5') as f:
#     html = f.read()

html = '''
<!DOCTYPE html>
<!--[if IE 6]><html class="ie lt-ie8"><![endif]-->
<!--[if IE 7]><html class="ie lt-ie8"><![endif]-->
<!--[if IE 8]><html class="ie ie8"><![endif]-->
<!--[if IE 9]><html class="ie ie9"><![endif]-->
<!--[if !IE]><!--> <html> <!--<![endif]-->

<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=Edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0,user-scalable=no">

  <!-- Start of Baidu Transcode -->
  <meta http-equiv="Cache-Control" content="no-siteapp" />
  <meta http-equiv="Cache-Control" content="no-transform" />
  <meta name="applicable-device" content="pc,mobile">
  <meta name="MobileOptimized" content="width"/>
  <meta name="HandheldFriendly" content="true"/>
  <meta name="mobile-agent" content="format=html5;url=https://www.jianshu.com/p/4b374b4556c5">
  <!-- End of Baidu Transcode -->

    <meta name="description"  content="课程目录 Python接口测试实战1（上）- 接口测试理论Python接口测试实战1（下）- 接口测试工具的使用Python接口测试实战2 - 使用Python发送请求Python接口测试实战3（上）- Python操作数据库Python接口测试实战3（下）- unittest测试框架Python接口测试实战4（上） - 接口测试框架实战Python接口测试实战4（下） - 框架完善：用例基...">

  <meta name="360-site-verification" content="604a14b53c6b871206001285921e81d8" />
  <meta property="wb:webmaster" content="294ec9de89e7fadb" />
  <meta property="qc:admins" content="104102651453316562112116375" />
  <meta property="qc:admins" content="11635613706305617" />
  <meta property="qc:admins" content="1163561616621163056375" />
  <meta name="google-site-verification" content="cV4-qkUJZR6gmFeajx_UyPe47GW9vY6cnCrYtCHYNh4" />
  <meta name="google-site-verification" content="HF7lfF8YEGs1qtCE-kPml8Z469e2RHhGajy6JPVy5XI" />
  <meta http-equiv="mobile-agent" content="format=html5; url=https://www.jianshu.com/p/4b374b4556c5">

  <!-- Apple -->
  <meta name="apple-mobile-web-app-title" content="简书">

    <!--  Meta for Smart App Banner -->
  <meta name="apple-itunes-app" content="app-id=888237539, app-argument=jianshu://notes/32888828">
  <!-- End -->

  <!--  Meta for Twitter Card -->
  <meta content="summary" property="twitter:card">
  <meta content="@jianshucom" property="twitter:site">
  <meta content="Python接口测试实战1（下）- 接口测试工具的使用" property="twitter:title">
  <meta content="课程目录 Python接口测试实战1（上）- 接口测试理论Python接口测试实战1（下）- 接口测试工具的使用Python接口测试实战2 - 使用Python发送请求Pyt..." property="twitter:description">
  <meta content="https://www.jianshu.com/p/4b374b4556c5" property="twitter:url">
  <!-- End -->

  <!--  Meta for OpenGraph -->
  <meta property="fb:app_id" content="865829053512461">
  <meta property="og:site_name" content="简书">
  <meta property="og:title" content="Python接口测试实战1（下）- 接口测试工具的使用">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://www.jianshu.com/p/4b374b4556c5">
  <meta property="og:description" content="课程目录 Python接口测试实战1（上）- 接口测试理论Python接口测试实战1（下）- 接口测试工具的使用Python接口测试实战2 - 使用Python发送请求Python接口测试实战3...">
  <!-- End -->

  <!--  Meta for Facebook Applinks -->
  <meta property="al:ios:url" content="jianshu://notes/32888828" />
  <meta property="al:ios:app_store_id" content="888237539" />
  <meta property="al:ios:app_name" content="简书" />

  <meta property="al:android:url" content="jianshu://notes/32888828" />
  <meta property="al:android:package" content="com.jianshu.haruki" />
  <meta property="al:android:app_name" content="简书" />
  <!-- End -->


    <title>Python接口测试实战1（下）- 接口测试工具的使用 - 简书</title>

  <meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="efvGhXoKhlmrxqEBUblGtGECU7JECxKJ/gZo7eADjkMO0ZciZaMrIA+2cOmQ2YV/3Ru8m0Kq7N2k1haK7L9cqg==" />

  <link rel="stylesheet" media="all" href="//cdn2.jianshu.io/assets/web-bfc15fabb3b20492f7d4.css" />
  
  <link rel="stylesheet" media="all" href="//cdn2.jianshu.io/assets/web/pages/notes/show/entry-f1bfe3a5bcbd20b68049.css" />

  <link href="//cdn2.jianshu.io/assets/favicons/favicon-e743bfb1821442341c3ab15bdbe804f7ad97676bd07a770ccc9483473aa76f06.ico" rel="shortcut icon" type="image/x-icon">
      <link rel="apple-touch-icon-precomposed" href="//cdn2.jianshu.io/assets/apple-touch-icons/57-a6f1f1ee62ace44f6dc2f6a08575abd3c3b163288881c78dd8d75247682a4b27.png" sizes="57x57" />
      <link rel="apple-touch-icon-precomposed" href="//cdn2.jianshu.io/assets/apple-touch-icons/72-fb9834bcfce738fd7b9c5e31363e79443e09a81a8e931170b58bc815387c1562.png" sizes="72x72" />
      <link rel="apple-touch-icon-precomposed" href="//cdn2.jianshu.io/assets/apple-touch-icons/76-49d88e539ff2489475d603994988d871219141ecaa0b1a7a9a1914f4fe3182d6.png" sizes="76x76" />
      <link rel="apple-touch-icon-precomposed" href="//cdn2.jianshu.io/assets/apple-touch-icons/114-24252fe693524ed3a9d0905e49bff3cbd0228f25a320aa09053c2ebb4955de97.png" sizes="114x114" />
      <link rel="apple-touch-icon-precomposed" href="//cdn2.jianshu.io/assets/apple-touch-icons/120-1bb7371f5e87f93ce780a5f1a05ff1b176828ee0d1d130e768575918a2e05834.png" sizes="120x120" />
      <link rel="apple-touch-icon-precomposed" href="//cdn2.jianshu.io/assets/apple-touch-icons/152-bf209460fc1c17bfd3e2b84c8e758bc11ca3e570fd411c3bbd84149b97453b99.png" sizes="152x152" />

  <!-- Start of 访问统计 -->
    <script>
    var _hmt = _hmt || [];
    (function() {
      var hm = document.createElement("script");
      hm.src = "//hm.baidu.com/hm.js?0c0e9d9b1e7d617b3e6842e85b9fb068";
      var s = document.getElementsByTagName("script")[0];
      s.parentNode.insertBefore(hm, s);
    })();
  </script>

  <!-- End of 访问统计 -->
</head>

  <!-- 只给10%的用户添加代码 -->
  <body lang="zh-CN" class="reader-black-font">
    <!-- 全局顶部导航栏 -->
<nav class="navbar navbar-default navbar-fixed-top" role="navigation">
  <div class="width-limit">
    <!-- 左上方 Logo -->
    <a class="logo" href="/"><img src="//cdn2.jianshu.io/assets/web/nav-logo-4c7bbafe27adc892f3046e6978459bac.png" alt="Nav logo" /></a>

    <!-- 右上角 -->
      <!-- 未登录显示登录/注册/写文章 -->
      <a class="btn write-btn" target="_blank" href="/writer#/">
        <i class="iconfont ic-write"></i>写文章
</a>      <a class="btn sign-up" id="sign_up" href="/sign_up">注册</a>
      <a class="btn log-in" id="sign_in" href="/sign_in">登录</a>

    <!-- 如果用户登录，显示下拉菜单 -->

    <div id="view-mode-ctrl">
    </div>
    <div class="container">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#menu" aria-expanded="false">
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
      </div>
      <div class="collapse navbar-collapse" id="menu">
        <ul class="nav navbar-nav">
            <li class="tab ">
              <a href="/">
                <span class="menu-text">首页</span><i class="iconfont ic-navigation-discover menu-icon"></i>
</a>            </li>
            <li class="tab ">
              <a id="web-nav-app-download-btn" class="app-download-btn" href="/apps?utm_medium=desktop&amp;utm_source=navbar-apps"><span class="menu-text">下载App</span><i class="iconfont ic-navigation-download menu-icon"></i></a>
            </li>
          <li class="search">
            <form target="_blank" action="/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
              <input type="text" name="q" id="q" value="" autocomplete="off" placeholder="搜索" class="search-input" />
              <a class="search-btn" href="javascript:void(null)"><i class="iconfont ic-search"></i></a>
</form>          </li>
        </ul>
      </div>
    </div>
  </div>
</nav>

    
<div class="note">
    <a target="_blank" href="/apps/redirect?utm_source=side-banner-click" id="web-note-ad-fixed"><span class="close">&times;</span></a>
  <div class="post">
    <div class="article">
        <h1 class="title">Python接口测试实战1（下）- 接口测试工具的使用</h1>

        <!-- 作者区域 -->
        <div class="author">
          <a class="avatar" href="/u/0115903ded22">
            <img src="//upload.jianshu.io/users/upload_avatars/7575721/5339c9d6-be6b-47cf-87cc-c0517467c6bc.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/96/h/96" alt="96" />
</a>          <div class="info">
            <span class="name"><a href="/u/0115903ded22">韩志超</a></span>
            <!-- 关注用户按钮 -->
            <div props-data-classes="user-follow-button-header" data-author-follow-button></div>
            <!-- 文章数据信息 -->
            <div class="meta">
              <!-- 如果文章更新时间大于发布时间，那么使用 tooltip 显示更新时间 -->
                <span class="publish-time" data-toggle="tooltip" data-placement="bottom" title="最后编辑于 2018.10.16 11:59">2018.08.27 10:02*</span>
              <span class="wordage">字数 3348</span>
            </div>
          </div>
          <!-- 如果是当前作者，加入编辑按钮 -->
        </div>


        <!-- 文章内容 -->
        <div data-note-content class="show-content">
          <div class="show-content-free">
            <h2>课程目录</h2>
<p><a href="https://www.jianshu.com/p/9d3f991c901a" target="_blank">Python接口测试实战1（上）- 接口测试理论</a><br>
<a href="https://www.jianshu.com/p/4b374b4556c5" target="_blank">Python接口测试实战1（下）- 接口测试工具的使用</a><br>
<a href="https://www.jianshu.com/p/e94a18950a53" target="_blank">Python接口测试实战2 - 使用Python发送请求</a><br>
<a href="https://www.jianshu.com/p/736ed1e724f0" target="_blank">Python接口测试实战3（上）- Python操作数据库</a><br>
<a href="https://www.jianshu.com/p/93f0c8b697b7" target="_blank">Python接口测试实战3（下）- unittest测试框架</a><br>
<a href="https://www.jianshu.com/p/90adb21844bd" target="_blank">Python接口测试实战4（上） - 接口测试框架实战</a><br>
<a href="https://www.jianshu.com/p/ed82716eef58" target="_blank">Python接口测试实战4（下） - 框架完善：用例基类，用例标签，重新运行上次失败用例</a><br>
<a href="https://www.jianshu.com/p/4422f38fa140" target="_blank">Python接口测试实战5（上） - Git及Jenkins持续集成</a><br>
<a href="https://www.jianshu.com/p/5dd299c23eb0" target="_blank">Python接口测试实战5（下） - RESTful、Web Service及Mock Server</a></p>
<blockquote>
<p>更多学习资料请加QQ群: 822601020获取</p>
</blockquote>
<h2>本节内容</h2>
<ul>
<li>抓包工具的使用</li>
<li>Postman的使用</li>
</ul>
<h2>抓包工具的使用</h2>
<h3>抓包工具简介</h3>
<ul>
<li>Chrome/Firefox 开发者工具: 浏览器内置，方便易用</li>
<li>Fiddler/Charles: 基于代理的抓包，功能强大，可以手机抓包，模拟弱网，拦截请求，定制响应
<ul>
<li>Fiddler: 免费，只支持Win</li>
<li>Charles: 收费，支持Win/Linux/Mac</li>
</ul>
</li>
<li>wireshark/tcpdumps：给予网卡层的抓包，数据量大，可以抓取tcp/udp等多种协议的数据包（需要做好过滤）
<ul>
<li>wireshark: 支持Win/Linux/Mac</li>
<li>tcpdumps: Linux抓包命令，功能强大，常用作服务端抓包<br>
<strong>什么是代理？</strong><br>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 165px;">
<div class="image-container-fill" style="padding-bottom: 19.88%;"></div>
<div class="image-view" data-width="830" data-height="165"><img data-original-src="//upload-images.jianshu.io/upload_images/7575721-2201dfc3c8e872d9.png" data-original-width="830" data-original-height="165" data-original-format="image/png" data-original-filesize="32440"></div>
</div>
<div class="image-caption">正向代理</div>
</div>
<br>
<strong>正向代理与反向代理</strong><br>
<div class="image-package">
<div class="image-container" style="max-width: 524px; max-height: 661px;">
<div class="image-container-fill" style="padding-bottom: 126.15%;"></div>
<div class="image-view" data-width="524" data-height="661"><img data-original-src="//upload-images.jianshu.io/upload_images/7575721-2811c480056a63d5.png" data-original-width="524" data-original-height="661" data-original-format="image/png" data-original-filesize="53375"></div>
</div>
<div class="image-caption">正向代理与反向代理</div>
</div>
</li>
</ul>
</li>
<li>正向代理中, 代理和客户端在一个局域网内，对服务器透明</li>
<li>反向带来中，代理和服务器在一个局域网内，对客户端透明<br>
例如：使用代理访问Google属于正向代理，通过不同的域名通过Nginx向同一台服务器请求不同的网站属于反向代理</li>
<li>反向代理可以做负载均衡</li>
<li>反省代理接口测试一般要先绑定本地hosts<br>
<strong>怎么手动添加代理?</strong>
</li>
<li>启动代理服务器，如开启Postman的代理服务（本机ip,默认端口5555）</li>
<li>Win设置-&gt;代理 -&gt; 配置代理ip和域名<br>
<strong>手机设置上网代理（手机抓包）</strong>
</li>
<li>笔记本和手机使用同一wifi上网</li>
<li>笔记本上启动代理服务器，如开启Postman的代理服务（本机ip,默认端口5555）</li>
<li>手机上长按wifi-&gt;选择管理网络或高级-&gt; 手动配置代理 -&gt; 配置代理ip和域名<br>
** 绑定hosts(适用于反向代理)**</li>
<li>Win: notepad C:\Windows\System32\drivers\etc\hosts</li>
<li>Linux: vim /etc/hosts<br>
格式： ip 域名</li>
</ul>
<h3>Chrome开发者工具</h3>
<ul>
<li>Elements: HTML元素面板，用于定位查看元素源代码</li>
<li>Console: js控制台面板，js命令行，查看前端日志</li>
<li>Sources: 资源面板，用于断点调试js</li>
<li>
<strong>Network</strong>: 请求信息面板，查看请求及响应信息</li>
<li>Timeline: 时间线面板，记录网站生命周期内所发生的各类事件</li>
<li>Profiles: 事件详情面板</li>
<li>Application: 本地存储，Session存储等资源信息</li>
<li>Secuity: 判断当前网页是否安全</li>
<li>Audits: 网络性能诊断</li>
</ul>
<p><strong>Network面板</strong><br>
</p><div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 512px;">
<div class="image-container-fill" style="padding-bottom: 51.2%;"></div>
<div class="image-view" data-width="1000" data-height="512"><img data-original-src="//upload-images.jianshu.io/upload_images/7575721-284b8e2030d275a8.png" data-original-width="1000" data-original-height="512" data-original-format="image/png" data-original-filesize="102522"></div>
</div>
<div class="image-caption">Network面板</div>
</div><p></p>
<ol>
<li>Console: 外观及功能控制
<ul>
<li>录制：记录或停止记录请求</li>
<li>清空： 清空所有请求</li>
<li>抓取快照：按帧捕获屏幕事件</li>
<li>过滤: 请用关闭过滤功能</li>
<li>搜索：搜索请求</li>
<li>Group by frame：按框架分组</li>
<li>Preserve log：页面重载时保留请求</li>
<li>Disable cache：禁用缓存</li>
<li>Offline：断网及弱网模拟</li>
</ul>
</li>
<li>Filters: 请求过滤器</li>
<li>Overview: 资源时间轴</li>
<li>Requests Table: 请求列表
<ul>
<li>Name: 资源名称</li>
<li>Status: HTTP状态码</li>
<li>Initiator: 请求源</li>
<li>Size: 从服务器下载的文件和请求的资源大小。如果是从缓存中取得的资源则该列会显示(from cache)</li>
<li>Timeline: 显示所有网络请求时间状态轴</li>
</ul>
</li>
<li>Summary: 请求总数，数据传输量，加载时间信息
<ul>
<li>DOMContentLoaded：页面上DOM完全加载并解析完毕</li>
<li>load：页面上所有DOM、CSS、JS、图片完全加载完毕</li>
</ul>
</li>
</ol>
<blockquote>
<p>导出请求：右击请求 -&gt; Copy -&gt; Copy as fetch / Copy as cUrl</p>
</blockquote>
<h3>Fiddler简介</h3>
<blockquote>
<p>Fiddler 4.6 下载 <a href="http://www.downza.cn/soft/234727.html" target="_blank" rel="nofollow">http://www.downza.cn/soft/234727.html</a></p>
</blockquote>
<p><strong>为什么使用Fiddler?</strong></p>
<ul>
<li>可以抓到请求数据，查看Raw格式/表单格式/Json/XML格式</li>
<li>可以拦截和修改请求</li>
<li>更强大的过滤器</li>
<li>可以抓取Postman/接口脚本发送的请求，方便调试</li>
<li>可以抓包手机请求 ...</li>
</ul>
<p><strong>Fiddler主界面</strong><br>
Fiddler的主界面分为 工具面板、会话面板、监控面板、状态面板<br>
</p><div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 413px;">
<div class="image-container-fill" style="padding-bottom: 59.0%;"></div>
<div class="image-view" data-width="1688" data-height="996"><img data-original-src="//upload-images.jianshu.io/upload_images/947566-66f000394932159c.jpg" data-original-width="1688" data-original-height="996" data-original-format="" data-original-filesize="670254"></div>
</div>
<div class="image-caption">Fiddler主界面</div>
</div><p></p>
<ul>
<li>
<strong>Inspectors</strong>: 检查员
<ul>
<li>Raw：请求的原始格式</li>
<li>WebForm: 请求的表单格式</li>
<li>Json：请求的Json格式请求</li>
<li>XML：请求的XML格式</li>
</ul>
</li>
<li>AutoResponsder: 自动回复，可用于构造响应，Mock，不修改服务器文件调试接口</li>
<li>
<strong>Composer</strong>: 设计者, 发送和调试请求</li>
<li>FidderScript:</li>
<li>
<strong>Filters</strong>: 过滤器
<ul>
<li>Hosts: 按服务器过滤</li>
<li>Clients Process: 按客户端程序过滤</li>
<li>Request Headers: 按请求头过滤</li>
<li>Breakpoints: 设置断点</li>
<li>Response Status Code: 按状态码过滤</li>
<li>Response Type and Size: 按响应类型及大学过滤</li>
<li>Response Headers: 按响应头过滤<br>
<strong>自动断点设置</strong><br>
菜单Rules -&gt; Automatic Breakpoints -&gt; Before Requests/After Requests<br>
<strong>手机抓包</strong><br>
安装fiddler的笔记本和手机使用同一wifi -&gt; 手机长按该wifi,选择高级 -&gt; 添加代理 ip为笔记本ip, 端口为8888 -&gt; 笔记本开启fiddler, 手机端访问网页</li>
</ul>
</li>
</ul>
<blockquote>
<p>参考： <a href="https://www.cnblogs.com/conquerorren/p/8472285.html#" target="_blank" rel="nofollow">Fiddler详细教程</a></p>
</blockquote>
<h3>服务端抓包 - tcpdumps</h3>
<h2>Postman的使用</h2>
<h3>常见接口测试工具</h3>
<ul>
<li>Postman: 简单方便的接口调试工具，便于分享和协作。具有接口调试，接口集管理，环境配置，参数化，断言，批量执行，录制接口，Mock Server, 接口文档，接口监控等功能</li>
<li>JMeter: 开源接口测试及压测工具，支持Linux及无界面运行</li>
<li>LR: 商业版接口性能测试工具，简单易用，功能强大</li>
<li>SoupUI: 开源，WebService接口常用测试工具，也可以测试Rest接口及接口安全</li>
</ul>
<h3>新版Postman使用简介</h3>
<blockquote>
<p>Postman 6.1.4 独立安装版 下载 <a href="http://www.downza.cn/soft/205171.html" target="_blank" rel="nofollow">http://www.downza.cn/soft/205171.html</a></p>
</blockquote>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 473px;">
<div class="image-container-fill" style="padding-bottom: 67.58%;"></div>
<div class="image-view" data-width="1055" data-height="713"><img data-original-src="//upload-images.jianshu.io/upload_images/7575721-7e55bae965258ea6.png" data-original-width="1055" data-original-height="713" data-original-format="image/png" data-original-filesize="57797"></div>
</div>
<div class="image-caption">Postman主界面</div>
</div>
<p><strong>工具栏</strong></p>
<ul>
<li>New: 新建，可以新建Request请求，Collection请求集，环境等等</li>
<li>Import: 导入，可以导入别人导出的请求集</li>
<li>Runner: 运行一个请求集（批量执行）</li>
<li>Invite: 邀请（需要注册，邀请进行协作）</li>
<li>同步图标： （需要注册，同步你的项目到云端）</li>
<li>抓包图标： 抓包/捕获请求，用于开启Postman代理， 手动设置代理（或手机代理）后可抓包/录制请求</li>
<li>设置图标： Postman设置</li>
<li>消息图标： 官方及协助消息</li>
<li>收藏图标： 我的收藏（需要注册）</li>
<li>云端图标： 用户云端数据（需要注册）</li>
</ul>
<p><strong>接口管理区</strong></p>
<ul>
<li>History: 请求历史记录，可以查询到之前的请求记录</li>
<li>Collections: 接口集，相当于一个接口项目或测试计划，接口集中可以建立无限极子文件夹，用于对接口进行分组管理</li>
</ul>
<p><strong>环境管理区</strong></p>
<ul>
<li>环境切换：用于切换环境</li>
<li>环境预览：用于快速预览环境中的所有变量</li>
<li>环境管理：用于添加修改环境及环境变量，以及全局变量</li>
</ul>
<p><strong>什么是环境</strong><br>
接口完整地址 = 服务地址 + 接口地址， 如</p>
<pre><code>www.sojson.com + /open/api/weather/json.shtml
</code></pre>
<p>环境是一套配置，包含许多环境变量。在接口测试中，根据部署在不同的服务器上，服务器地址有可能不同，而同一个接口，接口地址是不变的。为了测试部署在不同服务器上的同一套接口，我们可以建立不同的环境，不同环境中host变量使用不同的地址</p>
<p><strong>接口设计区</strong><br>
可以通过上方tab边上的+号，新建多个请求。接口设计区从上到下分为请求区和响应区</p>
<ul>
<li>请求区
<ul>
<li>请求地址行：可以选择请求方法（GET/POST/...），填写请求地址，发送请求和保存请求到测试集</li>
<li>请求数据区：分为授权，请求头，请求数据，请求发送前执行的脚本（用于准备数据），请求结束后执行的脚本（用于断言）</li>
</ul>
</li>
<li>响应区：
<ul>
<li>响应内容： 可以查看Pretty（美化格式），Raw（原始格式），Preview（HTML预览格式）</li>
<li>响应Cookie</li>
<li>响应头</li>
<li>测试结果，对应请求中Tests中设置的断言</li>
</ul>
</li>
</ul>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 473px;">
<div class="image-container-fill" style="padding-bottom: 67.58%;"></div>
<div class="image-view" data-width="1055" data-height="713"><img data-original-src="//upload-images.jianshu.io/upload_images/7575721-b54bbb849d1aa12a.png" data-original-width="1055" data-original-height="713" data-original-format="image/png" data-original-filesize="99843"></div>
</div>
<div class="image-caption">Postman主界面功能</div>
</div>
<p><strong>Collection请求集</strong><br>
测试集是Postman中接口管理的一个“整体”单位，运行、导出、分享等都是基于测试集的。</p>
<ul>
<li>
<p>新建测试集： New按钮-&gt;Collection 或 直接点击测试集列表上方的新建测试集按钮</p>
<br>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 473px;">
<div class="image-container-fill" style="padding-bottom: 67.58%;"></div>
<div class="image-view" data-width="1055" data-height="713"><img data-original-src="//upload-images.jianshu.io/upload_images/7575721-9ac1ac3adb615c13.png" data-original-width="1055" data-original-height="713" data-original-format="image/png" data-original-filesize="63469"></div>
</div>
<div class="image-caption">新建测试集</div>
</div>
<ul>
<li>授权： 测试集及其子文件夹下的接口统一使用该授权，不用每个接口再都单独设置一遍</li>
<li>请求前脚本： 测试集的每个接口公用的请求前脚本</li>
<li>请求后断言： 测试集每个接口公用的请求后脚本</li>
<li>请求集变量： 请求集中公用的一些变量</li>
</ul>
</li>
<li>子文件夹<br>
子文件夹的属性中同样拥有描述，授权，请求前脚本，和请求后断言（没有变量，一个请求集的变量统一管理），实现了不同范围（Scope）的Fixture功能。</li>
<li>请求集导出：请求集可以导出并发送给别人（不携带环境信息），别人通过导入来使用你的接口</li>
<li>请求集分享： 请求集直接分享给别人（双方都需要注册）</li>
</ul>
<p>** 环境管理**</p>
<br>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 473px;">
<div class="image-container-fill" style="padding-bottom: 67.58%;"></div>
<div class="image-view" data-width="1055" data-height="713"><img data-original-src="//upload-images.jianshu.io/upload_images/7575721-9a1cb4b7a504bba5.png" data-original-width="1055" data-original-height="713" data-original-format="image/png" data-original-filesize="78540"></div>
</div>
<div class="image-caption">新建环境</div>
</div><br>
<p>我们可以环境中设置多个变量，以供在请求中使用<br>
环境变量使用方法：<br>
选择环境，在请求URL或者请求Body里使用{{变量名}}来使用环境变量，变量可以在请求Body的各种格式中使用，但不能直接在请求前脚本（Pre-request Script）和请求后脚本（Tests）中使用</p>
<br>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 473px;">
<div class="image-container-fill" style="padding-bottom: 67.58%;"></div>
<div class="image-view" data-width="1055" data-height="713"><img data-original-src="//upload-images.jianshu.io/upload_images/7575721-b2d8bf07fbd2cd29.png" data-original-width="1055" data-original-height="713" data-original-format="image/png" data-original-filesize="73146"></div>
</div>
<div class="image-caption">环境变量的使用</div>
</div>
<p>环境管理中还可以点击“Global”添加全局变量，环境变量只有当选择了该环境时生效，全局变量在任何环境中生效，测试集中的变量只在当前测试集生效，当测试集变量，环境变量，全局变量有重复的变量名时，优先级为：环境变量&gt;全局变量&gt;测试集变量<br>
<strong>Params使用</strong><br>
当请求URL中参数很多时，不方便进行添加和查看，可以点击URL输入框后的Params按钮，以表格的方式添加变量及值，从表格添加后，变量和值会自动添加到URL中<br>
</p><div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 513px;">
<div class="image-container-fill" style="padding-bottom: 73.36%;"></div>
<div class="image-view" data-width="1055" data-height="774"><img data-original-src="//upload-images.jianshu.io/upload_images/7575721-eba92e50a1c61d3e.png" data-original-width="1055" data-original-height="774" data-original-format="image/png" data-original-filesize="82973"></div>
</div>
<div class="image-caption">添加URL参数</div>
</div><p></p>
<p><strong>请求设计</strong></p>
<ul>
<li>授权：如果接口需要授权，可以在该页面设置授权方式（type）和授权信息</li>
<li>Header: 请求头，可以设置请求类型（Content-Type）和Cookie</li>
<li>Body: 请求数据
<ul>
<li>form-data：混合表单，支持上传文件</li>
<li>x-www-form-urlencoded：文本表单</li>
<li>raw：原始格式，支持JSON/XML格式（后面可选择）</li>
<li>binary: 二进制格式，用于发送二进制数据流</li>
</ul>
</li>
<li>Pre-request Script: 请求前脚本，Javascript语法，用于在发送请求前生成一些动态数据或做一些处理</li>
<li>Tests：请求后脚本，Javascript语法，用于请求返回后做一些处理或断言结果</li>
</ul>
<p><strong>Postman发送各种格式请求的方法：</strong><br>
注意：选择不同的请求可是，会自动在Header中添加Content-Type信息<br>
</p><div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 513px;">
<div class="image-container-fill" style="padding-bottom: 73.36%;"></div>
<div class="image-view" data-width="1055" data-height="774"><img data-original-src="//upload-images.jianshu.io/upload_images/7575721-aa9a6a944329899f.png" data-original-width="1055" data-original-height="774" data-original-format="image/png" data-original-filesize="114186"></div>
</div>
<div class="image-caption">混合表单请求</div>
</div><br>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 605px;">
<div class="image-container-fill" style="padding-bottom: 86.53999999999999%;"></div>
<div class="image-view" data-width="1055" data-height="913"><img data-original-src="//upload-images.jianshu.io/upload_images/7575721-fbde5d4494c45f93.png" data-original-width="1055" data-original-height="913" data-original-format="image/png" data-original-filesize="117291"></div>
</div>
<div class="image-caption">传统表单请求</div>
</div><br>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 513px;">
<div class="image-container-fill" style="padding-bottom: 73.36%;"></div>
<div class="image-view" data-width="1055" data-height="774"><img data-original-src="//upload-images.jianshu.io/upload_images/7575721-995b11203be4c69b.png" data-original-width="1055" data-original-height="774" data-original-format="image/png" data-original-filesize="88460"></div>
</div>
<div class="image-caption">JSON格式请求</div>
</div><br>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 513px;">
<div class="image-container-fill" style="padding-bottom: 73.36%;"></div>
<div class="image-view" data-width="1055" data-height="774"><img data-original-src="//upload-images.jianshu.io/upload_images/7575721-ce3ddb66be5aaa69.png" data-original-width="1055" data-original-height="774" data-original-format="image/png" data-original-filesize="90736"></div>
</div>
<div class="image-caption">XML请求</div>
</div><p></p>
<p><strong>Tests断言</strong></p>
<ul>
<li>HTTP状态码断言:</li>
</ul>
<pre><code>tests["HTTP状态码200"]=responseCode.code == 200;
</code></pre>
<ul>
<li>响应包含内容断言：</li>
</ul>
<pre><code>tests["状态码200"] = responseBody.has("登录成功");
</code></pre>
<p>接口样例：<br>
POST  <a href="https://demo.fastadmin.net/admin/index/login.html" target="_blank" rel="nofollow">https://demo.fastadmin.net/admin/index/login.html</a>   用户名/密码： admin/123456<br>
</p><div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 694px;">
<div class="image-container-fill" style="padding-bottom: 99.24%;"></div>
<div class="image-view" data-width="1055" data-height="1047"><img data-original-src="//upload-images.jianshu.io/upload_images/7575721-4a5ba14efb542088.png" data-original-width="1055" data-original-height="1047" data-original-format="image/png" data-original-filesize="115632"></div>
</div>
<div class="image-caption">接口样例</div>
</div><br>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 694px;">
<div class="image-container-fill" style="padding-bottom: 99.24%;"></div>
<div class="image-view" data-width="1055" data-height="1047"><img data-original-src="//upload-images.jianshu.io/upload_images/7575721-81d6af50b1f4132b.png" data-original-width="1055" data-original-height="1047" data-original-format="image/png" data-original-filesize="96091"></div>
</div>
<div class="image-caption">断言方法</div>
</div><p></p>
<ul>
<li>JSON响应断言</li>
</ul>
<pre><code>var jsonData = JSON.parse(responseBody);
tests["code为200"] = jsonData.code==200
tests["msg为success"] = jsonData.msg == "success"
</code></pre>
<p>接口样例：<br>
GET <a href="http://www.tuling123.com/openapi/api?key=ec961279f453459b9248f0aeb6600bbe&amp;info=" target="_blank" rel="nofollow">http://www.tuling123.com/openapi/api?key=ec961279f453459b9248f0aeb6600bbe&amp;info=</a>你好<br>
</p><div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 616px;">
<div class="image-container-fill" style="padding-bottom: 49.36%;"></div>
<div class="image-view" data-width="1248" data-height="616"><img data-original-src="//upload-images.jianshu.io/upload_images/7575721-f5fb65c4afac83c3.png" data-original-width="1248" data-original-height="616" data-original-format="image/png" data-original-filesize="79103"></div>
</div>
<div class="image-caption">JSON响应断言</div>
</div><p></p>
<p><strong>Runner: 测试集批量执行</strong></p>
<ul>
<li>支持设置迭代次数</li>
<li>支持加载csv或json类测试数据<br>
操作方法：<br>
如<a href="https://demo.fastadmin.net/admin/index/login.html" target="_blank" rel="nofollow">https://demo.fastadmin.net/admin/index/login.html</a>接口</li>
<li>新建一个Collection，比如名称Demo2</li>
<li>填入URL：<a href="https://demo.fastadmin.net/admin/index/login.html" target="_blank" rel="nofollow">https://demo.fastadmin.net/admin/index/login.html</a>， 选择POST方法</li>
<li>
<p>请求数据（Body）格式选x-www-form-urlecoded，请求数据填写username   {{username}}  password  {{password}}，这里使用了两个变量来做参数化</p>
<br>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 616px;">
<div class="image-container-fill" style="padding-bottom: 49.36%;"></div>
<div class="image-view" data-width="1248" data-height="616"><img data-original-src="//upload-images.jianshu.io/upload_images/7575721-584b98ec14d6bb70.png" data-original-width="1248" data-original-height="616" data-original-format="image/png" data-original-filesize="81949"></div>
</div>
<div class="image-caption">请求设置</div>
</div>
</li>
<li>保存请求到Demo2中</li>
<li>
<p>在电脑上新建一个data.csv文件，第一行为变量名，下面是数据，如下图</p>
<br>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 616px;">
<div class="image-container-fill" style="padding-bottom: 49.36%;"></div>
<div class="image-view" data-width="1248" data-height="616"><img data-original-src="//upload-images.jianshu.io/upload_images/7575721-32602f0ba05c840e.png" data-original-width="1248" data-original-height="616" data-original-format="image/png" data-original-filesize="93075"></div>
</div>
<div class="image-caption">数据文件</div>
</div>
</li>
<li>
<p>点击Postman工具栏的Runner按钮，Collection选择Demo2， Data选择数据文件data.csv， 点击运行Demo2</p>
<br>
<div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 461px;">
<div class="image-container-fill" style="padding-bottom: 65.86%;"></div>
<div class="image-view" data-width="1280" data-height="843"><img data-original-src="//upload-images.jianshu.io/upload_images/7575721-095ad8df66066b3c.png" data-original-width="1280" data-original-height="843" data-original-format="image/png" data-original-filesize="60933"></div>
</div>
<div class="image-caption">Runner配置</div>
</div>
</li>
</ul>
<h2><div class="image-package">
<div class="image-container" style="max-width: 700px; max-height: 461px;">
<div class="image-container-fill" style="padding-bottom: 65.86%;"></div>
<div class="image-view" data-width="1280" data-height="843"><img data-original-src="//upload-images.jianshu.io/upload_images/7575721-84fc8a278d88f30a.png" data-original-width="1280" data-original-height="843" data-original-format="image/png" data-original-filesize="111865"></div>
</div>
<div class="image-caption">运行结果</div>
</div></h2>
<blockquote>
<p>个人微信号： lockingfree， 如有问题，欢迎交流</p>
</blockquote>

          </div>
        </div>
    </div>

    <!-- 如果是付费文章，未购买，则显示购买按钮 -->

    <!-- 连载目录项 -->

    <!-- 如果是付费文章 -->
      <!-- 如果是付费连载，已购买，且作者允许赞赏，则显示付费信息和赞赏 -->
        <div data-vcomp="free-reward-panel"></div>

      <div class="show-foot">
        <a class="notebook" href="/nb/26739010">
          <i class="iconfont ic-search-notebook"></i>
          <span>Python接口测试</span>
</a>        <div class="copyright" data-toggle="tooltip" data-html="true" data-original-title="转载请联系作者获得授权，并标注“简书作者”。">
          © 著作权归作者所有
        </div>
        <div class="modal-wrap" data-report-note>
          <a id="report-modal">举报文章</a>
        </div>
      </div>

      <!-- 文章底部作者信息 -->
        <div class="follow-detail">
          <div class="info">
            <a class="avatar" href="/u/0115903ded22">
              <img src="//upload.jianshu.io/users/upload_avatars/7575721/5339c9d6-be6b-47cf-87cc-c0517467c6bc.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/96/h/96" alt="96" />
</a>            <div props-data-classes="user-follow-button-footer" data-author-follow-button></div>
            <a class="title" href="/u/0115903ded22">韩志超</a>
          </div>
            <div class="signature">专注于分享系统的软件测试知识及课程
微信：lockingfree</div>
        </div>

    <div class="meta-bottom">
      <div class="btn like-group"></div>
      <div class="share-group">
        <a class="share-circle" data-action="weixin-share" data-toggle="tooltip" data-original-title="分享到微信">
          <i class="iconfont ic-wechat"></i>
        </a>
        <a class="share-circle" data-action="weibo-share" data-toggle="tooltip" href="javascript:void((function(s,d,e,r,l,p,t,z,c){var%20f=&#39;http://v.t.sina.com.cn/share/share.php?appkey=1881139527&#39;,u=z||d.location,p=[&#39;&amp;url=&#39;,e(u),&#39;&amp;title=&#39;,e(t||d.title),&#39;&amp;source=&#39;,e(r),&#39;&amp;sourceUrl=&#39;,e(l),&#39;&amp;content=&#39;,c||&#39;gb2312&#39;,&#39;&amp;pic=&#39;,e(p||&#39;&#39;)].join(&#39;&#39;);function%20a(){if(!window.open([f,p].join(&#39;&#39;),&#39;mb&#39;,[&#39;toolbar=0,status=0,resizable=1,width=440,height=430,left=&#39;,(s.width-440)/2,&#39;,top=&#39;,(s.height-430)/2].join(&#39;&#39;)))u.href=[f,p].join(&#39;&#39;);};if(/Firefox/.test(navigator.userAgent))setTimeout(a,0);else%20a();})(screen,document,encodeURIComponent,&#39;&#39;,&#39;&#39;,&#39;&#39;, &#39;推荐 韩志超 的文章《Python接口测试实战1（下）- 接口测试工具的使用》（ 分享自 @简书 ）&#39;,&#39;https://www.jianshu.com/p/4b374b4556c5?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=reader_share&amp;utm_source=weibo&#39;,&#39;页面编码gb2312|utf-8默认gb2312&#39;));" data-original-title="分享到微博">
          <i class="iconfont ic-weibo"></i>
        </a>
        <a class="share-circle" data-toggle="tooltip"  id="longshare" target="_blank">
            <div class="qrcode" id="qrcode">
             <img src="//cdn2.jianshu.io/assets/web/download-index-side-qrcode-cb13fc9106a478795f8d10f9f632fccf.png" alt="Download index side qrcode" />
             <p>下载app生成长微博图片</p>
             </div>
          <i class="iconfont ic-picture"></i>
        </a>
        <a class="share-circle more-share" tabindex="0" data-toggle="popover" data-placement="top" data-html="true" data-trigger="focus" href="javascript:void(0);" data-content='
          <ul class="share-list">
            <li><a href="javascript:void(function(){var d=document,e=encodeURIComponent,r=&#39;http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url=&#39;+e(&#39;https://www.jianshu.com/p/4b374b4556c5?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=reader_share&amp;utm_source=qzone&#39;)+&#39;&amp;title=&#39;+e(&#39;推荐 韩志超 的文章《Python接口测试实战1（下）- 接口测试工具的使用》&#39;),x=function(){if(!window.open(r,&#39;qzone&#39;,&#39;toolbar=0,resizable=1,scrollbars=yes,status=1,width=600,height=600&#39;))location.href=r};if(/Firefox/.test(navigator.userAgent)){setTimeout(x,0)}else{x()}})();"><i class="social-icon-sprite social-icon-zone"></i><span>分享到QQ空间</span></a></li>
            <li><a href="javascript:void(function(){var d=document,e=encodeURIComponent,r=&#39;https://twitter.com/share?url=&#39;+e(&#39;https://www.jianshu.com/p/4b374b4556c5?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=reader_share&amp;utm_source=twitter&#39;)+&#39;&amp;text=&#39;+e(&#39;推荐 韩志超 的文章《Python接口测试实战1（下）- 接口测试工具的使用》（ 分享自 @jianshucom ）&#39;)+&#39;&amp;related=&#39;+e(&#39;jianshucom&#39;),x=function(){if(!window.open(r,&#39;twitter&#39;,&#39;toolbar=0,resizable=1,scrollbars=yes,status=1,width=600,height=600&#39;))location.href=r};if(/Firefox/.test(navigator.userAgent)){setTimeout(x,0)}else{x()}})();"><i class="social-icon-sprite social-icon-twitter"></i><span>分享到Twitter</span></a></li>
            <li><a href="javascript:void(function(){var d=document,e=encodeURIComponent,r=&#39;https://www.facebook.com/dialog/share?app_id=483126645039390&amp;display=popup&amp;href=https://www.jianshu.com/p/4b374b4556c5?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=reader_share&amp;utm_source=facebook&#39;,x=function(){if(!window.open(r,&#39;facebook&#39;,&#39;toolbar=0,resizable=1,scrollbars=yes,status=1,width=450,height=330&#39;))location.href=r};if(/Firefox/.test(navigator.userAgent)){setTimeout(x,0)}else{x()}})();"><i class="social-icon-sprite social-icon-facebook"></i><span>分享到Facebook</span></a></li>
            <li><a href="javascript:void(function(){var d=document,e=encodeURIComponent,r=&#39;https://plus.google.com/share?url=&#39;+e(&#39;https://www.jianshu.com/p/4b374b4556c5?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=reader_share&amp;utm_source=google_plus&#39;),x=function(){if(!window.open(r,&#39;google_plus&#39;,&#39;toolbar=0,resizable=1,scrollbars=yes,status=1,width=450,height=330&#39;))location.href=r};if(/Firefox/.test(navigator.userAgent)){setTimeout(x,0)}else{x()}})();"><i class="social-icon-sprite social-icon-google"></i><span>分享到Google+</span></a></li>
            <li><a href="javascript:void(function(){var d=document,e=encodeURIComponent,s1=window.getSelection,s2=d.getSelection,s3=d.selection,s=s1?s1():s2?s2():s3?s3.createRange().text:&#39;&#39;,r=&#39;http://www.douban.com/recommend/?url=&#39;+e(&#39;https://www.jianshu.com/p/4b374b4556c5?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=reader_share&amp;utm_source=douban&#39;)+&#39;&amp;title=&#39;+e(&#39;Python接口测试实战1（下）- 接口测试工具的使用&#39;)+&#39;&amp;sel=&#39;+e(s)+&#39;&amp;v=1&#39;,x=function(){if(!window.open(r,&#39;douban&#39;,&#39;toolbar=0,resizable=1,scrollbars=yes,status=1,width=450,height=330&#39;))location.href=r+&#39;&amp;r=1&#39;};if(/Firefox/.test(navigator.userAgent)){setTimeout(x,0)}else{x()}})()"><i class="social-icon-sprite social-icon-douban"></i><span>分享到豆瓣</span></a></li>
          </ul>
        '>更多分享</a>
      </div>
    </div>
      <a id="web-note-ad-1" target="_blank" href="/apps/redirect?utm_source=note-bottom-click"><img src="//cdn2.jianshu.io/assets/web/web-note-ad-1-c2e1746859dbf03abe49248893c9bea4.png" alt="Web note ad 1" /></a>
    <div id="vue_comment"></div>
  </div>

  <div class="vue-side-tool" props-data-props-show-qr-code="0"></div>
</div>
<div class="note-bottom">
  <div class="js-included-collections"></div>
  <div data-vcomp="recommended-notes" data-lazy="1.5" data-note-id="32888828"></div>
  <!-- 相关文章 -->
  <div class="seo-recommended-notes">

        <div class="note have-img">
          <a class="cover" target="_blank" href="/p/f3919ae24325?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
            <img src="//upload-images.jianshu.io/upload_images/6900654-5d42373a6d368662.png?imageMogr2/auto-orient/strip|imageView2/1/w/300/h/240" alt="240" />
</a>          <a class="title" target="_blank" href="/p/f3919ae24325?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">接口测试之——fiddler抓包、过滤、断点调试</a>
          <p class="description">1.Fiddler的基本介绍 Fiddler的官方网站:www.fiddler2.com Fiddler官方网站提供了大量的帮助文档和视频教程， 这是学习Fiddler的最好资料。 Fiddler是最强大最好用的Web调试工具之一，它能记录所有客户端和服务器的http和ht...</p>
          <a class="author" target="_blank" href="/u/15af32481324?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
            <div class="avatar">
              <img src="//upload.jianshu.io/users/upload_avatars/6900654/a85976b9-4c80-409c-9876-d5c75b5d9a5d.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
            </div>
            <span class="name">龙瑜_</span>
</a>        </div>

        <div class="note have-img">
          <a class="cover" target="_blank" href="/p/46fd0faecac1?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
            <img src="//upload-images.jianshu.io/upload_images/7328262-54f7992145380c10.png?imageMogr2/auto-orient/strip|imageView2/1/w/300/h/240" alt="240" />
</a>          <a class="title" target="_blank" href="/p/46fd0faecac1?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">Spring Cloud</a>
          <p class="description">Spring Cloud为开发人员提供了快速构建分布式系统中一些常见模式的工具（例如配置管理，服务发现，断路器，智能路由，微代理，控制总线）。分布式系统的协调导致了样板模式, 使用Spring Cloud开发人员可以快速地支持实现这些模式的服务和应用程序。他们将在任何分布式...</p>
          <a class="author" target="_blank" href="/u/d90908cb0d85?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
            <div class="avatar">
              <img src="//cdn2.jianshu.io/assets/default_avatar/2-9636b13945b9ccf345bc98d0d81074eb.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
            </div>
            <span class="name">卡卡罗2017</span>
</a>        </div>

        <div class="note ">
                    <a class="title" target="_blank" href="/p/fb7d48083e5e?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">Java面试宝典Beta5.0</a>
          <p class="description">pdf下载地址：Java面试宝典 第一章内容介绍	20 第二章JavaSE基础	21 一、Java面向对象	21 1. 面向对象都有哪些特性以及你对这些特性的理解	21 2. 访问权限修饰符public、private、protected, 以及不写（默认）时的区别(201...</p>
          <a class="author" target="_blank" href="/u/773a782d9d83?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
            <div class="avatar">
              <img src="//upload.jianshu.io/users/upload_avatars/6480773/e7eb1b5f-9375-4d65-a47f-f46719569b93?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
            </div>
            <span class="name">王震阳</span>
</a>        </div>

        <div class="note have-img">
          <a class="cover" target="_blank" href="/p/458e039f527c?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
            <img src="//upload-images.jianshu.io/upload_images/947566-f51654e6f0018748.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/300/h/240" alt="240" />
</a>          <a class="title" target="_blank" href="/p/458e039f527c?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">Fiddler 移动端使用</a>
          <p class="description">简介 Fiddler（中文名称：小提琴）是一个HTTP的调试代理，以代理服务器的方式，监听系统的Http网络数据流动，Fiddler可以也可以让你检查所有的HTTP通讯，设置断点，以及Fiddle所有的“进出”的数据（我一般用来抓包）,Fiddler还包含一个简单却功能强大...</p>
          <a class="author" target="_blank" href="/u/8c384ed45927?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
            <div class="avatar">
              <img src="//upload.jianshu.io/users/upload_avatars/4130372/85be02ba5e64.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
            </div>
            <span class="name">JxMY</span>
</a>        </div>

        <div class="note have-img">
          <a class="cover" target="_blank" href="/p/876262a56324?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
            <img src="//upload-images.jianshu.io/upload_images/8459416-e7ffe640e34b9577.png?imageMogr2/auto-orient/strip|imageView2/1/w/300/h/240" alt="240" />
</a>          <a class="title" target="_blank" href="/p/876262a56324?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">Filddler抓包</a>
          <p class="description">原因 在现实项目中，由于开发的经常调试，接口的不稳定，和接口文档的不及时更新，我们选择做接口测试，更多的需要自己抓包分析，接口。 为什么选择Fiddler a.Firebug虽然可以抓包，但是对于分析http请求的详细信息，不够强大。模拟http请求的功能也不够，且fire...</p>
          <a class="author" target="_blank" href="/u/c1ab741ef52e?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
            <div class="avatar">
              <img src="//upload.jianshu.io/users/upload_avatars/8459416/cabbe1ed-5563-4307-9b70-f4ac7b065837.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
            </div>
            <span class="name">我为峰2014</span>
</a>        </div>

        <div class="note have-img">
          <a class="cover" target="_blank" href="/p/218170ec5db9?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
            <img src="//upload-images.jianshu.io/upload_images/10776747-bf192d0487d9b35d?imageMogr2/auto-orient/strip|imageView2/1/w/300/h/240" alt="240" />
</a>          <a class="title" target="_blank" href="/p/218170ec5db9?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">为了孩子，很多女人都容忍了丈夫出轨</a>
          <p class="description">一句“为了孩子”让多少女人抱着枕头悄悄的哭泣，不管是生活上的压力，还是来自老公的不作为，她们都打掉牙齿放在心里。她们以为自己扛下了所有的痛苦，老公就能够明白她们的辛苦，不求老公为自己分担，但求老公能给自己多一些关心。 但是男人身上的担子一旦有人分担，自己变得不那么累了的时候...</p>
          <a class="author" target="_blank" href="/u/02159f97dcbf?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
            <div class="avatar">
              <img src="//upload.jianshu.io/users/upload_avatars/10776747/398cfd01-2856-4e55-9681-6cef8c61efae.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
            </div>
            <span class="name">一吾安观</span>
</a>        </div>

        <div class="note have-img">
          <a class="cover" target="_blank" href="/p/e98ff0fb5e6f?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
            <img src="//upload-images.jianshu.io/upload_images/1911149-58cf2be0a90b723c.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/300/h/240" alt="240" />
</a>          <a class="title" target="_blank" href="/p/e98ff0fb5e6f?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">别只低头坚持了，开了外挂才算成功</a>
          <p class="description">有一种感觉，每天无论你打开什么资讯平台，满屏的“小目标”首富，各路“大佬”“大咖”，最起码也是一串后缀，无数个斜杠的优质青年，看得人眼花缭乱。这时，总有一个问题趁乱自动弹出：为啥他们能够跟开了外挂似的，开个公司、加个头衔跟吃饭上厕所般的简单？我们这群每天努力上进的“屌丝”差...</p>
          <a class="author" target="_blank" href="/u/b4d9a018085a?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
            <div class="avatar">
              <img src="//upload.jianshu.io/users/upload_avatars/1911149/1f29200c400c?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
            </div>
            <span class="name">董小琳</span>
</a>        </div>

        <div class="note have-img">
          <a class="cover" target="_blank" href="/p/fd3e3ee0a659?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
            <img src="//upload-images.jianshu.io/upload_images/7017143-d6edee0f9c636610.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/300/h/240" alt="240" />
</a>          <a class="title" target="_blank" href="/p/fd3e3ee0a659?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">国际思维导图专业等级认证——哈尔滨站</a>
          <p class="description">准备——出击——期盼胜利。 2018.3.10——3.11参加首届国际思维导图专业等级认证考试，经历了刻意练习从小图标到中心图，每天坚持听课，打卡，时间过得如白驹过隙。转眼间考试结束，但这段经历却令我难忘。 细细回味，对自己的表现还算满意，只是不知道到了裁判那里会得多少分？...</p>
          <a class="author" target="_blank" href="/u/a72a588fe748?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
            <div class="avatar">
              <img src="//upload.jianshu.io/users/upload_avatars/7017143/9135c544-8423-4c86-beb2-0dabc0e4bbef.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
            </div>
            <span class="name">雾里晨光</span>
</a>        </div>

        <div class="note have-img">
          <a class="cover" target="_blank" href="/p/732eb093e819?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
            <img src="//upload-images.jianshu.io/upload_images/11889017-6258d3702ccc5b68.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/300/h/240" alt="240" />
</a>          <a class="title" target="_blank" href="/p/732eb093e819?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">49天【能量性格学——相处之道】情绪觉知日记第3天</a>
          <p class="description">1、回放，我在事件当中是什么样子的情绪？ 情绪：平和，接纳 2、为什么有这样的情绪？从哪里来的？ 早上送孩子上学时外面一直在下雨️，雨不是很大但也不小，我们两个各自打了一把伞一路走一路聊，眼看过了十子路口再走十米就到学校了，因为下雨我不想过十字了，就对儿子说，妈妈不过十字了...</p>
          <a class="author" target="_blank" href="/u/5f1888029ca4?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
            <div class="avatar">
              <img src="//upload.jianshu.io/users/upload_avatars/11889017/025426a8-ca54-48f5-8a78-cba08c20fb6a.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
            </div>
            <span class="name">胡傲宣</span>
</a>        </div>

        <div class="note have-img">
          <a class="cover" target="_blank" href="/p/6137ddabbd5b?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
            <img src="//upload-images.jianshu.io/upload_images/8935924-b37b954aa10d1ef2.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/300/h/240" alt="240" />
</a>          <a class="title" target="_blank" href="/p/6137ddabbd5b?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">随记│三九第一天，冷水是我最好的朋友</a>
          <p class="description">文/养安子 今天是三九的第一天，这一天的颜色是黑色的。你猜到了，是牙痛带给我的。前四天，牙痛基本上是一下子痛，一下子不痛，不痛的时间更多些。所以，我还随手写了一首诗，《左牙》，里面用一种苦中作乐的心情写道：“痛与痛之间短暂的平静/也成了快感。”估计是这两句冒犯了上天，上天就...</p>
          <a class="author" target="_blank" href="/u/013c1e88acc3?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
            <div class="avatar">
              <img src="//upload.jianshu.io/users/upload_avatars/8935924/996600cd-c10d-4b26-9e8a-08c605db4191.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
            </div>
            <span class="name">养安子曰</span>
</a>        </div>
  </div>
</div>

    <script type="application/json" data-name="page-data">{"user_signed_in":false,"locale":"zh-CN","os":"windows","read_mode":"day","read_font":"font2","note_show":{"is_author":false,"is_following_author":false,"is_liked_note":false,"follow_state":0,"uuid":"f68b353c-7179-4afa-ab26-e3f63d68abfa"},"note":{"id":32888828,"slug":"4b374b4556c5","user_id":7575721,"notebook_id":26739010,"commentable":true,"likes_count":7,"views_count":899,"public_wordage":3348,"comments_count":2,"featured_comments_count":0,"total_rewards_count":1,"is_author":false,"paid_type":"free","paid":false,"paid_content_accessible":false,"author":{"nickname":"韩志超","total_wordage":31259,"followers_count":160,"total_likes_count":122}}}</script>
    
    <script src="//cdn2.jianshu.io/assets/babel-polyfill-6cd2d6b53fe3184b71cc.js" crossorigin="anonymous"></script>
    <script src="//cdn2.jianshu.io/assets/web-base-1a4dbaa751aeec694965.js" crossorigin="anonymous"></script>
<script src="//cdn2.jianshu.io/assets/web-9b1e3d09272b4d02ae53.js" crossorigin="anonymous"></script>
    
    <script src="//cdn2.jianshu.io/assets/web/pages/notes/show/entry-429c4cb17e5e3fb38b55.js" crossorigin="anonymous"></script>
    <script>
  (function(){
      var bp = document.createElement('script');
      var curProtocol = window.location.protocol.split(':')[0];
      if (curProtocol === 'https') {
          bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
      }
      else {
          bp.src = 'http://push.zhanzhang.baidu.com/push.js';
      }
      var s = document.getElementsByTagName("script")[0];
      s.parentNode.insertBefore(bp, s);
  })();
</script>

  </body>
</html>
'''


md = Tomd(html).markdown
print(md)