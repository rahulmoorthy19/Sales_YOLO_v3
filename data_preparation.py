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
        anob_x_min,anob_y_min,anob_x_max,anob_y_max,anob_brand=[],[],[],[],[]
        for j in range(number_of_objects):
            anob_x_min.append(i.split()[5*j+2])
            anob_y_min.append(i.split()[5*j+3])
            anob_x_max.append(str(int(i.split()[5*j+2])+int(i.split()[5*j+4])))
            anob_y_max.append(str(int(i.split()[5*j+3])+int(i.split()[5*j+5])))
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
        annotation_per_file.write(str(width)+" "+str(height)+"\n")
        for j in range(len(anob_brand)):
            annotation_per_file.write(anob_brand[j]+" "+anob_x_min[j]+" "+anob_y_min[j]+" "+anob_x_max[j]+" "+anob_y_max[j]+"\n")
        annotation_per_file.close()
    annotation_file.close()
    print("Train Test Distribution of Annotation Files done!")

def annotation_load(ann_dir, img_dir, labels=[]):
    all_insts = []
    seen_labels = {}
    for ann in sorted(os.listdir(ann_dir)):
        img = {'object':[]}
        img["filename"]=img_dir+os.path.basename(ann).split(".")[0]+".JPG"
        annotation_file = open(ann_dir+ann, "r")
        k=0
        obj = {}
        for j in annotation_file.readlines():
            if k==0:
                img['width'] = int(j.split()[0])
                img["height"]= int(j.split()[1])
            else:
                obj['name']=j.split()[0]
                if obj['name'] in seen_labels:
                    seen_labels[obj['name']] += 1
                else:
                    seen_labels[obj['name']] = 1
                if len(labels) > 0 and obj['name'] not in labels:
                    break
                else:
                    img['object'] += [obj]
                obj['xmin'] = int(round(float(j.split()[1])))
                obj['ymin'] = int(round(float(j.split()[2])))
                obj['xmax'] = int(round(float(j.split()[3])))
                obj['ymax'] = int(round(float(j.split()[4])))

            if len(img['object']) > 0:
                all_insts += [img]
            k=k+1
    return all_insts

# train_test_annotation_convert("A:\\Infilect_project\\Product_detector\\Dataset\\annotation.txt")
# all_insts,seen_labels=annotation_load("A:\\Infilect_project\\Product_detector\\Dataset\\Annotations\\train\\","A:\\Infilect_project\\Product_detector\\Dataset\\ShelfImages\\train\\",["0","1","2","3","4","5","6","7","8","9"])
