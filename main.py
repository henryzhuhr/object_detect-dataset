

import os
from objectdetect_dataset_processor import ObjDetectLabelParse

datasetparser=ObjDetectLabelParse(
    dataset_root=os.path.join(os.path.expanduser('~'),'datasets/gc10_detect'),
    )
datasetparser.voc2yolo()
datasetparser.yolov2coco()