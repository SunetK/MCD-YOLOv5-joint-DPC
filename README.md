# MCD-YOLOv5-joint-DPC
The detection and analysis of molecular clumps can lead to a better understanding of the star formation in the Milky Way galaxy. Herein, we present a molecular-clump-detection method based on an improved YOLOv5 joint Density Peak Clustering (DPC). We use an improved YOLOv5 to detect the positions of molecular clumps on the galactic plane to obtaining the spatial information. We use DPC algorithm to combine the detection results in the velocity direction.  
## MCD-YOLOv5
To enhance the ability of YOLOv5 in detecting small molecular clumps, we introduce Coordinate Attention (CA) module and Normalized Wasserstein Distance (NWD) loss function to YOLOv5. See the [YOLOv5 Docs](https://docs.ultralytics.com/yolov5) for full documentation on training, testing and deployment. 
### Install
Clone repo and install [requirements.txt](https://github.com/ultralytics/yolov5/blob/master/requirements.txt) in a
[**Python>=3.7.0**](https://www.python.org/) environment, including
[**PyTorch>=1.7**](https://pytorch.org/get-started/locally/).
### Train On Custom Data
Creating a custom model to detect your objects is an iterative process of collecting and organizing images, labeling your objects of interest, training a model, deploying it into the wild to make predictions, and then using that deployed model to collect examples of edge cases to repeat and improve.
#### 1. Create Dataset
YOLOv5 models must be trained on labelled data in order to learn classes of objects in that data. 
##### 1.1 Collect Images
YOLOv5 models will learn by example. You can use `Image.py` to get examples from the FITS files.
##### 1.2 Create Labels
Once you have collected images, you will need to annotate the objects of interest to create a ground truth for your model to learn from.
##### 1.3 Prepare Dataset for YOLOv5
#### 2. Select a Model
#### 3. Train
