# Python Basics


## Points to be carefull / Tips

#### Truthy and Falsy

In python 0 is evaluate as Falsy
Pay attention on the condition 

`if (value % 2):`
if this evaluates to 0, will be considered as False
so to make it True we can do
`if not(value % 2)` => True
`or (value % 2 == 0)` => True

```python
x = input("数字を入れて下さい \n ==>")
y = input("数字を入れて下さい \n ==>")

kaitou = int(x) + int(y)

# if not(kaitou % 3) and not(kaitou % 2):
#           0 => False      0 => False
#   not False => True        not False => True


# because is evaluating the result of kaitou % 3, if it is 0 
# than compare it to 0 
  
if (kaitou % 3 == 0) and (kaitou % 2 == 0):
    print(kaitou)
else:
    print("規格外")
```

#### Context Managers

usually to get data from a file, we use the file.open() and the we have to 
remember to close it with file.closer()

A better way is to use context Managers
```python
with open('file.txt', 'r') as f:
file_contents = f.read()
```

#### Get the index in loops with enumarate
Instead of creating a variable to keep count of the index value
We can use the enumarate method
```python
names = ['rene', 'takahashi', 'elo', 'takada']
for index, name in enumarate(names, start=1)
    print(index, name)
```

#### Get item from list allowing negative index
```python
pos = int(input("取り出す位置：　\n ==>"))
colors = ["blue", "red", "green", "yellow"]
length = len(colors)
```
> accepts negative position, length is 4 and negative position is also up to -4
> so it uses <= 
> length is 4 but starts from 0, so use onl < 

```python
if -length <= pos < length:
    item = colors[pos]
    print(item)
else:
    print("エラーになりました。")
```

Same idea as before but using try and except
```python
pos = int(input("取り出す位置：　\n ==>"))
colors = ["blue", "red", "green", "yellow"]
try:
    item = colors[pos]
    print(item)
except IndexError:
    print("Index Error")
except Exception as error:
    print(error)
```

## Python list methods
### .append(value) 
=> append to the end of list

### .insert(position, value) 
=> insert to specific position

### .pop(position) 
=> remove element from specific position  (if position is not provided the last item will be removed)

> Also used to move data to another variable
```python
fruits= ["apple", "orange", "banana", "peach"]
dessert = fruits.pop()
print(dessert, "\n", fruits)
```

### .remove(target) 
=> removes the first instance of the value
```python
colors = ['blue', 'red', 'yellow', 'red', 'green']
print('削除前', colors)
target = 'yellow'

#removes only the first instance of the target value
if target in colors :
    colors.remove(target)
print("削除後", colors)

# Remove all instances of the target value 

while target in colors:
    colors.remove(target)
print("削除後", colors)
```

### string.split()
> without param will separete each word
> with a param, will give a list with the string as value
```python
message = "may the force be with you !"
words = message.split()
print(words)
```
> ",space" will separate and remove the spaces
```python
fruits = "apple, orange, banana, mango"
fruit_list = fruits.split(", ")
print(fruit_list)
```
We can also use delimiter
```python
result = "23,45,56,87,90,123,231,256,321"
result_list = result.split(",", 3)
print(result_list)
```
And using the splice syntax [:3]
```python
top3 = result.split(",", 3)[:3]
print(top3)
```

### .join()
SEPARATOR.join(list)
```python
members = ["Tom", "Jerry", "Spike"]
name = " and ".join(members)
print(name)

```
