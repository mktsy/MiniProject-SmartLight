import multiprocessing as mp

from sheet.model_speech_recog import(
    runSpeechRecognition        
)
from sheet.control_by_app import(
    runControlLightByApp,
    runSetTime
)

if(__name__=='__main__'):
    task_speech_recognition = mp.Process(target=runSpeechRecognition)
    task_control_by_app = mp.Process(target=runControlLightByApp)
    task_set_time = mp.Process(target=runSetTime)

    task_speech_recognition.start()
    task_control_by_app.start()
    task_set_time.start()
