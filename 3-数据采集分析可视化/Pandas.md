# 一、Pandas介绍

## 学习目标

- 目标
  - 了解什么是pandas
  - 了解Numpy与Pandas的不同
  - 知道使用pandas的优势

------

## 1 Pandas介绍

![pandas](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctze6n6bj20yo076aam.jpg)

- 2008年WesMcKinney开发出的库
- 专门用于数据挖掘的开源python库
- **以Numpy为基础，借力Numpy模块在计算方面性能高的优势**
- **基于matplotlib，能够简便的画图**
- **独特的数据结构**

## 2 为什么使用Pandas

Numpy已经能够帮助我们处理数据，能够结合matplotlib解决部分数据展示等问题，那么pandas学习的目的在什么地方呢？

- **增强图表可读性**

  - 回忆我们在numpy当中创建学生成绩表样式：

  - 返回结果：

    ```python
    array([[92, 55, 78, 50, 50],
           [71, 76, 50, 48, 96],
           [45, 84, 78, 51, 68],
           [81, 91, 56, 54, 76],
           [86, 66, 77, 67, 95],
           [46, 86, 56, 61, 99],
           [46, 95, 44, 46, 56],
           [80, 50, 45, 65, 57],
           [41, 93, 90, 41, 97],
           [65, 83, 57, 57, 40]])
    ```

    如果数据展示为这样，可读性就会更友好：

    ![image-20190624090345499](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctz3y6dwj219k0j440q.jpg)

- **便捷的数据处理能力**

  ![img](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctz9n7ptj21c70u0te4.jpg)

- **读取文件方便**
- **封装了Matplotlib、Numpy的画图和计算**

## 3 小结

- pandas的优势【了解】
  - 增强图表可读性
  - 便捷的数据处理能力
  - 读取文件方便
  - 封装了Matplotlib、Numpy的画图和计算

# 二、 Pandas数据结构

## 学习目标

- 目标
  - 知道Pandas的Series结构
  - 掌握Pandas的Dataframe结构
  - 了解Pandas的MultiIndex与panel结构

------

Pandas中一共有三种数据结构，分别为：Series、DataFrame和MultiIndex（老版本中叫Panel ）。

其中Series是一维数据结构，DataFrame是二维的表格型数据结构，MultiIndex是三维的数据结构。

## 1.Series

Series是一个类似于一维数组的数据结构，它能够保存任何类型的数据，比如整数、字符串、浮点数等，**主要由一组数据和与之相关的索引两部分构成。**

![img](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctzcdn24j21ha0u0755.jpg)

### 1.1 Series的创建

```python
# 导入pandas
import pandas as pd

pd.Series(data=None, index=None, dtype=None)
```

- 参数：
  - data：传入的数据，可以是ndarray、list等
  - index：索引，必须是唯一的，且与数据的长度相等。如果没有传入索引参数，则默认会自动创建一个从0-N的整数索引。
  - dtype：数据的类型

通过已有数据创建

- 指定内容，默认索引

```python
pd.Series(np.arange(10))
# 运行结果
0    0
1    1
2    2
3    3
4    4
5    5
6    6
7    7
8    8
9    9
dtype: int64
```

- 指定索引

```python
pd.Series([6.7,5.6,3,10,2], index=[1,2,3,4,5])
# 运行结果
1     6.7
2     5.6
3     3.0
4    10.0
5     2.0
dtype: float64
```

- 通过字典数据创建

```python
color_count = pd.Series({'red':100, 'blue':200, 'green': 500, 'yellow':1000})
color_count
# 运行结果
blue       200
green      500
red        100
yellow    1000
dtype: int64
```

### 1.2 Series的属性

为了更方便地操作Series对象中的索引和数据，**Series中提供了两个属性index和values**

- index

```python
color_count.index

# 结果
Index(['blue', 'green', 'red', 'yellow'], dtype='object')
```

- values

```python
color_count.values

# 结果
array([ 200,  500,  100, 1000])
```

也可以使用索引来获取数据：

```python
color_count[2]

# 结果
100
```

## 2.DataFrame

DataFrame是一个类似于二维数组或表格(如excel)的对象，既有行索引，又有列索引

- 行索引，表明不同行，横向索引，叫index，0轴，axis=0
- 列索引，表名不同列，纵向索引，叫columns，1轴，axis=1

![img](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctzdsys8j21r60u076l.jpg)

### 2.1 DataFrame的创建

```python
# 导入pandas
import pandas as pd

pd.DataFrame(data=None, index=None, columns=None)
```

- 参数：
  - index：行标签。如果没有传入索引参数，则默认会自动创建一个从0-N的整数索引。
  - columns：列标签。如果没有传入索引参数，则默认会自动创建一个从0-N的整数索引。
- 通过已有数据创建

举例一：

```python
pd.DataFrame(np.random.randn(2,3))
```

![image-20190624084616637](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctzfyzvrj219805gq32.jpg)

回忆咱们在前面直接使用np创建的数组显示方式，比较两者的区别。

举例二：创建学生成绩表

```python
# 生成10名同学，5门功课的数据
score = np.random.randint(40, 100, (10, 5))

# 结果
array([[92, 55, 78, 50, 50],
       [71, 76, 50, 48, 96],
       [45, 84, 78, 51, 68],
       [81, 91, 56, 54, 76],
       [86, 66, 77, 67, 95],
       [46, 86, 56, 61, 99],
       [46, 95, 44, 46, 56],
       [80, 50, 45, 65, 57],
       [41, 93, 90, 41, 97],
       [65, 83, 57, 57, 40]])
```

**但是这样的数据形式很难看到存储的是什么的样的数据，可读性比较差！！**

**问题：如何让数据更有意义的显示**？

```python
# 使用Pandas中的数据结构
score_df = pd.DataFrame(score)
```

![image-20190624085446295](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctz5qmrdj21a20hi3za.jpg)

给分数数据增加行列索引,显示效果更佳

效果：

![image-20190624090129098](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctzka3gbj21cu0j0gmq.jpg)

- 增加行、列索引

```python
# 构造行索引序列
subjects = ["语文", "数学", "英语", "政治", "体育"]

# 构造列索引序列
stu = ['同学' + str(i) for i in range(score_df.shape[0])]

# 添加行索引
data = pd.DataFrame(score, columns=subjects, index=stu)
```

### 2.2 DataFrame的属性

- **shape**

```python
data.shape

# 结果
(10, 5)
```

- **index**

DataFrame的行索引列表

```python
data.index

# 结果
Index(['同学0', '同学1', '同学2', '同学3', '同学4', '同学5', '同学6', '同学7', '同学8', '同学9'], dtype='object')
```

- **columns**

DataFrame的列索引列表

```python
data.columns

# 结果
Index(['语文', '数学', '英语', '政治', '体育'], dtype='object')
```

- **values**

直接获取其中array的值

```python
data.values

array([[92, 55, 78, 50, 50],
       [71, 76, 50, 48, 96],
       [45, 84, 78, 51, 68],
       [81, 91, 56, 54, 76],
       [86, 66, 77, 67, 95],
       [46, 86, 56, 61, 99],
       [46, 95, 44, 46, 56],
       [80, 50, 45, 65, 57],
       [41, 93, 90, 41, 97],
       [65, 83, 57, 57, 40]])
```

- **T**

转置

```
data.T
```

结果

![image-20190624094546890](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctzaed56j219c0b63zn.jpg)

- **head(5)**：显示前5行内容

如果不补充参数，默认5行。填入参数N则显示前N行

```python
data.head(5)
```

![image-20190624094816880](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctziadx0j20y60b0aaj.jpg)

- **tail(5)**:显示后5行内容

如果不补充参数，默认5行。填入参数N则显示后N行

```python
data.tail(5)
```

### 2.3 DatatFrame索引的设置

需求：

![image-20190624095757620](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctz4w2hzj213y0j075e.jpg)

#### 2.3.1 修改行列索引值

```python
stu = ["学生_" + str(i) for i in range(score_df.shape[0])]

# 必须整体全部修改
data.index = stu
```

注意：以下修改方式是错误的

```python
# 错误修改方式
data.index[3] = '学生_3'
```

#### 2.3.2 重设索引

- reset_index(drop=False)
  - 设置新的下标索引
  - drop:默认为False，不删除原来索引，如果为True,删除原来的索引值

```python
# 重置索引,drop=False
data.reset_index()
```

![image-20190624100048415](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctzekei7j215u0iadh5.jpg)

```python
# 重置索引,drop=True
data.reset_index(drop=True)
```

#### 2.3.3 以某列值设置为新的索引

- set_index(keys, drop=True)
  - **keys** : 列索引名成或者列索引名称的列表
  - **drop** : boolean, default True.当做新的索引，删除原来的列

设置新索引案例

1、创建

```python
df = pd.DataFrame({'month': [1, 4, 7, 10],
                    'year': [2012, 2014, 2013, 2014],
                    'sale':[55, 40, 84, 31]})

   month  sale  year
0  1      55    2012
1  4      40    2014
2  7      84    2013
3  10     31    2014
```

2、以月份设置新的索引

```python
df.set_index('month')
       sale  year
month
1      55    2012
4      40    2014
7      84    2013
10     31    2014
```

3、设置多个索引，以年和月份

```python
df = df.set_index(['year', 'month'])
df
            sale
year  month
2012  1     55
2014  4     40
2013  7     84
2014  10    31
```

> 注：通过刚才的设置，这样DataFrame就变成了一个具有MultiIndex的DataFrame。

## 3.MultiIndex与Panel

### 3.1 MultiIndex

MultiIndex是三维的数据结构;

多级索引（也称层次化索引）是pandas的重要功能，可以在Series、DataFrame对象上拥有2个以及2个以上的索引。

#### 3.1.1 multiIndex的特性

打印刚才的df的行索引结果

```python
df.index

MultiIndex(levels=[[2012, 2013, 2014], [1, 4, 7, 10]],
           labels=[[0, 2, 1, 2], [0, 1, 2, 3]],
           names=['year', 'month'])
```

多级或分层索引对象。

- index属性
  - names:levels的名称
  - levels：每个level的元组值

```python
df.index.names
# FrozenList(['year', 'month'])

df.index.levels
# FrozenList([[1, 2], [1, 4, 7, 10]])
```

#### 3.1.2 multiIndex的创建

```python
arrays = [[1, 1, 2, 2], ['red', 'blue', 'red', 'blue']]
pd.MultiIndex.from_arrays(arrays, names=('number', 'color'))

# 结果
MultiIndex(levels=[[1, 2], ['blue', 'red']],
           codes=[[0, 0, 1, 1], [1, 0, 1, 0]],
           names=['number', 'color'])
```

### 3.2 Panel

#### 3.2.1 panel的创建

- *class* `pandas.Panel`(*data=None*, *items=None*, *major_axis=None*, *minor_axis=None*)
  - 作用：存储3维数组的Panel结构
  - 参数：
    - **data** : ndarray或者dataframe
    - **items** : 索引或类似数组的对象，axis=0
    - **major_axis** : 索引或类似数组的对象，axis=1
    - **minor_axis** : 索引或类似数组的对象，axis=2

```python
p = pd.Panel(data=np.arange(24).reshape(4,3,2),
                 items=list('ABCD'),
                 major_axis=pd.date_range('20130101', periods=3),
                 minor_axis=['first', 'second'])

# 结果
<class 'pandas.core.panel.Panel'>
Dimensions: 4 (items) x 3 (major_axis) x 2 (minor_axis)
Items axis: A to D
Major_axis axis: 2013-01-01 00:00:00 to 2013-01-03 00:00:00
Minor_axis axis: first to second
```

#### 3.2.2 查看panel数据

```
p[:,:,"first"]
p["B",:,:]
```

> **注：Pandas从版本0.20.0开始弃用：推荐的用于表示3D数据的方法是通过DataFrame上的MultiIndex方法**

## 4 小结

- pandas的优势【了解】
  - 增强图表可读性
  - 便捷的数据处理能力
  - 读取文件方便
  - 封装了Matplotlib、Numpy的画图和计算
- series【知道】
  - 创建
    - pd.Series([], index=[])
    - pd.Series({})
  - 属性
    - 对象.index
    - 对象.values
- DataFrame【掌握】
  - 创建
    - pd.DataFrame(data=None, index=None, columns=None)
  - 属性
    - shape -- 形状
    - index -- 行索引
    - columns -- 列索引
    - values -- 查看值
    - T -- 转置
    - head() -- 查看头部内容
    - tail() -- 查看尾部内容
  - DataFrame索引
    - 修改的时候,需要进行全局修改
    - 对象.reset_index()
    - 对象.set_index(keys)
- MultiIndex与Panel【了解】
  - multiIndex:
    - 类似ndarray中的三维数组
    - 创建：
      - pd.MultiIndex.from_arrays()
    - 属性：
      - 对象.index
  - panel：
    - pd.Panel(data, items, major_axis, minor_axis)
    - panel数据要是想看到,则需要进行索引到dataframe或者series才可以

# 三、 基本数据操作

## 学习目标

- 目标
  - 记忆DataFrame的形状、行列索引名称获取等基本属性
  - 应用Series和DataFrame的索引进行切片获取
  - 应用sort_index和sort_values实现索引和值的排序

------

为了更好的理解这些基本操作，我们将读取一个真实的股票数据。关于文件操作，后面在介绍，这里只先用一下API

```python
# 读取文件
data = pd.read_csv("./data/stock_day.csv")

# 删除一些列，让数据更简单些，再去做后面的操作
data = data.drop(["ma5","ma10","ma20","v_ma5","v_ma10","v_ma20"], axis=1)
```

![stockday](../images/stockday.png)

## 1 索引操作

Numpy当中我们已经讲过使用索引选取序列和切片选择，pandas也支持类似的操作，也可以直接使用列名、行名

称，甚至组合使用。

### 1.1 **直接使用行列索引(先列后行)**

获取'2018-02-27'这天的'close'的结果

```python
# 直接使用行列索引名字的方式（先列后行）
data['open']['2018-02-27']
23.53

# 不支持的操作
# 错误
data['2018-02-27']['open']
# 错误
data[:1, :2]
```

### 1.2 **结合loc或者iloc使用索引**

获取从'2018-02-27':'2018-02-22'，'open'的结果

```python
# 使用loc:只能指定行列索引的名字
data.loc['2018-02-27':'2018-02-22', 'open']

2018-02-27    23.53
2018-02-26    22.80
2018-02-23    22.88
Name: open, dtype: float64

# 使用iloc可以通过索引的下标去获取
# 获取前3天数据,前5列的结果
data.iloc[:3, :5]

            open    high    close    low
2018-02-27    23.53    25.88    24.16    23.53
2018-02-26    22.80    23.78    23.53    22.80
2018-02-23    22.88    23.37    22.82    22.71
```

### 1.3 **使用ix组合索引**

> Warning:Starting in 0.20.0, the `.ix` indexer is deprecated, in favor of the more strict `.iloc` and `.loc` indexers.

获取行第1天到第4天，['open', 'close', 'high', 'low']这个四个指标的结果

```python
# 使用ix进行下表和名称组合做引
data.ix[0:4, ['open', 'close', 'high', 'low']]

# 推荐使用loc和iloc来获取的方式
data.loc[data.index[0:4], ['open', 'close', 'high', 'low']]
data.iloc[0:4, data.columns.get_indexer(['open', 'close', 'high', 'low'])]

            open    close    high    low
2018-02-27    23.53    24.16    25.88    23.53
2018-02-26    22.80    23.53    23.78    22.80
2018-02-23    22.88    22.82    23.37    22.71
2018-02-22    22.25    22.28    22.76    22.02
```

## 2 赋值操作

对DataFrame当中的close列进行重新赋值为1

```python
# 直接修改原来的值
data['close'] = 1
# 或者
data.close = 1
```

## 3 排序

排序有两种形式，一种对于索引进行排序，一种对于内容进行排序

### 3.1 DataFrame排序

- 使用df.sort_values(by=, ascending=)
  - 单个键或者多个键进行排序,
  - 参数：
    - by：指定排序参考的键
    - ascending:默认升序
      - ascending=False:降序
      - ascending=True:升序

```python
# 按照开盘价大小进行排序 , 使用ascending指定按照大小排序
data.sort_values(by="open", ascending=True).head()
```

![image-20190624114304605](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctz6e3yjj21au098abf.jpg)

```python
# 按照多个键进行排序
data.sort_values(by=['open', 'high'])
```

![image-20190624114352409](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctzfiipdj219o09wdha.jpg)

- 使用df.sort_index给索引进行排序

这个股票的日期索引原来是从大到小，现在重新排序，从小到大

```python
# 对索引进行排序
data.sort_index()
```

![image-20190624114619379](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctz9zak4j21a409i403.jpg)

### 3.2 Series排序

- 使用series.sort_values(ascending=True)进行排序

series排序时，只有一列，不需要参数

```python
data['p_change'].sort_values(ascending=True).head()

2015-09-01   -10.03
2015-09-14   -10.02
2016-01-11   -10.02
2015-07-15   -10.02
2015-08-26   -10.01
Name: p_change, dtype: float64
```

- 使用series.sort_index()进行排序

与df一致

```python
# 对索引进行排序
data['p_change'].sort_index().head()

2015-03-02    2.62
2015-03-03    1.44
2015-03-04    1.57
2015-03-05    2.02
2015-03-06    8.51
Name: p_change, dtype: float64
```

## 4 总结

- 1.索引【掌握】
  - 直接索引 -- 先列后行,是需要通过索引的字符串进行获取
  - loc -- 先行后列,是需要通过索引的字符串进行获取
  - iloc -- 先行后列,是通过下标进行索引
  - ix -- 先行后列, 可以用上面两种方法混合进行索引
- 2.赋值【知道】
  - data[""] = **
  - data. **=**
- 3.排序【知道】
  - dataframe
    - 对象.sort_values()
    - 对象.sort_index()
  - series
    - 对象.sort_values()
    - 对象.sort_index()

# 四、 DataFrame运算

## 学习目标

- 目标
  - 应用add等实现数据间的加、减法运算
  - 应用逻辑运算符号实现数据的逻辑筛选
  - 应用isin, query实现数据的筛选
  - 使用describe完成综合统计
  - 使用max, min, mean, std完成统计计算
  - 使用idxmin、idxmax完成最大值最小值的索引
  - 使用cumsum等实现累计分析
  - 应用apply函数实现数据的自定义处理

------

## 1 算术运算

- add(other)

比如进行数学运算加上具体的一个数字

```python
data['open'].student_add(1)

2018 - 02 - 27
24.53
2018 - 02 - 26
23.80
2018 - 02 - 23
23.88
2018 - 02 - 22
23.25
2018 - 02 - 14
22.49
```

- sub(other)'

## 2 逻辑运算

### 2.1 逻辑运算符号

- 例如筛选data["open"] > 23的日期数据
  - data["open"] > 23返回逻辑结果

```python
data["open"] > 23

2018-02-27     True
2018-02-26    False
2018-02-23    False
2018-02-22    False
2018-02-14    False
# 逻辑判断的结果可以作为筛选的依据
data[data["open"] > 23].head()
```

![image-20190624115656264](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctzggdlbj21a009k403.jpg)

- 完成多个逻辑判断，

```python
data[(data["open"] > 23) & (data["open"] < 24)].head()
```

![image-20190624115753590](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctzh033ij219y09cjsy.jpg)

### 2.2 逻辑运算函数

- query(expr)
  - expr:查询字符串

通过query使得刚才的过程更加方便简单

```python
data.student_query("open<24 & open>23").head()
```

- isin(values)

例如判断'open'是否为23.53和23.85

```python
# 可以指定值进行一个判断，从而进行筛选操作
data[data["open"].isin([23.53, 23.85])]
```

![image-20190624115947522](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctzjuzobj219a09gwg0.jpg)

## 3 统计运算

### 3.1 describe

综合分析: 能够直接得出很多统计结果,`count`, `mean`, `std`, `min`, `max` 等

```python
# 计算平均值、标准差、最大值、最小值
data.describe()
```

![describe结果](../images/describe结果.png)

### 3.2 统计函数

Numpy当中已经详细介绍，在这里我们演示min(最小值), max(最大值), mean(平均值), median(中位数), var(方差), std(标准差),mode(众数)结果:

| `count`  | Number of non-NA observations                  |
| -------- | ---------------------------------------------- |
| `sum`    | **Sum of values**                              |
| `mean`   | **Mean of values**                             |
| `median` | Arithmetic median of values                    |
| `min`    | **Minimum**                                    |
| `max`    | **Maximum**                                    |
| `mode`   | Mode                                           |
| `abs`    | Absolute Value                                 |
| `prod`   | Product of values                              |
| `std`    | **Bessel-corrected sample standard deviation** |
| `var`    | **Unbiased variance**                          |
| `idxmax` | compute the index labels with the maximum      |
| `idxmin` | compute the index labels with the minimum      |

**对于单个函数去进行统计的时候，坐标轴还是按照默认列“columns” (axis=0, default)，如果要对行“index” 需要指定(axis=1)**

- max()、min()

```python
# 使用统计函数：0 代表列求结果， 1 代表行求统计结果
data.max(0)

open                   34.99
high                   36.35
close                  35.21
low                    34.01
volume             501915.41
price_change            3.03
p_change               10.03
turnover               12.56
my_price_change         3.41
dtype: float64
```

- std()、var()

```python
# 方差
data.var(0)

open               1.545255e+01
high               1.662665e+01
close              1.554572e+01
low                1.437902e+01
volume             5.458124e+09
price_change       8.072595e-01
p_change           1.664394e+01
turnover           4.323800e+00
my_price_change    6.409037e-01
dtype: float64

# 标准差
data.std(0)

open                   3.930973
high                   4.077578
close                  3.942806
low                    3.791968
volume             73879.119354
price_change           0.898476
p_change               4.079698
turnover               2.079375
my_price_change        0.800565
dtype: float64
```

- **median()：中位数**

中位数为将数据从小到大排列，在最中间的那个数为中位数。如果没有中间数，取中间两个数的平均值。

```python
df = pd.DataFrame({'COL1' : [2,3,4,5,4,2],
                   'COL2' : [0,1,2,3,4,2]})

df.median()

COL1    3.5
COL2    2.0
dtype: float64
```

- idxmax()、idxmin()

```python
# 求出最大值的位置
data.idxmax(axis=0)

open               2015-06-15
high               2015-06-10
close              2015-06-12
low                2015-06-12
volume             2017-10-26
price_change       2015-06-09
p_change           2015-08-28
turnover           2017-10-26
my_price_change    2015-07-10
dtype: object


# 求出最小值的位置
data.idxmin(axis=0)

open               2015-03-02
high               2015-03-02
close              2015-09-02
low                2015-03-02
volume             2016-07-06
price_change       2015-06-15
p_change           2015-09-01
turnover           2016-07-06
my_price_change    2015-06-15
dtype: object
```

### 3.3 累计统计函数

| 函数      | 作用                        |
| --------- | --------------------------- |
| `cumsum`  | **计算前1/2/3/…/n个数的和** |
| `cummax`  | 计算前1/2/3/…/n个数的最大值 |
| `cummin`  | 计算前1/2/3/…/n个数的最小值 |
| `cumprod` | 计算前1/2/3/…/n个数的积     |

**那么这些累计统计函数怎么用？**

![cumsum1](../images/cumsum1.png)

以上这些函数可以对series和dataframe操作

这里我们按照时间的从前往后来进行累计

- 排序

```python
# 排序之后，进行累计求和
data = data.sort_index()
```

- 对p_change进行求和

```python
stock_rise = data['p_change']
# plot方法集成了前面直方图、条形图、饼图、折线图
stock_rise.cumsum()

2015-03-02      2.62
2015-03-03      4.06
2015-03-04      5.63
2015-03-05      7.65
2015-03-06     16.16
2015-03-09     16.37
2015-03-10     18.75
2015-03-11     16.36
2015-03-12     15.03
2015-03-13     17.58
2015-03-16     20.34
2015-03-17     22.42
2015-03-18     23.28
2015-03-19     23.74
2015-03-20     23.48
2015-03-23     23.74
```

**那么如何让这个连续求和的结果更好的显示呢？**

![cumsum](../images/cumsum.png)

如果要使用plot函数，需要导入matplotlib.

```python
import matplotlib.pyplot as plt
# plot显示图形
stock_rise.cumsum().plot()
# 需要调用show，才能显示出结果
plt.show()
```

> 关于plot，稍后会介绍API的选择

## 4 自定义运算

- apply(func, axis=0)
  - func:自定义函数
  - axis=0:默认是列，axis=1为行进行运算
- 定义一个对列，最大值-最小值的函数

```python
data[['open', 'close']].apply(lambda x: x.max() - x.min(), axis=0)

open     22.74
close    22.85
dtype: float64
```

## 5 小结

- 算术运算【知道】
- 逻辑运算【知道】
  - 1.逻辑运算符号
  - 2.逻辑运算函数
    - 对象.query()
    - 对象.isin()
- 统计运算【知道】
  - 1.对象.describe()
  - 2.统计函数
  - 3.累积统计函数
- 自定义运算【知道】
  - apply(func, axis=0)

# 五、 Pandas画图

## 学习目标

- 目标
  - 了解DataFrame的画图函数
  - 了解Series的画图函数

------

## 1 pandas.DataFrame.plot

- `DataFrame.plot`(*kind='line'*)
- kind : str，需要绘制图形的种类
  - **‘line’ : line plot (default)**
  - ‘bar’ : vertical bar plot
  - ‘barh’ : horizontal bar plot
    - 关于“barh”的解释：
    - http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.barh.html
  - ‘hist’ : histogram
  - ‘pie’ : pie plot
  - ‘scatter’ : scatter plot

> 更多细节：https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.html?highlight=plot#pandas.DataFrame.plot

## 2 pandas.Series.plot

> 更多细节：https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.plot.html?highlight=plot#pandas.Series.plot

# 六、 文件读取与存储

## 学习目标

- 目标
  - 了解Pandas的几种文件读取存储操作
  - 应用CSV方式、HDF方式和json方式实现文件的读取和存储

------

我们的数据大部分存在于文件当中，所以pandas会支持复杂的IO操作，pandas的API支持众多的文件格式，如CSV、SQL、XLS、JSON、HDF5。

> 注：最常用的HDF5和CSV文件

![读取存储](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctzcw2uoj21660i041t.jpg)

## 1 CSV

### 1.1 read_csv

- pandas.read_csv(filepath_or_buffer, sep =',', usecols )
  - filepath_or_buffer:文件路径
  - sep :分隔符，默认用","隔开
  - usecols:指定读取的列名，列表形式
- 举例：读取之前的股票的数据

```python
# 读取文件,并且指定只获取'open', 'close'指标
data = pd.read_csv("./data/stock_day.csv", usecols=['open', 'close'])

            open    close
2018-02-27    23.53    24.16
2018-02-26    22.80    23.53
2018-02-23    22.88    22.82
2018-02-22    22.25    22.28
2018-02-14    21.49    21.92
```

### 1.2 to_csv

- DataFrame.to_csv(path_or_buf=None, sep=', ’, columns=None, header=True, index=True, mode='w', encoding=None)
  - path_or_buf :文件路径
  - sep :分隔符，默认用","隔开
  - columns :选择需要的列索引
  - header :boolean or list of string, default True,是否写进列索引值
  - index:是否写进行索引
  - mode:'w'：重写, 'a' 追加
- 举例：保存读取出来的股票数据
  - 保存'open'列的数据，然后读取查看结果

```python
# 选取10行数据保存,便于观察数据
data[:10].to_csv("./data/test.csv", columns=['open'])
# 读取，查看结果
pd.read_csv("./data/test.csv")

     Unnamed: 0    open
0    2018-02-27    23.53
1    2018-02-26    22.80
2    2018-02-23    22.88
3    2018-02-22    22.25
4    2018-02-14    21.49
5    2018-02-13    21.40
6    2018-02-12    20.70
7    2018-02-09    21.20
8    2018-02-08    21.79
9    2018-02-07    22.69
```

会发现将索引存入到文件当中，变成单独的一列数据。如果需要删除，可以指定index参数,删除原来的文件，重新保存一次。

```python
# index:存储不会讲索引值变成一列数据
data[:10].to_csv("./data/test.csv", columns=['open'], index=False)
```

## 2 HDF5

### 2.1 read_hdf与to_hdf

**HDF5文件的读取和存储需要指定一个键，值为要存储的DataFrame**

- pandas.read_hdf(path_or_buf，key =None，** kwargs)

  从h5文件当中读取数据

  - path_or_buffer:文件路径
  - key:读取的键
  - return:Theselected object

- DataFrame.to_hdf(path_or_buf, *key*, **\*kwargs*)

### 2.2 案例

- 读取文件

```python
day_close = pd.read_hdf("./data/day_close.h5")
```

如果读取的时候出现以下错误

![readh5](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctz4gblej213e0o2aea.jpg)

需要安装安装tables模块避免不能读取HDF5文件

```python
pip install tables
```

![tables](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctzbb4qoj211s0943z2.jpg)

- 存储文件

```python
day_close.to_hdf("./data/test.h5", key="day_close")
```

再次读取的时候, 需要指定键的名字

```python
new_close = pd.read_hdf("./data/test.h5", key="day_close")
```

**注意：优先选择使用HDF5文件存储**

- HDF5在存储的时候支持压缩，**使用的方式是blosc，这个是速度最快**的也是pandas默认支持的
- 使用压缩可以**提磁盘利用率，节省空间**
- HDF5还是跨平台的，可以轻松迁移到hadoop 上面

## 3 JSON

JSON是我们常用的一种数据交换格式，前面在前后端的交互经常用到，也会在存储的时候选择这种格式。所以我们需要知道Pandas如何进行读取和存储JSON格式。

### 3.1 read_json

- pandas.read_json(path_or_buf=None, orient=None, typ='frame', lines=False)

  - 将JSON格式准换成默认的Pandas DataFrame格式

  - orient : string,Indication of expected JSON string format.

    - 'split' : dict like {index -> [index], columns -> [columns], data -> [values]}

      - split 将索引总结到索引，列名到列名，数据到数据。将三部分都分开了

    - 'records' : list like [{column -> value}, ... , {column -> value}]

      - records 以`columns：values`的形式输出

    - 'index' : dict like {index -> {column -> value}}

      - index 以`index：{columns：values}...`的形式输出

    - 'columns' : dict like {column -> {index -> value}}

      ,默认该格式

      - colums 以`columns:{index:values}`的形式输出

    - 'values' : just the values array

      - values 直接输出值

  - lines : boolean, default False

    - 按照每行读取json对象

  - typ : default ‘frame’， 指定转换成的对象类型series或者dataframe

  ### 3.2 read_josn 案例

- 数据介绍

这里使用一个新闻标题讽刺数据集，格式为json。`is_sarcastic`：1讽刺的，否则为0；`headline`：新闻报道的标题；`article_link`：链接到原始新闻文章。存储格式为：

```jso
{"article_link": "https://www.huffingtonpost.com/entry/versace-black-code_us_5861fbefe4b0de3a08f600d5", "headline": "former versace store clerk sues over secret 'black code' for minority shoppers", "is_sarcastic": 0}
{"article_link": "https://www.huffingtonpost.com/entry/roseanne-revival-review_us_5ab3a497e4b054d118e04365", "headline": "the 'roseanne' revival catches up to our thorny political mood, for better and worse", "is_sarcastic": 0}
```

- 读取

orient指定存储的json格式，lines指定按照行去变成一个样本

```python
json_read = pd.read_json("./data/Sarcasm_Headlines_Dataset.json", orient="records", lines=True)
```

结果为：

![img](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctzf5rzfj215m0imaea.jpg)

### 3.3 to_json

- DataFrame.to_json(

  path_or_buf=None

  ,

   

  orient=None

  ,

   

  lines=False

  )

  - 将Pandas 对象存储为json格式
  - *path_or_buf=None*：文件地址
  - orient:存储的json形式，{‘split’,’records’,’index’,’columns’,’values’}
  - lines:一个对象存储为一行

### 3.4 案例

- 存储文件

```python
json_read.to_json("./data/test.json", orient='records')
```

结果

```
[{"article_link":"https:\/\/www.huffingtonpost.com\/entry\/versace-black-code_us_5861fbefe4b0de3a08f600d5","headline":"former versace store clerk sues over secret 'black code' for minority shoppers","is_sarcastic":0},{"article_link":"https:\/\/www.huffingtonpost.com\/entry\/roseanne-revival-review_us_5ab3a497e4b054d118e04365","headline":"the 'roseanne' revival catches up to our thorny political mood, for better and worse","is_sarcastic":0},{"article_link":"https:\/\/local.theonion.com\/mom-starting-to-fear-son-s-web-series-closest-thing-she-1819576697","headline":"mom starting to fear son's web series closest thing she will have to grandchild","is_sarcastic":1},{"article_link":"https:\/\/politics.theonion.com\/boehner-just-wants-wife-to-listen-not-come-up-with-alt-1819574302","headline":"boehner just wants wife to listen, not come up with alternative debt-reduction ideas","is_sarcastic":1},{"article_link":"https:\/\/www.huffingtonpost.com\/entry\/jk-rowling-wishes-snape-happy-birthday_us_569117c4e4b0cad15e64fdcb","headline":"j.k. rowling wishes snape happy birthday in the most magical way","is_sarcastic":0},{"article_link":"https:\/\/www.huffingtonpost.com\/entry\/advancing-the-worlds-women_b_6810038.html","headline":"advancing the world's women","is_sarcastic":0},....]
```

- 修改lines参数为True

```python
json_read.to_json("./data/test.json", orient='records', lines=True)
```

结果

```
{"article_link":"https:\/\/www.huffingtonpost.com\/entry\/versace-black-code_us_5861fbefe4b0de3a08f600d5","headline":"former versace store clerk sues over secret 'black code' for minority shoppers","is_sarcastic":0}
{"article_link":"https:\/\/www.huffingtonpost.com\/entry\/roseanne-revival-review_us_5ab3a497e4b054d118e04365","headline":"the 'roseanne' revival catches up to our thorny political mood, for better and worse","is_sarcastic":0}
{"article_link":"https:\/\/local.theonion.com\/mom-starting-to-fear-son-s-web-series-closest-thing-she-1819576697","headline":"mom starting to fear son's web series closest thing she will have to grandchild","is_sarcastic":1}
{"article_link":"https:\/\/politics.theonion.com\/boehner-just-wants-wife-to-listen-not-come-up-with-alt-1819574302","headline":"boehner just wants wife to listen, not come up with alternative debt-reduction ideas","is_sarcastic":1}
{"article_link":"https:\/\/www.huffingtonpost.com\/entry\/jk-rowling-wishes-snape-happy-birthday_us_569117c4e4b0cad15e64fdcb","headline":"j.k. rowling wishes snape happy birthday in the most magical way","is_sarcastic":0}...
```

## 4 小结

- pandas的CSV、HDF5、JSON文件的读取【知道】
  - 对象.read_**()
  - 对象.to_**()

# 七、 高级处理-缺失值处理

## 学习目标

- 目标
  - 应用isnull判断是否有缺失数据NaN
  - 应用fillna实现缺失值的填充
  - 应用dropna实现缺失值的删除
  - 应用replace实现数据的替换

------

![缺失值](images/缺失值.png)

## 1 如何处理nan

- 获取缺失值的标记方式(NaN或者其他标记方式)
- 如果缺失值的标记方式是NaN
  - 判断数据中是否包含NaN：
    - pd.isnull(df),
    - pd.notnull(df)
  - 存在缺失值nan:
    - 1、删除存在缺失值的:dropna(axis='rows')
      - 注：不会修改原数据，需要接受返回值
    - 2、替换缺失值:fillna(value, inplace=True)
      - value:替换成的值
      - inplace:True:会修改原数据，False:不替换修改原数据，生成新的对象
- 如果缺失值没有使用NaN标记，比如使用"？"
  - 先替换‘?’为np.nan，然后继续处理

## 2 电影数据的缺失值处理

- 电影数据文件获取

```python
# 读取电影数据
movie = pd.read_csv("./data/IMDB-Movie-Data.csv")
```

![img](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctzjbai5j21oq0fwtbt.jpg)

### 2.1 判断缺失值是否存在

- pd.notnull()

```
pd.notnull(movie)
Rank    Title    Genre    Description    Director    Actors    Year    Runtime (Minutes)    Rating    Votes    Revenue (Millions)    Metascore
0    True    True    True    True    True    True    True    True    True    True    True    True
1    True    True    True    True    True    True    True    True    True    True    True    True
2    True    True    True    True    True    True    True    True    True    True    True    True
3    True    True    True    True    True    True    True    True    True    True    True    True
4    True    True    True    True    True    True    True    True    True    True    True    True
5    True    True    True    True    True    True    True    True    True    True    True    True
6    True    True    True    True    True    True    True    True    True    True    True    True
7    True    True    True    True    True    True    True    True    True    True    False    True
np.all(pd.notnull(movie))
```

- pd.isnull()

### 2.2 存在缺失值nan,并且是np.nan

- 1、删除

pandas删除缺失值，使用dropna的前提是，缺失值的类型必须是np.nan

```python
# 不修改原数据
movie.dropna()

# 可以定义新的变量接受或者用原来的变量名
data = movie.dropna()
```

- 2、替换缺失值

```python
# 替换存在缺失值的样本的两列
# 替换填充平均值，中位数
# movie['Revenue (Millions)'].fillna(movie['Revenue (Millions)'].mean(), inplace=True)
```

替换所有缺失值：

```python
for i in movie.columns:
    if np.all(pd.notnull(movie[i])) == False:
        print(i)
        movie[i].fillna(movie[i].mean(), inplace=True)
```

### 2.3 不是缺失值nan，有默认标记的

数据是这样的：

![问号缺失值](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctz82ke5j20py0kuq49.jpg)

```python
wis = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data")
```

以上数据在读取时，可能会报如下错误：

```
URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:833)>
```

解决办法：

```python
# 全局取消证书验证
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
```

**处理思路分析：**

- 1、先替换‘?’为np.nan
  - df.replace(to_replace=, value=)
    - to_replace:替换前的值
    - value:替换后的值

```python
# 把一些其它值标记的缺失值，替换成np.nan
wis = wis.replace(to_replace='?', value=np.nan)
```

- 2、在进行缺失值的处理

```python
# 删除
wis = wis.dropna()
```

## 3 小结

- isnull、notnull判断是否存在缺失值【知道】
  - np.any(pd.isnull(movie)) # 里面如果有一个缺失值,就返回True
  - np.all(pd.notnull(movie)) # 里面如果有一个缺失值,就返回False
- dropna删除np.nan标记的缺失值【知道】
  - movie.dropna()
- fillna填充缺失值【知道】
  - movie[i].fillna(value=movie[i].mean(), inplace=True)
- replace替换具体某些值【知道】
  - wis.replace(to_replace="?", value=np.NaN)

# 七、 高级处理-数据离散化

## 学习目标

- 目标
  - 应用cut、qcut实现数据的区间分组
  - 应用get_dummies实现数据的one-hot编码

------

## 1 为什么要离散化

连续属性离散化的目的是为了简化数据结构，**数据离散化技术可以用来减少给定连续属性值的个数**。离散化方法经常作为数据挖掘的工具。

## 2 什么是数据的离散化

**连续属性的离散化就是在连续属性的值域上，将值域划分为若干个离散的区间，最后用不同的符号或整数** **值代表落在每个子区间中的属性值。**

离散化有很多种方法，这使用一种最简单的方式去操作

- 原始人的身高数据：165，174，160，180，159，163，192，184
- 假设按照身高分几个区间段：150~165, 165~180,180~195

这样我们将数据分到了三个区间段，我可以对应的标记为矮、中、高三个类别，最终要处理成一个"哑变量"矩阵

## 3 股票的涨跌幅离散化

我们对股票每日的"p_change"进行离散化

![哑变量矩阵](../images/哑变量矩阵.png)

### 3.1 读取股票的数据

先读取股票的数据，筛选出p_change数据

```python
data = pd.read_csv("./data/stock_day.csv")
p_change= data['p_change']
```

### 3.2 将股票涨跌幅数据进行分组

![股票涨跌幅分组](../images/股票涨跌幅分组.png)

使用的工具：

- pd.qcut(data, q)：
  - 对数据进行分组将数据分组，一般会与value_counts搭配使用，统计每组的个数
- series.value_counts()：统计分组次数

```python
# 自行分组
qcut = pd.qcut(p_change, 10)
# 计算分到每个组数据个数
qcut.value_counts()
```

自定义区间分组：

- pd.cut(data, bins)

```python
# 自己指定分组区间
bins = [-100, -7, -5, -3, 0, 3, 5, 7, 100]
p_counts = pd.cut(p_change, bins)
```

### 3.3 股票涨跌幅分组数据变成one-hot编码

- **什么是one-hot编码**

把每个类别生成一个布尔列，这些列中只有一列可以为这个样本取值为1.其又被称为热编码。

把下图中左边的表格转化为使用右边形式进行表示：

![image-20190316224151504](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctzitxhhj21y80mwgo6.jpg)

- pandas.get_dummies(*data*, *prefix=None*)
  - data:array-like, Series, or DataFrame
  - prefix:分组名字

```python
# 得出one-hot编码矩阵
dummies = pd.get_dummies(p_counts, prefix="rise")
```

![哑变量矩阵](../images/哑变量矩阵.png)

## 4 小结

- 数据离散化【知道】
  - 可以用来减少给定连续属性值的个数
  - 在连续属性的值域上，将值域划分为若干个离散的区间，最后用不同的符号或整数值代表落在每个子区间中的属性值。
- qcut、cut实现数据分组【知道】
  - qcut:大致分为相同的几组
  - cut:自定义分组区间
- get_dummies实现哑变量矩阵【知道】

# 九、 高级处理-合并

## 学习目标

- 目标
  - 应用pd.concat实现数据的合并
  - 应用pd.merge实现数据的合并

------

如果你的数据由多张表组成，那么有时候需要将不同的内容合并在一起分析

## 1 pd.concat实现数据合并

- pd.concat([data1, data2], axis=1)
  - 按照行或列进行合并,axis=0为列索引，axis=1为行索引

比如我们将刚才处理好的one-hot编码与原数据合并

![股票哑变量合并](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctzd7xowj21o80awtaw.jpg)

```python
# 按照行索引进行
pd.concat([data, dummies], axis=1)
```

## 2 pd.merge

- pd.merge(left, right, how='inner', on=None)
  - 可以指定按照两组数据的共同键值对合并或者左右各自
  - `left`: DataFrame
  - `right`: 另一个DataFrame
  - `on`: 指定的共同键
  - how:按照什么方式连接

| Merge method | SQL Join Name      | Description                               |
| ------------ | ------------------ | ----------------------------------------- |
| `left`       | `LEFT OUTER JOIN`  | Use keys from left frame only             |
| `right`      | `RIGHT OUTER JOIN` | Use keys from right frame only            |
| `outer`      | `FULL OUTER JOIN`  | Use union of keys from both frames        |
| `inner`      | `INNER JOIN`       | Use intersection of keys from both frames |

### 2.1 pd.merge合并

```
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                        'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                        'key2': ['K0', 'K0', 'K0', 'K0'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']})

# 默认内连接
result = pd.merge(left, right, on=['key1', 'key2'])
```

![内连接](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctzbw46rj20y8090aaw.jpg)

- 左连接

```python
result = pd.merge(left, right, how='left', on=['key1', 'key2'])
```

![左连接](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctz72swmj210809ygmn.jpg)

- 右连接

```python
result = pd.merge(left, right, how='right', on=['key1', 'key2'])
```

![右连接](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctzkqbwtj212c09ejsb.jpg)

- 外链接

```python
result = pd.merge(left, right, how='outer', on=['key1', 'key2'])
```

![外链接](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctz943irj212e0c4dh1.jpg)

## 3 总结

- pd.concat([数据1, 数据2], axis=**)【知道】
- pd.merge(left, right, how=, on=)【知道】
  - how -- 以何种方式连接
  - on -- 连接的键的依据是哪几个

# 十、 高级处理-交叉表与透视表

## 学习目标

- 目标
  - 应用crosstab和pivot_table实现交叉表与透视表

------

## 1 交叉表与透视表什么作用

**探究股票的涨跌与星期几有关？**

**以下图当中表示，week代表星期几，1,0代表这一天股票的涨跌幅是好还是坏，里面的数据代表比例**

**可以理解为所有时间为星期一等等的数据当中涨跌幅好坏的比例**

![交叉表透视表作用](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctzatjwfj20ca0bgwet.jpg)

![crosstab](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctz7keaij20m20f0wev.jpg)

- 交叉表：

  交叉表用于计算一列数据对于另外一列数据的分组个数(用于统计分组频率的特殊透视表)

  - pd.crosstab(value1, value2)

- 透视表：

  透视表是将原有的DataFrame的列分别作为行索引和列索引，然后对指定的列应用聚集函数

  - data.pivot_table(）

- - DataFrame.pivot_table([], index=[])

## 2 案例分析

### 2.1 数据准备

- 准备两列数据，星期数据以及涨跌幅是好是坏数据
- 进行交叉表计算

```python
# 寻找星期几跟股票张得的关系
# 1、先把对应的日期找到星期几
date = pd.to_datetime(data.index).weekday
data['week'] = date

# 2、假如把p_change按照大小去分个类0为界限
data['posi_neg'] = np.where(data['p_change'] > 0, 1, 0)

# 通过交叉表找寻两列数据的关系
count = pd.crosstab(data['week'], data['posi_neg'])
```

但是我们看到count只是每个星期日子的好坏天数，并没有得到比例，该怎么去做？

- 对于每个星期一等的总天数求和，运用除法运算求出比例

```python
# 算数运算，先求和
sum = count.sum(axis=1).astype(np.float32)

# 进行相除操作，得出比例
pro = count.div(sum, axis=0)
```

### 2.2 查看效果

使用plot画出这个比例，使用stacked的柱状图

```python
pro.plot(kind='bar', stacked=True)
plt.show()
```

### 2.3 使用pivot_table(透视表)实现

使用透视表，刚才的过程更加简单

```python
# 通过透视表，将整个过程变成更简单一些
data.pivot_table(['posi_neg'], index='week')
```

## 3 小结

- 交叉表与透视表的作用【知道】
  - 交叉表：计算一列数据对于另外一列数据的分组个数
  - 透视表：指定某一列对另一列的关系

# 十一、 高级处理-分组与聚合

## 学习目标

- 目标
  - 应用groupby和聚合函数实现数据的分组与聚合

------

**分组与聚合通常是分析数据的一种方式，通常与一些统计函数一起使用，查看数据的分组情况**

想一想其实刚才的交叉表与透视表也有分组的功能，所以算是分组的一种形式，只不过他们主要是计算次数或者计算比例！！看其中的效果：

![分组效果](../images/分组效果.png)

## 1 什么分组与聚合

![分组聚合原理](../images/分组聚合原理.png)

## 2 分组API

- DataFrame.groupby(key, as_index=False)
  - key:分组的列数据，可以多个
- 案例:不同颜色的不同笔的价格数据

```python
col =pd.DataFrame({'color': ['white','red','green','red','green'], 'object': ['pen','pencil','pencil','ashtray','pen'],'price1':[5.56,4.20,1.30,0.56,2.75],'price2':[4.75,4.12,1.60,0.75,3.15]})

color    object    price1    price2
0    white    pen    5.56    4.75
1    red    pencil    4.20    4.12
2    green    pencil    1.30    1.60
3    red    ashtray    0.56    0.75
4    green    pen    2.75    3.15
```

- 进行分组，对颜色分组，price进行聚合

```python
# 分组，求平均值
col.groupby(['color'])['price1'].mean()
col['price1'].groupby(col['color']).mean()

color
green    2.025
red      2.380
white    5.560
Name: price1, dtype: float64

# 分组，数据的结构不变
col.groupby(['color'], as_index=False)['price1'].mean()

color    price1
0    green    2.025
1    red    2.380
2    white    5.560
```

## 3 星巴克零售店铺数据

现在我们有一组关于全球星巴克店铺的统计数据，如果我想知道美国的星巴克数量和中国的哪个多，或者我想知道中国每个省份星巴克的数量的情况，那么应该怎么办？

> 数据来源：https://www.kaggle.com/starbucks/store-locations/data

![星巴克数据](../images/星巴克数据.png)

### 3.1 数据获取

从文件中读取星巴克店铺数据

```python
# 导入星巴克店的数据
starbucks = pd.read_csv("./data/starbucks/directory.csv")
```

### 3.2 进行分组聚合

```python
# 按照国家分组，求出每个国家的星巴克零售店数量
count = starbucks.groupby(['Country']).count()
```

**画图显示结果**

```python
count['Brand'].plot(kind='bar', figsize=(20, 8))
plt.show()
```

![星巴克数量画图](../images/星巴克数量画图.png)

假设我们加入省市一起进行分组

```python
# 设置多个索引，set_index()
starbucks.groupby(['Country', 'State/Province']).count()
```

![国家省市分组结果](../images/国家省市分组结果.png)

**仔细观察这个结构，与我们前面讲的哪个结构类似？？**

与前面的MultiIndex结构类似

## 4 小结

- groupby进行数据的分组【知道】
  - pandas中，抛开聚合谈分组，无意义

# 十二、 案例

## 学习目标

- 目标
  - 无

------

## 1 需求

现在我们有一组从2006年到2016年1000部最流行的电影数据

数据来源：https://www.kaggle.com/damianpanek/sunday-eda/data

- 问题1：我们想知道这些电影数据中评分的平均分，导演的人数等信息，我们应该怎么获取？
- 问题2：对于这一组电影数据，如果我们想rating，runtime的分布情况，应该如何呈现数据？
- 问题3：对于这一组电影数据，如果我们希望统计电影分类(genre)的情况，应该如何处理数据？

## 2 实现

首先获取导入包，获取数据

```
%matplotlib inline
import pandas  as pd 
import numpy as np
from matplotlib import pyplot as plt
#文件的路径
path = "./data/IMDB-Movie-Data.csv"
#读取文件
df = pd.read_csv(path)
```

### 2.1 问题一：

**我们想知道这些电影数据中评分的平均分，导演的人数等信息，我们应该怎么获取？**

- 得出评分的平均分

使用mean函数

```python
df["Rating"].mean()
```

- 得出导演人数信息

求出唯一值，然后进行形状获取

```python
## 导演的人数
# df["Director"].unique().shape[0]
np.unique(df["Director"]).shape[0]

644
```

### 2.2 问题二：

**对于这一组电影数据，如果我们想Rating，Runtime (Minutes)的分布情况，应该如何呈现数据？**

- 直接呈现，以直方图的形式

选择分数列数据，进行plot

```python
df["Rating"].plot(kind='hist',figsize=(20,8))
```

![img](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctzl9ks1j21ki0madgf.jpg)

- Rating进行分布展示

进行绘制直方图

```python
plt.figure(figsize=(20,8),dpi=80)
plt.hist(df["Rating"].values,bins=20)
plt.show()
```

修改刻度的间隔

```python
# 求出最大最小值
max_ = df["Rating"].max()
min_ = df["Rating"].min()

# 生成刻度列表
t1 = np.linspace(min_,max_,num=21)

# [ 1.9    2.255  2.61   2.965  3.32   3.675  4.03   4.385  4.74   5.095  5.45   5.805  6.16   6.515  6.87   7.225  7.58   7.935  8.29   8.645  9.   ]

# 修改刻度
plt.xticks(t1)

# 添加网格
plt.grid()
```

![img](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctzlp13wj21k20majtc.jpg)

- Runtime (Minutes)进行分布展示

进行绘制直方图

```python
plt.figure(figsize=(20,8),dpi=80)
plt.hist(df["Runtime (Minutes)"].values,bins=20)
plt.show()
```

修改间隔

```python
# 求出最大最小值
max_ = df["Runtime (Minutes)"].max()
min_ = df["Runtime (Minutes)"].min()

# # 生成刻度列表
t1 = np.linspace(min_,max_,num=21)

# 修改刻度
plt.xticks(np.linspace(min_,max_,num=21))

# 添加网格
plt.grid()
```

![img](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctz8mzg5j21k00mggnf.jpg)

### 2.3 问题三：

**对于这一组电影数据，如果我们希望统计电影分类(genre)的情况，应该如何处理数据？**

- 思路分析
  - 思路
    - 1、创建一个全为0的dataframe，列索引置为电影的分类，temp_df
    - 2、遍历每一部电影，temp_df中把分类出现的列的值置为1
    - 3、求和
- 1、创建一个全为0的dataframe，列索引置为电影的分类，temp_df

```python
# 进行字符串分割
temp_list = [i.split(",") for i in df["Genre"]]
# 获取电影的分类
genre_list = np.unique([i for j in temp_list for i in j]) 

# 增加新的列
temp_df = pd.DataFrame(np.zeros([df.shape[0],genre_list.shape[0]]),columns=genre_list)
```

- 2、遍历每一部电影，temp_df中把分类出现的列的值置为1

```python
for i in range(1000):
    #temp_list[i] ['Action','Adventure','Animation']
    temp_df.ix[i,temp_list[i]]=1
print(temp_df.sum().sort_values())
```

- 3、求和,绘图

```python
temp_df.sum().sort_values(ascending=False).plot(kind="bar",figsize=(20,8),fontsize=20,colormap="cool")


Musical        5.0
Western        7.0
War           13.0
Music         16.0
Sport         18.0
History       29.0
Animation     49.0
Family        51.0
Biography     81.0
Fantasy      101.0
Mystery      106.0
Horror       119.0
Sci-Fi       120.0
Romance      141.0
Crime        150.0
Thriller     195.0
Adventure    259.0
Comedy       279.0
Action       303.0
Drama        513.0
dtype: float64
```

![img](https://tva1.sinaimg.cn/large/e6c9d24ely1h1ctzhidr8j21k20q475y.jpg)