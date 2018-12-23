# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hapi/release/hook.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hapi/release/hook.proto',
  package='hapi.release',
  syntax='proto3',
  serialized_pb=_b('\n\x17hapi/release/hook.proto\x12\x0chapi.release\x1a\x1fgoogle/protobuf/timestamp.proto\"\x91\x04\n\x04Hook\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04kind\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\x10\n\x08manifest\x18\x04 \x01(\t\x12(\n\x06\x65vents\x18\x05 \x03(\x0e\x32\x18.hapi.release.Hook.Event\x12,\n\x08last_run\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06weight\x18\x07 \x01(\x05\x12\x38\n\x0f\x64\x65lete_policies\x18\x08 \x03(\x0e\x32\x1f.hapi.release.Hook.DeletePolicy\"\xe5\x01\n\x05\x45vent\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0f\n\x0bPRE_INSTALL\x10\x01\x12\x10\n\x0cPOST_INSTALL\x10\x02\x12\x0e\n\nPRE_DELETE\x10\x03\x12\x0f\n\x0bPOST_DELETE\x10\x04\x12\x0f\n\x0bPRE_UPGRADE\x10\x05\x12\x10\n\x0cPOST_UPGRADE\x10\x06\x12\x10\n\x0cPRE_ROLLBACK\x10\x07\x12\x11\n\rPOST_ROLLBACK\x10\x08\x12\x18\n\x14RELEASE_TEST_SUCCESS\x10\t\x12\x18\n\x14RELEASE_TEST_FAILURE\x10\n\x12\x0f\n\x0b\x43RD_INSTALL\x10\x0b\"C\n\x0c\x44\x65letePolicy\x12\r\n\tSUCCEEDED\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\x12\x18\n\x14\x42\x45\x46ORE_HOOK_CREATION\x10\x02\x42\tZ\x07releaseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_HOOK_EVENT = _descriptor.EnumDescriptor(
  name='Event',
  full_name='hapi.release.Hook.Event',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRE_INSTALL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POST_INSTALL', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRE_DELETE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POST_DELETE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRE_UPGRADE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POST_UPGRADE', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRE_ROLLBACK', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POST_ROLLBACK', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RELEASE_TEST_SUCCESS', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RELEASE_TEST_FAILURE', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CRD_INSTALL', index=11, number=11,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=306,
  serialized_end=535,
)
_sym_db.RegisterEnumDescriptor(_HOOK_EVENT)

_HOOK_DELETEPOLICY = _descriptor.EnumDescriptor(
  name='DeletePolicy',
  full_name='hapi.release.Hook.DeletePolicy',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCEEDED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BEFORE_HOOK_CREATION', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=537,
  serialized_end=604,
)
_sym_db.RegisterEnumDescriptor(_HOOK_DELETEPOLICY)


_HOOK = _descriptor.Descriptor(
  name='Hook',
  full_name='hapi.release.Hook',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='hapi.release.Hook.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kind', full_name='hapi.release.Hook.kind', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path', full_name='hapi.release.Hook.path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='manifest', full_name='hapi.release.Hook.manifest', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='events', full_name='hapi.release.Hook.events', index=4,
      number=5, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_run', full_name='hapi.release.Hook.last_run', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weight', full_name='hapi.release.Hook.weight', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delete_policies', full_name='hapi.release.Hook.delete_policies', index=7,
      number=8, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _HOOK_EVENT,
    _HOOK_DELETEPOLICY,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=604,
)

_HOOK.fields_by_name['events'].enum_type = _HOOK_EVENT
_HOOK.fields_by_name['last_run'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_HOOK.fields_by_name['delete_policies'].enum_type = _HOOK_DELETEPOLICY
_HOOK_EVENT.containing_type = _HOOK
_HOOK_DELETEPOLICY.containing_type = _HOOK
DESCRIPTOR.message_types_by_name['Hook'] = _HOOK

Hook = _reflection.GeneratedProtocolMessageType('Hook', (_message.Message,), dict(
  DESCRIPTOR = _HOOK,
  __module__ = 'hapi.release.hook_pb2'
  # @@protoc_insertion_point(class_scope:hapi.release.Hook)
  ))
_sym_db.RegisterMessage(Hook)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\007release'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
