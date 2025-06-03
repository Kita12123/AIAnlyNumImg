"""
モデル制御モジュール
"""
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split


def train(samples: np.ndarray, answers: np.ndarray) -> MLPClassifier:
    """機械学習モデル作成

    Args:
        samples (np.ndarray): 学習用サンプルデータ
        answers (np.ndarray): 学習用正解データ
    """
    # ニューラルネットワークによるクラス分類を行う
    # MLPClassifierクラスを使って、隠れ層１（ノード数：100）で
    # ニューラルネットワークを構築する
    # 今回使用するマシンのスペックの考慮や少しでも変化が分かりやすくするために
    # 学習回数の最大値(max_iter)を10としている
    clf = MLPClassifier(hidden_layer_sizes=(100,), verbose=True, max_iter=10, random_state=43)

    # 学習用データを使って学習させる
    clf.fit(samples, answers)

    return clf


def test(clf: MLPClassifier, samples: np.ndarray, answers: np.ndarray) -> float:
    """モデル評価

    Args:
        clf (MLPClassifier): 機械学習モデル
        samples (np.ndarray): サンプルデータ
        answers (np.ndarray): 正解データ

    Returns:
        float: 正解率
    """
    # テストデータを使って数字画像認識を行う
    #predict = clf.predict(samples)

    # 正解率出力
    score = clf.score(samples, answers)

    return score