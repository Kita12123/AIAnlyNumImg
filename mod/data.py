"""
データ制御モジュール
"""
# パッケージ読み込み
from sklearn.datasets import fetch_openml
import numpy as np
from sklearn.model_selection import train_test_split

# 関数定義
def load() -> tuple[np.ndarray]: # 戻り値のタイプ定義（なくてもいい）
    """データ読み込み
    MNISTデータを取得してnumpyの配列型に変換

    Returns:
        list: リスト（サンプルデータ、正解データ）
    """
    # MNISTデータ読み込み（サンプルデータ：数値手書き画像データ、正解データ：数値ラベルデータ）
    samples, answers = fetch_openml('mnist_784', version=1, data_home="sklearn_MNIST_data", return_X_y=True)

    # 戻り値（扱いやすくするためにnumpyに変換する）
    return np.array(samples), np.array(answers)


def adjust(samples: np.ndarray) -> np.ndarray:
    """サンプルデータ調整
    モデル学習の制御を上げるために、データを調整する

    Args:
        sample (np.ndarray): サンプルデータ

    Returns:
        np.ndarray: 調整後サンプルデータ
    """
    # 学習効率を上げるため、値（色）の範囲を0～255から0～1となるように小数で四捨五入する
    return np.round(samples / 255).astype(int)


def split(samples: np.ndarray, answers: np.ndarray) -> list[np.ndarray]:
    """データ分割
    学習用と評価用に分割する

    Args:
        samples (np.ndarray): サンプルデータ
        answers (np.ndarray): 正解データ

    Returns:
        list[np.ndarray]: 分割後データ（学習用サンプルデータ、評価用サンプルデータ、学習用正解データ、評価用正解データ）
    """
    # 学習データと評価データに分割する
    data = train_test_split(
                samples, answers,
                train_size=0.75, # 学習用データ割合
                test_size=0.25, # 評価用データ割合
                shuffle=True, # データ分割する前にシャッフルする
                random_state=43 # シャッフル制御（値が同じ場合、何度しても同じシャッフル結果になる）
            )
    return (
        data[0], # 学習用サンプルデータ
        data[1], # 評価用サンプルデータ
        data[2], # 学習用正解データ
        data[3]  # 評価用正解データ
    )