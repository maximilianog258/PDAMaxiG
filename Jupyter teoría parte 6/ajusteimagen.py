
from imageMejorada import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from utils2 import crearMatrix
import copy
import math as math


def ajustarBrillo(imagene, ajuste=1):
    """Recive un objeto de la clase Image y un valor de ajuste, retorna un objeto de la clase Image con el brillo ajustado según el valor pasado"""
    brilloajustado=copy.deepcopy(imagene)
    abrillar=brilloajustado.image
    #arraybrillo=np.full((imagene.fil,imagene.col,3), ajuste)
    abrillar2=abrillar*ajuste
    mask = abrillar2[:,:,:] > 255
    abrillar2[mask]=255
    brilloajustado.image=abrillar2

    # for rgb in range(3):
    #     for n in range(imagene.col):
    #         for m in range(imagene.fil):
    #             pixel=int(abrillar[m,n,rgb]*ajuste)
    #             if pixel<0:
    #                 pixel=0
    #             elif pixel>255:
    #                 pixel=255
    #             abrillar[m,n,rgb]=pixel
    #brilloajustado.showImage()
    return brilloajustado



def getHistograma(image):
    """Recibe un objeto de la clase Imagen, retorna una matriz 256x3 con los valores del histpgrama y también muestra 3 figuras con los 3 histogramas correspondientes"""
    #canales=getChannels(image)
    lista=np.arange(0,256,1)
    historojo, bins=np.histogram(image.image[:,:,0], bins=256, range=(0, 255))
    histoverde, bins=np.histogram(image.image[:,:,1], bins=256, range=(0, 255))
    histoazul, bins=np.histogram(image.image[:,:,2], bins=256, range=(0, 255))


    listarojos=historojo
    listaverdes=histoverde
    listaazules=histoazul
    
    # listarojos=np.histogram(canales[3])
    # listaverdes=np.histogram(canales[4])
    # listaazules=np.histogram(canales[5])
    # lista=[]
    # listarojos=[]
    # listaverdes=[]
    # listaazules=[]
    # for i in range(256):
    #     lista.append(i)
    #     listarojos.append(0)
    #     listaverdes.append(0)
    #     listaazules.append(0)


    # contador=0
    # for i in lista:
    #     for n in range(image.col):
    #         for m in range(image.fil):
    #             if (canales[3].image)[m,n]==i:
    #                 listarojos[i]=listarojos[i]+1
    #             if (canales[4].image)[m,n]==i:
    #                 listaverdes[i]=listaverdes[i]+1
    #             if (canales[5].image)[m,n]==i:
    #                 listaazules[i]=listaazules[i]+1
    #             contador=contador+1
    #             #print(contador)
    figrojo = plt.figure(figsize = (10, 5))
    plt.bar(lista, listarojos, color ='red')
    plt.xlabel("0 Negro, 255 Blanco")
    plt.ylabel("Cantidad de veces que se repite")
    plt.title("Histograma Rojo")
    figverde = plt.figure(figsize = (10, 5))
    plt.bar(lista, listaverdes, color ='green')
    plt.xlabel("0 Negro, 255 Blanco")
    plt.ylabel("Cantidad de veces que se repite")
    plt.title("Histograma Verde")
    figrazul= plt.figure(figsize = (10, 5))
    plt.bar(lista, listaazules, color ='blue')
    plt.xlabel("0 Negro, 255 Blanco")
    plt.ylabel("Cantidad de veces que se repite")
    plt.title("Histograma Azul")
    plt.show()


    # return [listarojos,listaverdes,listaazules]

def getChannels(image):
    """Recibe un objeto de la clase imagen y devuelve 3 objetos de la misma que corresponden cada uno a uno de los canales"""
    rojo=copy.deepcopy(image)
    verde=copy.deepcopy(image)
    azul=copy.deepcopy(image)
    rojo2=Image((image.fil,image.col,3))
    verde2=Image((image.fil,image.col,3))
    azul2=Image((image.fil,image.col,3))
    rojo2.image[:,:,0]=rojo.image[:,:,0]
    verde2.image[:,:,1]=verde.image[:,:,1]
    azul2.image[:,:,2]=azul.image[:,:,2]
    rojo.image=rojo.image[:,:,0]
    verde.image=verde.image[:,:,1]
    azul.image=azul.image[:,:,2]

    return rojo2,verde2,azul2,rojo,verde,azul

def ajustarContraste(image, alfa):
    """Ajusta el contraste de una imágen.
    
    Retorna una nueva imágen con las mismas dimensiones de la imágen original.

    Recive un objeto de la clase Image y un valor de ajuste, retorna un objeto de la clase Image con el contraste ajustado según el valor pasado


    """
    imagenProcesada=copy.deepcopy(image)
    s128=np.full((image.fil,image.col,3), 128)
    nueva=alfa*(imagenProcesada.image[:,:,:]-s128) + s128
    mask1 = nueva[ : , : , : ] > 255
    nueva[mask1]=255
    mask2 = nueva[ : , : , : ] < 0
    nueva[mask2]=0
    imagenProcesada.image=nueva
    # for canal in range(3):
    #     for i in range(imagenProcesada.fil):
    #         for j in range(imagenProcesada.col):
    #             pixel = int(alfa*(imagenProcesada.image[i][j][canal]-128) + 128)
    #             if pixel < 0:
    #                 pixel = 0
    #             elif pixel > 255:
    #                 pixel = 255
    #             imagenProcesada.image[i][j][canal] = pixel
                
    return imagenProcesada

def ajustarGamma(image, gamma):
    """ Recive un objeto de la clase Image y un valor de ajuste, retorna un objeto de la clase Image con la gamma ajustada según el valor pasado"""
    max=0
    imagenProcesada=copy.deepcopy(image)
    max=imagenProcesada.image.max()
    #for canal in range(3):
     #   for i in range(imagenProcesada.fil):
      #      for j in range(imagenProcesada.col):
       #         if imagenProcesada.image[i][j][canal]>maximo:
        #            maximo=imagenProcesada.image[i][j][canal]
    #print(maximo)
    #contador=0
    c=255/((max)**gamma)
    arraygamma=np.full((image.fil,image.col,3), gamma)
    #for canal in range(3):
     #   for i in range(imagenProcesada.fil):
      #      for j in range(imagenProcesada.col):
       #         pixel=c*(imagenProcesada.image[i][j][canal])**gamma
                #print(contador)
        #        contador=contador+1
         #       imagenProcesada.image[i][j][canal] = pixel
    imagenProcesada.image=c*np.power(imagenProcesada.image,arraygamma)
    return imagenProcesada

def aplicarKernel(image, kernel):
    """ Retorna un objeto de la clase imagen transformado con un kernel"""
    contador=0
    imagenProcesada=copy.deepcopy(image)
    c=kernel[0][0]+kernel[0][1]+kernel[0][2]+kernel[1][0]+kernel[1][1]+kernel[1][2]+kernel[2][0]+kernel[2][1]+kernel[2][2]
    if c==0:
        c=1
    a=0
    #array=[[a[i-1,j-1,canal] , a[i-1,j,canal],a[i-1,j+1,canal] ],[a[i,j-1,canal],a[i,j,canal] ,a[i,j+1,canal]],[a[i+1,j-1,canal],a[i+1,j,canal] ,a[i+1,j+1,canal]]]
    for canal in range(3):
        for i in range(1,imagenProcesada.fil-1):
            for j in range(1,imagenProcesada.col-1):
                a=imagenProcesada.image
                array=[[a[i-1,j-1,canal] , a[i-1,j,canal],a[i-1,j+1,canal] ],[a[i,j-1,canal],a[i,j,canal] ,a[i,j+1,canal]],[a[i+1,j-1,canal],a[i+1,j,canal] ,a[i+1,j+1,canal]]]
                array=np.array(array)
                kernel=np.array(kernel)
                suma=np.sum(array*kernel)
                #p00=(imagenProcesada.image[i-1,j-1,canal])*kernel[0][0]
                #p01=(imagenProcesada.image[i-1,j,canal])*kernel[0][1]
                #p02=(imagenProcesada.image[i-1,j+1,canal])*kernel[0][2]
                #p10=(imagenProcesada.image[i,j-1,canal])*kernel[1][0]
                #p11=(imagenProcesada.image[i,j,canal])*kernel[1][1]
                #p12=(imagenProcesada.image[i,j+1,canal])*kernel[1][2]
                #p20=(imagenProcesada.image[i+1,j-1,canal])*kernel[2][0]
                #p21=(imagenProcesada.image[i+1,j,canal])*kernel[2][1]
                #p22=(imagenProcesada.image[i+1,j+1,canal])*kernel[2][2]
                #pixel = (p00+p01+p02+p10+p11+p12+p20+p21+p22)//c
                pixel=suma//c
                #contador=contador+1
                if pixel < 0:
                    pixel = 0
                elif pixel > 255:
                    pixel = 255
                #pixel=int(pixel)
                #print(contador)
                imagenProcesada.image[i][j][canal] = pixel
    return imagenProcesada

def aplicarKernel2(image, kernel):
    imagenProcesada=copy.deepcopy(image)
    c=np.sum(kernel)
    if c==0:
        c=1
    a=0
    
    

def aplicarLog(image):
    """ Retorna un objeto de la clase imagen transformado con una función logarítmmica"""
    max=0
    imagenProcesada=copy.deepcopy(image)
    max=imagenProcesada.image.max()
    # for canal in range(3):
    #     for i in range(imagenProcesada.fil):
    #         for j in range(imagenProcesada.col):
    #             if imagenProcesada.image[i][j][canal]>maximo:
    #                 maximo=imagenProcesada.image[i][j][canal]
    c=255/(math.log(1+max))
    s1=np.full((image.fil,image.col,3), 1)
    nueva=c*(np.log((s1+imagenProcesada.image[:,:,:])))
    imagenProcesada.image=nueva
    # print(maximo)
    # contador=0
    # c=255/(math.log(1+maximo))
    # for canal in range(3):
    #     for i in range(imagenProcesada.fil):
    #         for j in range(imagenProcesada.col):
    #             pixel=c*(math.log((1+imagenProcesada.image[i][j][canal])))
    #             #print(contador)
    #             contador=contador+1
    #             imagenProcesada.image[i][j][canal] = pixel
    return imagenProcesada





def main():
    # #Mostrar su implementación aquí
    # #imagen2=Image((8,8,3))
    imagen=Image(filename='starship.jpg')
    imagen.showImage()
    brilloajustado=ajustarBrillo(imagen,1.6)
    # # amostrar=plt.imshow(brillosa2)
    brilloajustado.showImage()
    #contrastada=ajustarContraste(imagen,2)
    #contrastada.showImage()
    kernel=[[0.0625,0.125,0.0625],[0.125,0.25,0.125],[0.0625,0.125,0.0625]] #blur
    # #kernel=[[0,-1,0],[-1,8,-1],[0,-1,0]] #sharpen
    # #print(kernel[0][0]+kernel[0][1]+kernel[0][2]+kernel[1][0]+kernel[1][1]+kernel[1][2]+kernel[2][0]+kernel[2][1]+kernel[2][2])
    # kerneleada=aplicarKernel(imagen,kernel)
    # kerneleada.showImage()
    # #print(kernel[2][2])
    #gammaajustada=ajustarGamma(imagen,2)
    #gammaajustada.showImage()
    # canales=getChannels(imagen)
    # canales[0].showImage()
    # canales[1].showImage()
    # canales[2].showImage()
    #histo=getHistograma(imagen)
    # print(histo)
    # print(np.shape(histo))
    # logaritmeada=aplicarLog(imagen)
    # logaritmeada.showImage()


    pass

if __name__ == '__main__':
    
    main()


