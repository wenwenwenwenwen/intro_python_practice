## 函式
1. 定義函式good()，用它回傳list ['Harry', 'Ron', 'Hermione']
    ```python
    def good():
        return ["Harry", "Ron", "Herimone"]
    ```

2. 定義get_odd()的產生器函式，用它回傳range(10)的奇數。使用for迴圈印出第三個回傳值
    ```python
    >>> def get_odd(first=0, last=10, step=1):
    ...     number = first
    ...     while number < last:
    ...         if number % 2 != 0:
    ...             yield number
    ...         number += step
    ...
    >>> counts = 0
    >>> for i in get_odd():
    ...     if counts == 2:
    ...         print(i)
    ...     counts += 1
    ... 
    5
    >>>
    ```

3. 定義一個test裝飾器，用它在函式被呼叫時印出'start'，結束時印出'end'
    ```python
    >>> def test(func):
    ...     def new_func(*args, **kwargs):
    ...         print('start')
    ...         func(*args, **kwargs)
    ...         print('end')
    ...     return new_func
    ... 
    >>> @test
    ... def echo(value):
    ...     print(value)
    ... 
    >>> echo('echo')
    start
    echo
    end
    >>>
    ```

4. 定義OopsException的例外，發出這個例外看看會發生什麼事，接著寫一段程式捕捉例外，並印出'Caught an oops'
    ```python
    >>> class OopsException(Exception):
    ...     pass
    ... 
    >>> raise OopsException
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    __main__.OopsException
    >>> try:
    ...     raise OopsException
    ... except OopsException as e:
    ...     print('Caught an oops')
    ... 
    Caught an oops
    >>>
    ```