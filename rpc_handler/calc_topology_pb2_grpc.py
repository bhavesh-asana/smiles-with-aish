# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import calc_topology_pb2 as calc__topology__pb2


class TopologyServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateTopology = channel.unary_unary(
                '/topology.TopologyService/CreateTopology',
                request_serializer=calc__topology__pb2.CreateTopologyRequest.SerializeToString,
                response_deserializer=calc__topology__pb2.CreateTopologyResponse.FromString,
                )
        self.ReadTopology = channel.unary_unary(
                '/topology.TopologyService/ReadTopology',
                request_serializer=calc__topology__pb2.ReadTopologyRequest.SerializeToString,
                response_deserializer=calc__topology__pb2.ReadTopologyResponse.FromString,
                )
        self.UpdateTopology = channel.unary_unary(
                '/topology.TopologyService/UpdateTopology',
                request_serializer=calc__topology__pb2.UpdateTopologyRequest.SerializeToString,
                response_deserializer=calc__topology__pb2.UpdateTopologyResponse.FromString,
                )
        self.DeleteTopology = channel.unary_unary(
                '/topology.TopologyService/DeleteTopology',
                request_serializer=calc__topology__pb2.DeleteTopologyRequest.SerializeToString,
                response_deserializer=calc__topology__pb2.DeleteTopologyResponse.FromString,
                )
        self.ListTopology = channel.unary_unary(
                '/topology.TopologyService/ListTopology',
                request_serializer=calc__topology__pb2.ListTopologyRequest.SerializeToString,
                response_deserializer=calc__topology__pb2.ListTopologyResponse.FromString,
                )


class TopologyServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateTopology(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadTopology(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTopology(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTopology(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTopology(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TopologyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateTopology': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTopology,
                    request_deserializer=calc__topology__pb2.CreateTopologyRequest.FromString,
                    response_serializer=calc__topology__pb2.CreateTopologyResponse.SerializeToString,
            ),
            'ReadTopology': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadTopology,
                    request_deserializer=calc__topology__pb2.ReadTopologyRequest.FromString,
                    response_serializer=calc__topology__pb2.ReadTopologyResponse.SerializeToString,
            ),
            'UpdateTopology': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTopology,
                    request_deserializer=calc__topology__pb2.UpdateTopologyRequest.FromString,
                    response_serializer=calc__topology__pb2.UpdateTopologyResponse.SerializeToString,
            ),
            'DeleteTopology': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTopology,
                    request_deserializer=calc__topology__pb2.DeleteTopologyRequest.FromString,
                    response_serializer=calc__topology__pb2.DeleteTopologyResponse.SerializeToString,
            ),
            'ListTopology': grpc.unary_unary_rpc_method_handler(
                    servicer.ListTopology,
                    request_deserializer=calc__topology__pb2.ListTopologyRequest.FromString,
                    response_serializer=calc__topology__pb2.ListTopologyResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'topology.TopologyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TopologyService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateTopology(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/topology.TopologyService/CreateTopology',
            calc__topology__pb2.CreateTopologyRequest.SerializeToString,
            calc__topology__pb2.CreateTopologyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadTopology(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/topology.TopologyService/ReadTopology',
            calc__topology__pb2.ReadTopologyRequest.SerializeToString,
            calc__topology__pb2.ReadTopologyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateTopology(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/topology.TopologyService/UpdateTopology',
            calc__topology__pb2.UpdateTopologyRequest.SerializeToString,
            calc__topology__pb2.UpdateTopologyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteTopology(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/topology.TopologyService/DeleteTopology',
            calc__topology__pb2.DeleteTopologyRequest.SerializeToString,
            calc__topology__pb2.DeleteTopologyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListTopology(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/topology.TopologyService/ListTopology',
            calc__topology__pb2.ListTopologyRequest.SerializeToString,
            calc__topology__pb2.ListTopologyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)