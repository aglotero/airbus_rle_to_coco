import numpy as np
import pandas as pd
from skimage.data import imread
import matplotlib.pyplot as plt
import os
np.set_printoptions(threshold=np.inf)	# 规定完整打印numpy矩阵，便于调试观察

ROOT_DIR = '../input'   # 数据集根目录
csv_train = '../input/train_ship_segmentations_v2.csv'

# ref: https://www.kaggle.com/paulorzp/run-length-encode-and-decode
# mask_rle(string) --> rle_decode() -->  np.ndarry(np.unit8)
# shape: (height,width) , 1 - mask, 0 - background
def rle_decode(mask_rle, shape=(768, 768)):
    s = mask_rle.split()
    starts =  np.asarray(s[0::2], dtype=int)
    lengths = np.asarray(s[1::2], dtype=int)

    starts -= 1
    ends = starts + lengths
    img = np.zeros(shape[0]*shape[1], dtype=np.uint8)
    for lo, hi in zip(starts, ends):
        img[lo:hi] = 1
    return img.reshape(shape).T  # Needed to align to RLE direction

df = pd.read_csv(os.path.join(ROOT_DIR, csv_train))

ImageId = '0005d01c8.jpg'	# 2 ships
# ImageId = '0a8d5d261.jpg'	# 1 ship
# ImageId = 'f7c6d7036.jpg'   # difficlut
# ImageId = 'd63134c57.jpg'   # ???
# ImageId = '5ab6e21fc.jpg'   # ???



img = imread(os.path.join(ROOT_DIR, 'ships_train2018/' + ImageId))
rle_masks = df.loc[df['ImageId'] == ImageId, 'EncodedPixels'].tolist()

# Take the individual ship masks and create a single mask array for all ships
all_masks = np.zeros((768, 768))
for mask in rle_masks:
    all_masks += rle_decode(mask)


# fig, axarr = plt.subplots(1, 3, figsize=(15, 40))
fig, axarr = plt.subplots(1, 3)
axarr[0].axis('off'),
axarr[1].axis('off'),
axarr[2].axis('off')
axarr[0].imshow(img),
axarr[1].imshow(all_masks),
axarr[2].imshow(img)
axarr[2].imshow(all_masks, alpha=0.4)
plt.tight_layout(h_pad=0.1, w_pad=0.1)
# plt.savefig( os.path.join(ROOT_DIR, '../tmp', 'tmp.png') )
plt.show()