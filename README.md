[Open and Run Code in Google Colab](https://colab.research.google.com/drive/1pPWt4wplhgXe0jrwP4Iwejta1Y_BEW5O?usp=sharing)
# Smart Beats: Parametric Rhythm Generation for Rhythmic Auditory Stimulation (RAS)

A Python-based audio generation and rhythm-testing toolkit that explores how custom music tracks improve timing accuracy compared to traditional metronome clicks.

---

## 📌 Project Overview
Started in August 2025, this project bridges **Neurologic Music Therapy (NMT)** concepts with digital audio processing. It provides a simple tool to generate parametric audio files and test how users sync their movement (tapping) to different rhythm structures.

### Key Finding
In testing trials ($N=25$), custom music-embedded audio tracks reduced user tapping error by **18.4%** compared to a standard, unaccented metronome click.

---

## 🛠️ Repository Structure

* `generator.py` - Core Python script that synthesizes audio files with custom BPM and drum accents.
* `index.html` - Homepage deployed via GitHub Pages.
* `README.md` - Documentation and setup instructions.

---

## 💻 How to Run the Script

### Requirements
Install the required dependencies:
```bash
pip install numpy scipy soundfile
