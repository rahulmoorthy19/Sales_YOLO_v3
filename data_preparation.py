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
        anob_x,anob_y,anob_width,anob_height,anob_brand=[],[],[],[],[]
        for j in range(number_of_objects):
            anob_x.append(i.split()[5*j+2])
            anob_y.append(i.split()[5*j+3])
            anob_width.append(i.split()[5*j+4])
            anob_height.append(i.split()[5*j+5])
            anob_brand.append(i.split()[5*j+6])
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
        annotation_per_file = open("A:\\Infilect_project\\Product_detector\\Dataset\\Annotations\\"+data_dist+"\\"+file_name.split(".")[0]+".txt", "a")
        annotation_per_file.write(width+" "+height+"\n")
        for j in range(len(anob_brand)):
            annotation_per_file.write(anob_brand[j]+" "+anob_x[j]+" "+anob_y[j]+" "+anob_width[j]+" "+anob_height[j]+"\n")
        annotation_per_file.close()
    annotation_file.close()
    print("Train Test Distribution of Annotation Files done!")

def annotation_load(ann_dir, img_dir, cache_name, labels=[]):
    all_insts = []
    seen_labels = {}
    for ann in sorted(os.listdir(ann_dir)):
        img = {'object':[]}
        img["file_name"]=os.path.basename(ann)
        annotation_file = open(ann, "r")
        k=0
        obj = {}
        for j in annotation_file.readlines():
            if k==0:
                img['width'] = int(j.split()[0])
                img["height"]= int(j.split()[1])
            else:
                obj['name']=int(j.split()[0])
                if obj['name'] in seen_labels:
                    seen_labels[obj['name']] += 1
                else:
                    seen_labels[obj['name']] = 1
                img['object'] += [obj]
                obj['xmin'] = int(round(float(j.split()[1])))
                obj['xmax'] = int(round(float(j.split()[2])))
                obj['width'] = int(round(float(j.split()[3])))
                obj['height'] = int(round(float(j.split()[4])))

train_test_annotation_convert("A:\\Infilect_project\\Product_detector\\Dataset\\annotation.txt")
