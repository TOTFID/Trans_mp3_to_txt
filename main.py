import whisper
import torch


def speech_rec(model = 'base', path='songs/'):
   device = 'cuda' if torch.cuda.is_available() else 'cpu'
   whisper.load_model('medium').to(device)
   speech_model = whisper.load_model(model)
   result = speech_model.transcribe(f'{path}', fp16 = False)
   
   with open(f'result/transcription_{model}.txt', 'w') as file:
      file.write(result['text'])
