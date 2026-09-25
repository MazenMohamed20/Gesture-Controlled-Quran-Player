import os
import cv2
import mediapipe as mp
import pygame

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# Project Paths
base_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

video_path = os.path.join(
    base_dir,
    "assets",
    "videos",
    "test.mp4"
)

model_path = os.path.join(
    base_dir,
    "assets",
    "hand_landmarker.task"
)

audio_path = os.path.join(
    base_dir,
    "assets",
    "audio",
    "001 الفاتحة.mp3"
)


print("Audio path:", audio_path)
print("Video path:", video_path)
print("Model path:", model_path)

# Open Video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    raise FileNotFoundError(
        f"Cannot open video: {video_path}"
    )

# Video FPS
fps = cap.get(cv2.CAP_PROP_FPS)

if fps <= 0:
    fps = 30.0

print("Original FPS:", fps)

# Playback Speed
SPEED = 6.0

BASE_SPEED = 1.0

# Number of source frames to skip
frame_skip = max(
    1,
    int(SPEED / BASE_SPEED)
)

# Very small delay for high-speed playback
delay = 1

print("Playback speed:", SPEED, "x")
print("Frame skip:", frame_skip)

# MediaPipe Hand Landmarker
base_options = python.BaseOptions(
    model_asset_path=model_path
)

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.VIDEO,
    num_hands=2,

    # KEEPING YOUR TRACKING SETTINGS
    min_hand_detection_confidence=0.65,
    min_hand_presence_confidence=0.65,
    min_tracking_confidence=0.70
)

detector = vision.HandLandmarker.create_from_options(
    options
)

# Window
window_name = "GestureQuran AI"

cv2.namedWindow(
    window_name,
    cv2.WINDOW_NORMAL
)

cv2.resizeWindow(
    window_name,
    1100,
    920
)

# Hand Connections
connections = [

    # Thumb
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 4),

    # Index
    (0, 5),
    (5, 6),
    (6, 7),
    (7, 8),

    # Middle
    (5, 9),
    (9, 10),
    (10, 11),
    (11, 12),

    # Ring
    (9, 13),
    (13, 14),
    (14, 15),
    (15, 16),

    # Pinky
    (13, 17),
    (17, 18),
    (18, 19),
    (19, 20),

    # Palm
    (0, 17)
]

# Tracking Style
LINE_THICKNESS = 14
POINT_RADIUS = 12

FONT_SCALE = 0.8
FONT_THICKNESS = 2

# Gesture Control State
is_playing = False

audio_started = False

gesture_action = "WAITING"

# Finger Detection
def is_finger_open(hand_landmarks, tip, pip):

    return (
        hand_landmarks[tip].y
        <
        hand_landmarks[pip].y
    )

# Open Hand Recognition
def is_open_palm(hand_landmarks):

    index_open = is_finger_open(
        hand_landmarks,
        8,
        6
    )

    middle_open = is_finger_open(
        hand_landmarks,
        12,
        10
    )

    ring_open = is_finger_open(
        hand_landmarks,
        16,
        14
    )

    pinky_open = is_finger_open(
        hand_landmarks,
        20,
        18
    )

    open_fingers = sum([
        index_open,
        middle_open,
        ring_open,
        pinky_open
    ])

    return open_fingers >= 4

# Closed Hand / Fist Recognition
def is_fist(hand_landmarks):

    index_closed = (
        hand_landmarks[8].y
        >
        hand_landmarks[6].y
    )

    middle_closed = (
        hand_landmarks[12].y
        >
        hand_landmarks[10].y
    )

    ring_closed = (
        hand_landmarks[16].y
        >
        hand_landmarks[14].y
    )

    pinky_closed = (
        hand_landmarks[20].y
        >
        hand_landmarks[18].y
    )

    closed_fingers = sum([
        index_closed,
        middle_closed,
        ring_closed,
        pinky_closed
    ])

    return closed_fingers >= 4

# Audio Player
pygame.mixer.init()

if not os.path.exists(audio_path):

    raise FileNotFoundError(
        f"Cannot find audio file: {audio_path}"
    )

pygame.mixer.music.load(
    audio_path
)

# Video Playback State
frame_timestamp_ms = 0

# IMPORTANT:
# frame_counter MUST be outside the while loop
frame_counter = 0

# Video Loop
while True:

    ret, frame = cap.read()

    if not ret:

        print("Video finished.")

        break


    # Count EVERY source frame

    frame_counter += 1


    # Update MediaPipe timestamp for EVERY source frame

    frame_timestamp_ms += int(
        1000 / fps
    )


    # Skip frames according to playback speed

    if frame_counter % frame_skip != 0:

        continue


    # Original Frame

    original_frame = frame.copy()

    height, width, _ = original_frame.shape


    # BGR → RGB

    rgb_frame = cv2.cvtColor(
        original_frame,
        cv2.COLOR_BGR2RGB
    )


    # MediaPipe Image

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb_frame
    )


    # Hand Detection

    result = detector.detect_for_video(
        mp_image,
        frame_timestamp_ms
    )


    # Default Gesture

    gesture = "NO HAND"


    # Draw Tracking

    if result.hand_landmarks:

        # Use first detected hand
        hand_landmarks = result.hand_landmarks[0]


        # Detect Gesture

        if is_open_palm(hand_landmarks):

            gesture = "OPEN HAND"

        elif is_fist(hand_landmarks):

            gesture = "CLOSED HAND"

        else:

            gesture = "UNKNOWN"


        # OPEN HAND = PLAY / RESUME

        if gesture == "OPEN HAND":

            if not is_playing:

                # First time playing
                if not audio_started:

                    pygame.mixer.music.play()

                    audio_started = True

                # Resume after pause
                else:

                    pygame.mixer.music.unpause()


                is_playing = True

                gesture_action = "PLAY"


        # CLOSED HAND = PAUSE

        elif gesture == "CLOSED HAND":

            if is_playing:

                pygame.mixer.music.pause()

                is_playing = False

                gesture_action = "PAUSE"


        # UNKNOWN

        else:

            gesture_action = "WAITING"


        # Draw Connections

        for start, end in connections:

            x1 = int(
                hand_landmarks[start].x * width
            )

            y1 = int(
                hand_landmarks[start].y * height
            )

            x2 = int(
                hand_landmarks[end].x * width
            )

            y2 = int(
                hand_landmarks[end].y * height
            )


            cv2.line(
                original_frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                LINE_THICKNESS,
                cv2.LINE_AA
            )


        # Draw Points + Numbers

        for i, landmark in enumerate(
            hand_landmarks
        ):

            x = int(
                landmark.x * width
            )

            y = int(
                landmark.y * height
            )


            # Big Landmark Point

            cv2.circle(
                original_frame,
                (x, y),
                POINT_RADIUS,
                (0, 255, 0),
                -1,
                cv2.LINE_AA
            )


            # Number Background

            text = str(i)

            text_size, _ = cv2.getTextSize(
                text,
                cv2.FONT_HERSHEY_SIMPLEX,
                FONT_SCALE,
                FONT_THICKNESS
            )

            text_width, text_height = text_size


            cv2.rectangle(
                original_frame,
                (
                    x + 8,
                    y - text_height - 10
                ),
                (
                    x + text_width + 14,
                    y - 4
                ),
                (0, 0, 0),
                -1
            )


            # Landmark Number

            cv2.putText(
                original_frame,
                text,
                (
                    x + 10,
                    y - 8
                ),
                cv2.FONT_HERSHEY_SIMPLEX,
                FONT_SCALE,
                (255, 255, 255),
                FONT_THICKNESS,
                cv2.LINE_AA
            )


    # Gesture Display

    cv2.putText(
        original_frame,
        f"GESTURE: {gesture}",
        (30, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        (0, 255, 0),
        3,
        cv2.LINE_AA
    )


    # Action Display

    cv2.putText(
        original_frame,
        f"ACTION: {gesture_action}",
        (30, 105),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.0,
        (255, 255, 255),
        2,
        cv2.LINE_AA
    )


    # Audio Status

    audio_status = (
        "PLAYING"
        if is_playing
        else "PAUSED"
    )

    cv2.putText(
        original_frame,
        f"AUDIO: {audio_status}",
        (30, 145),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (255, 255, 255),
        2,
        cv2.LINE_AA
    )


    # Playback Speed Display

    cv2.putText(
        original_frame,
        f"SPEED: {SPEED}x",
        (30, 185),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (255, 255, 255),
        2,
        cv2.LINE_AA
    )


    # Display Size

    display_frame = cv2.resize(
        original_frame,
        (640, 360),
        interpolation=cv2.INTER_AREA
    )


    # Show Video

    cv2.imshow(
        window_name,
        display_frame
    )


    # Quit

    if cv2.waitKey(delay) & 0xFF == ord("q"):

        break

# Cleanup
cap.release()

detector.close()

pygame.mixer.music.stop()

pygame.mixer.quit()

cv2.destroyAllWindows()