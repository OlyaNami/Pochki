import cv2
import numpy as np

print(__name__)

class Extract:

    @staticmethod
    def overlay(dataset):
        overlay = dataset.overlay_array(0x6000)
        overlay = overlay * 255
        return overlay

    @staticmethod
    def pixels(dataset):
        voxels = dataset.pixel_array
        # print(f'[DEFAULT] Min val: {np.min(voxels)}, Max val: {np.max(voxels)}')
        voxels = Extract.rescale(dataset, voxels)
        # print(f'[EXTRACTED] Min val: {np.min(voxels)}, Max val: {np.max(voxels)}')
        pixels = voxels / np.max(voxels)
        pixels = 255 * pixels
        return pixels

    @staticmethod
    def voxels2pixels(dataset, voxels):
        # print(f'[DEFAULT] Min val: {np.min(voxels)}, Max val: {np.max(voxels)}')
        voxels = Extract.rescale(dataset, voxels)
        # print(f'[EXTRACTED] Min val: {np.min(voxels)}, Max val: {np.max(voxels)}')
        pixels = voxels / np.max(voxels)
        pixels = 255 * pixels
        return pixels

    @staticmethod
    def voxels(dataset):
        voxels = dataset.pixel_array
        return voxels

    @staticmethod
    def boxes(overlay):
        cnts = cv2.findContours(overlay, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
        boxes = [cv2.boundingRect(cnt) for cnt in cnts]
        return boxes

    @staticmethod
    def rescale(dataset, voxels):
        try:
            intercept = dataset.RescaleIntercept
            slope = dataset.RescaleSlope
        except AttributeError:
            intercept, slope = 0, 1

        if slope != 1:
            voxels = slope * voxels.astype(np.float64)
            voxels = voxels.astype(np.int16)
        voxels += np.int16(intercept)

        try:
            center, width = dataset.WindowCenter[0], dataset.WindowWidth[0]
        except TypeError:
            center, width = dataset.WindowCenter, dataset.WindowWidth
        except AttributeError:
            return voxels

        # print(f'Window information: center - {center}, width - {width}')
        top_voxel, bot_voxel = center + int(width / 2), center - int(width / 2)
        voxels = voxels - bot_voxel
        voxels = np.where(voxels < 0, 0, voxels)
        voxels = np.where(voxels > top_voxel - bot_voxel, top_voxel - bot_voxel, voxels)

        return voxels
