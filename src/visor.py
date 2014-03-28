# Visor

from procgame import *


# all paths
game_path = "C:\P-ROC\pyprocgame-master\games\VXtra_start/"
speech_path = game_path +"sound/speech/"
sound_path = game_path +"sound/fx/"
music_path = game_path +"sound/music/"
dmd_path = game_path +"dmd/"

class Visor(game.Mode):

        def __init__(self, game, priority):
                super(Bumpers, self).__init__(game, priority)
                self.game.sound.register_sound('visor', sound_path+"lasergun1.wav")
                

        def mode_started(self):
                self.visor1=0

        def mode_stopped(self):
                pass

                
## switches
                
        def sw_visor1_active(self,sw):
             self.game.sound.play("visor")
             self.game.score(10)

        def sw_Bbumper_active(self,sw):
             self.game.sound.play("bumper3")
             self.game.score(10)

        def sw_Lbumper_active(self,sw):
             self.game.sound.play("bumper2")
             self.game.score(10)





## Lampen


## Mode functions
        
                     
## Animations
                
        def bumpers_animation(self):
                pass
##                self.title_layer = dmd.TextLayer(110, 2, self.game.fonts['num_09Bx7'], "center", opaque=False) #num_09Bx7 num_14x10
##                self.title_layer.set_text(str(self.energyscore),True)  
##                anim = dmd.Animation().load(dmd_path+'slings.dmd')
##                self.animation_layer = dmd.AnimatedLayer(frames=anim.frames, opaque=False, repeat=False, hold=False, frame_time=4)
##                self.layer = dmd.GroupedLayer(128, 32, [self.animation_layer, self.title_layer])
##                self.delay(name='clear_layer', event_type=None, delay=3, handler=self.clear_layer)
            
        def clear_layer(self):
             self.layer = None
