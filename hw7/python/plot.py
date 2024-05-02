import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

csv_file = 'data.csv'
plt.style.use('fivethirtyeight')


def animate(i):
    data = pd.read_csv(csv_file)
    t_vals = data['timestamp']
    x_vals = data['x']
    # y_vals = data['y']
    # z_vals = data['z']
    x_filtered_vals = data['x_filtered']

    plt.cla()

    plt.plot(t_vals, x_vals, label='x')
    # plt.plot(t_vals, y_vals, label='y')
    # plt.plot(t_vals, z_vals, label='z')
    plt.plot(t_vals, x_filtered_vals, label='x_filtered')

    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()


# ani = FuncAnimation(plt.gcf(), animate, interval=500)
animate(0)
