import cv2
import random
import numpy as np
from matplotlib import pyplot as plt


class AugmentationClass:
    # read image and save in class
    def __init__(self, path):
        self.img = cv2.imread(path)

    #image crop
    def crop(self, h_start, h_end, w_start, w_end):
        img_crop = self.img[h_start:h_end, w_start:w_end]
        return img_crop

    #color shift
    def random_light_color(self):
        # brightness
        B, G, R = cv2.split(self.img)

        b_rand = random.randint(-50, 50)
        if b_rand == 0:
            pass
        elif b_rand > 0:
            lim = 255 - b_rand
            B[B > lim] = 255
            B[B <= lim] = (b_rand + B[B <= lim]).astype(self.img.dtype)
        elif b_rand < 0:
            lim = 0 - b_rand
            B[B < lim] = 0
            B[B >= lim] = (b_rand + B[B >= lim]).astype(self.img.dtype)

        g_rand = random.randint(-50, 50)
        if g_rand == 0:
            pass
        elif g_rand > 0:
            lim = 255 - g_rand
            G[G > lim] = 255
            G[G <= lim] = (g_rand + G[G <= lim]).astype(self.img.dtype)
        elif g_rand < 0:
            lim = 0 - g_rand
            G[G < lim] = 0
            G[G >= lim] = (g_rand + G[G >= lim]).astype(self.img.dtype)

        r_rand = random.randint(-50, 50)
        if r_rand == 0:
            pass
        elif r_rand > 0:
            lim = 255 - r_rand
            R[R > lim] = 255
            R[R <= lim] = (r_rand + R[R <= lim]).astype(self.img.dtype)
        elif r_rand < 0:
            lim = 0 - r_rand
            R[R < lim] = 0
            R[R >= lim] = (r_rand + R[R >= lim]).astype(self.img.dtype)

        img_merge = cv2.merge((B, G, R))
        # img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        return img_merge

    #rotation
    def rotation(self, x, y, angle, scale):
        img = self.img
        M = cv2.getRotationMatrix2D((self.img.shape[1] / x, self.img.shape[0] / y), angle, scale)  # center, angle, scale
        img_rotate = cv2.warpAffine(img, M, (self.img.shape[1], self.img.shape[0]))
        return img_rotate

    def perspective_transform(self):
        img = self.img
        (height, width, channels) = img.shape

    # perspective transform
    def random_warp(self):
        height, width, channels = self.img.shape

        # warp:
        random_margin = 60
        x1 = random.randint(-random_margin, random_margin)
        y1 = random.randint(-random_margin, random_margin)
        x2 = random.randint(width - random_margin - 1, width - 1)
        y2 = random.randint(-random_margin, random_margin)
        x3 = random.randint(width - random_margin - 1, width - 1)
        y3 = random.randint(height - random_margin - 1, height - 1)
        x4 = random.randint(-random_margin, random_margin)
        y4 = random.randint(height - random_margin - 1, height - 1)

        dx1 = random.randint(-random_margin, random_margin)
        dy1 = random.randint(-random_margin, random_margin)
        dx2 = random.randint(width - random_margin - 1, width - 1)
        dy2 = random.randint(-random_margin, random_margin)
        dx3 = random.randint(width - random_margin - 1, width - 1)
        dy3 = random.randint(height - random_margin - 1, height - 1)
        dx4 = random.randint(-random_margin, random_margin)
        dy4 = random.randint(height - random_margin - 1, height - 1)

        pts1 = np.float32([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
        pts2 = np.float32([[dx1, dy1], [dx2, dy2], [dx3, dy3], [dx4, dy4]])
        M_warp = cv2.getPerspectiveTransform(pts1, pts2)
        img_warp = cv2.warpPerspective(self.img, M_warp, (width, height))
        return img_warp

if __name__ == "__main__":
    test = AugmentationClass("/home/lihuiting/Homework01/640.jpg")
    # img_change=test.crop(100,200,100,300)
    # img_change=test.random_light_color()
    # img_change=test.rotation( 2,  2, 60, 0.5)
    # img_change=test.random_warp()
    cv2.imshow('img_change', img_change)
    #key = cv2.waitKey()
    #if key == 27:
        #cv2.destroyAllWindows()