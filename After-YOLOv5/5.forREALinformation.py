import cv2
import os
import numpy as np

def sys_moments(img):
    moments = cv2.moments(img)
    humoments = cv2.HuMoments(moments)
    humoment = -(np.log(np.abs(humoments))) / np.log(10)
    return humoment

def main():
    f1 = open("Core_data/Crops/G100/G100_0099.txt", 'w+', encoding='utf-8')
    f2 = open("rectangle_data/G100/rectangle_G100_0099.txt", 'w+', encoding='utf-8')
    input_dir = "Core_data/Crops/G100/G100_0099/core/"
    aa = os.listdir(input_dir)
    aa.sort(key=lambda x:int(x.split('.')[0].split('_')[-2]))
    abc = 0
    kernel = np.ones((3, 3), np.uint8)

    zs = len(aa) * 7
    cxx = []
    cyy = []
    czz = []
    x11 = []
    y11 = []
    x22 = []
    y22 = []
    for ia in aa:
        grayy = cv2.imread(input_dir + ia)
        erosion_img = cv2.erode(grayy, kernel)
        erosion_dilate_img = cv2.dilate(erosion_img, kernel)
        erosion_dilate_img_gray = cv2.cvtColor(erosion_dilate_img, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(erosion_dilate_img_gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)

        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        x1 = []
        y1 = []
        x2 = []
        y2 = []
        for c in contours:
            x, y, w, h = cv2.boundingRect(c)
            x1.append(x)
            y1.append(y)
            x2.append(x + w)
            y2.append(y + h)

        M = cv2.moments(thresh)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cZ = ia
        cxx.append(cX)
        cyy.append(cY)
        czz.append(cZ)
        x11.append(min(x1))
        y11.append(min(y1))
        x22.append(max(x2))
        y22.append(max(y2))
        cv2.circle(grayy, (cX, cY), 5, (255, 255, 255), -1)
        cv2.putText(grayy, "centroid", (cX - 25, cY - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    for cs0 in range(zs):
        if cs0 % 7 == 0:
            abc = abc + 1
            f1.write("%s %s %s\n" % (str(czz[abc - 1]), str(cxx[abc - 1]), str(cyy[abc - 1])))
            f2.write("%s %s %s %s %s\n" % (str(czz[abc - 1]), str(x11[abc - 1]), str(y11[abc - 1]), str(x22[abc - 1]), str(y22[abc - 1])))
    f1.close()
    f2.close()


if __name__ == '__main__':
    main()
    print("well done")
