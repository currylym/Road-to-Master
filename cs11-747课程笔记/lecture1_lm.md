
# A Simple (?) Exercise:Predicting the Next Word

## 句子概率计算

> $$p(X)=\prod_iP(x_i|x_1,...,x_{i-1})$$  

## count based 语言模型

### 计算方式

> $$P(x_i|x_{i-1},...,x_{i-n-1})=\frac{c(x_i,...,x_{i-n-1})}{c(x_{i-1},...,x_{i-n-1})}$$  
> 平滑：  
> $$P(x_i|x_{i-1},...,x_{i-n-1})=\lambda*P(x_i|)$$



