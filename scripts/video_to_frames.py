import cv2
import os
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python src/extract_frames.py <input_video_path> <output_frames_dir> <frame_interval>")
        sys.exit(1)

    input_video_path = sys.argv[1]
    output_frames_dir = sys.argv[2]
    frame_interval = int(sys.argv[3]) # Extract every Nth frame

    if not os.path.exists(output_frames_dir):
        os.makedirs(output_frames_dir)

    print(f"Opening video: {input_video_path}")
    vidcap = cv2.VideoCapture(input_video_path)
    if not vidcap.isOpened():
        print(f"Error: Could not open video file {input_video_path}")
        sys.exit(1)

    count = 0
    frame_idx = 0
    success, image = vidcap.read()

    while success:
        if frame_idx % frame_interval == 0:
            frame_filename = os.path.join(output_frames_dir, f"frame_{count:06d}.jpg")
            cv2.imwrite(frame_filename, image)     # save frame as JPEG file
            print(f"Extracted frame {count:06d} (video frame {frame_idx})")
            count += 1
        success, image = vidcap.read()
        frame_idx += 1

    vidcap.release()
    print(f"Finished extracting {count} frames to {output_frames_dir}")
