from manim import *
from pathlib import Path
import os
from sys import platform
os.environ["PATH"] = os.environ["PATH"] + r";C:\Users\lucas\AppData\Local\Programs\MiKTeX\miktex\bin\x64\\"

FLAGS = f'-pqh'
SCENE = 'Test'

class Test(Scene):
    def construct(self):
       ax = Axes()
       ax.add_coordinates()
       labels = ax.get_axis_labels(x_label='x', y_label='y').set_color(BLUE)
       self.add(labels)

       self.add(ax)



if __name__ == '__main__':
     script_name = f'{Path(__file__).resolve()}'
     if platform == 'darwin':
         script_name = script_name.replace(' ', '\ ')
     os.system(f'manim {script_name} {FLAGS} {SCENE}')