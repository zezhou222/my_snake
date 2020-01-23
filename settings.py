import os

width = 500
height = 500

speed_frame_num = 12
frame_num = 6

lattice_size = 20

project_path = os.getcwd()
static_path = os.path.join(project_path, 'static')
black_image = os.path.join(static_path, 'black.jpg')
red_image = os.path.join(static_path, 'red.jpg')
gray_image = os.path.join(static_path, 'gray.jpg')
