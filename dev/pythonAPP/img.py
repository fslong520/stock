#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, traceback, sys, time
sys.setrecursionlimit(10 * 10)


def createImg(inputs=None):
    if inputs == None:
        inputs = ''
    dirName = inputs
    path = os.path.abspath(__file__)
    for i in range(4):
        path = os.path.dirname(path)
    dirName = os.path.join(path, 'blog.wiki', 'img', dirName)
    #files = os.listdir(dirName)# 无法遍历子目录
    files = []
    splitString = os.path.join('blog.wiki', 'img', dirName)
    for parent, dirnames, filenames in os.walk(dirName):
        for filename in filenames:
            trueFileName = os.path.join(parent, filename)
            if len(trueFileName.split(splitString)) > 1:
                files.append(trueFileName.split(splitString)[1])
    imgs = []

    for i in files:
        if len(i.split('.')) > 1:
            if i.split('.')[1] in ['jpg', 'png', 'bmp', 'jpeg']:
                imgs.append(os.path.join('img', inputs, i))
    for i in range(len(imgs)):
        imgs[i] = imgs[i].replace('\\', '/')
    htmlCode = ''
    markdownCode = ''
    for i in imgs:
        htmlCode += '\n<p align="center">\n    <img src="https://raw.githubusercontent.com/'
        htmlCode += 'wiki/fslong520/blog/img/{}{}">\n</p>'.format(inputs,i)
        markdownCode += '\n<p align="center">  \n![](https://raw.githubusercontent.com/'
        markdownCode += 'wiki/fslong520/blog/img/{}{})\n</p>'.format(inputs,i)
    return ('#' * 80 + '\nhtml代码如下：\n{}'.format(htmlCode) + '\n\n\n' +
            '#' * 80 + '\nmarkdown代码如下：\n{}'.format(markdownCode), len(imgs))


def inputData():
    inputs = input('请输入需要生成图片代码的文件夹地址(blog.wiki/img下面的地址):')
    try:
        dirName = inputs
        path = os.path.abspath(__file__)
        for i in range(4):
            path = os.path.dirname(path)
        dirName = os.path.join(path, 'blog.wiki', 'img', dirName)
        files = os.listdir(dirName)  # 无法遍历子目录
    except Exception:
        print('请输入正确的文件目录！\n')
        inputData()
    finally:
        return inputs


def createImgFile(inputs):
    pypath = os.path.join(os.path.dirname(__file__), 'imgs.html')
    with open(pypath, 'w+', encoding='utf-8', errors='ignore') as f:
        data = createImg(inputs)
        f.write(data[0])
    return data[1]


if __name__ == "__main__":

    inputs = inputData()
    count = 0
    if inputs == '':
        infoString = '图片'
    else:
        infoString = inputs

    while True:
        try:
            count += 1
            print('开始第{}次生成{}目录下照片文件图床链接请稍候...'.format(count, infoString))
            imgNum = createImgFile(inputs)
            print('{}目录链接生成完毕，总共有{}张图片，请前往./imgs.html文件查看。\n'.format(
                infoString, imgNum))
            time.sleep(3)
        except KeyboardInterrupt:
            print('谢谢使用')
            break