from skimage.io import imread
import matplotlib.pyplot as plt

def show_imagen(imagen):
    imagen = imread("archivo donde tenga cargada la imagen que quiero mostrar")
    

plt.imshow(imagen)

if __name__ == "__main__":
    print(type(imagen))
    print(imagen.shape)