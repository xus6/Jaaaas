#!/usr/bin/env python
# coding: utf-8

# In[39]:


################################create info####################################
# project name ： copydemo
# description  ： 在原目录下创建新目录，并在保存本文件情况下，将目录下剩余所有文件以及文件夹复制至新建目录
# Author        ： dusen
# Create date   ： 2020/03/19
# Update date   ： 2020/08/26
####################### modification ##############################
import shutil
import os


oldpath= os.getcwd()#"E:\\work\\practice\\python\\python学习例程\\复制"

# 将根目录下的文件复制到此目录下的新建目录
def copyfile(newfoldername):
	allfiels = os.listdir(oldpath)
	newpath=oldpath + '/' + newfoldername #新建目录名
	if os.path.exists(newpath):
		pass
	else:
		os.makedirs(newpath)	
	for file in allfiels:
		if 'copyfile0.0' not in file and newfoldername not in file:
			copyrecur(oldpath,newpath,file)
# 递归函数
def copyrecur(oldfile,newfile,file):
	oldfile = oldfile + '/' + file
	newfile = newfile + '/' + file
	if os.path.isfile(oldfile): # 复制文件到新建目录
		try:
			shutil.copyfile(oldfile, newfile)
			os.remove(oldfile) #删除原目录下文件
		except Exception as e:
			# raise e
			pass
			print(e)
	else:
		try:
			if os.path.exists(newfile):
				pass
			else:
				os.makedirs(newfile)
			allfiles = os.listdir(oldfile)
			for file_lowerlevel in allfiles:
				copyrecur(oldfile,newfile,file_lowerlevel)
			if len(os.listdir(oldfile)) == 0:
				shutil.rmtree(oldfile)
		except Exception as e:
			# raise e
			pass
			print(e)

# 主程序入口
if __name__ == '__main__':	  
	try:
		copyfile('uncover')
	except Exception as e:
		print (e)
		print ('程序异常请联系开发人员')
		input()









