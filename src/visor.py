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
                self.game.lampctrl.register_show('lampshow_visor' ,lampshow_path +"Pinbot_1.lampshow")
                

        def mode_started(self):
                print "visor_mode started"
                self.visor1=0
                self.visor2=0
                self.visor3=0
                self.visor4=0
                self.visor5=0
                self.game.lampctrl.play_show('lampshow_visor', repeat=True)

        def mode_stopped(self):
                self.game.lampctrl.stop_show()

                
## switches
                
        def sw_visor1_active(self,sw):
             self.game.lampctrl.stop_show()   
             self.game.sound.play("visor_uit")
             self.game.score(10)
             if self.visor1 < 5: self.visor1 += 1
             self.update_lamps()
             print "Visor 1 is nu: " , self.visor1

        def sw_visor2_active(self,sw):
             self.game.lampctrl.stop_show()   
             self.game.sound.play("visor_uit")
             self.game.score(10)
             if self.visor2 < 5: self.visor2 += 1
             self.update_lamps()
             print "Visor 2 is nu: " , self.visor2
             
        def sw_visor3_active(self,sw):
             self.game.lampctrl.stop_show()   
             self.game.sound.play("visor_uit")
             self.game.score(10)
             if self.visor3 < 5: self.visor3 += 1
             self.update_lamps()
             print "Visor 3 is nu: " , self.visor3
             
        def sw_visor4_active(self,sw):
             self.game.lampctrl.stop_show()
             self.game.sound.play("visor_uit")
             self.game.score(10)
             if self.visor4 < 5: self.visor4 += 1
             self.update_lamps()
             print "Visor 4 is nu: " , self.visor4
             
        def sw_visor5_active(self,sw):
             self.game.lampctrl.stop_show()   
             self.game.sound.play("visor_uit")
             self.game.score(10)
             if self.visor5 < 5: self.visor5 += 1
             self.update_lamps()
             print "Visor 5 is nu: " , self.visor5




## Lampen

        def update_lamps(self):
                if self.visor1 + self.visor2 + self.visor3 + self.visor4 + self.visor5 == 25:
                        
                for x in range(self.visor1):
                        self.game.effects.drive_lamp('yellow' + str(x+1), 'on')
                for x in range(self.visor2):
                        self.game.effects.drive_lamp('blue' + str(x+1), 'on')
                for x in range(self.visor3):
                        self.game.effects.drive_lamp('orange' + str(x+1), 'on')
                for x in range(self.visor4):
                        self.game.effects.drive_lamp('green' + str(x+1), 'on')
                for x in range(self.visor5):
                        self.game.effects.drive_lamp('red' + str(x+1), 'on')

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
