# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: suggested-videos/suggested_videos_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from common import common_types_pb2 as common_dot_common__types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='suggested-videos/suggested_videos_service.proto',
  package='killrvideo.suggested_videos',
  syntax='proto3',
  serialized_options=_b('\252\002\032KillrVideo.SuggestedVideos'),
  serialized_pb=_b('\n/suggested-videos/suggested_videos_service.proto\x12\x1bkillrvideo.suggested_videos\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19\x63ommon/common_types.proto\"m\n\x17GetRelatedVideosRequest\x12)\n\x08video_id\x18\x01 \x01(\x0b\x32\x17.killrvideo.common.Uuid\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x14\n\x0cpaging_state\x18\x10 \x01(\t\"\x9f\x01\n\x18GetRelatedVideosResponse\x12)\n\x08video_id\x18\x01 \x01(\x0b\x32\x17.killrvideo.common.Uuid\x12\x42\n\x06videos\x18\x02 \x03(\x0b\x32\x32.killrvideo.suggested_videos.SuggestedVideoPreview\x12\x14\n\x0cpaging_state\x18\x03 \x01(\t\"o\n\x1aGetSuggestedForUserRequest\x12(\n\x07user_id\x18\x01 \x01(\x0b\x32\x17.killrvideo.common.Uuid\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x14\n\x0cpaging_state\x18\x10 \x01(\t\"\xa1\x01\n\x1bGetSuggestedForUserResponse\x12(\n\x07user_id\x18\x01 \x01(\x0b\x32\x17.killrvideo.common.Uuid\x12\x42\n\x06videos\x18\x02 \x03(\x0b\x32\x32.killrvideo.suggested_videos.SuggestedVideoPreview\x12\x14\n\x0cpaging_state\x18\x03 \x01(\t\"\xca\x01\n\x15SuggestedVideoPreview\x12)\n\x08video_id\x18\x01 \x01(\x0b\x32\x17.killrvideo.common.Uuid\x12.\n\nadded_date\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x1e\n\x16preview_image_location\x18\x04 \x01(\t\x12(\n\x07user_id\x18\x05 \x01(\x0b\x32\x17.killrvideo.common.Uuid2\xa3\x02\n\x15SuggestedVideoService\x12\x7f\n\x10GetRelatedVideos\x12\x34.killrvideo.suggested_videos.GetRelatedVideosRequest\x1a\x35.killrvideo.suggested_videos.GetRelatedVideosResponse\x12\x88\x01\n\x13GetSuggestedForUser\x12\x37.killrvideo.suggested_videos.GetSuggestedForUserRequest\x1a\x38.killrvideo.suggested_videos.GetSuggestedForUserResponseB\x1d\xaa\x02\x1aKillrVideo.SuggestedVideosb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,common_dot_common__types__pb2.DESCRIPTOR,])




_GETRELATEDVIDEOSREQUEST = _descriptor.Descriptor(
  name='GetRelatedVideosRequest',
  full_name='killrvideo.suggested_videos.GetRelatedVideosRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='video_id', full_name='killrvideo.suggested_videos.GetRelatedVideosRequest.video_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='killrvideo.suggested_videos.GetRelatedVideosRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paging_state', full_name='killrvideo.suggested_videos.GetRelatedVideosRequest.paging_state', index=2,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=140,
  serialized_end=249,
)


_GETRELATEDVIDEOSRESPONSE = _descriptor.Descriptor(
  name='GetRelatedVideosResponse',
  full_name='killrvideo.suggested_videos.GetRelatedVideosResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='video_id', full_name='killrvideo.suggested_videos.GetRelatedVideosResponse.video_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='videos', full_name='killrvideo.suggested_videos.GetRelatedVideosResponse.videos', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paging_state', full_name='killrvideo.suggested_videos.GetRelatedVideosResponse.paging_state', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=252,
  serialized_end=411,
)


_GETSUGGESTEDFORUSERREQUEST = _descriptor.Descriptor(
  name='GetSuggestedForUserRequest',
  full_name='killrvideo.suggested_videos.GetSuggestedForUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='killrvideo.suggested_videos.GetSuggestedForUserRequest.user_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='killrvideo.suggested_videos.GetSuggestedForUserRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paging_state', full_name='killrvideo.suggested_videos.GetSuggestedForUserRequest.paging_state', index=2,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=413,
  serialized_end=524,
)


_GETSUGGESTEDFORUSERRESPONSE = _descriptor.Descriptor(
  name='GetSuggestedForUserResponse',
  full_name='killrvideo.suggested_videos.GetSuggestedForUserResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='killrvideo.suggested_videos.GetSuggestedForUserResponse.user_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='videos', full_name='killrvideo.suggested_videos.GetSuggestedForUserResponse.videos', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paging_state', full_name='killrvideo.suggested_videos.GetSuggestedForUserResponse.paging_state', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=527,
  serialized_end=688,
)


_SUGGESTEDVIDEOPREVIEW = _descriptor.Descriptor(
  name='SuggestedVideoPreview',
  full_name='killrvideo.suggested_videos.SuggestedVideoPreview',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='video_id', full_name='killrvideo.suggested_videos.SuggestedVideoPreview.video_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='added_date', full_name='killrvideo.suggested_videos.SuggestedVideoPreview.added_date', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='killrvideo.suggested_videos.SuggestedVideoPreview.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preview_image_location', full_name='killrvideo.suggested_videos.SuggestedVideoPreview.preview_image_location', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='killrvideo.suggested_videos.SuggestedVideoPreview.user_id', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=691,
  serialized_end=893,
)

_GETRELATEDVIDEOSREQUEST.fields_by_name['video_id'].message_type = common_dot_common__types__pb2._UUID
_GETRELATEDVIDEOSRESPONSE.fields_by_name['video_id'].message_type = common_dot_common__types__pb2._UUID
_GETRELATEDVIDEOSRESPONSE.fields_by_name['videos'].message_type = _SUGGESTEDVIDEOPREVIEW
_GETSUGGESTEDFORUSERREQUEST.fields_by_name['user_id'].message_type = common_dot_common__types__pb2._UUID
_GETSUGGESTEDFORUSERRESPONSE.fields_by_name['user_id'].message_type = common_dot_common__types__pb2._UUID
_GETSUGGESTEDFORUSERRESPONSE.fields_by_name['videos'].message_type = _SUGGESTEDVIDEOPREVIEW
_SUGGESTEDVIDEOPREVIEW.fields_by_name['video_id'].message_type = common_dot_common__types__pb2._UUID
_SUGGESTEDVIDEOPREVIEW.fields_by_name['added_date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SUGGESTEDVIDEOPREVIEW.fields_by_name['user_id'].message_type = common_dot_common__types__pb2._UUID
DESCRIPTOR.message_types_by_name['GetRelatedVideosRequest'] = _GETRELATEDVIDEOSREQUEST
DESCRIPTOR.message_types_by_name['GetRelatedVideosResponse'] = _GETRELATEDVIDEOSRESPONSE
DESCRIPTOR.message_types_by_name['GetSuggestedForUserRequest'] = _GETSUGGESTEDFORUSERREQUEST
DESCRIPTOR.message_types_by_name['GetSuggestedForUserResponse'] = _GETSUGGESTEDFORUSERRESPONSE
DESCRIPTOR.message_types_by_name['SuggestedVideoPreview'] = _SUGGESTEDVIDEOPREVIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetRelatedVideosRequest = _reflection.GeneratedProtocolMessageType('GetRelatedVideosRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETRELATEDVIDEOSREQUEST,
  __module__ = 'suggested_videos.suggested_videos_service_pb2'
  # @@protoc_insertion_point(class_scope:killrvideo.suggested_videos.GetRelatedVideosRequest)
  ))
_sym_db.RegisterMessage(GetRelatedVideosRequest)

GetRelatedVideosResponse = _reflection.GeneratedProtocolMessageType('GetRelatedVideosResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETRELATEDVIDEOSRESPONSE,
  __module__ = 'suggested_videos.suggested_videos_service_pb2'
  # @@protoc_insertion_point(class_scope:killrvideo.suggested_videos.GetRelatedVideosResponse)
  ))
_sym_db.RegisterMessage(GetRelatedVideosResponse)

GetSuggestedForUserRequest = _reflection.GeneratedProtocolMessageType('GetSuggestedForUserRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETSUGGESTEDFORUSERREQUEST,
  __module__ = 'suggested_videos.suggested_videos_service_pb2'
  # @@protoc_insertion_point(class_scope:killrvideo.suggested_videos.GetSuggestedForUserRequest)
  ))
_sym_db.RegisterMessage(GetSuggestedForUserRequest)

GetSuggestedForUserResponse = _reflection.GeneratedProtocolMessageType('GetSuggestedForUserResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETSUGGESTEDFORUSERRESPONSE,
  __module__ = 'suggested_videos.suggested_videos_service_pb2'
  # @@protoc_insertion_point(class_scope:killrvideo.suggested_videos.GetSuggestedForUserResponse)
  ))
_sym_db.RegisterMessage(GetSuggestedForUserResponse)

SuggestedVideoPreview = _reflection.GeneratedProtocolMessageType('SuggestedVideoPreview', (_message.Message,), dict(
  DESCRIPTOR = _SUGGESTEDVIDEOPREVIEW,
  __module__ = 'suggested_videos.suggested_videos_service_pb2'
  # @@protoc_insertion_point(class_scope:killrvideo.suggested_videos.SuggestedVideoPreview)
  ))
_sym_db.RegisterMessage(SuggestedVideoPreview)


DESCRIPTOR._options = None

_SUGGESTEDVIDEOSERVICE = _descriptor.ServiceDescriptor(
  name='SuggestedVideoService',
  full_name='killrvideo.suggested_videos.SuggestedVideoService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=896,
  serialized_end=1187,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetRelatedVideos',
    full_name='killrvideo.suggested_videos.SuggestedVideoService.GetRelatedVideos',
    index=0,
    containing_service=None,
    input_type=_GETRELATEDVIDEOSREQUEST,
    output_type=_GETRELATEDVIDEOSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetSuggestedForUser',
    full_name='killrvideo.suggested_videos.SuggestedVideoService.GetSuggestedForUser',
    index=1,
    containing_service=None,
    input_type=_GETSUGGESTEDFORUSERREQUEST,
    output_type=_GETSUGGESTEDFORUSERRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SUGGESTEDVIDEOSERVICE)

DESCRIPTOR.services_by_name['SuggestedVideoService'] = _SUGGESTEDVIDEOSERVICE

# @@protoc_insertion_point(module_scope)
