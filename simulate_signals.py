# simulate_signals.py
# Purpose: Simulate synthetic ECG, EEG, and EDA signals

import neurokit2 as nk  #NeuroKit2 provides physiological signal simulation and processing 
                        #Library for physiological signal simulation

#Simulate ECG signal (used to derive HRV)
# --- ECG Simulation (for HRV) ---
def simulate_ecg(duration=60, heart_rate=75):
    """
    Simulates ECG signal based on average heart rate.
    duration: total time in seconds (recommended ≥60s for HRV)
    heart_rate: average BPM (e.g. 65 for relaxed, 85 for stressed)
    """
    return nk.ecg_simulate(duration=duration, heart_rate=heart_rate)

#Simulate EEG signal (used for mental state analysis)
# --- EEG Simulation ---
def simulate_eeg(duration=60, sampling_rate=250, frequency=[10]):
    """
    Simulates EEG signal.
    sampling_rate: typically 250Hz is sufficient for alpha/beta bands.
    frequency: dominant frequency (e.g. 10Hz for alpha = relaxed)
    """
    return nk.eeg_simulate(duration=duration, sampling_rate=sampling_rate, frequency=frequency)

#Simulate EDA signal (skin conductance, used for stress detection)
# --- EDA Simulation ---
def simulate_eda(duration=60, sampling_rate=250, scr_number=5):
    """
    Simulates EDA signal.
    scr_number: number of Skin Conductance Responses (SCRs) in the signal.
    Higher scr_number indicates higher arousal/stress.
    """
    return nk.eda_simulate(duration=duration, sampling_rate=sampling_rate, scr_number=scr_number)

# --- Suggested Presets for Mental States ---
def simulate_relaxed():
    """
    Preset: Relaxed state
    HR ~ 65-70 BPM
    EEG ~ Alpha (8–12Hz)
    EDA ~ Few SCRs
    """
    return (
        simulate_ecg(heart_rate=68),
        simulate_eeg(frequency=[10]),
        simulate_eda(scr_number=2)
    )

def simulate_focused():
    """
    Preset: Focused state
    HR ~ 75-85 BPM
    EEG ~ Low Beta (12–16Hz)
    EDA ~ Moderate SCRs
    """
    return (
        simulate_ecg(heart_rate=80),
        simulate_eeg(frequency=[14]),
        simulate_eda(scr_number=5)
    )

def simulate_stressed():
    """
    Preset: Stressed state
    HR ~ 90-100+ BPM
    EEG ~ High Beta (18–25Hz)
    EDA ~ High SCRs
    """
    return (
        simulate_ecg(heart_rate=95),
        simulate_eeg(frequency=[20]),
        simulate_eda(scr_number=9)
    )



