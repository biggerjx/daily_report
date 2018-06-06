from tkinter import *
from swagger import *

root = Tk()

root.title("获取swagger接口数据")
root.geometry('300x150')

url_l = Label(root,text="url") #标签
url_l.pack() #指定包管理器放置组件
url_text = Entry() #创建文本框
url_text.pack()

tag_l = Label(root,text="tag") #标签
tag_l.pack() #指定包管理器放置组件
tag_text = Entry() #创建文本框
tag_text.pack()

swagger_url = url_text.get() #获取文本框内容
tag = tag_text.get()

#button
Button(root, text="生成数据").pack()
#, command =get_api_result(swagger_url, "1.101.0")
#get_api_result(swagger_url, tag)

root.mainloop()