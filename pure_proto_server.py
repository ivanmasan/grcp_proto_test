import socket
import time
import numpy as np

import image_pb2


def receive_all(sock, n):
    """Helper function to receive n bytes from a socket"""
    data = b''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('', 9996))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            size_bytes = receive_all(conn, 4)

            if size_bytes is None:
                time.sleep(0.1)
                continue

            print("Receiving Message", time.time())
            t = time.time()

            size = int.from_bytes(size_bytes, byteorder='big')
            message = receive_all(conn, size)

            print("Received Message", time.time() - t)
            t = time.time()

            received_image = image_pb2.PointCloud()
            received_image.ParseFromString(message)

            print("Parsed Protobuf Message", time.time() - t)
            t = time.time()

            received_image = np.frombuffer(received_image.data, dtype=np.float32).reshape(
                (received_image.rows, received_image.columns, received_image.depth))

            print("Parsed Numpy Buffer", time.time() - t)
            print(time.time())
