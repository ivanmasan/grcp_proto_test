import socket
import time
import numpy as np


def recvall_into(read_socket, buffer):
    if buffer.nbytes > 0:
        bytes_view = buffer.cast("b")
        while bytes_view:
            bytes_received = read_socket.recv_into(bytes_view)
            if bytes_received == 0:
                raise RuntimeError("Connection closed unexpectedly")
            bytes_view = bytes_view[bytes_received:]


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('', 9995))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        while True:
            print("START")
            size = np.empty((2, ), dtype=np.int32)
            recvall_into(conn, size.data)
            image_height, image_width = size

            point_cloud_data = np.empty((image_height, image_width, 3), dtype=np.float32)

            recvall_into(conn, point_cloud_data.data)

            print(time.time())
            print(point_cloud_data)
