---
layout: post
title: '2019-09-09-玩转Linux-03-Win10下使用wsl与VS code结合进行Python开发(新增GUI相关内容)'
date: 2019-9-09
author: fslong
cover: 'https://raw.githubusercontent.com/wiki/fslong520/blog/img/VScodeAndWsl/debian.jpg'
tags: linux,wsl,Python
---
  
&emsp;&emsp;*“不积跬步无以至千里，不积小流无以成江海”，这个系列是我在玩Linux的时候写的一些东西。*  
   

---
&emsp;&emsp;先交代下故事背景：现在Win10最新的预览版已经加入了wsl2，已经支持了docker，用了Linux4.19内核，非常的好用，同时性能杠杠的，笔者一台好久之前的笔记本wsl2使用Unixbench跑分大约1620分，全盘格式化装Deepin跑分1700分，基本上可以理解为误差了，并且依然可以是`\\wsl$`访问wsl2的文件目录。由于工作关系，本人用了一段时间的Deepin，实事求是地讲Deepin非常的不错，日常使用也完全没问题的，但我遇到了在移动文件时候文件丢失的问题（exFat分区→Ntfs分区）然后就凉凉了，并且还是离不开OneDrive还有Microsoft office全家桶，于是叛变了两个礼拜的我又回到了Win10的怀抱。但大家都知道，Windows下面Python开发坑也不少，挺难受的，那有没有二者兼得的方法？答案是有的，那就是使用wsl和VS code结合的方法。但是网上很多教程其实都有点问题，有些不好用，有些配置比较麻烦，本人意外的发现VS code官方文档其实已经有了推荐的方法，本文在此基础上夹带了一些私货，供大家体验。由于很多小伙被没有升级到最新的预览版，用不了wsl2，下文以另外一台只有wsl1的电脑为例讲解如何使用。  

### 一、原理   
&emsp;&emsp;原理其实很简单，用的是远程连接wsl。是使用VS code远程连接WSL进行开发，但是由于wsl本身就在本地，还可以跟Win10系统的本地文件交互（现在性能已经挺好了），所以实际上在这些文件的操作又可以使用Win10系统，非常的舒服。       

### 二、配置方法 
#### （一）、第一步自然是安装VScode和wsl，相关教程很多，不在这里赘述，最终结果如下图所示：   
<p align="center">
    <img src="https://raw.githubusercontent.com/wiki/fslong520/blog/img/VScodeAndWsl/debian.jpg">
    <img src="https://raw.githubusercontent.com/wiki/fslong520/blog/img/VScodeAndWsl/vscode.jpg">
</p>  

#### (二)、在vscode里面安装插件`remote-wsl`，如下图：  
<p align="center">
    <img src="https://raw.githubusercontent.com/wiki/fslong520/blog/img/VScodeAndWsl/vscode.jpg">
</p>   

&emsp;&emsp;安装完了之后，我们点击左下角的和`><`按钮，在上方框框里选择`Ropen folder in wsl`，如下图所示：  
<p align="center">
    <img src="https://raw.githubusercontent.com/wiki/fslong520/blog/img/VScodeAndWsl/remote-wsl.jpg">
</p>    

&emsp;&emsp;首次运行得等会儿，会安装一些服务，然后有`Node.js`的联网请求，当然是点允许，如下图所示：  
<p align="center">
    <img src="https://raw.githubusercontent.com/wiki/fslong520/blog/img/VScodeAndWsl/node.jpg">
</p>  

&emsp;&emsp;之后的界面就会变成如下：
<p align="center">
    <img src="https://raw.githubusercontent.com/wiki/fslong520/blog/img/VScodeAndWsl/completely.jpg">
</p>  

&emsp;&emsp;这里有个需要注意的地方，其实在wsl里面我们也装了一个vscode的服务，我们现在在vscode里面安装插件的时候可以看到左侧有个`local`还有个`wsl`分类，如下图所示：  
<p align="center">
    <img src="https://raw.githubusercontent.com/wiki/fslong520/blog/img/VScodeAndWsl/localAndWsl.jpg">
</p>  

&emsp;&emsp;这就表示其实我们编程的时候很多东西都是调用的wsl里头的东西，所以我们安装插件的时候要想在wsl里面也能用，必须要把他安装到wsl里面才能使用，比如下面的语言包：  
<p align="center">
    <img src="https://raw.githubusercontent.com/wiki/fslong520/blog/img/VScodeAndWsl/Chinese.jpg">
</p>  

&emsp;&emsp;**其实就是用VScode远程连接进行开发，没什么特殊的！**  
  

&emsp;&emsp;需要注意的是: <font color="red">安装完这个插件以后，当我们在打开文件夹的时候就会有两种提示，一种是打开本地，一种是打开wsl。由于在wsl中电脑磁盘是挂载在/mnt/目录下的，所以在打开wsl目录的时候就会有以下的提示：</font>  
<p align="center">
    <img src="https://raw.githubusercontent.com/wiki/fslong520/blog/img/VScodeAndWsl/openFolder.jpg">
</p>  

&emsp;&emsp;如果我们点击右边的`show local`自然是打开Windows目录下的文件夹，使用起来很方便，如下图：  
<p align="center">
    <img src="https://raw.githubusercontent.com/wiki/fslong520/blog/img/VScodeAndWsl/openLocal.jpg">
</p>    

&emsp;&emsp;不过个人还是建议直接一直就在wsl下得了，反正也能直接读写windows10的目录，笔者直接就是在OneDrive当中开发（日常关着的，过几天启动下OneDrive同步一次），这样不影响性能还是同步，还能使用wsl，简直美滋滋。

#### (三)、运行GUI程序：
&emsp;&emsp;在开发的过程中我们往往需要运行一些GUI程序，或者自己编写一个GUI程序，比如使用海龟画图，这种情况下就需要GUI相关支持了，其实实现也很简单，用的是x11服务，只要开一个x11服务即可，相关软件很多Xmanager、xming、mobaXterm等都可以，笔者用的是mobaXterm，他对wsl支持很友好。  
1、安装mobaXterm，官网下载地址是（个人版就可以了）: [https://mobaxterm.mobatek.net/download.html](https://mobaxterm.mobatek.net/download.html)    
2、将物理机ip地址设为静态ip，然后再mobaXterm里新建一个session，选择wsl，如下图：  

<p align="center">
    <img src="https://raw.githubusercontent.com/wiki/fslong520/blog/img/VScodeAndWsl/newsession.jpg">
</p>  

3、打开刚刚新建的session，如果显示有一行 ` Your DISPLAY is set to 192.168.2.77:0.0 ` 说明一切正常，这句话里面的ip地址自然是你自己的，如下图：  

<p align="center">
    <img src="https://raw.githubusercontent.com/wiki/fslong520/blog/img/VScodeAndWsl/opensession.jpg">
</p>   

4、此时还不可以的，我们需要写入环境变量`export DISPLAY="192.168.2.77:0.0"`，里面的ip地址是我的ip地址，你换成你的就是了，然后运行`source ~/.bashrc`使环境变量生效，此时你就可以在vscode的终端里运行任意GUI程序了，python写的gui程序也完全没问题，但前提是mobaXterm不能关（如果没打开刚刚那个wsl的session，mobaXterm会自动开启一个），下图一个是新立德一个是python的海龟库绘图：   
 
<p align="center">
    <img src="https://raw.githubusercontent.com/wiki/fslong520/blog/img/VScodeAndWsl/synaptic.jpg">
</p>   
<p align="center">
    <img src="https://raw.githubusercontent.com/wiki/fslong520/blog/img/VScodeAndWsl/turtle.jpg">
</p>   




&emsp;&emsp;**到这里教程就结束了，这个教程很简单，就是教大家怎么使用wsl和vscode配合进行开发，具体能产生什么样的火花还需要你来开发！**


---   
  
> **声明：**
> 微信公众平台对于markdown支持不够友好，建议阅读原文。