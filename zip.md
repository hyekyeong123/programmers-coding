파이썬 에서는 zip이라는 내장함수가 있다. zip() 은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.

아래와 같이 Number 와 Name이 있다고 한다. 이때 이 두개의 List를 하나의 연관된 리스트로 만들어야 한다고 하자. 그럼 아래와 같이 간단하게 만들수 있다.

```python
Number = [1,2,3,4]
Name = ['hong','gil','dong','nim']
Number_Name = list(zip(Number,name))
print(Number_Name)
# 결과 : [(1 ,'hong'), (2 ,'gil'), (3 ,'dong'), (4 ,'nim')]
```

이번에는 하나의 연관된 List가 아닌 하나의 딕셔너리로 만든다고 하자.

```python
Number = [1,2,3,4]
Name = ['hong','gil','dong','nim']
dic = {}
for i in range(len(Number)) :
    dic[Number[i]] = Name[i]print(dic)
# 결과 : {1 : 'hong' , 2 : 'gil' , 3 : 'dong' , 4 : 'nim'}
```

위와같이 만드는 방법이 일반적으로 만드는 방법이다. 이제 zip을 사용해 만들어 보자

```python
Number = [1,2,3,4]
Name = ['hong','gil','dong','nim']
dic = {}
for number , name in zip(Number,Name):
    dic[number] = nameprint(dic)
# 결과 : {1 : 'hong' , 2 : 'gil' , 3 : 'dong' , 4 : 'nim'}
```
