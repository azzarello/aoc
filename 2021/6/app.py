import numpy as np
import pandas as pd


def load_fish():
    f = open("input")
    fish = np.array([int(x) for x in f.read().rstrip().split(",")])
    fish_df = pd.DataFrame(columns=(0, 1, 2, 3, 4, 5, 6, 7, 8), index=[0])
    for x in range(9):
        fish_df[x] = len(np.where(fish == x)[0])
        # print(np.where(fish == x))
        # print(np.where(fish == x)[0])
    return fish_df


def grow(df):
    prev_df = df.copy(deep=True)
    for x in range(1, 9):  # all fish have a day deducted
        df[x - 1] += prev_df[x]
        df[x] -= prev_df[x]
    df[6] += prev_df[0]  # all 0s become 6s
    df[8] += prev_df[0]  # all 0s become new 8s
    df[0] -= prev_df[0]  # no more 0s (except the "new" 0s)

    return df


if __name__ == "__main__":
    for days in [80, 256]:
        fish_df = load_fish()
        for d in range(days):
            grow(fish_df)
        print(f"The population after {days} days is: {sum(fish_df.loc[0])}")
