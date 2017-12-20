# -*- coding: utf-8 -*-
# @Author: H3ric Young
# @Date:   2017-12-19 15:21:50
# @Last Modified by:   H3ric Young
# @Last Modified time: 2017-12-19 17:56:46

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                                   $$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                                                                     $$$
# $                                                                                                        $$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$        $$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$$$$$$
# $$$$$$$$$$$$$$$                      $$$$     $$$$$$$           $$$$$    $$$$     $$$$$$$$$$$$       $$$$$$$$$
# $$$$$$$$$$$$$                       $$$$      $$$$$$$            $$$    $$$     $$$$$$$$$$$$$       $$$$$$$$$$
# $$$$$$$$$$$$    $$$$$$$$$$$     $$$$$$        $$$$$$    $$$$     $$    $$$    $$$$$$$$$$$$$$      $$$$$$$$$$$$
# $$$$$$$$$$$     $$$$$$$$$$$    $$$$$$    $    $$$$$$    $$$$    $$$    $     $$$$$$$$$$$$$$      $$$$$$$$$$$$$
# $$$$$$$$$$$        $$$$$$$    $$$$$$    $$    $$$$$            $$$         $$$$$$$$$$$$$$$      $$$$$$$$$$$$$$
# $$$$$$$$$$$$        $$$$$$    $$$$$    $$$    $$$$           $$$$$         $$$$$$$$$$$$$$     $$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$      $$$$    $$$$$            $$$$    $$     $$$$    $     $$$$$$$$$$$$$     $$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$    $$$$     $$$$             $$$     $$$    $$$$    $$     $$$$$$$$$$$    $$$$$$$$$$$$$$$$$$$
# $$$$$$$$           $$$$$    $$$     $$$$$$    $$$    $$$$    $$$    $$$     $$$$$$$$$$    $$$$$$$$$$$$$$$$$$$$
# $$$$$$$          $$$$$$     $$     $$$$$$$    $$    $$$$$    $$     $$$$     $$$$$$$    $$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$  $$   $$$  $       $$   $$$  $$            $       $$  $      $$      $$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$   $     $  $$  $$$   $  $$$  $   $$$$$$   $$   $$  $$  $$  $$$$$  $$$$$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$  $$        $  $$$$  $   $$$  $$    $$$$  $$$      $$   $      $$     $$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$   $  $$    $   $$$   $  $$$  $$$$$   $$  $$$   $   $$  $$  $$$$$$$$$  $$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$  $   $$   $$       $$$      $$      $$   $$$  $$   $   $             $$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\\
# 
# 读取mnist数据集
import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/",one_hot = True)


# num = input("请输入需要识别的数字:")
# num = num.rstrip()
# 设置参数的大小
sess = tf.InteractiveSession()
x = tf.placeholder(tf.float32,[None,784])

W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x,W)+b)
y_ = tf.placeholder(tf.float32,[None,10])

cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_*tf.log(y),reduction_indices = [1]))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

#训练
for i in range(1000):
	batch_xs,batch_ys = mnist.train.next_batch(100)
	sess.run(train_step,feed_dict={x:batch_xs,y_:batch_ys})

#测试
correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(y,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
# print(sess.run(accuracy,feed_dict={x:mnist.test.images,y_:mnist.test.labels}))


batch_x, batch_y = mnist.test.next_batch(1)   #取一组训练数据

# batch_x 为（1，784）数组（保存图像信息） batch_y 为（1,10）（保存图像标签，第几位数是1，就表示几）
# print(sess.run(accuracy, feed_dict={x: batch_x, y_: batch_y}))  #验证训练数据的准确性
# im = np.reshape(batch_x,(28,28))   #将一维数组转化为28*28的图像数组  float32 （0-1）
#此时通过观察数组中数字部分，能大致的看出图像表示的数字
#为了直观的看到，可以将数组转化为图像
from PIL import Image
# imag=Image.fromarray(np.uint8(im*255))  #这里读入的数组是 float32 型的，范围是 0-1，而 PIL.Image 数据是 uinit8 型的，范围是0-255，要进行转换
# imag.show()
# imag.save('./photo/t3.png')

for i in range(10):
	imm =np.array(Image.open("./photo/"+str(i)+".jpg").convert('L')) #打开图片，转化为灰度并转化为数组size（n,m） 值0-255
	imm = imm/255           #将值转化为0-1
	# imm = -imm+1
	imm_3 = Image.fromarray(imm)    #转化为图像
	imm_4 = imm_3.resize([28,28])   #压缩    
	im_array = np.array(imm_4)     #转化为数组
	fs = im_array.reshape((1,784))  #转化为符合验证一维的数组
	print(str(i),".jpg中的数字为:",sess.run(tf.argmax(y,1), feed_dict={x: fs, y_: batch_y})) #输出模型的识别值 
#或者
#
# 
# imm =np.array(Image.open("./photo/t"+str(num)+".png").convert('L').resize([28,28]))
# imm = 255-imm  #imm、255  反向处理
# imm = imm/255
# # imm = -imm+1   #自己测试图片效果太差，示例的数组无字处为0（黑底白字）。可以通过自定义函数转化自己的数组，这里利用的是最简单的 函数
# imm = imm.reshape((1,784))
# print("该数字为：",sess.run(tf.argmax(y,1), feed_dict={x: imm}))  #tf.argmax 算出模型值