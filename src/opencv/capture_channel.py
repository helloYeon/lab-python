"""
OpenCV学習: 4分割映像から特定のチャンネルをキャプチャする
"""
import cv2
import os
from typing import List
import numpy as np


def rotate_and_split_into_channels(
    frame: np.ndarray, IMAGE_WIDTH: int, IMAGE_HEIGHT: int
) -> List[np.ndarray]:
    """
    フレームを回転して4つのチャンネルに分割する

    参考:
        https://github.com/optim-mdi/object_detector/blob/63fa3cf03d8511d86b98f56a04a5b4b12406ea7b/object_detector.py#L320

    Args:
        frame: 入力フレーム
        IMAGE_WIDTH: 元の動画の幅（使用していない）
        IMAGE_HEIGHT: 元の動画の高さ（使用していない）

    Returns:
        [ch1, ch2, ch3, ch4] のリスト
        ch1: 左上, ch2: 右上, ch3: 左下, ch4: 右下
    """
    # 回転（cv2.rotate の 2 は 270度回転 = 90度反時計回り）
    # 1280x720 → 270度回転 → 720x1280
    img = cv2.resize(frame, (IMAGE_WIDTH, IMAGE_HEIGHT))
    img = cv2.rotate(img, 2)

    # 回転後のサイズで分割（幅と高さが入れ替わる）
    # 720x1280 を 4分割 → 各チャンネルは 360x640
    rotated_height, rotated_width = img.shape[:2]
    w_half = rotated_width // 2
    h_half = rotated_height // 2

    # 4つのチャンネルに分割
    # 270度回転後の位置から元のチャンネルを取得
    ch1 = img[h_half:rotated_height, 0:w_half]           # 回転後の左下（元のCh1）
    ch2 = img[0:h_half, 0:w_half]                        # 回転後の左上（元のCh2）
    ch3 = img[h_half:rotated_height, w_half:rotated_width] # 回転後の右下（元のCh3）
    ch4 = img[0:h_half, w_half:rotated_width]            # 回転後の右上（元のCh4）

    return [ch1, ch2, ch3, ch4]


def capture_channel_from_frame(
    video_path,
    frame_number,
    channel,
    output_path=None,
    IMAGE_WIDTH=None,
    IMAGE_HEIGHT=None
):
    """
    動画の特定フレームから特定チャンネルをキャプチャする

    Args:
        video_path: 動画ファイルのパス
        frame_number: キャプチャしたいフレーム番号（0から始まる）
        channel: チャンネル番号（1, 2, 3, 4）
        output_path: 保存先のファイルパス（Noneの場合は自動生成）
        IMAGE_WIDTH: リサイズ後の幅（Noneの場合は元の動画サイズを使用）
        IMAGE_HEIGHT: リサイズ後の高さ（Noneの場合は元の動画サイズを使用）
        rotate_channel: Trueの場合、チャンネル画像を90度時計回りに回転（縦長にする）

    Returns:
        成功した場合True、失敗した場合False
    """
    # チャンネル番号のチェック
    if channel not in [1, 2, 3, 4]:
        print(f"エラー: チャンネル番号は 1, 2, 3, 4 のいずれかを指定してください")
        return False

    # 動画ファイルを開く
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"エラー: 動画ファイルを開けません: {video_path}")
        return False

    # 動画の情報を取得
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # IMAGE_WIDTH/HEIGHT が指定されていない場合は元のサイズを使用
    if IMAGE_WIDTH is None:
        IMAGE_WIDTH = original_width
    if IMAGE_HEIGHT is None:
        IMAGE_HEIGHT = original_height

    print(f"動画情報:")
    print(f"  総フレーム数: {total_frames}")
    print(f"  FPS: {fps}")
    print(f"  元の解像度: {original_width}x{original_height}")
    print(f"  270度回転後: {original_height}x{original_width}")
    print(f"  各チャンネルの解像度: {original_height//2}x{original_width//2}")

    # フレーム番号が範囲内かチェック
    if frame_number >= total_frames or frame_number < 0:
        print(f"エラー: フレーム番号 {frame_number} は範囲外です（0-{total_frames-1}）")
        cap.release()
        return False

    # 特定のフレームにジャンプ
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

    # フレームを読み込む
    ret, frame = cap.read()

    if not ret:
        print(f"エラー: フレーム {frame_number} を読み込めませんでした")
        cap.release()
        return False

    # チャンネルに分割
    channels = rotate_and_split_into_channels(frame, IMAGE_WIDTH, IMAGE_HEIGHT)
    selected_channel = channels[channel - 1]  # channel は 1-4 なので -1 する

    # 出力パスが指定されていない場合は自動生成
    if output_path is None:
        output_path = f"src/opencv/output/frame_{frame_number:04d}_ch{channel}.jpg"

    # 出力ディレクトリを作成
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    # 画像を保存
    cv2.imwrite(output_path, selected_channel)

    # 保存した画像のサイズを取得して表示
    h, w = selected_channel.shape[:2]
    print(f"\nフレーム {frame_number} のチャンネル {channel} を保存しました: {output_path}")
    print(f"  保存した画像サイズ: {w}x{h}")

    # プレビュー表示（ESCキーで閉じる）
    cv2.imshow(f"Frame {frame_number} - Channel {channel}", selected_channel)

    print("ESCキーを押すとウィンドウが閉じます")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cap.release()
    return True


if __name__ == "__main__":
    video_path = "src/opencv/sample01_with_frame_numbers.mp4"

    # 使用例: 30フレーム目のCh1（左上）をキャプチャ（縦長にする）
    print("=== 特定フレーム・特定チャンネルのキャプチャ（縦長） ===")
    ch = 1
    capture_channel_from_frame(
        video_path,
        frame_number=30,
        channel=1,  # Ch1（左上）
        output_path=f"src/opencv/outputs/frame_ch{ch}.jpg",
    )
