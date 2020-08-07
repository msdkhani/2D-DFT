#2D DFT in image processing
#import Just the needed library to work with image
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageDraw
import cmath

#2D-DFT Fourmula
def DFT2D(padded):
    M,N = np.shape(padded)

    dft2d = np.zeros((M,N),dtype=complex)
    for k in range(M):
        for l in range(N):
            sum_matrix = 0.0

            for m in range(M):
                for n in range(N):

                    e = cmath.exp(- 2j * np.pi * (float(k * m) / M + float(l * n) / N))
                    sum_matrix +=  padded[m,n] * e

            dft2d[k,l] = sum_matrix
    return dft2d

#Inverse 2D-DFT
def IDFT2D(dft2d):
    M,N=dft2d.shape 
    pixels = np.zeros((M,N))

    for m in range(M):
        for n in range(N):

            sum_ = 0.0
            for k in range(M):
                for l in range(N):

                    e = cmath.exp(2j * np.pi * (float(k * m) / N + float(l * n) / M))
                    sum_ += dft2d[l][k] * e

            #get the real part of pixel to show the image
            pixel = sum_.real/M/N
            pixels[n, m] = (pixel)

    return pixels

#generate Ideal Low-pass filter
def lowPass(padded):
    #size of image
    U,V = np.shape(padded)
    #H is our filter
    H = np.zeros((U,V))
    D = np.zeros((U,V))
    U0 = int(U/2)
    V0 = int(V/2)
    #cut off
    D0 = 10
    for u in range(U):
        for v in range(V):
            u2 = np.power(u,2)
            v2 = np.power(v,2)
            D[u,v] = np.sqrt(u2+v2)
        
    for u in range(U):
        for v in range(V):        
            if D[np.abs(u-U0),np.abs(v-V0)] <= D0:
                H[u,v] = 1
            else:
                H[u,v] = 0
    return H

if __name__ == "__main__":
    fig = plt.figure()

    #import image and conver it into gray-scale
    image = Image.open("profile.jpg").convert("L")
    #resize image
    image = image.resize((30,30))
    #get the pixels of image into array
    f = np.asarray(image)
    M, N = np.shape(f) # (img x, img y)
    #padded the image with M*2-1 and N*2-1 size
    P,Q = M*2-1,N*2-1
    shape = np.shape(f)
    #our padded array
    fp = np.zeros((P, Q))
    #import our image into padded array
    fp[:shape[0],:shape[1]] = f

    #create new matrix to center the transform
    fpc = np.zeros((P, Q))
    for x in range(P):
        for y in range(Q):
            fpc[x,y]=fp[x,y]*np.power(-1,x+y)
    #Transform the image into frequency domian
    dft2d = DFT2D(fpc)
    #create Low-pass filter
    H = lowPass(dft2d)
    #apply filter by mutliply it with transformed image
    G=np.multiply(dft2d,H)
    #get the inverse of DFT
    g = IDFT2D(G)
    #recenter the image
    ga = np.asarray(g)
    P,Q=np.shape(ga)
    gp = np.zeros((P,Q))
    for x in range(P):
        for y in range(Q):
            gp[x,y] = ga[x,y]*np.power(-1,x+y)
    #extraction the image from padded array 
    org_img=gp[:shape[0],:shape[1]]

    #plot and show filtered image
    a = fig.add_subplot(3, 3, 1)
    imgplot = plt.imshow(image,cmap='gray')
    a.set_title('Original image')

    a = fig.add_subplot(3, 3, 2)
    imgplot = plt.imshow(fp,cmap='gray')
    a.set_title('padded image')

    a = fig.add_subplot(3, 3, 3)
    imgplot = plt.imshow(fpc,cmap='gray')
    a.set_title('center transform')

    a = fig.add_subplot(3 , 3, 4)
    imgplot1 = plt.imshow(dft2d.real,cmap='gray')
    a.set_title('2D Dft')
    

    a = fig.add_subplot(3, 3, 5)
    imgplot = plt.imshow(H,cmap='gray')
    a.set_title('filter')

    a = fig.add_subplot(3, 3, 6)
    imgplot = plt.imshow(G.real,cmap='gray')
    a.set_title('filtered image')

    a = fig.add_subplot(3, 3, 7)
    imgplot = plt.imshow(g,cmap='gray')
    a.set_title('Inverse DFT image')

    a = fig.add_subplot(3, 3, 8)
    imgplot = plt.imshow(gp,cmap='gray')
    a.set_title('recenter ')

    a = fig.add_subplot(3, 3, 9)
    imgplot2 = plt.imshow(org_img,cmap='gray')
    a.set_title('filtered Image')
    plt.show()