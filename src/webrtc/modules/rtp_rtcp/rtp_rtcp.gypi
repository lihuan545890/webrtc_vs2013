# Copyright (c) 2011 The WebRTC project authors. All Rights Reserved.
#
# Use of this source code is governed by a BSD-style license
# that can be found in the LICENSE file in the root of the source
# tree. An additional intellectual property rights grant can be found
# in the file PATENTS.  All contributing project authors may
# be found in the AUTHORS file in the root of the source tree.

{
  'targets': [
    {
      'target_name': 'rtp_rtcp',
      'type': 'static_library',
      'dependencies': [
        '<(webrtc_root)/system_wrappers/system_wrappers.gyp:system_wrappers',
        '<(webrtc_root)/modules/modules.gyp:paced_sender',
        '<(webrtc_root)/modules/modules.gyp:remote_bitrate_estimator',
      ],
      'sources': [
        # Common
        'interface/fec_receiver.h',
        'interface/receive_statistics.h',
        'interface/remote_ntp_time_estimator.h',
        'interface/rtp_header_parser.h',
        'interface/rtp_payload_registry.h',
        'interface/rtp_receiver.h',
        'interface/rtp_rtcp.h',
        'interface/rtp_rtcp_defines.h',
        'source/bitrate.cc',
        'source/bitrate.h',
        'source/byte_io.h',
        'source/fec_receiver_impl.cc',
        'source/fec_receiver_impl.h',
        'source/receive_statistics_impl.cc',
        'source/receive_statistics_impl.h',
        'source/remote_ntp_time_estimator.cc',
        'source/rtp_header_parser.cc',
        'source/rtp_rtcp_config.h',
        'source/rtp_rtcp_impl.cc',
        'source/rtp_rtcp_impl.h',
        'source/rtcp_packet.cc',
        'source/rtcp_packet.h',
        'source/rtcp_receiver.cc',
        'source/rtcp_receiver.h',
        'source/rtcp_receiver_help.cc',
        'source/rtcp_receiver_help.h',
        'source/rtcp_sender.cc',
        'source/rtcp_sender.h',
        'source/rtcp_utility.cc',
        'source/rtcp_utility.h',
        'source/rtp_header_extension.cc',
        'source/rtp_header_extension.h',
        'source/rtp_receiver_impl.cc',
        'source/rtp_receiver_impl.h',
        'source/rtp_sender.cc',
        'source/rtp_sender.h',
        'source/rtp_utility.cc',
        'source/rtp_utility.h',
        'source/ssrc_database.cc',
        'source/ssrc_database.h',
        'source/tmmbr_help.cc',
        'source/tmmbr_help.h',
        # Audio Files
        'source/dtmf_queue.cc',
        'source/dtmf_queue.h',
        'source/rtp_receiver_audio.cc',
        'source/rtp_receiver_audio.h',
        'source/rtp_sender_audio.cc',
        'source/rtp_sender_audio.h',
        # Video Files
        'source/fec_private_tables_random.h',
        'source/fec_private_tables_bursty.h',
        'source/forward_error_correction.cc',
        'source/forward_error_correction.h',
        'source/forward_error_correction_internal.cc',
        'source/forward_error_correction_internal.h',
        'source/h264_sps_parser.cc',
        'source/h264_sps_parser.h',
        'source/producer_fec.cc',
        'source/producer_fec.h',
        'source/rtp_packet_history.cc',
        'source/rtp_packet_history.h',
        'source/rtp_payload_registry.cc',
        'source/rtp_receiver_strategy.cc',
        'source/rtp_receiver_strategy.h',
        'source/rtp_receiver_video.cc',
        'source/rtp_receiver_video.h',
        'source/rtp_sender_video.cc',
        'source/rtp_sender_video.h',
        'source/video_codec_information.h',
        'source/rtp_format.cc',
        'source/rtp_format.h',
        'source/rtp_format_h264.cc',
        'source/rtp_format_h264.h',
        'source/rtp_format_vp8.cc',
        'source/rtp_format_vp8.h',
        'source/rtp_format_video_generic.cc',
        'source/rtp_format_video_generic.h',
        'source/vp8_partition_aggregator.cc',
        'source/vp8_partition_aggregator.h',
        # Mocks
        'mocks/mock_rtp_rtcp.h',
        'source/mock/mock_rtp_payload_strategy.h',
      ], # source
      # TODO(jschuh): Bug 1348: fix size_t to int truncations.
      'msvs_disabled_warnings': [ 4267, ],
    },
  ],
}
