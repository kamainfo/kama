import cv2
image = cv2.imread("test1.png")

grayimage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow('original',image)
cv2.imshow('Gray',grayimage)
cv2.imwrite('Graynew1.jpg',grayimage)


print(image.shape)

print(image.size)
