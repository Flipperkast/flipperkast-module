# Bumpers

from procgame import *
import locale

# all paths
game_path = "C:\P-ROC\pyprocgame-master\games\VXtra_start/"
speech_path = game_path +"sound/speech/"
sound_path = game_path +"sound/fx/"
music_path = game_path +"sound/music/"
dmd_path = game_path +"dmd/"

class Droptargets(game.Mode):

        def __init__(self, game, priority):
                super(Droptargets, self).__init__(game, priority)
                
        def mode_started(self):
                self.reset_droptargets()
				self.ejectlampjes = 0

        def mode_stopped(self):
                pass

        def sw_droptarget1_active(self, sw):
                self.handle_droptarget(0)
        def sw_droptarget2_active(self, sw):
                self.handle_droptarget(1)
        def sw_droptarget3_active(self, sw):
                self.handle_droptarget(2)
        def reset_droptargets(self):
				if self.game.switches.droptarget1.is_active() or self.game.switches.droptarget2.is_active() or self.game.switches.droptarget3.is_active():
					self.game.coils.Drops_RightInsBFlash.pulse(80)
				self.droptargets = [False, False, False]	
        def handle_droptarget(self, target):
                self.droptargets[target] = True
                if sum(self.droptargets) == 3:
			self.ejectlampjes += 1
                        self.game.sound.play("sound_droptarget3")
                        self.reset_droptargets()
                else:
                        self.game.score(20)
                        self.game.sound.play("sound_droptarget1_2")
                for x in range(self.ejectlampjes):
                        self.game.effects.drive_lamp('eject' + str(x), 'on')
