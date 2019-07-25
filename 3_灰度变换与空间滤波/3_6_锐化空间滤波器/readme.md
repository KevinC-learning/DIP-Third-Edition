## 1. 使用二阶微分锐化图像——拉普拉斯算子

### 拉普拉斯算子

一种典型的各向同性的微分算子，可用于检测图像中灰度图片的区域

$$
\nabla^{2} f=\frac{\partial^{2} f}{\partial x^{2}}+\frac{\partial^{2} f}{\partial y^{2}}
$$

根据上述的差分近似可以推导出

$$
\nabla^{2} f(x, y)=f(x+1, y)+f(x-1, y)+f(x, y+1)+f(x, y-1)-4 f(x, y)
$$

### 锐化过程

1. 使用拉普拉斯过滤器得到图像中灰度突变的区域$\nabla^{2} f(x, y)$
2. 使用原图像加上$\nabla^{2} f(x, y)$，如下

$$
g(x, y)=f(x, y)+c\left[\nabla^{2} f(x, y)\right]
$$

- 其中c为可变参数

### 运行
```python
python TEST_laplace_sharpen.py
```


## 2. 非锐化屏蔽与高提升滤波

非锐化屏蔽的基本思想是`从原图像中减去原图经平滑的后的图像后再加上原图像`，从而突出了灰度斜率变化的点

具体步骤如下：
1. 模糊原图，得到经平滑后的图像
2. 从原图减去模糊图像得到非锐化屏蔽模板
3. 原图加上非锐化屏蔽模板

$f(x, y)$表示原图，$\overline{f}(x, y)$表示模糊图像，公式描述如下：

$$
g(x, y)=f(x, y)+k * (f(x, y)-\overline{f}(x, y))
$$

- k = 1时，为`非锐化屏蔽`
- k > 1时，为`高提升滤波`

### 运行
```python
python TEST_unsharpened_masking.py
```

## 3. 一阶微分锐化图像——梯度

在二维图像$f$中，点$(x, y)$的梯度为

$$
\nabla f \equiv \operatorname{grad}(f) \equiv\left[\begin{array}{c}{g_{x}} \\ {g_{y}}\end{array}\right]=\left[\begin{array}{c}{\frac{\partial f}{\partial x}} \\ {\frac{\partial f}{\partial y}}\end{array}\right]
$$

它表示在$(x, y)$处，变化最快的方向，而该梯度的值表示该点变化快慢的程度，为方便实现，使用`绝对值`来近似
$$
M(x, y) \approx\left|g_{x}\right|+\left|g_{y}\right|
$$

### 运行
```python
python TEST_sharpen_gradient.py
```