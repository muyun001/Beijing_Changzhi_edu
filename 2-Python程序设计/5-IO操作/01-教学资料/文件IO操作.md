# 文件IO操作

## 文件读写步骤：

1. 打开文件，创建文件对象

   ```python
   # 常用的文件读写
   f = open(文件路径, 访问模式, 编码格式)
   ```

2. 对文件进行读写操作

   ```python
   f.read()
   f.write()
   ```

​	读写模式：

| 模式 | 描述                                                         |
| :--: | ------------------------------------------------------------ |
|  r   | 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。 |
|  rb  | Read byte以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。 |
|  r+  | 打开一个文件用于读写。文件指针将会放在文件的开头。           |
| rb+  | 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。 |
|  w   | 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
|  wb  | 以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
|  w+  | 打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| wb+  | 以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
|  a   | 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
|  ab  | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
|  a+  | 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。 |
| ab+  | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。 |

3. 关闭文件

```python
f.close()
```

## 1. 打开文件，创建文件对象

```python
file_path = ""
file = open(file_path, "r")
# 此时可以查看一下指针的位置
print("指针位置1:", file.tell())
```

## 2. 文件读取

```python
f = open(file_path, "r")
		- r.readable()：
        - 判断文件是否可读，返回bool类型  
	  
    - f.read():
        - 一次性读取文件的所有内容，返回字符串
        - 刚开始时，指针在文件开头
        - 读取内容之后，指针在文件结尾，所以再次读取文件时，读到的内容为空
        - f.read(n): 读取前n个字符， 回车符（\n）也算一个字符

    - f.readline()：
        - 一次读取文件的一行内容，返回字符串（一般用于读取大文件）
        - 刚开始时，指针在文件开头
        - 读取内容之后，指针在下一行的开头，所以再次读取文件时，读到新一行的内容
        - f.readline(n):读取这一行的前n个字符，回车符（\n）也算一个字符
        - 一般使用while循环读取,当读取内容为空时退出

    - r.readlines()：
        - 一次读取文件的所有行，返回列表（一般用于读取小文件）
        - 刚开始时，指针在文件开头
        - 读取内容之后，指针在文件末尾
```

### 2.1 `file.readable()` 

```python
# 判断文件是否可读,返回bool类型
file_path = ""
file = open(file_path, "r")
print(file.readable())
file.close()
```

### 2.2 `file.read()`

```python
'''
- 一次性读取文件的所有内容，返回字符串
- 刚开始时，指针在文件开头
- 读取内容之后，指针在文件结尾，所以再次读取文件时，读到的内容为空
- f.read(n): 读取前n个字符， 回车符（\n）也算一个字符
'''
file_path = ""
file = open(file_path, "r")
text = file.read()
print(type(text))  # str类型
print("text:", text)  # 一次性读取文件中的所有内容， 返回一个字符串
print(len(text))
print("指针位置2:", file.tell())
text2 = file.read()
print("text2:", text2)  # 读取到的内容为空

text2 = file.read(5)
print(len(text2))
print(text2)  # baidu

text3 = file.read(5)
print(len(text3))
print(text3)
file.close()
```

### 2.3 `file.readline()`

```python
'''
- 一次读取文件的一行内容，返回字符串（一般用于读取大文件）
- 刚开始时，指针在文件开头
- 读取内容之后，指针在下一行的开头，所以再次读取文件时，读到新一行的内容
- f.readline(n):读取这一行的前n个字符，回车符（\n）也算一个字符
- 一般使用while循环读取,当读取内容为空时退出
'''
# files.readline()
file_path = ""
file = open(file_path, "r")
print("指针位置1:", file.tell())

text_line_1 = file.readline()
print(text_line_1)
print("指针位置2：", file.tell())

text_line_2 = file.readline()
print(text_line_2)
print("指针位置3：", file.tell())

text_line_3 = file.readline(4)  # 读取这一行的前4个字符
print(text_line_3)
print("指针位置3：", file.tell())

while True:
    text = file.readline()
    if text.strip() == "":
        break
    print(text)  # 每次读取一行， 返回一个字符串
file.close()
```



### 2.4 `file.readlines()`

```python
"""
- 一次读取文件的所有行，返回列表（一般用于读取小文件）
- 刚开始时，指针在文件开头
- 读取内容之后，指针在文件末尾
"""
file_path = ""
file = open(file_path, "r")
text = file.readlines()
print(text)
file.close()
```

## 3. 文件写入

```python
文件写入
f = open(file_path, "w")
		- f.writeable(): 
        - 判断文件是否可写，返回bool类型  

  	- f.write()：
        - 刚开始时，指针在文件开头
        - 写入的数据是字符串类型
        - 写入数据后，指针在文件结尾
        - 写入数据会把之前内容覆盖掉

    - f.writelines()
        - 刚开始时，指针在文件开头
        - 写入的数据是列表类型
        - 写入数据后，指针在文件末尾
        - 写入数据会把之前内容覆盖掉
```

### 3.1 `file.writeable()`

```python
"""
判断文件是否可写，返回bool类型  
"""
file_path = ""
file = open(file_path, "w")
print(f.writeable())
file.close()
```

### 3.2 `file.write()`

```python
"""
- 刚开始时，指针在文件开头
- 写入的数据是字符串类型
- 写入数据后，指针在文件结尾
- 写入数据会把之前内容覆盖掉
"""
file_path = ""
file = open(file_path, "w")

print("指针位置1：", file.tell())

file.write("s")

print("指针位置2：", file.tell())

file.write("sougou")

print("指针位置3:", file.tell())

file.close()
```

### 3.3 `file.writelines()`

```python
"""
- 刚开始时，指针在文件开头
- 写入的数据是列表类型
- 写入数据后，指针在文件末尾
- 写入数据会把之前内容覆盖掉
"""
file_path = ""
file = open(file_path, "w")
print("指针位置1:", file.tell())

file.writelines(["sougou\n", "sougou\n"])

print("指针位置2:", file.tell())

file.writelines(["baidu\n", "baidu\n"])

file.close()
```

## 4. 可读可写

```
可读可写
open(file_path, "r+")
    - 刚开始时指针在文件的开头
    - file.read()之后，指针在文件末尾
    - file.write()时，从末尾开始写，写入完成后，指针在文件末尾

open(file_path, "w+")
    - 在刚开始时，会格式化文件，把文件清空，所以读取文件时，读取内容为空
    - 在刚开始时，指针在文件开头
    - file.write()时，从文件开头开始写入,写入完成后，指针在文件末尾
    - 可以使用file.seek(0) 将指针移到文件开头
    - 使用file.seek(0)之后，可以正常file.read()文件

open(file_path, "a+")   append()追加
    - 在刚开始时，指针在文件末尾，所以直接读取文件，读取内容为空
    - file.write()时，从文件末尾写入数据，不会覆盖掉之前的内容。写入数据之后，指针在文件末尾

```

### 4.1 `open(file_path, "r+")`

```python
"""
- 刚开始时指针在文件的开头
- files.read()之后，指针在文件末尾
- files.write()时，从末尾开始写，写入完成后，指针在文件末尾
"""
file_path = ""
file = open(file_path, "r+")
print("指针位置1：", file.tell())

text = file.read()
print("text:", text)
print("指针位置2：", file.tell())

text2 = file.read()
print("text2:", text2)

file.write("sougou")
print("指针位置3：", file.tell())

file.close()
```



### 4.2 `open(file_path, "w+")`

```python
"""
- 在刚开始时，会格式化文件，把文件清空，所以读取文件时，读取内容为空
- 在刚开始时，指针在文件开头
- files.write()时，从文件开头开始写入,写入完成后，指针在文件末尾
- 可以使用file.seek(0) 将指针移到文件开头
- 使用file.seek(0)之后，可以正常file.read()文件
"""
file_path = ""
file = open(file_path, "w+")
print("指针位置1：", file.tell())

# text = files.read()
# print("text:", text)

file.write("baidu")

print("指针位置2：", file.tell())

# 改变指针位置
file.seek(0)
print("files.seek(0)之后,指针位置：", file.tell())

text2 = file.read()
print("text2:", text2)

print("指针位置3：", file.tell())

file.close()
```



### 4.3 `open(file_path, "a+")`

```python
"""
- 在刚开始时，指针在文件末尾，所以直接读取文件，读取内容为空
- files.write()时，从文件末尾写入数据，不会覆盖掉之前的内容。写入数据之后，指针在文件末尾
"""
file_path = ""
file = open(file_path, "a+")
print("指针位置1：", file.tell())
text = file.read()
print("text:", text)
print("指针位置2：", file.tell())
file.write("sougou")
print("指针位置3：", file.tell())

file.close()
```

## 5. `with open`进阶写法

```python
"""
无需file.close()
"""

# 读
file_path = ""
with open(file_path, "r") as file:
    file.read()

# 写
file_path = ""
with open(file_path, "w") as file:
    file.write()

# 追加
file_path = ""
with open(file_path, "a") as file:
    file.write()

# 无论读写，都可以设置编码格式
file_path = ""
with open(file_path, "r", encoding="utf-8") as file:
    file.read()

```

```python
file.truncate(0)  # 清空文件的内容
file.flush()  # 直接推送数据到文件
```

