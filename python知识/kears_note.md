
keras使用技巧
<!-- TOC -->

- [指定GPU/CPU](#%E6%8C%87%E5%AE%9Agpucpu)

<!-- /TOC -->
# 指定GPU/CPU

```
# 0表示使用cpu。不指定会默认使用环境中的gpu

# 代码内部指定

import tensorflow as tf
import keras.backend.tensorflow_backend as KTF
 
KTF.set_session(tf.Session(config=tf.ConfigProto(device_count={'gpu':0})))

# 命令行指定

CUDA_VISIBLE_DEVICES="0" python3 train.py
```

# 如何使用bert

## bert官方介绍

> BERT, or **B**idirectional **E**ncoder **R**epresentations from **T**ransformers

- BERT was built upon recent work in pre-training contextual representations — including Semi-supervised Sequence Learning, Generative Pre-Training, ELMo, and ULMFit — but crucially these models are all unidirectional or shallowly bidirectional. This means that each word is only contextualized using the words to its left (or right).**Using BERT has two stages: Pre-training and fine-tuning.**

## 官方发布的模型（英文/中文/多语言）

- A TensorFlow checkpoint (bert_model.ckpt) containing the pre-trained weights (which is actually 3 files).
- A vocab file (vocab.txt) to map WordPiece to word id.
- A config file (bert_config.json) which specifies the hyperparameters of the model.

## 官方tips

- If using your own vocabulary, make sure to change vocab_size in bert_config.json. If you use a larger vocabulary without changing this, you will likely get NaNs when training on GPU or TPU due to unchecked out-of-bounds access.
- If your task has a large domain-specific corpus available (e.g., "movie reviews" or "scientific papers"), it will likely be beneficial to run additional steps of pre-training on your corpus, starting from the BERT checkpoint.
- The learning rate we used in the paper was 1e-4. However, if you are doing additional steps of pre-training starting from an existing BERT checkpoint, you should use a smaller learning rate (e.g., 2e-5).

## keras调用方法


