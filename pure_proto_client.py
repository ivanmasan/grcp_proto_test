import numpy as np
import time
import image_pb2
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((socket.gethostname(), 9996))
    print("Connected", time.time())

    image_height = 2064
    image_width = 1544

    point_cloud_data = np.random.rand(image_height, image_width, 3).astype(np.float32)

    print("Start", time.time())
    t = time.time()

    bytes_cloud = point_cloud_data.tobytes()

    print("Bitified Numpy", time.time() - t)
    t = time.time()

    image = image_pb2.PointCloud(
        data=bytes_cloud,
        rows=point_cloud_data.shape[0],
        columns=point_cloud_data.shape[1],
        depth=point_cloud_data.shape[2],
    )

    print("Serialized Numpy", time.time() - t)
    t = time.time()

    image_bytes = image.SerializeToString()

    print("Serialized Protobuf", time.time() - t)
    t = time.time()

    message_size = len(image_bytes)
    image_bytes = message_size.to_bytes(4, byteorder='big') + image_bytes

    print("Added Length", time.time() - t)
    t = time.time()

    s.sendall(image_bytes)
    print("Sent Message", time.time() - t)
    t = time.time()
    print(time.time())
