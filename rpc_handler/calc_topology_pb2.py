# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calc_topology.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x63\x61lc_topology.proto\x12\x08topology\"\xd0\x01\n\x0c\x43\x61lcTopology\x12\x0f\n\x07symbols\x18\x01 \x03(\t\x12\x10\n\x08geometry\x18\x02 \x03(\t\x12\x12\n\nmol_charge\x18\x03 \x01(\x01\x12\x18\n\x10mol_multiplicity\x18\x04 \x01(\x03\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x0f\n\x07\x63omment\x18\x06 \x01(\t\x12\x14\n\x0cmass_numbers\x18\x07 \x03(\x03\x12\x0e\n\x06masses\x18\x08 \x03(\x01\x12\x15\n\ratomic_number\x18\t \x03(\x01\x12\x13\n\x0b\x61tom_labels\x18\n \x03(\t\"A\n\x15\x43reateTopologyRequest\x12(\n\x08topology\x18\x01 \x01(\x0b\x32\x16.topology.CalcTopology\"B\n\x16\x43reateTopologyResponse\x12(\n\x08topology\x18\x01 \x01(\x0b\x32\x16.topology.CalcTopology\"?\n\x13ReadTopologyRequest\x12(\n\x08topology\x18\x01 \x01(\x0b\x32\x16.topology.CalcTopology\"@\n\x14ReadTopologyResponse\x12(\n\x08topology\x18\x01 \x01(\x0b\x32\x16.topology.CalcTopology\"A\n\x15UpdateTopologyRequest\x12(\n\x08topology\x18\x01 \x01(\x0b\x32\x16.topology.CalcTopology\"B\n\x16UpdateTopologyResponse\x12(\n\x08topology\x18\x01 \x01(\x0b\x32\x16.topology.CalcTopology\"A\n\x15\x44\x65leteTopologyRequest\x12(\n\x08topology\x18\x01 \x01(\x0b\x32\x16.topology.CalcTopology\"B\n\x16\x44\x65leteTopologyResponse\x12(\n\x08topology\x18\x01 \x01(\x0b\x32\x16.topology.CalcTopology\"\x15\n\x13ListTopologyRequest\"@\n\x14ListTopologyResponse\x12(\n\x08topology\x18\x01 \x01(\x0b\x32\x16.topology.CalcTopology2\xb8\x03\n\x0fTopologyService\x12U\n\x0e\x43reateTopology\x12\x1f.topology.CreateTopologyRequest\x1a .topology.CreateTopologyResponse\"\x00\x12O\n\x0cReadTopology\x12\x1d.topology.ReadTopologyRequest\x1a\x1e.topology.ReadTopologyResponse\"\x00\x12U\n\x0eUpdateTopology\x12\x1f.topology.UpdateTopologyRequest\x1a .topology.UpdateTopologyResponse\"\x00\x12U\n\x0e\x44\x65leteTopology\x12\x1f.topology.DeleteTopologyRequest\x1a .topology.DeleteTopologyResponse\"\x00\x12O\n\x0cListTopology\x12\x1d.topology.ListTopologyRequest\x1a\x1e.topology.ListTopologyResponse\"\x00\x62\x06proto3')



_CALCTOPOLOGY = DESCRIPTOR.message_types_by_name['CalcTopology']
_CREATETOPOLOGYREQUEST = DESCRIPTOR.message_types_by_name['CreateTopologyRequest']
_CREATETOPOLOGYRESPONSE = DESCRIPTOR.message_types_by_name['CreateTopologyResponse']
_READTOPOLOGYREQUEST = DESCRIPTOR.message_types_by_name['ReadTopologyRequest']
_READTOPOLOGYRESPONSE = DESCRIPTOR.message_types_by_name['ReadTopologyResponse']
_UPDATETOPOLOGYREQUEST = DESCRIPTOR.message_types_by_name['UpdateTopologyRequest']
_UPDATETOPOLOGYRESPONSE = DESCRIPTOR.message_types_by_name['UpdateTopologyResponse']
_DELETETOPOLOGYREQUEST = DESCRIPTOR.message_types_by_name['DeleteTopologyRequest']
_DELETETOPOLOGYRESPONSE = DESCRIPTOR.message_types_by_name['DeleteTopologyResponse']
_LISTTOPOLOGYREQUEST = DESCRIPTOR.message_types_by_name['ListTopologyRequest']
_LISTTOPOLOGYRESPONSE = DESCRIPTOR.message_types_by_name['ListTopologyResponse']
CalcTopology = _reflection.GeneratedProtocolMessageType('CalcTopology', (_message.Message,), {
  'DESCRIPTOR' : _CALCTOPOLOGY,
  '__module__' : 'calc_topology_pb2'
  # @@protoc_insertion_point(class_scope:topology.CalcTopology)
  })
_sym_db.RegisterMessage(CalcTopology)

CreateTopologyRequest = _reflection.GeneratedProtocolMessageType('CreateTopologyRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATETOPOLOGYREQUEST,
  '__module__' : 'calc_topology_pb2'
  # @@protoc_insertion_point(class_scope:topology.CreateTopologyRequest)
  })
_sym_db.RegisterMessage(CreateTopologyRequest)

CreateTopologyResponse = _reflection.GeneratedProtocolMessageType('CreateTopologyResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATETOPOLOGYRESPONSE,
  '__module__' : 'calc_topology_pb2'
  # @@protoc_insertion_point(class_scope:topology.CreateTopologyResponse)
  })
_sym_db.RegisterMessage(CreateTopologyResponse)

ReadTopologyRequest = _reflection.GeneratedProtocolMessageType('ReadTopologyRequest', (_message.Message,), {
  'DESCRIPTOR' : _READTOPOLOGYREQUEST,
  '__module__' : 'calc_topology_pb2'
  # @@protoc_insertion_point(class_scope:topology.ReadTopologyRequest)
  })
_sym_db.RegisterMessage(ReadTopologyRequest)

ReadTopologyResponse = _reflection.GeneratedProtocolMessageType('ReadTopologyResponse', (_message.Message,), {
  'DESCRIPTOR' : _READTOPOLOGYRESPONSE,
  '__module__' : 'calc_topology_pb2'
  # @@protoc_insertion_point(class_scope:topology.ReadTopologyResponse)
  })
_sym_db.RegisterMessage(ReadTopologyResponse)

UpdateTopologyRequest = _reflection.GeneratedProtocolMessageType('UpdateTopologyRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATETOPOLOGYREQUEST,
  '__module__' : 'calc_topology_pb2'
  # @@protoc_insertion_point(class_scope:topology.UpdateTopologyRequest)
  })
_sym_db.RegisterMessage(UpdateTopologyRequest)

UpdateTopologyResponse = _reflection.GeneratedProtocolMessageType('UpdateTopologyResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATETOPOLOGYRESPONSE,
  '__module__' : 'calc_topology_pb2'
  # @@protoc_insertion_point(class_scope:topology.UpdateTopologyResponse)
  })
_sym_db.RegisterMessage(UpdateTopologyResponse)

DeleteTopologyRequest = _reflection.GeneratedProtocolMessageType('DeleteTopologyRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETETOPOLOGYREQUEST,
  '__module__' : 'calc_topology_pb2'
  # @@protoc_insertion_point(class_scope:topology.DeleteTopologyRequest)
  })
_sym_db.RegisterMessage(DeleteTopologyRequest)

DeleteTopologyResponse = _reflection.GeneratedProtocolMessageType('DeleteTopologyResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETETOPOLOGYRESPONSE,
  '__module__' : 'calc_topology_pb2'
  # @@protoc_insertion_point(class_scope:topology.DeleteTopologyResponse)
  })
_sym_db.RegisterMessage(DeleteTopologyResponse)

ListTopologyRequest = _reflection.GeneratedProtocolMessageType('ListTopologyRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTTOPOLOGYREQUEST,
  '__module__' : 'calc_topology_pb2'
  # @@protoc_insertion_point(class_scope:topology.ListTopologyRequest)
  })
_sym_db.RegisterMessage(ListTopologyRequest)

ListTopologyResponse = _reflection.GeneratedProtocolMessageType('ListTopologyResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTTOPOLOGYRESPONSE,
  '__module__' : 'calc_topology_pb2'
  # @@protoc_insertion_point(class_scope:topology.ListTopologyResponse)
  })
_sym_db.RegisterMessage(ListTopologyResponse)

_TOPOLOGYSERVICE = DESCRIPTOR.services_by_name['TopologyService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CALCTOPOLOGY._serialized_start=34
  _CALCTOPOLOGY._serialized_end=242
  _CREATETOPOLOGYREQUEST._serialized_start=244
  _CREATETOPOLOGYREQUEST._serialized_end=309
  _CREATETOPOLOGYRESPONSE._serialized_start=311
  _CREATETOPOLOGYRESPONSE._serialized_end=377
  _READTOPOLOGYREQUEST._serialized_start=379
  _READTOPOLOGYREQUEST._serialized_end=442
  _READTOPOLOGYRESPONSE._serialized_start=444
  _READTOPOLOGYRESPONSE._serialized_end=508
  _UPDATETOPOLOGYREQUEST._serialized_start=510
  _UPDATETOPOLOGYREQUEST._serialized_end=575
  _UPDATETOPOLOGYRESPONSE._serialized_start=577
  _UPDATETOPOLOGYRESPONSE._serialized_end=643
  _DELETETOPOLOGYREQUEST._serialized_start=645
  _DELETETOPOLOGYREQUEST._serialized_end=710
  _DELETETOPOLOGYRESPONSE._serialized_start=712
  _DELETETOPOLOGYRESPONSE._serialized_end=778
  _LISTTOPOLOGYREQUEST._serialized_start=780
  _LISTTOPOLOGYREQUEST._serialized_end=801
  _LISTTOPOLOGYRESPONSE._serialized_start=803
  _LISTTOPOLOGYRESPONSE._serialized_end=867
  _TOPOLOGYSERVICE._serialized_start=870
  _TOPOLOGYSERVICE._serialized_end=1310
# @@protoc_insertion_point(module_scope)
