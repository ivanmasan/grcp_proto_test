from __future__ import print_function

import logging

import time
import numpy as np
import grpc
import image_pb2
import image_pb2_grpc


MAX_MESSAGE_LENGTH = 40 * 1024 ** 2


def run():
    options = [
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH),
    ]

    with grpc.insecure_channel('localhost:50051', options=options) as channel:
        stub = image_pb2_grpc.ImageProcessorStub(channel)

        image_height = 2064
        image_width = 1544

        image_data = np.random.randint(0, 255, (image_height, image_width, 1)).astype(np.uint8)

        start_time = time.time()

        image = image_pb2.Image(
            data=image_data.tobytes(),
            rows=image_data.shape[0],
            columns=image_data.shape[1]
        )

        response = stub.SendImage(image)
        print("Image Process Time", response.success, time.time() - start_time)

        point_cloud_data = np.random.rand(image_height, image_width, 3).astype(np.float32)

        start_time = time.time()

        image = image_pb2.PointCloud(
            data=point_cloud_data.tobytes(),
            rows=point_cloud_data.shape[0],
            columns=point_cloud_data.shape[1],
            depth=point_cloud_data.shape[2],
        )

        response = stub.SendPointCloud(image)
        print("Point Cloud Process Time", response.success, time.time() - start_time)

        point_cloud_data = np.random.rand(image_height, image_width, 3).astype(np.float32)

        start_time = time.time()

        def yield_image(point_cloud_data):
            image_bytes = point_cloud_data.tobytes()

            while len(image_bytes) > 0:
                yield image_pb2.PointCloud(
                    data=image_bytes[:8*1024**2],
                    rows=point_cloud_data.shape[0],
                    columns=point_cloud_data.shape[1],
                    depth=point_cloud_data.shape[2],
                )
                image_bytes = image_bytes[8*1024**2:]

        response = stub.SendPointCloudStream(yield_image(point_cloud_data))
        print("Point Cloud Process Time", response.success, time.time() - start_time)




if __name__ == '__main__':
    logging.basicConfig()
    run()
