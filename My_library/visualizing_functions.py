from skimage.io import imread
import matplotlib.pyplot as plt
import seaborn as sns

# Algunas configuraciones de los paquetes
sns.set(color_codes = True)
pd.set_option("display.max_rows", 500)


# para eliminar los warnings
import warnings
warnings.filterwarnings("ignore")

def show_imagen(imagen):
    imagen = imread("archivo donde tenga cargada la imagen que quiero mostrar")
    

plt.imshow(imagen)

if __name__ == "__main__":
    print(type(imagen))
    print(imagen.shape)




    """" FuncFormatter; que acepta una función definida por el usuario que brinda un control detallado sobre los outputs de kit"""
def format_func(value, tick_number):
    pass
    # find number of multiples of pi/2
    N = int(np.round(2 * value / np.pi))
    if N == 0:
        return "0"
    elif N == 1:
        return r"$\pi/2$"
    elif N == 2:
        return r"$\pi$"
    elif N % 2 > 0:
        return r"${0}\pi/2$".format(N)
    else:
        return r"${0}\pi$".format(N // 2)