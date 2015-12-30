import pyaudio
import wave
import numpy
import psutil, os
import time
import scipy.signal as signal
from multiprocessing import Process, Value, Lock


def audio_loop(file, ratio, end, chunk_size, fast_resample=True):

    proc = psutil.Process(os.getpid())
    proc.nice(-5)
    while True:
        #chunk = 2048/2
        wf = wave.open(file, 'rb')
        data = wf.readframes(chunk_size.value)
        p = pyaudio.PyAudio()
        stream = p.open(
            format = p.get_format_from_width(wf.getsampwidth()), 
            channels = wf.getnchannels(),
            rate = wf.getframerate(),
            output = True,
            frames_per_buffer = chunk_size.value)
        while data != '':
            #need to try locking here for multiprocessing
            array = numpy.fromstring(data, dtype=numpy.int16)
            data = signal.resample(array, chunk_size.value*ratio.value)
            stream.write(data.astype(int).tostring())
            data = wf.readframes(chunk_size.value)
        
        stream.close()
        p.terminate()

        if end:
            break

# Start audio in seperate process to be non-blocking
class Audio:
    def __init__(self, file, fast_resample, end=False,):
        self.chunk = 2048
        self.file = file
        self.ratio = Value('d' , 1.0)
        self.chunk_size = Value('i', 2048/2)
    	self.p = Process(target=audio_loop, args=(self.file,
                                                  self.ratio,
                                                  end,
                                                  self.chunk_size,
                                                  fast_resample))

    def start_audio_loop(self):
        self.p.start()

    def stop_audio(self):
        self.p.terminate()
        self.p.join()
        


    def change_ratio(self, ratio):
        self.ratio.value = ratio

    def change_chunk_size(self, increase):
        if increase:
            self.chunk_size.value = 2048/4
        else:
            self.chunk_size.value = 2048/2
            
        
          
