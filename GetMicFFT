from processing.sound import *

fft = None
in_stream = None
bands = 512
spectrum = [0.0] * bands

def setup():
    global fft, in_stream
    size(512, 360)
    background(255)
    
    # Finde alle verfügbaren Audioquellen
    audio_sources = AudioIn.getDevices()
    print("Verfügbare Audioquellen:")
    for source in audio_sources:
        print(source)
    
    # Wähle die gewünschte Audioquelle aus
    selected_source_index = 0  # Index der ausgewählten Audioquelle in der Liste
    in_stream = AudioIn(this, selected_source_index)
    in_stream.start()
    
    # Initialisiere das FFT-Objekt
    fft = FFT(this, bands)
    fft.input(in_stream)

def draw():
    global spectrum
    background(255)
    
    # Analysiere das Spektrum
    fft.analyze(spectrum)
    
    for i in range(bands):
        x = map(i, 0, bands, 0, width)
        y = map(spectrum[i], 0, 1, height, 0)
        
        # Zeichne die Balken für das Frequenzband
        stroke(0)
        line(x, height, x, y)

def stop():
    global in_stream
    in_stream.stop()
    in_stream.close()
