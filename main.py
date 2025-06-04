"""
数字画像認識AI

学習方法：教師あり学習（正解データあり）

以下のサイトの５ステップを参考に実装
https://last-data.co.jp/media/machine-learning-procedure/
"""
import mod # フォルダー名／ファイル名を指定してインポートすることができる


def main():
    """
    エントリーポイント
    """
    #STEP1：学習データの読み込み
    samples, answers = mod.data.load()

    #STEP2：データの前処理
    samples_adjust = mod.data.adjust(samples)

    #STEP3：データの分割
    train_samples, test_samples, train_answers, test_answers = mod.data.split(samples_adjust, answers)

    #STEP4：モデルの学習
    clf = mod.model.train(train_samples, train_answers)

    #STEP5：モデルの評価
    score = mod.model.test(clf, test_samples, test_answers)

    print("正解率: ", score)


if __name__ == "__main__": # こちらのファイルを指定して、実行した場合
    main()