from threading import Thread, Event
import pyaudio


class Recorder:
    """Class that records and stores audio data"""

    def __init__(self) -> None:
        """Initialising variables necessary to record audio"""
        self.audio = pyaudio.PyAudio()
        self.recorded = []
        self.thread_event = None
        self.stream = self.audio.open(
            format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        self.recording_thread = Thread(target=self.__get_audio)

    def start_recording(self) -> None:
        """Start recording thread and initalise event that will enable thread to close"""
        self.thread_event = Event()
        self.recording_thread.start()

    def __get_audio(self) -> None:
        """Function to retrieve audio from the stream and clean up audio and stream variables after recording has completed"""
        while not self.thread_event.is_set():
            data = self.stream.read(1024)
            self.recorded.append(data)

        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

    def stop_recording(self) -> None:
        """Setting a event which will stop the recording loop"""
        self.thread_event.set()

    def get_bytes(self) -> bytes:
        """Join the bytes together and return them to the caller"""
        return b"".join(self.recorded)
