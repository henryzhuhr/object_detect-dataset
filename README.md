# 目标检测数据集处理
这是一个目标检测预处理的脚本库，

## 功能
- [x] VOC -> yolo
- [x] [yolo -> coco](#yolo-to-coco): 转化为 COCO 数据集用于 [ultralytics/yolov5](https://github.com/ultralytics/yolov5) 项目
## 安装
```
pip3 install -r requirements.txt
```
## 使用说明

目录结构
```bash
·
└── objdect-dataset # 数据集目录
    ├── src         # 原始数据，按照类别进行归档
    ├── labeled     # 压缩、重命名后的文件，在这里进行标注
    ├── VOC         # VOC 标准数据集，用于训练
    └── coco        # coco 标准数据集，用于训练
```

加载数据集目录
> 例如数据集目录位于 `~/datasets/objdect-dataset` 
```python
import os
from objectdetect_dataset_processor import ObjDetectLabelParse

datasetparser=ObjDetectLabelParse(
    dataset_root=os.path.expanduser('~')+'datasets/objdect-dataset',
    )
```

###  VOC to yolo
```python
datasetparser.voc2yolo()
```



###  yolo to coco
COCO: https://cocodataset.org


转化为 coco 数据集，并在 `objdect-dataset` 目录下生成 `coco` 目录
```python
datasetparser.yolov2coco()
```
> 
```bash
└── objdect-dataset 
    ├── ...
    └── coco        # + coco 标准数据集，用于训练
```



## 相关仓库

- [labelImg](https://github.com/tzutalin/labelImg): 用于目标检测数据的图像标注软件