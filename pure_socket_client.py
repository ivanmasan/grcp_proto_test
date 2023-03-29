import numpy as np
import time
import image_pb2
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((socket.gethostname(), 9995))

    image_height = 2064
    image_width = 1544
    point_cloud_data = np.random.rand(image_height, image_width, 3).astype(np.float32)
    size = np.array([image_height, image_width], dtype=np.int32)

    print(time.time())

    s.sendall(size.data)
    s.sendall(point_cloud_data.data)

