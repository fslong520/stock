#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, traceback, sys
sys.setrecursionlimit(10 * 10)


def createImg():
    inputs = input('请输入需要生成图片代码的文件夹地址(blog.wiki/img下面的地址):')
    dirName = inputs
    path = os.path.abspath(__file__)
    for i in range(4):
        path = os.path.dirname(path)
    dirName = os.path.join(path, 'blog.wiki', 'img', dirName)
    files = os.listdir(dirName)
    imgs = []

    for i in files:
        if len(i.split('.')) > 1:
            if i.split('.')[1] in ['jpg', 'png', 'bmp', 'jpeg']:
                imgs.append(os.path.join('img', inputs, i))
    for i in range(len(imgs)):
        imgs[i] = imgs[i].replace('\\', '/')
    htmlCode = '<p align="center">\n'
    markdownCode = '<p align="center">  \n'
    for i in imgs:
        htmlCode += '    <img src="https://raw.githubusercontent.com/'
        htmlCode += 'wiki/fslong520/blog/{}">\n'.format(i)
        markdownCode += '![](https://raw.githubusercontent.com/'
        markdownCode += 'wiki/fslong520/blog/{})\n'.format(i)
    htmlCode += '</p>'
    markdownCode += '</p>'
    return '#' * 80 + '\nhtml代码如下：\n{}'.format(
        htmlCode) + '\n\n\n' + '#' * 80 + '\nmarkdown代码如下：\n{}'.format(
            markdownCode)


if __name__ == "__main__":

    def createImgFile():
        pypath = os.path.join(os.path.dirname(__file__), 'imgs.html')
        try:
            with open(pypath, 'w+', encoding='utf-8', errors='ignore') as f:
                data = createImg()
                f.write(data)
        except Exception:
            traceback.print_exc()
            createImgFile()

    createImgFile()