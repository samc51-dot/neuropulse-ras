# NeuroPulse: Precision Auditory Entrainment Platform

**NeuroPulse** is an open-source research apparatus and real-time audio synthesizer engineered to evaluate Rhythmic Auditory Stimulation (RAS) frameworks for neuromotor rehabilitation.

---

## 🔬 Abstract & Key Findings
Conventional motor rehabilitation frequently relies on unmodulated, metronomic auditory cues. **NeuroPulse** investigates the clinical efficacy of algorithmic, frequency-accented auditory stimuli (140 Hz low-frequency pulse paired with a 1200 Hz high-frequency downbeat accent) versus baseline metronomes.

* **18.4% Variance Reduction:** Empirical testing across 25 subjects demonstrated an 18.4% reduction in mean motor timing error ($p < 0.001$).
* **Internal Clock Retention:** Demonstrated predictive timing stability with an average internal drift of only 28.1 ms during periods of transient acoustic silence.
* **Inhibitory Control:** Achieved an 86.2% synchronization accuracy score when subjects were exposed to syncopated off-beat acoustic distractors.

---

## 🛠️ Architecture & Signal Processing

The platform combines client-side Web Audio API audio rendering with high-resolution telemetry data collection:

1. **Audio Synthesis Pipeline:** Built using JavaScript Web Audio API (`AudioContext`) and prototyped in Python (`SciPy`, `NumPy`) to deliver precise 44.1 kHz multi-frequency acoustic structures without phase distortion or click transients.
2. **Precision Telemetry:** Logs user interaction timestamps using sub-millisecond hardware timers (`window.performance.now()`) to measure latency and compute Mean Absolute Error ($MAE$).
3. **Interactive Battery:** Features three standardized protocols:
   * *Continuous Synchronization* (120 BPM baseline entrainment)
   * *Phase Resetting & Internal Clock* (Silent interval tempo retention)
   * *Off-Beat Suppression* (Syncopated distractor filtering)

---

## 🚀 Live Demo & Repository Access
* **Live Telemetry App:** [https://samc51-dot.github.io/smart-beats-ras/](https://samc51-dot.github.io/smart-beats-ras/)
* **Author:** [Your Name] (South Hills High School)
* **Status:** Preprint manuscript prepared for *bioRxiv* / *IEEE Transactions on Neural Systems and Rehabilitation Engineering*.

---

## 📄 Citation
```bibtex
@article{neuropulse2026,
  title={NeuroPulse: Precision Auditory Entrainment for Neuromotor Rehabilitation},
  author={[Your Name]},
  institution={South Hills High School},
  year={2026},
  url={[https://samc51-dot.github.io/smart-beats-ras/](https://samc51-dot.github.io/smart-beats-ras/)}
}
