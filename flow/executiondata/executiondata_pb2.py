# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flow/executiondata/executiondata.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flow.entities import block_execution_data_pb2 as flow_dot_entities_dot_block__execution__data__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&flow/executiondata/executiondata.proto\x12\x0b\x66low.access\x1a(flow/entities/block_execution_data.proto\"4\n GetExecutionDataByBlockIDRequest\x12\x10\n\x08\x62lock_id\x18\x01 \x01(\x0c\"d\n!GetExecutionDataByBlockIDResponse\x12?\n\x14\x62lock_execution_data\x18\x01 \x01(\x0b\x32!.flow.entities.BlockExecutionData2\x8e\x01\n\x10\x45xecutionDataAPI\x12z\n\x19GetExecutionDataByBlockID\x12-.flow.access.GetExecutionDataByBlockIDRequest\x1a..flow.access.GetExecutionDataByBlockIDResponseBL\n\x1aorg.onflow.protobuf.accessZ.github.com/onflow/flow/protobuf/go/flow/accessb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flow.executiondata.executiondata_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032org.onflow.protobuf.accessZ.github.com/onflow/flow/protobuf/go/flow/access'
  _GETEXECUTIONDATABYBLOCKIDREQUEST._serialized_start=97
  _GETEXECUTIONDATABYBLOCKIDREQUEST._serialized_end=149
  _GETEXECUTIONDATABYBLOCKIDRESPONSE._serialized_start=151
  _GETEXECUTIONDATABYBLOCKIDRESPONSE._serialized_end=251
  _EXECUTIONDATAAPI._serialized_start=254
  _EXECUTIONDATAAPI._serialized_end=396
# @@protoc_insertion_point(module_scope)