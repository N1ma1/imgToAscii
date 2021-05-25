import sys, random
import numpy as np 
import math 
from PIL import Image 
gscale2 = "@%#*+=-:." 
# gscale2 = '.-*@'
def getAverageL(image): 
    im = np.array(image) 
    w,h = im.shape 
    return np.average(im.reshape(w*h)) 
def convertImageToAscii(fileName, cols, scale): 
    global gscale1, gscale2 
    image = Image.open(fileName).convert('L') 
    W, H = image.size[0], image.size[1] 
    # print("input image dims: %d x %d" % (W, H)) 
    w = W/cols 
    h = w/scale 
    rows = int(H/h) 
    # print("cols: %d, rows: %d" % (cols, rows)) 
    # print("tile dims: %d x %d" % (w, h)) 
    if cols > W or rows > H: 
        # print("Image too small for specified cols ; {")
        print("be molla ridi. ye aks gonde tar bede ; {") 

        exit(0) 
    aimg = [] 
    for j in range(rows): 
        y1 = int(j*h)
        y2 = int((j+1)*h) 
        if j == rows-1: 
            y2 = H 
        aimg.append("") 
        for i in range(cols): 
            x1 = int(i*w)
            x2 = int((i+1)*w)
            if i == cols-1: 
                x2 = W 
            img = image.crop((x1, y1, x2, y2)) 
            avg = int(getAverageL(img))
            #print(avg)
            gsval = gscale2[int((avg*9)/255)]
            aimg[j] += gsval 
    return aimg 

def main(imgFile,cols=60,path=''):  
    # This program converts an image into ASCII art ; {
    outFile = 'out.txt'
    scale = 0.43
    # print('generating ASCII art') 
    aimg = convertImageToAscii(imgFile, cols, scale) 
    if(path != ''):
        f = open(path+outFile,'w')
    else:
        f = open(outFile, 'w') 
    for row in aimg: 
        f.write(row + '\n') 
    f.close() 
    print("ASCII art written to %s" % outFile) 
if __name__ == "__main__":
    main(sys.argv[1],int(sys.argv[2])) 
