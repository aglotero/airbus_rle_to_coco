## COCO数据集制作
针对 [Airbus Ship Detection Challenge](https://www.kaggle.com/c/airbus-ship-detection) 制作的RLE转COCO数据集转换工具

1. airbus提供的数据是RLE格式的，将其转化为COCO数据集格式(.json)

2. 数据集中存在大量的负样本，将其删除，只保留存在正样本的图片

## 文件结构

    airbus_dataset
    ├─input
    │  ├─annotations            # 标注文件
    │  └─ships_train2018        # 图片
    ├─src                       # 本代码所在文件夹
    │  └─ xxx.py                # 可执行脚本
    └─tmp                       # 中间文件夹


## 安装步骤

1、安装pycocotool

    git clone https://github.com/waleedka/coco
    cd coco/PythonAPI
    make
    python setup.py install

2、安装pycococreator

下面给出的不一定最新，可参见[项目Github](https://github.com/waspinator/pycococreator)


    pip install git+git://github.com/waspinator/pycococreator.git@0.2.0

3、安装pandas

    pip install pandas
