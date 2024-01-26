from xml.dom import minidom
import os

classes={"helmet":0,"head":1,"person":2}

def convert_coordinates(size, box):
    dw = 1.0/size[0]
    dh = 1.0/size[1]
    x = (box[0]+box[1])/2.0
    y = (box[2]+box[3])/2.0
    w = box[1]-box[0]
    h = box[3]-box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def converter(classes):
    
    old_labels_path = "../data/validations_old"
    new_labels_path = "data/validations/"
    

    for file_name in os.listdir(old_labels_path):
        old_file = minidom.parse(f"{old_labels_path}/{file_name}")
        
        name_out = (file_name[:-4]+'.txt')

        with open(f"{new_labels_path}/{name_out}", "w") as new_file:

            itemlist = old_file.getElementsByTagName('object')
            size = old_file.getElementsByTagName('size')[0]
            width = int((size.getElementsByTagName('width')[0]).firstChild.data)
            height = int((size.getElementsByTagName('height')[0]).firstChild.data)

            for item in itemlist:
                # get class label
                class_name =  (item.getElementsByTagName('name')[0]).firstChild.data
                if class_name in classes:
                    label_str = str(classes[class_name])
                else:
                    label_str = "-1"
                    print (f"{class_name} not in function classes")

                # get bbox coordinates
                xmin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmin')[0]).firstChild.data
                ymin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymin')[0]).firstChild.data
                xmax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmax')[0]).firstChild.data
                ymax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymax')[0]).firstChild.data
                b = (float(xmin), float(xmax), float(ymin), float(ymax))
                bb = convert_coordinates((width,height), b)
                #print(bb)

                new_file.write(f"{label_str} {' '.join([(f'{a}.6f') for a in bb])}\n")

        print (f"wrote {name_out}")



def main():
    converter(classes)


if __name__ == '__main__':
    main()