import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

def animate(i):
    df = pd.read_csv("time-price-oi.csv")
    df.drop(df.iloc[-i])
    print(df)
    x = df["Time"]
    y = df["OI"]

    plt.cla()

    plt.plot(x, y, label="Open Interest")

    plt.legend(loc="upper left")
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()
