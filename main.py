# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import math
import matplotlib.pyplot as plt

import numpy as np

RADIUS = 0.2
SIZE = 1000


def create_sample_data(low, high, delta, n):
    data = [0] * n
    for i in range(n):
        if i != 0:
            randint = data[i-1]
            if randint < low:
                randint = randint + delta
        else:
            randint = np.random.randint(low, high)
        upper_delta = randint + (delta / 2)+1
        lower_delta = randint - (delta / 2)+1
        random_randint = np.random.randint(lower_delta, upper_delta)
        data[i] = random_randint
    return data


def random_spaced(low, high, delta, n, size=None):
    """
    Choose n random values between low and high, with minimum spacing delta.

    If size is None, one sample is returned.
    Set size=m (an integer) to return m samples.

    The values in each sample returned by random_spaced are in increasing
    order.
    """
    empty_space = high - low - (n - 1) * delta
    # if empty_space < 0:
    #     raise ValueError("not possible")

    if size is None:
        u = np.random.rand(n)
    else:
        u = np.random.rand(size, n)

    x = empty_space * np.sort(u, axis=-1)
    return low + x + delta * np.arange(n)


def generate_sample_data():
    return


# Press the green button in the gutter to run the script.
def calculate_velocity(rpm_array):
    velocity_by_time = [0] * len(rpm_array)

    for i, rpm in enumerate(rpm_array):
        velocity = ((2 * math.pi * RADIUS) / 60) * rpm
        velocity_by_time[i] = velocity
    return velocity_by_time


def plot_data(velocity_by_time):
    x = np.arange(1, SIZE + 1)
    # plotting
    plt.title("Line graph")
    plt.xlabel("Time in ms")
    plt.ylabel("Speed in m/s")
    plt.plot(x, velocity_by_time, color="red")
    plt.grid()
    plt.show()


if __name__ == '__main__':
    sample_data = create_sample_data(100, 400, 25, SIZE)
    velocity_data = calculate_velocity(sample_data)
    plot_data(velocity_data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
