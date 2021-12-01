#今天学numpy
import numpy as np
a=np.array([1,2,3])
print(a)
b=np.array([[1,2],[3,4]])
print(b)
#控制外围维数
c=np.array([1,2,3,4,5],ndmin=2)
print(c)
d=np.array([1,2,3,4,5],dtype=complex)
print(d)
#判断数据类型
dt=np.dtype(np.int32)
print(dt)
dt1=np.dtype('i4')
print(dt1)
dt2 = np.dtype('<i4') #<代表字节顺序标序，和单纯的i4如果不超标没区别
print(dt2)
dt3 = np.dtype([('age',np.int32)])
e= np.array([(10,),(20,),(30,)], dtype = dt3) #dtype是用来定义数据类型的
print(e)
dt4 = np.dtype([('age',np.int32)])
a = np.array([(10,),(20,),(30,)], dtype = dt4)
print(a['age'])
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
student1=np.array([('xiaofu',12,1)],dtype=student)#需要调用的时候可以调用
print(student1['name'])
#ndim用来查看数据维度
f=np.arange(24)
print(f.ndim)
g=f.reshape(2,4,3)
print(g.ndim)
#shape用来查看数组行列数，同时可以通过直接指定shape指数达到reshape效果
a=np.array([[1,2,3],[4,5,6]])
print(a.shape)
a = np.array([[1,2,3],[4,5,6]])
a.shape =  (3,2)
print (a)
#itemsize用来查看每个元素占用多少位字节，多少位巴拉巴拉
a=np.array([1,2,3,4,5],dtype=np.int8)
print(a.itemsize)
b=np.array([1,2,3,4,5],dtype=np.int32)
print(b.itemsize)
#flags用来查看内存中的信息，入门基本没啥用
c=np.array([1,2,3,4,5])
print(c.flags)
x = np.empty([3,2], dtype = int)
print (x)
#自定义零矩阵
z = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])
print(z)
# 自定义全1矩阵
x = np.ones([2,2], dtype = int)
print(x)
x=(1,2,3)
y=np.asarray(x)
print(y)
#arange函数自动生成数组返回ndarray函数
z=np.arange(5)
print(z)
#linspace和arange区别：linspace从1开始，而且可以指定步长，是arange特殊形式
a = np.linspace(1,10,10)
print(a)
#logspace用于创建等比数列
