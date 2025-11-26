"""
OpenCV学習: 動画の各フレームにフレーム番号を書き込む
"""
import cv2
import os


def add_frame_numbers_to_video(input_path, output_path, font_scale=2, thickness=3, color=(0, 255, 0)):
    """
    動画の各フレームにフレーム番号を書き込んで新しい動画を作成する

    Args:
        input_path: 入力動画ファイルのパス
        output_path: 出力動画ファイルのパス
        font_scale: フォントサイズ（デフォルト: 2）
        thickness: 文字の太さ（デフォルト: 3）
        color: 文字の色 (B, G, R)（デフォルト: 緑）
    """
    # 動画を開く
    cap = cv2.VideoCapture(input_path)

    if not cap.isOpened():
        print(f"エラー: 動画ファイルを開けません: {input_path}")
        return False

    # 動画の情報を取得
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    print(f"動画情報:")
    print(f"  総フレーム数: {total_frames}")
    print(f"  FPS: {fps}")
    print(f"  解像度: {width}x{height}")


    # 動画ライターを作成
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    if not out.isOpened():
        print(f"エラー: 出力ファイルを作成できません: {output_path}")
        cap.release()
        return False

    print(f"\n処理中...")
    frame_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # フレーム番号のテキストを追加
        text = f"Frame: {frame_count}"

        # テキストのサイズを取得して背景を描画
        (text_width, text_height), baseline = cv2.getTextSize(
            text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness
        )

        # 左上に配置（背景付き）
        x, y = 10, 50

        # 背景の矩形を描画（黒い半透明背景）
        overlay = frame.copy()
        cv2.rectangle(
            overlay,
            (x - 5, y - text_height - 5),
            (x + text_width + 5, y + baseline + 5),
            (0, 0, 0),
            -1
        )
        # 半透明にする
        cv2.addWeighted(overlay, 0.6, frame, 0.4, 0, frame)

        # テキストを描画
        cv2.putText(
            frame,
            text,
            (x, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            font_scale,
            color,
            thickness,
            cv2.LINE_AA
        )

        # フレームを書き込む
        out.write(frame)

        frame_count += 1

        # 進捗表示
        if frame_count % 30 == 0:
            progress = (frame_count / total_frames) * 100
            print(f"  進捗: {frame_count}/{total_frames} フレーム ({progress:.1f}%)")

    # リソースを解放
    cap.release()
    out.release()

    print(f"\n完了: {output_path} を作成しました")
    print(f"総フレーム数: {frame_count}")
    return True


if __name__ == "__main__":
    # 使用例
    input_video = "src/opencv/sample01.mp4"
    output_video = "src/opencv/outputs/sample01_with_frame_numbers.mp4"

    print("=== フレーム番号付き動画を作成 ===\n")
    add_frame_numbers_to_video(
        input_video,
        output_video,
        font_scale=2,      # フォントサイズ
        thickness=3,       # 文字の太さ
        color=(0, 255, 0)  # 緑色 (B, G, R)
    )

    print(f"\n作成された動画を確認してください: {output_video}")
