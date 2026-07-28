from pathlib import Path

import numpy as np
import pandas as pd


def numpy_demo():
    print("=== NumPy Demo ===")
    print()

    # 1. 创建一个二维 NumPy 数组
    # 可以把它理解成一个 2 行 3 列的矩阵
    x = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])

    print("1. NumPy array:")
    print(x)
    print()

    # 2. 查看数组形状
    # shape 返回的是：几行几列
    # 这里 (2, 3) 表示 2 行 3 列
    print("2. Shape:")
    print(x.shape)
    print()

    # 3. axis=0 表示按列计算
    # 例如第一列是 1 和 4，平均值是 2.5
    print("3. Mean by column, axis=0:")
    print(x.mean(axis=0))
    print()

    # 4. axis=1 表示按行计算
    # 例如第一行是 1, 2, 3，平均值是 2
    print("4. Mean by row, axis=1:")
    print(x.mean(axis=1))
    print()

    # 5. 切片：取出第二列
    # Python 下标从 0 开始，所以第 2 列的下标是 1
    # x[:, 1] 的意思是：取所有行的第 1 列
    print("5. Second column:")
    print(x[:, 1])
    print()

    # 6. 求和
    # x.sum() 会把数组里所有数字加起来
    print("6. Sum of all elements:")
    print(x.sum())
    print()

    # 7. 求最大值
    # x.max() 会找出数组里最大的数字
    print("7. Max value:")
    print(x.max())
    print()

    # 8. Broadcasting 广播机制
    # x 是 2 行 3 列
    # y 是长度为 3 的一维数组
    # NumPy 会自动把 y 扩展到每一行上
    y = np.array([10, 20, 30])

    print("8. Broadcasting, x + y:")
    print(x + y)
    print()

    # 9. 矩阵乘法
    # x 的形状是 (2, 3)
    # w 的形状是 (3, 1)
    # 所以 x @ w 的结果形状是 (2, 1)
    w = np.array([
        [1],
        [2],
        [3]
    ])

    print("9. Matrix multiplication, x @ w:")
    print(x @ w)
    print()


def pandas_demo():
    print("=== Pandas Demo ===")
    print()

    # 1. 找到当前项目根目录
    # __file__ 表示当前 Python 文件的位置
    # parents[1] 表示往上找两层，得到项目根目录 llm-internship-30days
    project_root = Path(__file__).resolve().parents[1]

    # 2. 拼出数据文件路径
    # 最终路径类似：
    # C:\Users\15611\PyCharmMiscProject\llm-internship-30days\data\sample_text.csv
    data_path = project_root / "data" / "sample_text.csv"

    print("1. Data file path:")
    print(data_path)
    print()

    # 3. 使用 pandas 读取 CSV 文件
    # CSV 可以理解成一种表格文件
    # 读取后会变成 DataFrame
    df = pd.read_csv(data_path)

    print("2. DataFrame head:")
    print(df.head())
    print()

    # 4. 查看数据基本信息
    # info() 可以看到列名、非空数量、数据类型
    print("3. DataFrame info:")
    df.info()
    print()

    # 5. 查看标签分布
    # value_counts() 可以统计每个标签出现了多少次
    # 这里可以看到 spam 和 ham 各有多少条
    print("4. Label counts:")
    print(df["label"].value_counts())
    print()

    # 6. 去掉空值
    # dropna() 会删除包含缺失值的行
    df = df.dropna()

    print("5. Shape after dropna:")
    print(df.shape)
    print()

    # 7. 单独取出 text 列
    # 这列是短信文本内容
    print("6. Text column preview:")
    print(df["text"].head())
    print()

    # 8. 单独取出 label 列
    # 这列是分类标签，spam 表示垃圾短信，ham 表示正常短信
    print("7. Label column preview:")
    print(df["label"].head())
    print()


def main():
    numpy_demo()
    pandas_demo()


if __name__ == "__main__":
    main()