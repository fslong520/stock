---
layout: post
title: '玩转wsl-01-使用Xmanager本地登录wsl图形化界面'
date: 2018-12-03
author: fslong
cover: 'https://raw.githubusercontent.com/wiki/fslong520/blog/img/杂/2018.12.03/2018-12-03-01.jpg'
tags: wsl
---
  
&emsp;&emsp;*“不积跬步无以至千里，不积小流无以成江海”，这个系列是我在玩wsl的时候写的一些东西。*  
   

---
&emsp;&emsp;关于wsl如果看过之前笔者写的东西，大家一定不会陌生，就是Windows10下面的一个Linux子系统，本人一般玩的都是Debian Linux。默认就跟服务器版本一样，只有最基础的东西，但某些特殊用途，还是需要图形化界面来展现的，在之前笔者介绍的是用Xming来开启Linux子系统图形化界面，而今天笔者要跟大家分享的是使用Xmanger来实现同样的功能。简单提一句，Xmanger也是Xwindows的实现方式之一，他是商业软件，而Xming是开源软件，个人实测Xmanger图形界面性能要好过Xming一些，其他关于Xmanger的内容大家自行了解便好，笔者也不是特别了解。
## 一、在Windows10下安装Debian Linux子系统
&emsp;&emsp;详情请查看网络上相关内容或者我的个人博客，十分简单，这不是今天的重点，在此就不再赘述。  
## 二、下载安装Xmanager
&emsp;&emsp;Xmanager是一个商业收费软件，可以下载试用，地址是：[http://www.xshellcn.com/xiazai.html](http://www.xshellcn.com/xiazai.html)，申请界面如下图： 
![](https://raw.githubusercontent.com/wiki/fslong520/blog/img/杂/2018.12.03/2018-12-03-02.jpg)  
&emsp;&emsp;安装十分简单，双击安装包，然后一路下一步就是了，具体动图如下：  
![](https://raw.githubusercontent.com/wiki/fslong520/blog/img/杂/2018.12.03/2018-12-03-gif-01.gif)  
&emsp;&emsp;安装好了之后打开Xmanager备用即可。
## 三、Debian Linux子系统的配置
&emsp;&emsp;这里使用的是ssh链接，就用默认的22端口即可，具体步骤如下：  
1、安装openssh，代码：`sudo apt install openssh-server`，笔者这是已经安装好的，如下图：  
![](https://raw.githubusercontent.com/wiki/fslong520/blog/img/杂/2018.12.03/2018-12-03-09.jpg)  
2、彻底重启ssh服务，代码`sudo service ssh --full-restart`，如下图：  
![](https://raw.githubusercontent.com/wiki/fslong520/blog/img/杂/2018.12.03/2018-12-03-10.jpg)  
3、安装xfce4桌面，代码:`sudo apt install xfce4`，这一步会消耗一定时间，请耐心等待，笔者安装时候没有截图，卸载截图也太麻烦，这个比较简单，就不放图了。  
&emsp;&emsp;此时ssh服务已经启动，Xfce4桌面也已安装完毕，如果想更换端口或者用户名什么的，请查看ssh相关内容，这里也不再叙述。
## 四、新建Xstart并连接Linux子系统
&emsp;&emsp;Xstart可以使用ssh登录Linux并执行一段命令，于是笔者猜想是不是也能同Xming一样执行`startx`命令呢？于是开始实践：  
1. 点击主界面的工具，选择Xstart，命名为Debian；
2. 协议选择ssh，主机填入127.0.0.1，用户名使用wsl的用户名，验证选择password（建议点击password旁边的设置，进去之后填入密码并保存，免得每次都输入密码）;
3. 命令填入`startxfce4`;
4. 点击保存，然后点击运行，如果前面没有保存密码，这里会提示输入密码；
5. 如果第一次运行xfce4桌面，会问你使用什么样的用户配置，选择default就是了；
6. 笔者安装了中文字体，安装了xfce4-terminal之后做了简单配置如下图：  

![](https://raw.githubusercontent.com/wiki/fslong520/blog/img/杂/2018.12.03/2018-12-03-01.jpg)    

&emsp;&emsp;整个过程动图如下：  
![](https://raw.githubusercontent.com/wiki/fslong520/blog/img/杂/2018.12.03/2018-12-03-gif-02.gif)   

&emsp;&emsp;至此，今天的内容主体就完成了，Ubuntu等其他wsl理论上也可以使用同样的方法启动图形化界面，有几点需要说下：  
1. Xstart开始之前，必须确保Linux子系统的ssh服务开启，可以设置开机自启；
2. 相比于Xming，使用本文中的方法不用终端一直处于开启状态，只要Linux子系统的ssh服务在后台运行，就可以链接；
3. 相比于Xming，这种方法的图形性能要好些，以前用Xming的时候有时候会遇到卡顿的情况；
4. 如果你有云服务器，也可以安装一个图形化界面，使用相同的方法链接，只不过主机部分就得填写你的服务器的地址；
5. Xmanger属性里有很多设置，比如窗口模式什么的，大家可以自行摸索下。

---   
  
> **声明：**
> 微信公众平台对于markdown支持不够友好，建议阅读原文。