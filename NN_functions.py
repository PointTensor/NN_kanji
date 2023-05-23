import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image

#This function turns text into a picture

def txt_img(txt):
    fig = plt.figure()
    fig.set_figheight(1.6)
    fig.set_figwidth(1.6)
    plt.axis('off')
    plt.text(-0.05, 0.03, txt, dict(size=100))
    plt.ioff()



#This function takes each kanji from the dataframe, converts it into a grayscale image, and then the image into a numpy array and then appends it into a list called data

def img_data(df, int, fin, font):
    matplotlib.rcParams['font.family'] = [font]
    no = 0
    data=[]
    for i in df['kanji'][int:fin]:
        txt_img(i)
        name = '/Users/rashidalawadhi/Documents/GitHub/NN_kanji/kanji_images_CNN_extra'+'_'+font+'/kanji_' + str(no)+'.png'
        plt.savefig(name, dpi=25)
        no +=1
        data.append(np.array(Image.open(name).convert('L')))
        plt.ioff()
        plt.close()
    
    return data
