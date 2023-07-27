# import math
#
# DIGITSDICT = [
#     (1, 1, 1, 1, 1, 1, 0),
#     (0, 1, 1, 0, 0, 0, 0),
#     (1, 1, 0, 1, 1, 0, 1),
#     (1, 1, 1, 1, 0, 0, 1),
#     (0, 1, 1, 0, 0, 1, 1),
#     (1, 1, 1, 0, 0, 1, 1),
#     (1, 0, 1, 1, 0, 1, 1),
#     (1, 0, 1, 1, 1, 1, 1),
#     (1, 1, 1, 0, 0, 0, 0),
#     (1, 1, 1, 1, 1, 1, 1),
#     (1, 1, 1, 1, 0, 1, 1),
#     (0, 1, 1, 1, 1, 0, 1),
# ]
#
# def euclidean_distance(tuple1, tuple2):
#     return math.sqrt(sum((x - y) ** 2 for x, y in zip(tuple1, tuple2)))
#
#
# def find_closest_tuple(target_list, tuple_list):
#     closest_tuple = None
#     closest_distance = float('inf')
#
#     for tuple_item in tuple_list:
#         distance = euclidean_distance(target_list, tuple_item)
#         if distance < closest_distance:
#             closest_tuple = tuple_item
#             closest_distance = distance
#     return closest_tuple
# def replace_tuple_if_not_present(target_tuple, tuple_list):
#     try:
#         index = tuple_list.index(target_tuple)
#     except ValueError:
#         closest_tuple = find_closest_tuple(target_tuple, tuple_list)
#         index = tuple_list.index(closest_tuple)
#     tuple_list[index] = target_tuple
#
# on = [0] * 7
# replace_tuple_if_not_present(on, DIGITSDICT)
# print(on)

import matplotlib.pyplot as plt
import matplotlib.image

image_path = 'inter/bc7541ca0fd1dc8f85c04-roi.png'
img = plt.imread(image_path)

image_path1 = 'inter/3d41c82d9702445c1d133-roi.png'
img1 = plt.imread(image_path1)

image_path2 = 'inter/64d763b23c9defc3b68c2-roi.png'
img2 = plt.imread(image_path2)

image_path3 = 'inter/e61bbf5dfe462d1874572-roi.png'
img3 = plt.imread(image_path3)

fig, axs = plt.subplots(2, 2)
axs[0, 0].imshow(img)
axs[0, 1].imshow(img1)
axs[1, 1].imshow(img2)
axs[1, 0].imshow(img2)
plt.show()
