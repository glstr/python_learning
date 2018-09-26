# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import rdguard_pb2 as rdguard__pb2


class GuarderStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SayHello = channel.unary_unary(
        '/rdproto.Guarder/SayHello',
        request_serializer=rdguard__pb2.HelloRequest.SerializeToString,
        response_deserializer=rdguard__pb2.HelloReply.FromString,
        )
    self.Fury = channel.unary_unary(
        '/rdproto.Guarder/Fury',
        request_serializer=rdguard__pb2.FuryRequest.SerializeToString,
        response_deserializer=rdguard__pb2.FuryReply.FromString,
        )


class GuarderServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SayHello(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Fury(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GuarderServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SayHello': grpc.unary_unary_rpc_method_handler(
          servicer.SayHello,
          request_deserializer=rdguard__pb2.HelloRequest.FromString,
          response_serializer=rdguard__pb2.HelloReply.SerializeToString,
      ),
      'Fury': grpc.unary_unary_rpc_method_handler(
          servicer.Fury,
          request_deserializer=rdguard__pb2.FuryRequest.FromString,
          response_serializer=rdguard__pb2.FuryReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'rdproto.Guarder', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
