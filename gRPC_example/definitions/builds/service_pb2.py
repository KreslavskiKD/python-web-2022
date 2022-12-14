# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='service.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rservice.proto\"\x06\n\x04Null\" \n\x0fRequestForAJoke\x12\r\n\x05theme\x18\x01 \x01(\t\"\x1c\n\x08\x41nekdote\x12\x10\n\x08\x61nekdote\x18\x01 \x01(\t2Q\n\x0bTestService\x12\x16\n\x06Health\x12\x05.Null\x1a\x05.Null\x12*\n\x0bGetAnekdote\x12\x10.RequestForAJoke\x1a\t.Anekdoteb\x06proto3'
)




_NULL = _descriptor.Descriptor(
  name='Null',
  full_name='Null',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=23,
)


_REQUESTFORAJOKE = _descriptor.Descriptor(
  name='RequestForAJoke',
  full_name='RequestForAJoke',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='theme', full_name='RequestForAJoke.theme', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=57,
)


_ANEKDOTE = _descriptor.Descriptor(
  name='Anekdote',
  full_name='Anekdote',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='anekdote', full_name='Anekdote.anekdote', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=87,
)

DESCRIPTOR.message_types_by_name['Null'] = _NULL
DESCRIPTOR.message_types_by_name['RequestForAJoke'] = _REQUESTFORAJOKE
DESCRIPTOR.message_types_by_name['Anekdote'] = _ANEKDOTE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Null = _reflection.GeneratedProtocolMessageType('Null', (_message.Message,), {
  'DESCRIPTOR' : _NULL,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:Null)
  })
_sym_db.RegisterMessage(Null)

RequestForAJoke = _reflection.GeneratedProtocolMessageType('RequestForAJoke', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTFORAJOKE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:RequestForAJoke)
  })
_sym_db.RegisterMessage(RequestForAJoke)

Anekdote = _reflection.GeneratedProtocolMessageType('Anekdote', (_message.Message,), {
  'DESCRIPTOR' : _ANEKDOTE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:Anekdote)
  })
_sym_db.RegisterMessage(Anekdote)



_TESTSERVICE = _descriptor.ServiceDescriptor(
  name='TestService',
  full_name='TestService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=89,
  serialized_end=170,
  methods=[
  _descriptor.MethodDescriptor(
    name='Health',
    full_name='TestService.Health',
    index=0,
    containing_service=None,
    input_type=_NULL,
    output_type=_NULL,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAnekdote',
    full_name='TestService.GetAnekdote',
    index=1,
    containing_service=None,
    input_type=_REQUESTFORAJOKE,
    output_type=_ANEKDOTE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TESTSERVICE)

DESCRIPTOR.services_by_name['TestService'] = _TESTSERVICE

# @@protoc_insertion_point(module_scope)
