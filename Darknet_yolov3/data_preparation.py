import os
import glob
from PIL import Image

def train_test_annotation_convert(txt_name):
    train_data=[f for f in os.listdir("A:\\Infilect_project\\Product_detector\\Dataset\\ShelfImages\\train") if f.endswith('.JPG')]
    test_data=[f for f in os.listdir("A:\\Infilect_project\\Product_detector\\Dataset\\ShelfImages\\test") if f.endswith('.JPG')]
    annotation_file = open(txt_name, "r")
    for i in annotation_file.readlines():
        file_name=i.split()[0]
        number_of_objects=int(i.split()[1])
        anob_x_mid,anob_y_mid,anob_width,anob_height,anob_brand=[],[],[],[],[]
        data_dist=""
        width=0
        height=0
        if file_name in train_data:
            data_dist="train"
            im = Image.open('A:\\Infilect_project\\Product_detector\\Dataset\\ShelfImages\\train\\'+file_name)
            width, height = im.size
        else:
            data_dist="test"
            im = Image.open("A:\\Infilect_project\\Product_detector\\Dataset\\ShelfImages\\test\\"+file_name)
            width, height = im.size
        for j in range(number_of_objects):
            x_min=int(i.split()[5*j+2])
            x_max=int(i.split()[5*j+2])+int(i.split()[5*j+4])
            y_min=int(i.split()[5*j+3])
            y_max=int(int(i.split()[5*j+3])+int(i.split()[5*j+5]))
            anob_brand.append(i.split()[5*j+6])
            anob_width.append(round(int(i.split()[5*j+4])/width,2))
            anob_height.append(round(int(i.split()[5*j+5])/height,2))
            anob_x_mid.append(round(((x_min+x_max)/2)/width,2))
            anob_y_mid.append(round(((y_min+y_max)/2)/height,2))
        annotation_per_file = open("A:\\Infilect_project\\Product_detector\\Dataset\\Darknet_annotations\\"+data_dist+"\\"+file_name.split(".")[0]+".txt", "a")
        for j in range(len(anob_brand)):
            annotation_per_file.write(anob_brand[j]+" "+str(anob_x_mid[j])+" "+str(anob_y_mid[j])+" "+str(anob_width[j])+" "+str(anob_height[j])+"\n")
        annotation_per_file.close()
    annotation_file.close()
    print("Train Test Distribution of Annotation Files done!")

def train_test_write():
    dataset_file_train=open("A:\\Infilect_project\\Product_detector\\Sales_YOLO_v3\\Darknet_yolov3\\darknet\\product_train.txt","a")
    for i in glob.glob("A:\\Infilect_project\\Product_detector\\Dataset\\ShelfImages\\train\\*.JPG"):
        dataset_file_train.write(i+"\n")
    dataset_file_train.close()
    dataset_file_test=open("A:\\Infilect_project\\Product_detector\\Sales_YOLO_v3\\Darknet_yolov3\\darknet\\product_test.txt","a")
    for i in glob.glob("A:\\Infilect_project\\Product_detector\\Dataset\\ShelfImages\\test\\*.JPG"):
        dataset_file_test.write(i+"\n")
    dataset_file_test.close()
    print("Write Complete")
# train_test_annotation_convert("A:\\Infilect_project\\Product_detector\\Dataset\\annotation.txt")
train_test_write()
