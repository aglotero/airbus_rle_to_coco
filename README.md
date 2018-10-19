## 制作COCO数据集

本代码是针对Kaggle比赛 [Airbus Ship Detection Challenge](https://www.kaggle.com/c/airbus-ship-detection) 制作的RLE-->COCO 数据集转换工具;

主要有以下几个功能：

1. 数据集中存在大量的负样本，将其删除，只保留存在实例的图片
2. airbus提供的数据是RLE格式的，将其转化为COCO数据集格式，得到标准的.json标注文件
3. 筛选出不好的标注文件

## Make COCO Dateset

This code is for Kaggle competiton [Airbus Ship Detection Challenge](https://www.kaggle.com/c/airbus-ship-detection), which can help you transform RLE into COCO annotations. It has 3 main functions:

1. Delete useless images without ships;

2. Transform RLE into COCO annotations;

3. Store bad annotations into folder ../tmp/bad_anns;


![dataset annotation](https://github.com/pascal1129/airbus_rle_to_coco/blob/master/image/result.png)



## File structure

    airbus_dataset
    ├─input                                     # dataset and annotations
    │  ├─annotations            		
    │  │  └─ instances_ships_train2018.json     # .json, which will be generated by us
    │  │
    │  ├─ships_train2018                        # ship pictures
    │  │  ├─ 000d42241.jpg
    │  │  ├─ 000e6378b.jpg
    │  │  └─ xxx.jpg
    │  │
    │  └─train_ship_segmentations_v2.csv        # annotations in RLE style
    │
    ├─airbus_rle_to_coco                        # here we are
    │  ├─ 0_airbus_delete_empty_im.py           # delete images without ships
    │  ├─ 0_csv_show_RLE.py                     # show annotations in RLE style
    │  ├─ 1_ships_to_coco.py                    # turn RLE into COCO
    │  └─ 2_pycoco_API_Demo.ipynb               # show annotations in COCO style 
    │
    └─tmp                                       # bad annotations


## Installation

1、install pycocotool

    git clone https://github.com/waleedka/coco
    cd coco/PythonAPI
    make
    python setup.py install

2、install [pycococreator](https://github.com/waspinator/pycococreator)


    pip install git+git://github.com/waspinator/pycococreator.git@0.2.0

3、install pandas and something others

    pip install pandas



## Step

1. run  0_airbus_delete_empty_im.py, which can delete empty images without ships

2. run  0_csv_show_RLE.py, which can show dataset in RLE style

3. run  1_ships_to_coco.py, which generates .json file. Here is a finished one:  

   [instances_ships_train2018.json](https://storage.googleapis.com/kaggle-forum-message-attachments/inbox/1998668/159ec0e9b79f7eae65826a1a3377e970/instances_ships_train2018.zip)

4. run  2_pycoco_API_Demo.ipynb, which can show dataset in COCO style
