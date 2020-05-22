import argparse
from scipy.io import wavfile
import numpy as np
import io
from random import randrange

def mix_files(sig_file, noise_file, noise_gain, mix_file):
    rate, sig = wavfile.read(sig_file)
    rate2, noise = wavfile.read(noise_file)
    if rate != rate2:
        raise ValueError("Sample rate of signal and noise must be the same")
    # if sig.shape != noise.shape:
    #     raise ValueError(f'Data length of signal {sig.shape} and noise {noise.shape} must be the same')
    sig_len = sig.shape[0]
    noise_len = noise.shape[0]
    if noise_len < sig_len:
        noise = np.pad(noise, (0, sig_len-noise_len), 'constant')
    elif noise_len > sig_len:
        sig = np.pad(sig, (0, noise_len-sig_len), 'constant')

    mix = sig + (noise_gain * noise) / (1.0 + noise_gain)

    wavfile.write(rate=rate, data=mix.astype('int16'), filename=mix_file)


def create_debabble_input_file(corpus_dir, output_dir, noise_gain, speaker_number):

    valid_set_start = 384
    is_training_set = (speaker_number < valid_set_start)

    sig_file = f'{corpus_dir}/bidir_full_ops_clean/speaker_{speaker_number}_clean.wav'
    if is_training_set:
        noise_file = f'{corpus_dir}/bidir_full_ops_train_noise/train_noise_{speaker_number:03}.wav'
    else:
        noise_number = speaker_number - valid_set_start
        noise_file = f'{corpus_dir}/bidir_full_ops_valid_noise/noise_validation_{noise_number}.wav'

    mix_file = f'{output_dir}/speaker_{speaker_number}_{noise_gain}_noise.wav'
    mix_files(sig_file, noise_file, noise_gain, mix_file)


num_speakers = 476

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Recombine debabble clean voice with corresponding noise file')
    parser.add_argument('--speaker_number', '-n', type=int, help='Speaker number - if not provided, process entire '
                                                                 'corpus')
    parser.add_argument('--corpus_directory', '-c', type=str, default='.', help='Location of debabble corpus')
    parser.add_argument('--output_directory', '-o', type=str, default='.', help='Location of output mix file')
    parser.add_argument('--noise_gain', '-g', type=float,  help='Gain of noise relative to signal - if not provided, '
                                                                'generate for gains of [1.3, 1.7, 2.1, 2.5]')

    parser.set_defaults(batched=None)

    args = parser.parse_args()
    if args.speaker_number is None:
        speaker_numbers = range(num_speakers)
    else:
        speaker_numbers = [args.speaker_number]

    corpus_dir = args.corpus_directory
    output_dir = args.output_directory

    if args.noise_gain is None:
        noise_gains = [1.3, 1.7, 2.1, 2.5]
    else:
        noise_gains = [args.noise_gain]

    for speaker_number in speaker_numbers:
        for noise_gain in noise_gains:
            create_debabble_input_file(corpus_dir, output_dir, noise_gain, speaker_number)
