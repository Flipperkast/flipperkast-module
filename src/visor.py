# Visor

from procgame import *


# all paths
game_path = "C:\P-ROC\pyprocgame-master\games\VXtra_start/"
speech_path = game_path +"sound/speech/"
sound_path = game_path +"sound/fx/"
music_path = game_path +"sound/music/"
dmd_path = game_path +"dmd/"
lampshow_path = game_path +"lampshows/"

class Visor(game.Mode):

        def __init__(self, game, priority):
                super(Visor, self).__init__(game, priority)
				#Niet meer nodig omdat alle geluiden al zijn geregristreerd bij general_play
                #self.game.sound.register_sound('visor_aan', sound_path+"lasergun1.wav")
                #self.game.sound.register_sound('visor_uit', sound_path+"lasergun2.wav")
                self.game.lampctrl.register_show('lampshow_visor' ,lampshow_path +"Pinbot_1.lampshow")
                

        def mode_started(self):
                print "visor_mode started"
                self.colors = ['yellow', 'blue', 'orange', 'green', 'red']
                self.visor = [0,0,0,0,0]
                self.game.lampctrl.play_show('lampshow_visor', repeat=True)

        def mode_stopped(self):
                self.game.lampctrl.stop_show()

                
## switches
        def update_visor(self, num):
                 self.game.lampctrl.stop_show()
                 self.game.sound.play("sound_lasergun2")
                 self.game.score(10)
                 if self.visor[num] < 5: self.visor[num] += 1
                 self.update_lamps()
                 print "Visor", num , "is nu:", self.visor[num]
			 
        def sw_visor1_active(self,sw):
             self.update_visor(0)

        def sw_visor2_active(self,sw):
             self.update_visor(1)
             
        def sw_visor3_active(self,sw):
             self.update_visor(2)
             
        def sw_visor4_active(self,sw):
             self.update_visor(3)
             
        def sw_visor5_active(self,sw):
             self.update_visor(4)

## Lampen

        def update_lamps(self):
                if sum(self.visor) == 25:
                        pass
                for x in range(len(self.visor)):
                        for y in range(self.visor[x]):
                                self.game.effects.drive_lamp(self.colors[x] + str(y+1), 'on')
                

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
