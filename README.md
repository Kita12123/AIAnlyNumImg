# AIAnlyNumImg
数値画像認識AI 参考: https://www.jcsc.co.jp/news/p883/

# 環境構築

1. Pythonインストール

    ### Macの場合
    参考: https://zenn.dev/kenghaya/articles/9f07914156fab5

    brew install pyenv
    pyenv install -list
    pyenv install 3.12.10
    pyenv local 3.12.10
    source .zshrc

    ### Windowsの場合

    公式サイトからダウンロード
    https://www.python.org/


2. 仮想環境構築

    python -m venv .venv

3. パッケージインストール

    ### Macの場合
    .venv\Scripts\activate
    pip install -r requirements.txt

    ### Windowsの場合
    ※PowerShellでなく、Command Promptで実行すること
    .venv\Scripts\activate.bat
    pip install -r requirements.txt

3. アプリ実行

    main.pyを開く
    ※vscodeの右下が、.venvの環境を読み込んでいること
    F5（デバック実行）または右上の▷ボタン押下