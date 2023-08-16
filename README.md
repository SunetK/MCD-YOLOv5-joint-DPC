# MCD-YOLOv5-joint-DPC
The detection and analysis of molecular clumps can lead to a better understanding of the star formation in the Milky Way galaxy. Herein, we present a molecular-clump-detection method based on an improved YOLOv5 joint Density Peak Clustering (DPC). We use an improved YOLOv5 to detect the positions of molecular clumps on the galactic plane to obtaining the spatial information. We use DPC algorithm to combine the detection results in the velocity direction.  
## MCD-YOLOv5
To enhance the ability of YOLOv5 in detecting small molecular clumps, we introduce Coordinate Attention (CA) module and Normalized Wasserstein Distance (NWD) loss function to YOLOv5. See the [YOLOv5 Docs](https://docs.ultralytics.com/yolov5) for full documentation on training, testing and deployment. 
### Install
Clone repo and install [requirements.txt](https://github.com/SunetK/MCD-YOLOv5-joint-DPC/blob/main/MCD-YOLOv5/requirements.txt) in a
[**Python>=3.7.0**](https://www.python.org/) environment, including
[**PyTorch>=1.7**](https://pytorch.org/get-started/locally/).
### Train On Custom Data
Creating a custom model to detect your objects is an iterative process of collecting and organizing images, labeling your objects of interest, training a model, deploying it into the wild to make predictions, and then using that deployed model to collect examples of edge cases to repeat and improve.
#### 1. Create Dataset
MCD-YOLOv5 must be trained on labelled data in order to learn classes of objects in that data. 
##### 1.1 Collect Images
MCD-YOLOv5 models will learn by example of molecular clumps. You can use `Image.py` to get examples from the FITS files.
##### 1.2 Create Labels
Once you have collected examples of molecular clumps, you will need to annotate the objects of interest to create a ground truth for MCD-YOLOv5 to learn from. You can use `Xml.py` to get annotations from the clump parameter table.
##### 1.3 Prepare Dataset for YOLOv5
Once you have collected examples and created labels, you should put them in the folders named JPEGImages and Annotations in VOCdevkit, respectively. Then, you should use `xml2txt.py` and `split_data.py` to divide the dataset into a training set, a validation set, and a test set.
#### 2. Train
You can use `train.py` to train the MCD-YOLOv5 on your data.
#### 3. Detect
Once the training is over, you can use the `detect.py` to detect the new examples.
## After-YOLOv5
After the detection of MCD-YOLOv5, you should put the results into the `After-YOLOv5` to get the input of DPC. You just need run the grogram in turn and put the new examples, the detection results, and FITS files in Specified folders, you can realize it.
## DPC
You can get the results of the DPC by using `mainDensityClust.mat`.
Finally, you should save the clustering results in txt text and use `Result.py` to get the clump-detection results.
