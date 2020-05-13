import glob
from PIL import Image
train_width=list()
train_height=list()
test_width=list()
test_height=list()
for i in sorted(glob.glob("A:\\Infilect_project\\Product_detector\\Dataset\\ShelfImages\\train\\*.JPG")):
    im = Image.open(i)
    width, height = im.size
    train_width.append(width)
    train_height.append(height)
for i in sorted(glob.glob("A:\\Infilect_project\\Product_detector\\Dataset\\ShelfImages\\test\\*.JPG")):
    im = Image.open(i)
    width, height = im.size
    test_width.append(width)
    test_height.append(height)
print("Max width train "+str(max(train_width)))
print("Min width train "+str(min(train_width)))
print("Max height train "+str(max(train_height)))
print("Min height train "+str(min(train_height)))
print("Max width test "+str(max(test_width)))
print("Min width test "+str(min(test_width)))
print("Max height test "+str(max(test_height)))
print("Min height test "+str(min(test_height)))
