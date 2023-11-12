from main import speech_rec
from pathlib import Path


def main():
   enter_path = str(input('Choose file: '))
   song_path = f'songs/{enter_path}'
   final_path = Path(song_path)
   
   if final_path.exists():
      print('file exists\n')
   else: FileNotFoundError
   
   models = {1: 'tiny', 2: 'base', 3: 'small', 4: 'medium', 5: 'large'}
   
   for i, v in models.items():
      print(f'{i}:{v}')
      
   model = int(input('Choose model: '))
   
   if model not in models.keys():
      raise KeyError(f'Model {model} incorect')
  
   print(f'Starting with the {model} model')

   speech_rec(model=models[model], path=song_path) 

if __name__ == '__main__':
   main()
   
