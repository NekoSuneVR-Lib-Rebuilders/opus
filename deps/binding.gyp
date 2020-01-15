{
	"variables": {
		"target_arch%": "x64"
	},
	"target_defaults": {
		"default_configuration": "Debug",
		"configuration": {
			"Debug": {
				"defines": [ "DEBUG", "_DEBUG" ],
				"msvs_settings": {
					"VSSLCompilerTool": {
						"RuntimeLibrary": 1,
					},
				},
			},
			"Release": {
				"defines": [ "NODEBUG" ],
				"msvs_settings": {
					"VSSLCompilerTool": {
						"RuntimeLibrary": 0,
					},
				},
			},
		},
		"msvs_settings": {
			"VCLinkerTool": {
				"GenerateDebugInformation": "true",
			},
		},
	},
	"targets": [
		{
			"target_name": "libopus",
			"type": "static_library",
			"sources": [
				"opus/src/opus_multistream.c",
				"opus/src/opus_projection_encoder.c",
				"opus/src/analysis.c",
				"opus/src/mlp_data.c",
				"opus/src/opus_multistream_encoder.c",
				"opus/src/opus_projection_decoder.c",
				"opus/src/mapping_matrix.c",
				"opus/src/opus_compare.c",
				"opus/src/mlp.c",
				"opus/src/opus.c",
				"opus/src/opus_multistream_decoder.c",
				"opus/src/opus_decoder.c",
				"opus/src/repacketizer.c",
				"opus/src/opus_encoder.c",
				"opus/silk/decode_frame.c",
				"opus/silk/float/inner_product_FLP.c",
				"opus/silk/float/scale_vector_FLP.c",
				"opus/silk/float/find_pred_coefs_FLP.c",
				"opus/silk/float/schur_FLP.c",
				"opus/silk/float/warped_autocorrelation_FLP.c",
				"opus/silk/float/burg_modified_FLP.c",
				"opus/silk/float/find_LPC_FLP.c",
				"opus/silk/float/LPC_inv_pred_gain_FLP.c",
				"opus/silk/float/scale_copy_vector_FLP.c",
				"opus/silk/float/noise_shape_analysis_FLP.c",
				"opus/silk/float/pitch_analysis_core_FLP.c",
				"opus/silk/float/bwexpander_FLP.c",
				"opus/silk/float/LTP_analysis_filter_FLP.c",
				"opus/silk/float/LTP_scale_ctrl_FLP.c",
				"opus/silk/float/corrMatrix_FLP.c",
				"opus/silk/float/encode_frame_FLP.c",
				"opus/silk/float/sort_FLP.c",
				"opus/silk/float/find_pitch_lags_FLP.c",
				"opus/silk/float/residual_energy_FLP.c",
				"opus/silk/float/LPC_analysis_filter_FLP.c",
				"opus/silk/float/autocorrelation_FLP.c",
				"opus/silk/float/k2a_FLP.c",
				"opus/silk/float/regularize_correlations_FLP.c",
				"opus/silk/float/find_LTP_FLP.c",
				"opus/silk/float/energy_FLP.c",
				"opus/silk/float/apply_sine_window_FLP.c",
				"opus/silk/float/wrappers_FLP.c",
				"opus/silk/float/process_gains_FLP.c",
				"opus/silk/stereo_quant_pred.c",
				"opus/silk/LPC_inv_pred_gain.c",
				"opus/silk/process_NLSFs.c",
				"opus/silk/NSQ.c",
				"opus/silk/check_control_input.c",
				"opus/silk/NLSF_del_dec_quant.c",
				"opus/silk/LPC_analysis_filter.c",
				"opus/silk/dec_API.c",
				"opus/silk/resampler.c",
				"opus/silk/sort.c",
				"opus/silk/VAD.c",
				"opus/silk/resampler_private_AR2.c",
				"opus/silk/LPC_fit.c",
				"opus/silk/control_SNR.c",
				"opus/silk/decode_parameters.c",
				"opus/silk/pitch_est_tables.c",
				"opus/silk/fixed/warped_autocorrelation_FIX.c",
				"opus/silk/fixed/apply_sine_window_FIX.c",
				"opus/silk/fixed/residual_energy16_FIX.c",
				"opus/silk/fixed/schur64_FIX.c",
				"opus/silk/fixed/residual_energy_FIX.c",
				"opus/silk/fixed/noise_shape_analysis_FIX.c",
				"opus/silk/fixed/encode_frame_FIX.c",
				"opus/silk/fixed/schur_FIX.c",
				"opus/silk/fixed/autocorr_FIX.c",
				"opus/silk/fixed/burg_modified_FIX.c",
				"opus/silk/fixed/pitch_analysis_core_FIX.c",
				"opus/silk/fixed/find_LTP_FIX.c",
				"opus/silk/fixed/find_LPC_FIX.c",
				"opus/silk/fixed/corrMatrix_FIX.c",
				"opus/silk/fixed/k2a_FIX.c",
				"opus/silk/fixed/LTP_scale_ctrl_FIX.c",
				"opus/silk/fixed/process_gains_FIX.c",
				"opus/silk/fixed/k2a_Q16_FIX.c",
				"opus/silk/fixed/regularize_correlations_FIX.c",
				"opus/silk/fixed/LTP_analysis_filter_FIX.c",
				"opus/silk/fixed/vector_ops_FIX.c",
				"opus/silk/fixed/find_pitch_lags_FIX.c",
				"opus/silk/fixed/find_pred_coefs_FIX.c",
				"opus/silk/control_audio_bandwidth.c",
				"opus/silk/decoder_set_fs.c",
				"opus/silk/NLSF_unpack.c",
				"opus/silk/bwexpander.c",
				"opus/silk/resampler_rom.c",
				"opus/silk/shell_coder.c",
				"opus/silk/decode_pulses.c",
				"opus/silk/bwexpander_32.c",
				"opus/silk/decode_core.c",
				"opus/silk/PLC.c",
				"opus/silk/tables_NLSF_CB_WB.c",
				"opus/silk/table_LSF_cos.c",
				"opus/silk/tables_pulses_per_block.c",
				"opus/silk/tables_gain.c",
				"opus/silk/inner_prod_aligned.c",
				"opus/silk/resampler_down2_3.c",
				"opus/silk/NSQ_del_dec.c",
				"opus/silk/decode_pitch.c",
				"opus/silk/NLSF_VQ_weights_laroia.c",
				"opus/silk/interpolate.c",
				"opus/silk/debug.c",
				"opus/silk/tables_other.c",
				"opus/silk/LP_variable_cutoff.c",
				"opus/silk/NLSF_decode.c",
				"opus/silk/encode_pulses.c",
				"opus/silk/control_codec.c",
				"opus/silk/stereo_LR_to_MS.c",
				"opus/silk/HP_variable_cutoff.c",
				"opus/silk/encode_indices.c",
				"opus/silk/init_decoder.c",
				"opus/silk/stereo_encode_pred.c",
				"opus/silk/NLSF_VQ.c",
				"opus/silk/init_encoder.c",
				"opus/silk/resampler_private_IIR_FIR.c",
				"opus/silk/resampler_private_up2_HQ.c",
				"opus/silk/sigm_Q15.c",
				"opus/silk/sum_sqr_shift.c",
				"opus/silk/tables_LTP.c",
				"opus/silk/resampler_down2.c",
				"opus/silk/code_signs.c",
				"opus/silk/tables_NLSF_CB_NB_MB.c",
				"opus/silk/gain_quant.c",
				"opus/silk/tables_pitch_lag.c",
				"opus/silk/NLSF_stabilize.c",
				"opus/silk/stereo_find_predictor.c",
				"opus/silk/A2NLSF.c",
				"opus/silk/NLSF2A.c",
				"opus/silk/VQ_WMat_EC.c",
				"opus/silk/NLSF_encode.c",
				"opus/silk/log2lin.c",
				"opus/silk/stereo_decode_pred.c",
				"opus/silk/lin2log.c",
				"opus/silk/CNG.c",
				"opus/silk/enc_API.c",
				"opus/silk/biquad_alt.c",
				"opus/silk/quant_LTP_gains.c",
				"opus/silk/resampler_private_down_FIR.c",
				"opus/silk/ana_filt_bank_1.c",
				"opus/silk/stereo_MS_to_LR.c",
				"opus/silk/decode_indices.c",
				"opus/celt/rate.c",
				"opus/celt/entdec.c",
				"opus/celt/modes.c",
				"opus/celt/celt_lpc.c",
				"opus/celt/laplace.c",
				"opus/celt/cwrs.c",
				"opus/celt/celt.c",
				"opus/celt/entcode.c",
				"opus/celt/celt_decoder.c",
				"opus/celt/celt_encoder.c",
				"opus/celt/mdct.c",
				"opus/celt/quant_bands.c",
				"opus/celt/vq.c",
				"opus/celt/bands.c",
				"opus/celt/kiss_fft.c",
				"opus/celt/entenc.c",
				"opus/celt/mathops.c",
				"opus/celt/pitch.c",
			],
			"cflags": [
				"-fvisibility=hidden",
				"-W",
				"-Wstrict-prototypes",
				"-Wall",
				"-Wextra",
				"-Wcast-align",
				"-Wnested-externs",
				"-Wshadow",
				"-Wno-parentheses",
				"-Wno-unused-parameter",
				"-Wno-sign-compare",
				"-Wno-maybe-uninitialized",
			],
			"include_dirs": [
				"config/opus/<(OS)/<(target_arch)",
				"opus/include",
				"opus/celt",
				"opus/silk",
				"opus/silk/float",
			],
			"defines": [
				"PIC",
				"HAVE_CONFIG_H",
			],
		},
	],
}
