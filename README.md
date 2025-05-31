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

2. 仮想環境構築

    python -m venv .venv →vscodeで作成した仮想環境を読み込むこと
    pip install -r requirements.txt

3. アプリ実行