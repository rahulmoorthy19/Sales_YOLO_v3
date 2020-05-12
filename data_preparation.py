import os
import glob

def train_test_annotation_convert(txt_name):
    train_data=[f for f in os.listdir("A:\\Infilect_project\\Product_detector\\Dataset\\ShelfImages\\train") if f.endswith('.JPG')]
    test_data=[f for f in os.listdir("A:\\Infilect_project\\Product_detector\\Dataset\\ShelfImages\\test") if f.endswith('.JPG')]
    annotation_file = open(txt_name, "r")
    for i in annotation_file.readlines():
        file_name=i.split()[0]
        number_of_objects=int(i.split()[1])
        anob_x,anob_y,anob_width,anob_height,anob_brand=[],[],[],[],[]
        for j in range(number_of_objects):
            anob_x.append(i.split()[5*j+2])
            anob_y.append(i.split()[5*j+3])
            anob_width.append(i.split()[5*j+4])
            anob_height.append(i.split()[5*j+5])
            anob_brand.append(i.split()[5*j+6])
        data_dist=""
        if file_name in train_data:
            data_dist="train"
        else:
            data_dist="test"
        annotation_per_file = open("A:\\Infilect_project\\Product_detector\\Dataset\\Annotations\\"+data_dist+"\\"+file_name.split(".")[0]+".txt", "a")
        for j in range(len(anob_brand)):
            annotation_per_file.write(anob_brand[j]+" "+anob_x[j]+" "+anob_y[j]+" "+anob_width[j]+" "+anob_height[j]+"\n")
        annotation_per_file.close()
    annotation_file.close()
    print("Train Test Distribution of Annotation Files done!")



train_test_annotation_convert("A:\\Infilect_project\\Product_detector\\Dataset\\annotation.txt")
