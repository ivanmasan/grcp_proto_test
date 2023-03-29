from concurrent import futures
import logging
import numpy as np
import grpc
import image_pb2
import image_pb2_grpc


class ImageProcessor(image_pb2_grpc.ImageProcessorServicer):

    def SendImage(self, request, context):
        received_image = np.frombuffer(request.data, dtype=np.int8).reshape(
            (request.rows, request.columns, 1))
        return image_pb2.Processed(success=True)

    def SendPointCloud(self, request, context):
        received_image = np.frombuffer(request.data, dtype=np.float32).reshape(
            (request.rows, request.columns, request.depth))
        return image_pb2.Processed(success=True)

    def SendPointCloudStream(self, request_iterator, context):
        image_bytes = b''
        for request in request_iterator:
            image_bytes += request.data

        received_image = np.frombuffer(image_bytes, dtype=np.float32).reshape(
            (request.rows, request.columns, request.depth))

        return image_pb2.Processed(success=True)


MAX_MESSAGE_LENGTH = 40 * 1024 ** 2


def serve():
    port = '50051'
    options = [
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH),
    ]

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1), options=options)
    image_pb2_grpc.add_ImageProcessorServicer_to_server(ImageProcessor(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
