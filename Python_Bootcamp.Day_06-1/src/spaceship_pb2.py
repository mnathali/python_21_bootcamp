# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceship.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='spaceship.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0fspaceship.proto\"\x80\x03\n\tSpaceship\x12\'\n\talignment\x18\x01 \x01(\x0e\x32\x14.Spaceship.Alignment\x12\x0c\n\x04name\x18\x02 \x01(\t\x12$\n\nship_class\x18\x03 \x01(\x0e\x32\x10.Spaceship.Class\x12\x0e\n\x06length\x18\x04 \x01(\x02\x12\x11\n\tcrew_size\x18\x05 \x01(\x05\x12\r\n\x05\x61rmed\x18\x06 \x01(\x08\x12$\n\x08officers\x18\x08 \x03(\x0b\x32\x12.Spaceship.Officer\x1a>\n\x07Officer\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t\x12\x0c\n\x04rank\x18\x03 \x01(\t\" \n\tAlignment\x12\x08\n\x04\x41LLY\x10\x00\x12\t\n\x05\x45NEMY\x10\x01\"\\\n\x05\x43lass\x12\x0c\n\x08\x43ORVETTE\x10\x00\x12\x0b\n\x07\x46RIGATE\x10\x01\x12\x0b\n\x07\x43RUISER\x10\x02\x12\r\n\tDESTROYER\x10\x03\x12\x0b\n\x07\x43\x41RRIER\x10\x04\x12\x0f\n\x0b\x44READNOUGHT\x10\x05\"\x8f\x01\n\x0b\x43oordinates\x12\x13\n\x0b\x61scension_h\x18\x01 \x01(\x05\x12\x13\n\x0b\x61scension_m\x18\x02 \x01(\x05\x12\x13\n\x0b\x61scension_s\x18\x03 \x01(\x02\x12\x13\n\x0b\x64\x65\x63lination\x18\x04 \x01(\x05\x12\x15\n\rdeclination_m\x18\x05 \x01(\x05\x12\x15\n\rdeclination_s\x18\x06 \x01(\x02\x32\x31\n\x06Report\x12\'\n\tGetReport\x12\x0c.Coordinates\x1a\n.Spaceship0\x01\x62\x06proto3'
)



_SPACESHIP_ALIGNMENT = _descriptor.EnumDescriptor(
  name='Alignment',
  full_name='Spaceship.Alignment',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ALLY', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENEMY', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=278,
  serialized_end=310,
)
_sym_db.RegisterEnumDescriptor(_SPACESHIP_ALIGNMENT)

_SPACESHIP_CLASS = _descriptor.EnumDescriptor(
  name='Class',
  full_name='Spaceship.Class',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CORVETTE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FRIGATE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CRUISER', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DESTROYER', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CARRIER', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DREADNOUGHT', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=312,
  serialized_end=404,
)
_sym_db.RegisterEnumDescriptor(_SPACESHIP_CLASS)


_SPACESHIP_OFFICER = _descriptor.Descriptor(
  name='Officer',
  full_name='Spaceship.Officer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_name', full_name='Spaceship.Officer.first_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='Spaceship.Officer.last_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rank', full_name='Spaceship.Officer.rank', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=214,
  serialized_end=276,
)

_SPACESHIP = _descriptor.Descriptor(
  name='Spaceship',
  full_name='Spaceship',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='alignment', full_name='Spaceship.alignment', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='Spaceship.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ship_class', full_name='Spaceship.ship_class', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='length', full_name='Spaceship.length', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='crew_size', full_name='Spaceship.crew_size', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='armed', full_name='Spaceship.armed', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='officers', full_name='Spaceship.officers', index=6,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SPACESHIP_OFFICER, ],
  enum_types=[
    _SPACESHIP_ALIGNMENT,
    _SPACESHIP_CLASS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=404,
)


_COORDINATES = _descriptor.Descriptor(
  name='Coordinates',
  full_name='Coordinates',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ascension_h', full_name='Coordinates.ascension_h', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ascension_m', full_name='Coordinates.ascension_m', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ascension_s', full_name='Coordinates.ascension_s', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='declination', full_name='Coordinates.declination', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='declination_m', full_name='Coordinates.declination_m', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='declination_s', full_name='Coordinates.declination_s', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=407,
  serialized_end=550,
)

_SPACESHIP_OFFICER.containing_type = _SPACESHIP
_SPACESHIP.fields_by_name['alignment'].enum_type = _SPACESHIP_ALIGNMENT
_SPACESHIP.fields_by_name['ship_class'].enum_type = _SPACESHIP_CLASS
_SPACESHIP.fields_by_name['officers'].message_type = _SPACESHIP_OFFICER
_SPACESHIP_ALIGNMENT.containing_type = _SPACESHIP
_SPACESHIP_CLASS.containing_type = _SPACESHIP
DESCRIPTOR.message_types_by_name['Spaceship'] = _SPACESHIP
DESCRIPTOR.message_types_by_name['Coordinates'] = _COORDINATES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Spaceship = _reflection.GeneratedProtocolMessageType('Spaceship', (_message.Message,), {

  'Officer' : _reflection.GeneratedProtocolMessageType('Officer', (_message.Message,), {
    'DESCRIPTOR' : _SPACESHIP_OFFICER,
    '__module__' : 'spaceship_pb2'
    # @@protoc_insertion_point(class_scope:Spaceship.Officer)
    })
  ,
  'DESCRIPTOR' : _SPACESHIP,
  '__module__' : 'spaceship_pb2'
  # @@protoc_insertion_point(class_scope:Spaceship)
  })
_sym_db.RegisterMessage(Spaceship)
_sym_db.RegisterMessage(Spaceship.Officer)

Coordinates = _reflection.GeneratedProtocolMessageType('Coordinates', (_message.Message,), {
  'DESCRIPTOR' : _COORDINATES,
  '__module__' : 'spaceship_pb2'
  # @@protoc_insertion_point(class_scope:Coordinates)
  })
_sym_db.RegisterMessage(Coordinates)



_REPORT = _descriptor.ServiceDescriptor(
  name='Report',
  full_name='Report',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=552,
  serialized_end=601,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetReport',
    full_name='Report.GetReport',
    index=0,
    containing_service=None,
    input_type=_COORDINATES,
    output_type=_SPACESHIP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_REPORT)

DESCRIPTOR.services_by_name['Report'] = _REPORT

# @@protoc_insertion_point(module_scope)