---
title: 18-Tensorflow 学习笔记之安装相关
date: 2018-10-07 10:32:04
categories: 学习
tags: [深度学习,Tensorflow]
toc: true
--- 
### 安装方法
&emsp;&emsp;<font color='#ff0000'>*暂且只说cpu版本的，因为我买不起gtx2080。*</font>  
**方法1、**   
&emsp;&emsp;直接`pip3 install tensorflow`安装通用版本；  
**方法2、**  
针对自己计算机安装编译好的特定版本的轮文件：  
1. 前往GitHub搜索tensorflow；
2. 根据你电脑系统情况下载编译好的轮文件，笔者是Intel的cpu，64位系统，Linux系统，python3.6，下载如图所示版本：![1.根据你的cpu下载tensorflow.png](https://i.loli.net/2018/10/14/5bc2ba7499c2d.png)
3. cd到下载下来的轮文件（比如我下下来是`tensorflow-1.10.0-cp36-cp36m-linux_x86_64.whl`)所在目录，`pip3 install tensorflow-1.10.0-cp36-cp36m-linux_x86_64.whl`即可完成安装。
---
### 安装中的坑  
1. 方法1中的方法安装的是通用x86版本的tensorflow，比如笔者的电脑如果这种方法安装会报错：
    ```
    I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
    ``` 
    意思是针对你电脑cpu有专门版本的tensorflow，支持专门的指令集。别看这个报错是个`warning`而已，他很可能会导致后续你的numpy依赖出问题，装哪个版本都会报warning，虽然程序能够正常执行，但总看这些warning多难受呀，所以建议用方法2安装；
2. 方法2中如果你用的是`pipenv`虚拟环境，直接运行`pipenv install tensorflow-1.10.0-cp36-cp36m-linux_x86_64.whl`会报错，此时我们可以进入`pipenv shell`然后运行`pip3 install tensorflow-1.10.0-cp36-cp36m-linux_x86_64.whl`即可安装本地轮文件版本的tensorflow，这时一切正常。
---