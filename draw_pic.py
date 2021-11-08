import pandas as pd
import matplotlib.pyplot as plt

read=pd.read_csv("./acc-loss-1.csv")

#x=read[["train_loss", "train_acc"]]
#y=read[["valid_loss", "valid_acc"]]
#plt.plot(read["train_loss"])
#plt.plot(read["valid_loss"])
plt.subplot(121)
plt.plot(read["train_acc"], label='train_acc')
plt.plot(read["valid_acc"], label='valid_acc')
plt.legend()  # 让图例生效
plt.title("", fontsize=24)
plt.xlabel("Epoch", fontsize=14)
plt.ylabel("Accuracy", fontsize=14)


plt.subplot(122)
plt.plot(read["train_loss"], label='train_loss', color='r')
plt.plot(read["valid_loss"], label='valid_loss', color='g')
plt.legend()  # 让图例生效
plt.title("", fontsize=24)
plt.xlabel("Epoch", fontsize=14)
plt.ylabel("Loss", fontsize=14)
#plt.plot(squares, linewidth=5)

#设置图表标题，并给坐标轴加上标签


#设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
plt.show()

plt.savefig('E:\\工作目标\\f2.png',dpi = 900)