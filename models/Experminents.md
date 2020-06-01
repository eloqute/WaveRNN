## WaveRNN 

### Corpora used:

1. LJSpeech
1. Debabble large_data_set (trained on Librispeech/noise)
1. Stephen Fry reading all seven Harry Potter books (not public domain)
1. Debabble trained on LJSpeech input/output/noise
    
   
### For all corpora, datasets were constructed by:

1.  Converting to 22Kh/32bit f.p. wav if necessary
1.  Segmenting
1.  Converting to series of mel spectrograms
1.  Encoding to 8-but mu-law (for fast training using softmax)

# Training
WaveRNN takes both a mu-law encoded audio stream and mel spectrograms for input to its Input layer during training.   
Based on current values of the audio/mels, it predicts the next audio block.  Training minimises a cross-entropy loss function 
comparing the prediction against the mu-law encoded clean audio (i.e. the voice audio, unmixed with noise corresponding with the input to debabble).

#Expermiments

Prior to running any experiments,  debabbled audio was fed into a pretrained WveRNN network trained to 800k steps on LJSpeech.   
This didn't improve the quality of the audio (link here).   We decided to train WaveRNN on the Debabble large dataset.

Initially, test on 
### debabble.exp01
*  Train on clean debabble input with a target of clean debabble input 
    dataset:
    x: Debabble (Librispeech) clean input
    y: Debabble (Librispeech) clean input
    training steps: 825k
##### Results 
(link here)

### debabble.exp02
*  Train the network with a mixture of debabble input and clean input, bothe with the same target of clean input, in an
attempt to get the network to learn to recognize debabbled audio, and interpret it as clean audio
    dataset:
    x: Debabble (Librispeech) clean input+ denoised output 50/50
    y: Debabble (Librispeech) clean input
    training steps: 1.5M
##### Results 
(link here)
  
### StephenFryHarryPotter.exp01
*  Train the network on a different, large single-speaker corpus, in order for us to learn its resilience to training data
    distribution:
    x: StephenFryHarryPotter
    y: StephenFryHarryPotter
    training steps: 1M
##### Results 
(link here)

### StephenFryHarryPotter.exp02
*  Train the network with different window size/overlap segment size (changed from Tacotron 2 paper to  use debabble values)
in order to whether is can resolve shorter transient distortion
    dataset:
    x: StephenFryHarryPotter
    y: StephenFryHarryPotter
    training steps: 750k
##### Results 
(link here)


### debabble/LJSpeech.exp01
*  Train the network with output from debabble trained on LJSpeech
    dataset:
    x: Debabble (LJSpeech) denoised output
    y: Debabble (LJSpeech) clean input
    training steps: 1M
##### Results 
(link here)

## debabble/LJSpeech.exp02
*  Train the network with input to debabble trained on LJSpeech 
    dataset:
    x: Debabble (LJSpeech) clean input
    y: Debabble (LJSpeech) clean input
    training steps: 1M
##### Results 
(link here)




