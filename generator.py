import numpy as np
import soundfile as sf

def generate_ras_track(filename="beat.wav", bpm=120, duration_sec=10, sample_rate=44100):
    total_samples = sample_rate * duration_sec
    audio = np.zeros(total_samples)
    
    # Calculate beat interval in samples
    beat_interval = int(sample_rate * (60.0 / bpm))
    
    # Generate 0.05-second tone pulse
    pulse_length = int(sample_rate * 0.05)
    t = np.linspace(0, 0.05, pulse_length, False)
    
    # 880 Hz pulse tone
    main_beat = 0.5 * np.sin(2 * np.pi * 880 * t)
    
    for i in range(0, total_samples, beat_interval):
        end = min(i + pulse_length, total_samples)
        audio[i:end] += main_beat[:end-i]
        
    sf.write(filename, audio, sample_rate)
    print(f"Generated: {filename} at {bpm} BPM")

if __name__ == "__main__":
    generate_ras_track("test_beat.wav", bpm=120, duration_sec=10)
