
# Safety Helmet Detection 
![Maintained](https://img.shields.io/badge/Maintained%3F-yes-green.svg)

### Index:

* [Description](#description)<br>
* [Technical](#technical)<br>
* [Colaborate](#colab)<br>

<a name="description"></a>
# Description

Object detection system developed with deep learning techniques, capable to recognize if workers in construction areas are using their safety helmet in mandatory areas. The next objective it's to detect not only the helmets but also the people who puntually are unprotected, creating a warning.


**Safety Helmet** will be an integrated part of a dedicated ecosystem for secure safety habits on working dangerous areas, focusing on the scalability of the detection system trying to make it capable of covering the most scenarios posibles.



This project also haves a Colab repository for online testing at 
[Colab page](https://colab.research.google.com/drive/1JRMI-gtHzw-gFXSa3lsQNnJ9fDMumQEg?usp=sharing).

### Made with:

![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)

<a name="technical"></a>
# Technical

### Dataset:

The dataset consist of 5000 images `/data/images` with annotations `/data/labels`, then divided on training and test subgroups.

> [!NOTE]
> I used a converter `/tools/coverter.py` to addapt the previous labels format (.xml) to an accepted one (.txt), read script documentation before using

See full dataset documentation on [this link](https://www.kaggle.com/datasets/andrewmvd/hard-hat-detection).

### Training:

Consist of a traditional YoloV8 training with a pretrained model, we apply a fine tunning for helmet detection using our custom dataset

```
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model.train(data="data.yaml", epochs=10)
result = model.val()
path = model.export(format="onnx")
```

### Test output:

We recieve our trained model at `/runs/detect/train6/weights/best.pt` with some metrics for training analysis.

[![confusion-matrix-normalized.png](https://i.postimg.cc/rpQMnB0P/confusion-matrix-normalized.png)](https://postimg.cc/VSrx5HFq)

<a name="colab"></a>
# Colaborate

If you want to colaborate on this project, you are invited to create a Pull Request with a descriptive text of the changes/updates.

You can also contact me: 
[jomarkow@gmail.com](mailto:jomarkow@gmail.com)

We hope you liked the project, if so, I invite you to leave a star ⭐, thanks for read :).



