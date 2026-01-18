export class SoundManager {
    constructor() {
        this.ctx = null;
        this.masterGain = null;
        this.engineOsc = null;
        this.engineGain = null;
        this.isMuted = false;
    }

    init() {
        if (this.ctx) return;
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        this.ctx = new AudioContext();
        this.masterGain = this.ctx.createGain();
        this.masterGain.gain.value = 0.5; // Default volume
        this.masterGain.connect(this.ctx.destination);
    }

    startEngine() {
        if (!this.ctx) this.init();
        if (this.engineOsc) return;

        // Engine rumble: Sawtooth wave
        this.engineOsc = this.ctx.createOscillator();
        this.engineOsc.type = 'sawtooth';
        this.engineOsc.frequency.value = 50; // Idle

        this.engineGain = this.ctx.createGain();
        this.engineGain.gain.value = 0.1;

        // Lowpass filter to muffle the harsh sawtooth
        this.engineFilter = this.ctx.createBiquadFilter();
        this.engineFilter.type = 'lowpass';
        this.engineFilter.frequency.value = 400;

        this.engineOsc.connect(this.engineFilter);
        this.engineFilter.connect(this.engineGain);
        this.engineGain.connect(this.masterGain);
        this.engineOsc.start();
    }

    stopEngine() {
        if (this.engineOsc) {
            this.engineOsc.stop();
            this.engineOsc = null;
        }
    }

    updateEngine(speedPercent) {
        if (!this.engineOsc) return;
        // Pitch rises with speed
        // 50Hz (Idle) -> 200Hz (Max)
        const targetFreq = 50 + (speedPercent * 150);
        this.engineOsc.frequency.exponentialRampToValueAtTime(targetFreq, this.ctx.currentTime + 0.1);

        // Filter opens up
        this.engineFilter.frequency.value = 400 + (speedPercent * 600);

        // Tremolo/Variance could be added but keep simple
    }

    playSiren() {
        if (!this.ctx) return;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();

        osc.type = 'square';
        osc.frequency.setValueAtTime(600, this.ctx.currentTime);
        // Wee-woo effect
        osc.frequency.linearRampToValueAtTime(800, this.ctx.currentTime + 0.3);
        osc.frequency.linearRampToValueAtTime(600, this.ctx.currentTime + 0.6);
        osc.frequency.linearRampToValueAtTime(800, this.ctx.currentTime + 0.9);
        osc.frequency.linearRampToValueAtTime(600, this.ctx.currentTime + 1.2);

        gain.gain.value = 0.1;
        gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 1.2);

        osc.connect(gain);
        gain.connect(this.masterGain);
        osc.start();
        osc.stop(this.ctx.currentTime + 1.2);
    }

    playCrash() {
        if (!this.ctx) return;
        // White noise burst
        const bufferSize = this.ctx.sampleRate * 1.0; // 1 sec
        const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
        const data = buffer.getChannelData(0);
        for (let i = 0; i < bufferSize; i++) {
            data[i] = Math.random() * 2 - 1;
        }

        const noise = this.ctx.createBufferSource();
        noise.buffer = buffer;

        const filter = this.ctx.createBiquadFilter();
        filter.type = 'lowpass';
        filter.frequency.value = 1000;

        const gain = this.ctx.createGain();
        gain.gain.setValueAtTime(0.5, this.ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 1.0);

        noise.connect(filter);
        filter.connect(gain);
        gain.connect(this.masterGain);
        noise.start();
    }

    playHit() {
        if (!this.ctx) return;
        // Punch sound: rapid pitch drop sine/triangle
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();

        osc.type = 'triangle';
        osc.frequency.setValueAtTime(200, this.ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(50, this.ctx.currentTime + 0.2);

        gain.gain.setValueAtTime(0.3, this.ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.2);

        osc.connect(gain);
        gain.connect(this.masterGain);

        osc.start();
        osc.stop(this.ctx.currentTime + 0.2);
    }

    playWin() {
        if (!this.ctx) return;
        // Arpeggio
        const notes = [440, 554, 659, 880]; // A major
        notes.forEach((freq, i) => {
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            osc.type = 'square';
            osc.frequency.value = freq;

            const start = this.ctx.currentTime + (i * 0.1);
            gain.gain.setValueAtTime(0.1, start);
            gain.gain.exponentialRampToValueAtTime(0.001, start + 0.5);

            osc.connect(gain);
            gain.connect(this.masterGain);
            osc.start(start);
            osc.stop(start + 0.5);
        });
    }
}
