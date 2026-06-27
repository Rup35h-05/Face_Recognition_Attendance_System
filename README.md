# Unsupervised CNN–LSTM Autoencoder for Gait Anomaly Detection in Parkinson's Disease Using Video Analysis

## Abstract

Parkinson's disease is a progressive neurological disorder that significantly affects human gait and mobility. Early identification of abnormal gait patterns is crucial for monitoring disease progression and assisting clinical assessment. This project presents an unsupervised deep learning framework for detecting gait anomalies in Parkinson's disease using video data. A hybrid CNN–LSTM autoencoder model is proposed, where Convolutional Neural Networks (CNNs) extract spatial features from individual video frames and Long Short-Term Memory (LSTM) networks capture temporal gait dynamics across frames. The model is trained end-to-end without labeled data, learning normal gait patterns through reconstruction. Anomaly detection is achieved using reconstruction error as an anomaly score. Experimental results on Parkinson's turning gait videos demonstrate that the proposed approach effectively identifies abnormal gait behavior. A Streamlit-based web application is developed to visualize anomaly scores, reconstruction error heatmaps, and temporal anomaly curves, making the system interactive and user-friendly.

## 1. Introduction

Parkinson's disease (PD) is a chronic neurodegenerative disorder characterized by motor impairments such as bradykinesia, rigidity, tremors, and gait abnormalities. Gait-related symptoms, including hesitation during turning, instability, and freezing-like behavior, are among the earliest indicators of Parkinsonian movement disorders. Traditional gait assessment relies on clinical observation and sensor-based analysis, which can be subjective, time-consuming, and resource-intensive.

Recent advances in computer vision and deep learning have enabled automatic analysis of human motion using video data. However, most existing approaches rely on supervised learning techniques that require large amounts of labeled clinical data, which is often difficult to obtain. To address this limitation, this project explores an unsupervised learning approach for gait anomaly detection using video-based analysis.

The proposed system employs a CNN–LSTM autoencoder to learn normal gait patterns from Parkinson's gait videos and detect deviations using reconstruction error. This approach eliminates the need for manual labeling and provides a scalable solution for gait anomaly analysis.

## 2. Problem Definition

Early detection and quantitative analysis of gait abnormalities in Parkinson's disease remain challenging due to the lack of labeled datasets and objective assessment tools. Most existing video-based gait analysis systems require supervised classification with explicit labels, which are not always available. Therefore, there is a need for an unsupervised, video-based gait analysis system that can automatically identify abnormal gait patterns without relying on labeled data.

## 3. Objectives

1. Design a video-based gait analysis system using deep learning.
2. Develop a CNN–LSTM autoencoder for unsupervised learning of gait patterns.
3. Detect gait anomalies using reconstruction error without labeled data.
4. Visualize anomaly scores, heatmaps, and temporal anomaly curves.
5. Deploy the trained model using a Streamlit-based web interface for interactive analysis.

## 4. Literature Survey

Several studies have explored gait analysis for Parkinson's disease using wearable sensors, such as accelerometers and gyroscopes. While sensor-based methods provide accurate measurements, they require specialized hardware and controlled environments. Recent research has shifted towards vision-based gait analysis using deep learning techniques.

CNNs have been widely used for extracting spatial features from gait images and video frames. LSTM networks have proven effective in modeling temporal dependencies in sequential data, including human motion. Autoencoders have been successfully applied for anomaly detection in medical imaging and time-series data by learning normal patterns and detecting deviations.

However, most existing methods focus on supervised classification or sensor-based approaches. Unsupervised video-based gait anomaly detection using CNN–LSTM autoencoders remains relatively unexplored, motivating the proposed work.

## 5. Proposed Work

This project proposes an unsupervised CNN–LSTM autoencoder framework for detecting gait anomalies in Parkinson's disease using video data. The system processes gait videos, extracts spatial features using CNNs, models temporal dynamics using LSTMs, and reconstructs the input video. Reconstruction error is used as an anomaly score to identify abnormal gait patterns. A web-based interface is developed to visualize the results.

## 6. Methodology & Implementation

### 6.1 Dataset

The project uses publicly available Parkinson's turning gait videos. The dataset contains multiple video recordings of individuals performing turning-in-place tasks. No explicit labels indicating gait abnormality or severity are provided.

### 6.2 Preprocessing

- Videos are sampled into fixed-length frame sequences.
- Frames are resized to 64×64 pixels.
- Pixel values are normalized to the range [0, 1].

### 6.3 Model Architecture

- **CNN Encoder:** Extracts spatial features from each video frame.
- **LSTM Encoder:** Captures temporal gait dynamics across frames.
- **Latent Representation:** Compact spatio-temporal gait embedding.
- **LSTM Decoder:** Reconstructs temporal motion sequence.
- **CNN Decoder:** Reconstructs video frames from latent features.

### 6.4 Training

The autoencoder is trained in an unsupervised manner using Mean Squared Error (MSE) loss between original and reconstructed frames. The model learns normal gait patterns present in the dataset.

### 6.5 Anomaly Detection

Anomaly scores are computed using reconstruction error:

- Low error indicates normal gait.
- High error indicates abnormal gait patterns.

### 6.6 Deployment

A Streamlit web application allows users to upload gait videos and view:

- Overall anomaly score
- Frame-wise anomaly curve
- Reconstruction error heatmaps

## 7. Results & Discussion

The trained CNN–LSTM autoencoder successfully reconstructed normal gait patterns while producing higher reconstruction errors for abnormal movements. The anomaly scores provided a quantitative measure of gait irregularity. Heatmap visualizations highlighted regions of significant reconstruction error, particularly during turning phases. The temporal anomaly curves effectively captured variations in gait behavior across video frames. The results demonstrate the effectiveness of the proposed unsupervised approach for gait anomaly detection.

## 8. Conclusion

This project presents an unsupervised CNN–LSTM autoencoder framework for detecting gait anomalies in Parkinson's disease using video data. By eliminating the need for labeled datasets, the proposed method offers a scalable and practical solution for gait analysis. Experimental results confirm that reconstruction error can effectively identify abnormal gait patterns. The integration of a web-based interface further enhances usability and real-world applicability. Future work may include incorporating multimodal sensor data, extending the model to supervised classification, and validating the system with clinical assessments.

## Tech Stack

- Python
- CNN + LSTM (PyTorch / TensorFlow)
- Streamlit (web interface)
- NumPy, OpenCV (video preprocessing)

## Installation

```bash
git clone https://github.com/your-username/parkinson-gait-anomaly-detection.git
cd parkinson-gait-anomaly-detection
pip install -r requirements.txt
```

## Usage

```bash
streamlit run app.py
```

Upload a gait video through the interface to view the anomaly score, frame-wise anomaly curve, and reconstruction error heatmap.

## Project Structure

```
.
├── data/                 # Gait video dataset
├── models/               # CNN-LSTM autoencoder architecture
├── preprocessing/        # Frame extraction & normalization scripts
├── app.py                # Streamlit web application
├── train.py              # Model training script
├── requirements.txt
└── README.md
```

## References

1. Goodfellow, I., Bengio, Y., & Courville, A., *Deep Learning*, MIT Press, 2016.
2. Hochreiter, S., & Schmidhuber, J., "Long Short-Term Memory," *Neural Computation*, 1997.
3. Sabour, S., Frosst, N., & Hinton, G., "Dynamic Routing Between Capsules," *NeurIPS*, 2017.
4. Pereira, C. R., et al., "Automatic gait analysis for Parkinson's disease classification," *Pattern Recognition Letters*, 2018.
5. Bishop, C. M., *Pattern Recognition and Machine Learning*, Springer, 2006.

## License

This project is intended for academic and research purposes.
