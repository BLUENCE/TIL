import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
from skimage import io, transform
from torchvision import transforms
import torch



###### getdata.py 코드 뜯어보기 #######

def getCropped(img, e):

    alpha = 0.3
    w_x = int(math.floor(alpha * img.shape[1]))
    w_y = int(math.floor(alpha * img.shape[0]))

    if w_x % 2 == 0:
        w_x = w_x + 1

    if w_y % 2 == 0:
        w_y = w_y + 1

    im_face = np.ones((w_y, w_x, 3))
    im_face[:, :, 0] = 123 * np.ones((w_y, w_x))
    im_face[:, :, 1] = 117 * np.ones((w_y, w_x))
    im_face[:, :, 2] = 104 * np.ones((w_y, w_x))

    center = [math.floor(e[0] * img.shape[1]), math.floor(e[1] * img.shape[0])]
    d_x = math.floor((w_x - 1) / 2)
    d_y = math.floor((w_y - 1) / 2)

    bottom_x = center[0] - d_x - 1
    delta_b_x = 0
    if bottom_x < 0:
        delta_b_x = 1 - bottom_x
        bottom_x = 0

    top_x = center[0] + d_x - 1
    delta_t_x = w_x - 1
    if top_x > img.shape[1] - 1:
        delta_t_x = w_x - (top_x - img.shape[1] + 1)
        top_x = img.shape[1] - 1

    bottom_y = center[1] - d_y - 1
    delta_b_y = 0
    if bottom_y < 0:
        delta_b_y = 1 - bottom_y
        bottom_y = 0

    top_y = center[1] + d_y - 1
    delta_t_y = w_y - 1
    if top_y > img.shape[0] - 1:
        delta_t_y = w_y - (top_y - img.shape[0] + 1)
        top_y = img.shape[0] - 1


    x = img[int(bottom_y): int(top_y + 1), int(bottom_x): int(top_x + 1), :]
    x = np.ascontiguousarray(x)

    try:
        x = transform.resize(x,(227, 227))
        return x
    except:
        # print('begins') #TODO, are there corrupt images?
        # print(x)
        # print(x.shape)
        # print('ends')
        print('corruption')
        return img


# img = cv2.imread('./00039036.jpg')
img = cv2.imread('./00080697.jpg')  # 하키, 첫번째 이미지

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()

s = img.shape
print('img.shape', s)

# bbox_corr = np.array([0.24, 0.04, 0.68, 0.93])
bbox_corr = np.array([0.29, 0.11, 0.68, 0.89])
bbox_corr[bbox_corr < 0] = 0.0
bbox = np.copy(img[int(bbox_corr[1] * s[0]): int(np.ceil(bbox_corr[1] * s[0] + bbox_corr[3] * s[0])),
               int(bbox_corr[0] * s[1]): int(np.ceil(bbox_corr[0] * s[1] + bbox_corr[2] * s[1]))])


bbox = np.ascontiguousarray(bbox)
bbox = transform.resize(bbox, (227, 227))
# plt.imshow(bbox)
# plt.show()

img = np.ascontiguousarray(img)
img = transform.resize(img, (227, 227))
# plt.imshow(img)
# plt.show()

# eyes = np.array([0.39648438, 0.14453125])
eyes = np.array([0.41272727, 0.21429687])
eyes_bbox = (eyes - bbox_corr[:2])/bbox_corr[2:]
# print('eyes_bbox', eyes_bbox)

cropped_bbox = getCropped(bbox, eyes_bbox)
cropped_bbox = np.ascontiguousarray(cropped_bbox)
# plt.imshow(cropped_bbox)
# plt.show()


gaze = np.array([0.51090909, 0.31132813])
eyes_loc_size = 13
gaze_label_size = 5  # "하나"의 shit grid 의 행과 열의 사이즈, 5를하면 5x5 그리드가 만들어짐

eyes_loc = np.zeros((eyes_loc_size, eyes_loc_size))
# print('eyes_loc 1', eyes_loc)

# subject 의 눈중심 좌표부분을  13x13 그리드에 1로 표시해줌
eyes_loc[int(np.floor(eyes_loc_size * eyes[1]))][int(np.floor(eyes_loc_size * eyes[0]))] = 1
# print('eyes_loc 2', eyes_loc)


grid_size = 5  # 총 shit시킬 그리드의 개수

v_x = [0, 1, -1, 0, 0]
v_y = [0, 0, 0, -1, 1]

x_pix = gaze[0]
y_pix = gaze[1]

# 5x5 그리드를 gird_size 개수(5) 만큼 만듬
shifted_grids = np.zeros((grid_size, gaze_label_size, gaze_label_size))
# [[[0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0.]]
#
#  [[0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0.]] 이거를 5개 만듬

for i in range(5):

	x_grid = int(np.floor(gaze_label_size * gaze[0] + (v_x[i] * (1 / (grid_size * 3.0)))))
	y_grid = int(np.floor(gaze_label_size * gaze[1] + (v_y[i] * (1 / (grid_size * 3.0)))))

	if x_grid < 0:
		x_grid = 0
	elif x_grid > 4:
		x_grid = 4
	if y_grid < 0:
		y_grid = 0
	elif y_grid > 4:
		y_grid = 4

	try:  # target의 위치값을 grid 5개에 넣어줌
		shifted_grids[i][y_grid][x_grid] = 1
	except:
		print("**************")
		print("eyes: ", eyes)
		print("eyes_bbox: ", eyes_bbox)
		print("gaze: ", gaze)
		print("grid vals: ", x_grid, y_grid)
		plt.imshow(img)
		plt.savefig('./a.jpg')
		exit()

# print('shifted_grids', shifted_grids)
# [[[0. 0. 0. 0. 0.]
#   [0. 0. 1. 0. 0.]
#   [0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0.]]
#
#  [[0. 0. 0. 0. 0.]
#   [0. 0. 1. 0. 0.]
#   [0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0.]]
#
#  [[0. 0. 0. 0. 0.]
#   [0. 0. 1. 0. 0.]
#   [0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0.]]
#
#  [[0. 0. 0. 0. 0.]
#   [0. 0. 1. 0. 0.]
#   [0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0.]]
#
#  [[0. 0. 0. 0. 0.]
#   [0. 0. 1. 0. 0.]
#   [0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0.]]]

eyes_loc = torch.from_numpy(eyes_loc).contiguous()  # 13x13
shifted_grids = torch.from_numpy(shifted_grids).contiguous()  # 5x5 짜리 5개

# numpy 에서 view는 참조복사다. 즉 원본이 바뀌면 복사본도 함께 바뀐다.
# 5x5 짜리 그리드 matrix 5개 => 5 x 25 짜리 matrix 1개로 바꿔준다.
shifted_grids = shifted_grids.view(1, 5, 25)

gaze_final = np.ones(100)
gaze_final *= -1
print('gaze_final.shape', gaze.shape)  # (2,)

gaze_final[:gaze.shape[0]] = gaze  # 100개의 -1 array에서 앞에 2칸만 gaze 값으로 준다.
print('gaze_final ', gaze_final)

# img = 전체 이미지 227x227

# img shape (227, 227, 3)
# transposed_img shape (3, 227, 227)
# bbox shape (227, 227, 3)
# transposed_bbox shape (3, 227, 227)

img = img.transpose((2, 0, 1))
# array -> tensor 형태로 변형
img = torch.from_numpy(img.copy()).contiguous()

bbox = bbox.transpose((2, 0, 1))
# array -> tensor 형태로 변형
bbox = torch.from_numpy(bbox.copy()).contiguous()

normtransform = transforms.Compose([
	transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

img = normtransform(img.float())
bbox = normtransform(bbox.float())

sample = (img.float(), bbox.float(), eyes_loc.float(), shifted_grids.float(), eyes, eyes_bbox, gaze_final)


print('img.shape', img.shape)  # 전체이미지 torch.Size([3, 227, 227])
print('bbox.shape', bbox.shape)  # 얼굴이미지 torch.Size([3, 227, 227])
print('eyes_loc.shape', eyes_loc.shape)  # 눈중심 좌표부분을  13x13 그리드에 1로 표시해줌 torch.Size([13, 13])
print('shifted_grids.shape', shifted_grids.shape)  # torch.Size([1, 5, 25])
print('eyes.shape', eyes.shape)  # (2,)
print('eyes_bbox.shape', eyes_bbox.shape)  # 집중할 바운딩박스 자른후 227x227했을때 보정된 eyes값 (2,)
print('gaze_final.shape', gaze_final.shape)  #  앞에 2개 gaze값 나머지 -1, (100,)

print('@sample', sample)



###### train.py 코드 #######

shifted_targets = shifted_grids
print('shifted_target', shifted_targets.shape ) # torch.Size([1, 5, 25])
print('squeeze_shifted_target', shifted_targets.cuda().squeeze().shape)  #  torch.Size([5, 25])

print('@shifted_targets[:, 0, :]', shifted_targets[:, 0, :])  # shifted_target중에 첫번째 그리드가 0이고 하나씩 늘려감
print(shifted_targets[:, 0, :].max(1)[1]) # 0번째 output 적용

for j in range(1, 5):  # 1,2,3,4번째 output 적용
	print(shifted_targets[:, j, :].max(1)[1])



###### gazenet.py 코드 #######

# 104번째 줄까지 봄