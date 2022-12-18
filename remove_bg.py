import numpy as np
from pathlib import Path
from tqdm import tqdm
import os
import shutil
from music21 import *
import cv2
from rembg import remove, new_session

session = new_session()

if __name__ == '__main__':
    
    def gray_remove(fish_data_dir):
        
        for idx, i in enumerate(fish_data_dir):
            im = cv2.imread(str(i))
            im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            out = im_gray.copy()
            out = 255-out
            cv2.imwrite(str(fish_data_dir[idx].parent)+f'grayed_fish_{idx}.png', out)
                
        for file in tqdm(Path(fish_data_dir).rglob('*.png')):
            input_path = str(file)
            output_path = str(file.parent / (file.stem + ".out.png"))

            with open(input_path, 'rb') as i:
                with open(output_path, 'wb') as o:
                    input = i.read()
                    output = remove(input, session=session)
                    o.write(output)
                    
    def normal_remove(fish_data_dir):
        
        for file in tqdm(Path(fish_data_dir).rglob('*.png')):
            input_path = str(file)
            output_path = str(file.parent / (file.stem + ".out.png"))

            with open(input_path, 'rb') as i:
                with open(output_path, 'wb') as o:
                    input = i.read()
                    output = remove(input, session=session)
                    o.write(output)     
                    
    def move_dir(fish_data_dir):
        for idx, i in enumerate(list(fish_data_dir)):
            shutil.move(str(i), f'/home/hyerin/userdata/music_aquarium/Fish-Bowl/fish_{idx}.png')