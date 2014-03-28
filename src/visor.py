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
                super(Visor, self).__init__(game, priority)
                self.game.sound.register_sound('visor_aan', sound_path+"lasergun1.wav")
                self.game.sound.register_sound('visor_uit', sound_path+"lasergun2.wav")
                

        def mode_started(self):
                print "visor_mode started"
                self.visor1=0
                self.visor2=0
                self.visor3=0
                self.visor4=0
                self.visor5=0

        def mode_stopped(self):
                pass

                
## switches
                
        def sw_visor1_active(self,sw):
                if self.visor1==0:
                        self.game.sound.play("visor_uit")
                        self.visor1=1
                if self.visor1==1:
                        self.game.sound.play("visor_aan")
                self.game.score(100)
                self.update_lamps()

        def sw_visor2_active(self,sw):
             self.game.sound.play("visor_uit")
             self.game.score(10)
             self.visor2 += 1
             print "Visor 2 is nu: " , self.visor2
             
        def sw_visor3_active(self,sw):
             self.game.sound.play("visor_uit")
             self.game.score(10)
             self.visor3 += 1
             print "Visor 3 is nu: " , self.visor3
             
        def sw_visor4_active(self,sw):
             self.game.sound.play("visor_uit")
             self.game.score(10)
             self.visor4 += 1
             print "Visor 4 is nu: " , self.visor4
             
        def sw_visor5_active(self,sw):
             self.game.sound.play("visor_uit")
             self.game.score(10)
             self.visor5 += 1
             print "Visor 5 is nu: " , self.visor5




## Lampen

        def update_lamps(self):
                if self.visor1==1:
                        self.game.effects.drive_lamp('yellow1','on')
                        self.game.effects.drive_lamp('yellow2','on')
                        self.game.effects.drive_lamp('yellow3','on')
                        self.game.effects.drive_lamp('yellow4','on')
                        self.game.effects.drive_lamp('yellow5','on')
                else:
                        self.game.effects.drive_lamp('yellow1','medium')
                        self.game.effects.drive_lamp('yellow2','medium')
                        self.game.effects.drive_lamp('yellow3','medium')
                        self.game.effects.drive_lamp('yellow4','medium')
                        self.game.effects.drive_lamp('yellow5','medium')

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
