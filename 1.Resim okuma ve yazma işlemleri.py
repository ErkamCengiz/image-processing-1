import cv2

resim = cv2.imread('indir.jpg',0) ##0 resmi siyah çıkartır##

cv2.imshow('cicek', resim)
cv2.imwrite('siyah.png',resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
