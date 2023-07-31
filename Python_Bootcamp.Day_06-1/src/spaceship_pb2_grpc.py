# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import spaceship_pb2 as spaceship__pb2


class ReportStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetReport = channel.unary_stream(
                '/Report/GetReport',
                request_serializer=spaceship__pb2.Coordinates.SerializeToString,
                response_deserializer=spaceship__pb2.Spaceship.FromString,
                )


class ReportServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetReport(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ReportServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetReport': grpc.unary_stream_rpc_method_handler(
                    servicer.GetReport,
                    request_deserializer=spaceship__pb2.Coordinates.FromString,
                    response_serializer=spaceship__pb2.Spaceship.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Report', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Report(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetReport(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Report/GetReport',
            spaceship__pb2.Coordinates.SerializeToString,
            spaceship__pb2.Spaceship.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)