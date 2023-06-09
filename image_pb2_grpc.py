# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import image_pb2 as image__pb2


class ImageProcessorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendImage = channel.unary_unary(
                '/ImageProcessor/SendImage',
                request_serializer=image__pb2.Image.SerializeToString,
                response_deserializer=image__pb2.Processed.FromString,
                )
        self.SendPointCloud = channel.unary_unary(
                '/ImageProcessor/SendPointCloud',
                request_serializer=image__pb2.PointCloud.SerializeToString,
                response_deserializer=image__pb2.Processed.FromString,
                )
        self.SendPointCloudStream = channel.stream_unary(
                '/ImageProcessor/SendPointCloudStream',
                request_serializer=image__pb2.PointCloud.SerializeToString,
                response_deserializer=image__pb2.Processed.FromString,
                )


class ImageProcessorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendImage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendPointCloud(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendPointCloudStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ImageProcessorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendImage': grpc.unary_unary_rpc_method_handler(
                    servicer.SendImage,
                    request_deserializer=image__pb2.Image.FromString,
                    response_serializer=image__pb2.Processed.SerializeToString,
            ),
            'SendPointCloud': grpc.unary_unary_rpc_method_handler(
                    servicer.SendPointCloud,
                    request_deserializer=image__pb2.PointCloud.FromString,
                    response_serializer=image__pb2.Processed.SerializeToString,
            ),
            'SendPointCloudStream': grpc.stream_unary_rpc_method_handler(
                    servicer.SendPointCloudStream,
                    request_deserializer=image__pb2.PointCloud.FromString,
                    response_serializer=image__pb2.Processed.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ImageProcessor', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ImageProcessor(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ImageProcessor/SendImage',
            image__pb2.Image.SerializeToString,
            image__pb2.Processed.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendPointCloud(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ImageProcessor/SendPointCloud',
            image__pb2.PointCloud.SerializeToString,
            image__pb2.Processed.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendPointCloudStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/ImageProcessor/SendPointCloudStream',
            image__pb2.PointCloud.SerializeToString,
            image__pb2.Processed.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
