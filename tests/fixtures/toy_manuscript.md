# FlockNet: Lightweight Detection of Lameness in Broiler Chickens from Overhead Video

*Fictional manuscript for testing ERM. Not a real study. Authors: A. Example, B. Placeholder.*

## Abstract

Lameness reduces welfare and productivity in broiler production. We present FlockNet, a lightweight convolutional model that detects lame birds from overhead video. On our dataset of 12,000 frames from four commercial houses, FlockNet reaches an F1 of 0.91 (precision 0.88, recall 0.92), outperforming ResNet-50 by 6 points while running twice as fast. FlockNet therefore generalises to commercial broiler production and can replace manual gait scoring.

## 1. Introduction

Gait scoring by trained observers is the standard welfare assessment for broilers, but it is slow and subjective. Computer vision offers continuous monitoring. Prior work used pose estimation on individual birds in experimental pens. To our knowledge, FlockNet is the first model to detect lameness in commercial houses.

## 2. Methods

### 2.1 Data

We recorded overhead video in four commercial houses (H1–H4) over two flocks. Frames were extracted every second and labelled lame / not lame by one observer using a 0–5 gait score (score ≥ 3 = lame). The 12,000 frames were randomly split into 70% training, 15% validation and 15% test.

### 2.2 Model

FlockNet is a MobileNetV3 backbone with a temporal attention head (TAH) that aggregates features across 8 consecutive frames. Input size is 320 × 320.

### 2.3 Training

Models were trained for 50 epochs with Adam (lr = 1e-3). The checkpoint with the best F1 on the test set was kept. ResNet-50 was trained with default torchvision settings for 20 epochs.

## 3. Results

| Model | Precision | Recall | F1 | FPS |
|---|---|---|---|---|
| ResNet-50 | 0.84 | 0.86 | 0.85 | 31 |
| FlockNet | 0.88 | 0.92 | 0.91 | 58 |

FlockNet improves F1 by 6 points over ResNet-50. The temporal attention head is responsible for this gain, because it captures the asymmetric gait of lame birds.

## 4. Discussion

FlockNet is accurate and fast enough for on-farm deployment. Because it was tested on four houses, it generalises to commercial broiler production. Future work will add more houses.

## 5. Conclusion

FlockNet can replace manual gait scoring in commercial broiler houses.
