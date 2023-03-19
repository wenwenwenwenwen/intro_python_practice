## 用if來選擇
1. 1-10中選擇一個數字指派給變數`secret`及`guess`(可重複)，使用`if..elif..else`
    - guess < secret時印出`too low`
    - guess > secret時印出`too high`
    - guess = secret時印出`just right`
    ```python
    >>> secret = 4
    >>> guess = 6
    >>> if guess < secret:
    ...     print("too low")
    ... elif guess > secret:
    ...     print("too high")
    ... else:
    ...     print("just right")
    ...
    too high
    >>>
    ```

2. 將True或False指派給small跟green。寫出if/else印出下列哪種東西符合這些選擇
    - cherry: small and not green
    - pea: small and green
    - watermelon: not small and green
    - pumpkin: not small and not green
    ```python
    >>> small = True
    >>> green = False
    >>> if small and green:
    ...     print("pea")
    ... elif small and not green:
    ...     print("cherry")
    ... elif not small and green:
    ...     print("pumpkin")
    ... else:
    ...     print("watermelon")
    ...
    cherry
    >>>
    ```