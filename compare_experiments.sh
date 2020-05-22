#!/usr/bin/env bash


speaker_num=$1
noise_amount=$2
output_root=/mnt/d/data/test
output_subdir=$3
output_dir="${output_root}/${output_subdir}"

corpus=StephenFryHarryPotter

voc_mode='RAW'


step_number=325K

checkpoints_dir=/mnt/d/data/checkpoints
hp_dir=/mnt/d/data/hparams

input_file="/mnt/d/data/debabble/audio_results/large_data_set/unprocessed/bidir_full_ops/speaker_${speaker_num}_${noise_amount}_noise.wav"

mkdir -p "${output_dir}"
experiment='exp01'
python gen_wavernn.py --file "${input_file}" -o "${output_dir}" -p test_ -w "${checkpoints_dir}/${corpus}_${experiment}_${voc_mode}.wavernn/wave_step${step_number}_weights.pyt" --hp_file="${hp_dir}/hparams.${corpus}.${experiment}.py"
experiment='exp02'
python gen_wavernn.py --file "${input_file}" -o "${output_dir}" -p test_ -w "${checkpoints_dir}/${corpus}_${experiment}_${voc_mode}.wavernn/wave_step${step_number}_weights.pyt" --hp_file="${hp_dir}/hparams.${corpus}.${experiment}.py"
