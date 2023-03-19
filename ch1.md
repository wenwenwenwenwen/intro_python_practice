## 初嘗Py
1. 安裝Python(Miniconda)
    ```bash
    $sudo apt update && upgrade
    $sudo apt install curl # if have no curl
    $curl Miniconda3-lastest-Linux-x86_64.sh
    $bash Miniconda3-latest-Linux-x86_64.sh
    # if don't want to use conda env as default,
    # then type `no` when asking about whether to initialize conda
    ```
    - if reply `yes` when asking about whether to initialize conda
        ```bash
        $. .bashrc # source .bashrc
        ```
    - if reply `no`, every time when need to use conda env
        ```bash
        $. <conda dir path>/bin/activate # source <conda activate path>
        ```
    
    Create conda environment
    ```
    conda create --name <env name> python=<python version>
    ```

2. 啟動Python3互動式解譯器
    ```bash
    $python3
    Python 3.9.16 (main, Mar  8 2023, 14:00:05)
    [GCC 11.2.0] :: Anaconda, Inc. on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```

#### 在Python互動式解譯器中
3. 輸入`8 * 9`
    ```python
    >>>8 * 9
    72
    >>>
    ```

4. 輸入`47`
    ```python
    >>>47
    47
    >>>
    ```

5. 輸入`print(47)`
    ```python
    >>>print(47)
    47
    >>>
    ```