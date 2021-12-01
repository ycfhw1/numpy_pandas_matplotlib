from matplotlib import pyplot as plt
import random
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #正常显示负号
# plt.figure(figsize=(10,8),dpi=80)
x=range(1,5)
y_1=[1,2,3,4]
y_2=[3,4,5,6]
z=[random.randint(20,35) for i in range(4)]
plt.plot(x,y_1,label="my")
plt.plot(x,y_2,label="friend")
#_x=x
_x=list(x)[::2]
_xtick_labels=["你好,{}".format(i) for i in _x]
#plt.xticks(range(1,5))
# plt.xticks(_x,_xtick_labels)
# plt.xticks(_x,_xtick_labels,rotation=90)
# plt.grid(alpha=0.1)
plt.legend(loc="upper right")
plt.show()
