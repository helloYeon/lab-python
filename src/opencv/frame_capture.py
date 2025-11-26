"""
OpenCV基本学習: 動画から特定のフレームをキャプチャする
"""
import cv2
import os


def capture_specific_frame(video_path, frame_number, output_path="captured_frame.jpg"):
    """
    動画から特定のフレームをキャプチャして保存する

    Args:
        video_path: 動画ファイルのパス
        frame_number: キャプチャしたいフレーム番号（0から始まる）
        output_path: 保存先のファイルパス
    """
    # 動画ファイルを開く
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"エラー: 動画ファイルを開けません: {video_path}")
        return False

    # 動画の情報を表示
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(f"動画情報:")
    print(f"  総フレーム数: {total_frames}")
    print(f"  FPS: {fps}")
    print(f"  解像度: {width}x{height}")

    # フレーム番号が範囲内かチェック
    if frame_number >= total_frames or frame_number < 0:
        print(f"エラー: フレーム番号 {frame_number} は範囲外です（0-{total_frames-1}）")
        cap.release()
        return False

    # 特定のフレームにジャンプ（これが重要！）
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

    # フレームを読み込む
    ret, frame = cap.read()

    if ret:
        # 出力ディレクトリを作成（必要な場合）
        output_dir = os.path.dirname(output_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        # フレームを保存
        cv2.imwrite(output_path, frame)
        print(f"フレーム {frame_number} を {output_path} に保存しました")

        # プレビュー表示（ESCキーで閉じる）
        cv2.imshow(f"Frame {frame_number}", frame)
        print("ESCキーを押すとウィンドウが閉じます")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        cap.release()
        return True
    else:
        print(f"エラー: フレーム {frame_number} を読み込めませんでした")
        cap.release()
        return False


def capture_multiple_frames(video_path, frame_numbers, output_dir="frames"):
    """
    動画から複数のフレームをキャプチャする

    Args:
        video_path: 動画ファイルのパス
        frame_numbers: キャプチャしたいフレーム番号のリスト
        output_dir: 保存先のディレクトリ
    """
    # 出力ディレクトリを作成
    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"エラー: 動画ファイルを開けません: {video_path}")
        return

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    for frame_num in frame_numbers:
        if frame_num >= total_frames or frame_num < 0:
            print(f"スキップ: フレーム {frame_num} は範囲外です")
            continue

        # 特定のフレームにジャンプ
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
        ret, frame = cap.read()

        if ret:
            output_path = os.path.join(output_dir, f"frame_{frame_num:04d}.jpg")
            cv2.imwrite(output_path, frame)
            print(f"フレーム {frame_num} を保存しました: {output_path}")
        else:
            print(f"エラー: フレーム {frame_num} を読み込めませんでした")

    cap.release()
    print(f"\n完了: {len(frame_numbers)} フレームを処理しました")


if __name__ == "__main__":
    # 使用例
    video_path = "src/opencv/sample01_with_frame_numbers.mp4"

    # 例1: 特定のフレーム（例: 30フレーム目）をキャプチャ
    print("=== 例1: 単一フレームのキャプチャ ===")
    capture_specific_frame(video_path, frame_number=30, output_path="src/opencv/outputs/frame_30.jpg")

    # 例2: 複数のフレームをキャプチャ
    print("\n=== 例2: 複数フレームのキャプチャ ===")
    frame_list = [0, 30, 60, 90, 120]  # 0, 30, 60, 90, 120フレーム目
    capture_multiple_frames(video_path, frame_list, output_dir="src/opencv/outputs/frames")
