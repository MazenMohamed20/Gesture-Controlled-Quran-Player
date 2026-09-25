# GestureQuran AI

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=28&duration=3000&pause=1000&color=00C853&center=true&vCenter=true&width=700&lines=Gesture-Controlled+Quran+Player;Computer+Vision+%7C+Hand+Tracking;Control+Audio+with+Hand+Gestures" alt="Typing Animation" />

<br>

<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
<img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-red?style=for-the-badge&logo=opencv" />
<img src="https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange?style=for-the-badge" />
<img src="https://img.shields.io/badge/Pygame-Audio-green?style=for-the-badge" />

</div>

---

## About The Project

**Gesture-Controlled Quran Player** is a Computer Vision project that allows users to control Quran audio playback using hand gestures instead of a traditional mouse or keyboard.

The project is built with:

- Python
- OpenCV
- MediaPipe
- Pygame

The current prototype focuses on two main gestures:

- Open Hand → Play / Resume Quran Recitation
- Closed Hand → Pause Quran Recitation

This project represents the first step toward developing more advanced gesture-based and accessibility-focused interaction systems.

---

## Why This Project?

Traditional computer interaction usually depends on a mouse, keyboard, or touchscreen.

This project explores an alternative approach:

> Using hand gestures as a natural way to interact with digital systems.

The idea can potentially be developed into accessibility-oriented solutions for people who may have difficulty using traditional input devices.

The current version is a prototype, with plans to add more gestures and controls in future versions.

---

## How It Works

Video Input
    ↓
OpenCV
    ↓
RGB Conversion
    ↓
MediaPipe Hand Landmarker
    ↓
21 Hand Landmarks
    ↓
Gesture Recognition
    ↓
Open Hand / Closed Hand
    ↓
Gesture Command
    ↓
Pygame Audio Control
    ↓
Play / Pause Quran Recitation

---

## Features

- Real-time hand tracking
- 21-point hand landmark detection
- Hand gesture recognition
- Open hand detection
- Closed hand detection
- Play Quran audio
- Pause Quran audio
- Resume Quran audio
- Real-time gesture status
- Real-time audio status
- Visual hand landmark tracking
- Support for up to two detected hands
- Video-based testing
- Adjustable playback speed
- Adjustable MediaPipe confidence values

---

## Gesture Controls

| Gesture | Action |
|--------|--------|
| Open Hand | Play / Resume |
| Closed Hand | Pause |
| Unknown Gesture | Waiting |
| No Hand | Waiting |

---

## Hand Tracking

The project uses MediaPipe Hand Landmarker to detect the user's hand and track 21 landmarks.

Landmark structure:

0  - Wrist

1-4   - Thumb
5-8   - Index Finger
9-12  - Middle Finger
13-16 - Ring Finger
17-20 - Pinky

These landmarks are used to analyze finger positions and determine the detected gesture.

---

## Gesture Recognition

The system analyzes the position of the hand landmarks to determine whether the fingers are extended or closed.

Example:

hand_landmarks[8].y < hand_landmarks[6].y

This is used as part of the logic for determining whether the index finger is extended.

The same concept is applied to the other fingers to distinguish between an open hand and a closed hand.

---

## Accuracy

Gesture recognition can be affected by:

- Lighting conditions
- Hand position
- Camera quality
- Motion blur
- Hand orientation
- Distance from the camera
- Occlusion

The project uses MediaPipe confidence parameters to improve detection and tracking stability.

Example configuration:

min_hand_detection_confidence = 0.65
min_hand_presence_confidence = 0.65
min_tracking_confidence = 0.70

These values can be adjusted depending on the testing environment.

---

## Project Structure

GestureQuran-AI/
│
├── app/
│   └── main.py
│
├── assets/
│   ├── audio/
│   │   └── Quran Audio
│   │
│   ├── videos/
│   │   └── test.mp4
│   │
│   └── hand_landmarker.task
│
├── README.md
│
└── requirements.txt

---

## Installation

Clone the repository:

git clone https://github.com/MazenMohamed20/GestureQuran-AI.git

Move into the project directory:

cd GestureQuran-AI

Install the required packages:

py -m pip install opencv-python
py -m pip install mediapipe
py -m pip install pygame

Or install everything using:

py -m pip install -r requirements.txt

---

## Requirements

Example requirements.txt:

opencv-python
mediapipe
pygame

---

## Run The Project

Run the application using:

py app/main.py

The application will open the video window and start detecting hand gestures.

Press Q to exit the application.

---

## Playback Speed

The project supports adjustable video playback speed.

Example:

SPEED = 8.0

The value can be changed depending on the testing requirements.

---

## Audio Control

The Quran audio is controlled using Pygame.

### Open Hand

When an open hand is detected:

PLAY / RESUME

The Quran recitation starts or resumes.

### Closed Hand

When a closed hand is detected:

PAUSE

The Quran recitation pauses.

The system keeps track of the current audio state so that opening the hand resumes the existing audio instead of restarting it.

---

## Accessibility

One of the main goals of this project is to explore how Computer Vision can support more accessible human-computer interaction.

Instead of depending only on:

Mouse
Keyboard
Touchscreen

the user can interact with the system through:

Hand Gestures

This concept could potentially be expanded into assistive technologies for users who have difficulty using traditional input devices.

---

## Current Status

Project Status: Prototype

[✓] Hand Detection
[✓] Hand Tracking
[✓] 21 Hand Landmarks
[✓] Open Hand Detection
[✓] Closed Hand Detection
[✓] Gesture Recognition
[✓] Play
[✓] Pause
[✓] Resume
[✓] Audio Status
[✓] Gesture Status
[✓] Video Testing

---

## Future Development

This project is only the first step.

Planned improvements include:

- More hand gestures
- Next Surah gesture
- Previous Surah gesture
- Volume control
- Mute / Unmute
- Restart recitation
- Gesture-based Surah selection
- Better gesture classification
- Improved tracking stability
- Real-time webcam support
- Multiple Quran recitations
- User-customizable gestures
- Graphical User Interface
- More accessibility features

---

## Future Vision

The long-term goal is to transform the current prototype into a more complete gesture-controlled Quran player.

The project will focus on improving:

Accuracy
Stability
Gesture Variety
Accessibility
User Experience
Real-Time Performance

The goal is not simply to recognize hand gestures, but to explore how Computer Vision can create more natural and accessible ways for people to interact with technology.

---

## Demo

A demonstration video can show:

Hand Tracking
    ↓
Gesture Recognition
    ↓
Open Hand
    ↓
PLAY / RESUME

Closed Hand
    ↓
PAUSE

The demo highlights the complete interaction between Computer Vision and audio control.

---

## Learning Purpose

This project is part of my practical learning journey in:

- Computer Vision
- Artificial Intelligence
- Machine Learning
- Python
- OpenCV
- MediaPipe
- Human-Computer Interaction
- Accessibility Technologies

It demonstrates how Computer Vision concepts can be transformed into a practical real-world application.

---

## Author

### Mazen Mohamed

AI & ML Developer

Areas of Interest:

- Artificial Intelligence
- Machine Learning
- Computer Vision
- Generative AI
- AI Agents
- Python
- Backend Development

GitHub:

https://github.com/MazenMohamed20

---

## License

This project is created for educational and development purposes.

Please make sure that any Quran audio files distributed with or alongside the project are used according to their applicable permissions and licensing terms.

---

## Final Note

GestureQuran AI started as a Computer Vision experiment focused on hand tracking and gesture recognition.

It has now evolved into a prototype that connects:

Computer Vision
+
Gesture Recognition
+
Audio Control
+
Accessibility

This is only the first step.

More gestures, more controls, and more accessibility features are planned for future versions.

---

<div align="center">

GestureQuran AI

Turning Hand Gestures into Interaction

Built with Python, OpenCV, MediaPipe and Pygame.

<br>

Created by **Mazen Mohamed**

</div>
