import os
import pandas as pd
import numpy as np
from PIL import Image

im_path = '../input/ships_train2018'
csv_train = '../input/train_ship_segmentations_v2.csv'

if __name__ == '__main__':
    # 读取原始标注文件
    df = pd.read_csv(csv_train)
    print("所有标注数： ",df.shape[0])

    # 去除空标注
    df = df.dropna(axis=0)
    num_of_ships = df.shape[0]
    print("实例标注数： ",num_of_ships)

    # 新建一个空集合，用于存放图片名称
    images = set()
    for line in range(num_of_ships):
        if df.iloc[line,0] not in images:
            images.add(df.iloc[line,0])
    print("含船图片数： ",len(images))

    # 删除无船图片
    count = 0
    ims = os.listdir(im_path)
    for im in ims:
        if im not in images:
            os.remove(os.path.join(im_path, im))
            count += 1
    print('%d images is deleted.'%(count))