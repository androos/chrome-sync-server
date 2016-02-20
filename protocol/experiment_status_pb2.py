# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experiment_status.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import experiments_specifics_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='experiment_status.proto',
  package='sync_pb',
  serialized_pb='\n\x17\x65xperiment_status.proto\x12\x07sync_pb\x1a\x1b\x65xperiments_specifics.proto\"2\n\x17\x45xperimentStatusRequest\x12\x17\n\x0f\x65xperiment_name\x18\x01 \x03(\t\"r\n\x18\x45xperimentStatusResponse\x12#\n\x15poll_interval_seconds\x18\x01 \x01(\x05:\x04\x33\x36\x30\x30\x12\x31\n\nexperiment\x18\x02 \x03(\x0b\x32\x1d.sync_pb.ExperimentsSpecificsB\x02H\x03')




_EXPERIMENTSTATUSREQUEST = _descriptor.Descriptor(
  name='ExperimentStatusRequest',
  full_name='sync_pb.ExperimentStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='experiment_name', full_name='sync_pb.ExperimentStatusRequest.experiment_name', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=65,
  serialized_end=115,
)


_EXPERIMENTSTATUSRESPONSE = _descriptor.Descriptor(
  name='ExperimentStatusResponse',
  full_name='sync_pb.ExperimentStatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='poll_interval_seconds', full_name='sync_pb.ExperimentStatusResponse.poll_interval_seconds', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=3600,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='experiment', full_name='sync_pb.ExperimentStatusResponse.experiment', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=117,
  serialized_end=231,
)

_EXPERIMENTSTATUSRESPONSE.fields_by_name['experiment'].message_type = experiments_specifics_pb2._EXPERIMENTSSPECIFICS
DESCRIPTOR.message_types_by_name['ExperimentStatusRequest'] = _EXPERIMENTSTATUSREQUEST
DESCRIPTOR.message_types_by_name['ExperimentStatusResponse'] = _EXPERIMENTSTATUSRESPONSE

class ExperimentStatusRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EXPERIMENTSTATUSREQUEST

  # @@protoc_insertion_point(class_scope:sync_pb.ExperimentStatusRequest)

class ExperimentStatusResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EXPERIMENTSTATUSRESPONSE

  # @@protoc_insertion_point(class_scope:sync_pb.ExperimentStatusResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), 'H\003')
# @@protoc_insertion_point(module_scope)
