
# tensorflow note

> 基于tf2.0
```shell
# tf2环境搭建
conda create -n your_env_name python=X.X（2.7、3.6等)
```

## Eager execution

> TensorFlow的`Eager execution`是一个命令式编程环境，该环境可立即评估操作，而无需构建图：操作返回具体值，而不是构建计算图以便稍后运行。 这使得TensorFlow和调试模型的入门变得容易，并且也减少了样板。