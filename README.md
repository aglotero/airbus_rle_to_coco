## Make COCO Dateset

本代码是针对Kaggle比赛 [Airbus Ship Detection Challenge](https://www.kaggle.com/c/airbus-ship-detection) 制作的RLE-->COCO 数据集转换工具;

主要有以下几个功能：

1. 数据集中存在大量的负样本，将其删除，只保留存在实例的图片
2. airbus提供的数据是RLE格式的，将其转化为COCO数据集格式，得到标准的.json标注文件
3. 筛选出不好的标注文件



This code is for Kaggle competiton [Airbus Ship Detection Challenge](https://www.kaggle.com/c/airbus-ship-detection), which can help you transform RLE to coco dataset. It has 3 main functions:

1. Delete useless images without ships;
2. Transform RLE into coco;
3. Store bad annotations into folder ../tmp/bad_anns;

## File structure

    airbus_dataset
    ├─input						# dataset
    │  ├─annotations            # .json
    │  └─ships_train2018        # pictures
    ├─airbus_rle_to_coco        # this code
    │  └─ xxx.py
    └─tmp                       # bad annotations


## Installation

1、install pycocotool

    git clone https://github.com/waleedka/coco
    cd coco/PythonAPI
    make
    python setup.py install

2、install [pycococreator](https://github.com/waspinator/pycococreator)


    pip install git+git://github.com/waspinator/pycococreator.git@0.2.0

3、install pandas

    pip install pandas
