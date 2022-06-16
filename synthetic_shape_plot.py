# Synthetic shape image plot and save
import numpy as np
import cv2

shapes = [
        'draw_lines',
        'draw_polygon',
        'draw_multiple_polygons',
        'draw_ellipses',
        'draw_star',
        'draw_checkerboard',
        'draw_stripes',
        'draw_cube',
        'gaussian_noise'
    ]

IMAGE_SAVE = False
IMAGE_PLOT = False


for shape in shapes:
    kpts = np.load('./data/synthetic_shapes/{}/points/training/302.npy'.format(shape))
    img = cv2.imread('./data/synthetic_shapes/{}/images/training/302.png'.format(shape))
    print('{} kpts shape : '.format(shape), kpts.shape)
    for kp in kpts:
        x , y = map(int,kp)
        cv2.circle(img, (y, x), 2, (0, 255, 0), 1, cv2.LINE_AA)
    if IMAGE_SAVE == True:
        cv2.imwrite('{}.png'.format(shape), img)
    
    if IMAGE_PLOT == True:
        cv2.imshow('{}'.format(shape),img)
        cv2.waitKey(0)