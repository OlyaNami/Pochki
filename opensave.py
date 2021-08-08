import cv2
import pydicom

from dcm_classes import Extract

print(__name__) 


def opensave(dcmpath, savepath):
    dataset = pydicom.dcmread(dcmpath)

    pixels = Extract.pixels(dataset)
    cv2.imwrite(savepath, pixels)


if __name__ == '__main__':
    opensave('mammary_gland.dcm', 'result.jpg')

