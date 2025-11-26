<!-- @format -->

# OpenCV 学習用スクリプト

## セットアップ

```bash
pip install opencv-python
```

## スクリプト一覧

### 1. frame_capture.py

動画から特定のフレームをキャプチャする基本スクリプト

```bash
python src/opencv/frame_capture.py
```

- 指定したフレーム番号の画像を保存
- 複数フレームを一度にキャプチャ可能
- `cap.set(cv2.CAP_PROP_POS_FRAMES, フレーム番号)` で任意のフレームにジャンプ

### 2. add_frame_numbers.py

動画の各フレームにフレーム番号を書き込んだ新しい動画を作成。

```bash
python src/opencv/add_frame_numbers.py
```

- 各フレームの左上に「Frame: 0」「Frame: 1」...と表示
- キャプチャしたフレームが正しいか確認するのに便利

### 3. capture_channel.py

4 分割映像から特定のチャンネルをキャプチャ。

```bash
python src/opencv/capture_channel.py
```

- 270 度回転して 4 つのチャンネル（Ch1〜Ch4）に分割
- 特定のフレーム・特定のチャンネルを指定してキャプチャ
- リサイズオプション付き

```python
# 使用例
capture_channel_from_frame(
    "src/opencv/sample01.mp4",
    frame_number=30,
    channel=1,  # 1=左上, 2=右上, 3=左下, 4=右下
    resize_channel=(480, 854)  # オプション: リサイズ
)
```
