import cv2

# img path
img = cv2.imread('lena.png')

# convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# equalize the histogram of the grayscale image
equ = cv2.equalizeHist(gray)

# Calculate mean and standard deviation of the equalized image
mean, std = cv2.meanStdDev(equ)

# Show the mean and standard deviation
print('Mean: {:.2f}, Standard Deviation: {:.2f}'.format(mean[0][0], std[0][0]))
