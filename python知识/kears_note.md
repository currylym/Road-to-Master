
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