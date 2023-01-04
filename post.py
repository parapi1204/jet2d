import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.getcwd()
POST_DIR = "postProcessing"

U0 = 1.0  # [m/s]
jetDiam = 0.001  # [m]
rho = 1  # [kg/m3]
nu = 1e-5  # [m2/s]
M = rho * U0**2 * jetDiam

position = {
    "U00": 0,
    "U01": 0.001,
    "U02": 0.002,
    "U03": 0.003,
    "U04": 0.004,
    "U05": 0.005,
    "U10": 0.010,
    "U20": 0.020,
    "U30": 0.030,
    "U50": 0.050,
    "U100": 0.1,
}


if __name__ == "__main__":

    postPath = os.path.join(BASE_DIR, POST_DIR)
    postFiles = os.listdir(postPath)
    positionDirList = [f for f in postFiles if os.path.isdir(os.path.join(postPath, f))]

    for positionDir in positionDirList:

        print(f"Drowing figure of {positionDir}...")

        positionPath = os.path.join(BASE_DIR, POST_DIR, positionDir)
        positionFiles = os.listdir(positionPath)
        timeDirList = [
            f for f in positionFiles if os.path.isdir(os.path.join(positionPath, f))
        ]

        for i, timeDir in enumerate(timeDirList):
            df = pd.read_csv(
                os.path.join(BASE_DIR, POST_DIR, positionDir, timeDir, "line_U.xy"),
                header=None,
                sep="\t",
                names=["y", "u", "v", "w"],
            )

            x = df["u"] / U0
            y = df["y"]

            fig = plt.figure(figsize=(2.13, 6.4))
            ax = fig.add_subplot(1, 1, 1)
            # 右と上の枠線削除
            ax.spines["right"].set_visible(False)
            ax.spines["top"].set_visible(False)
            # x軸をy軸中心にシフト
            ax.spines["bottom"].set_position(("data", 0))
            # y軸の目盛値を削除
            ax.tick_params(labelleft=False, left=False)
            ax.tick_params(labelsize=16)
            # x軸の目盛値を設定
            ax.set_xticks([0, 0.5, 1.0])
            # x軸の範囲、ラベル名を設定
            ax.set_xlim(-0.05, 1.1)
            ax.set_xlabel("U/U0", loc="right", fontsize=16)

            ax.plot(x, y, lw=3)
            saveName = f"{positionDir}_{i}.png"
            savePath = os.path.join(BASE_DIR, POST_DIR, positionDir, saveName)
            fig.savefig(savePath, transparent=True)
            plt.close()
