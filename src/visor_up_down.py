# Visor

from procgame import *


# all paths
game_path = "C:\P-ROC\pyprocgame-master\games\VXtra_start/"
sound_path = game_path +"sound/fx/"
dmd_path = game_path +"dmd/"
lampshow_path = game_path +"lampshows/"

class Visor_up_down(game.Mode):

        def __init__(self, game, priority):
                super(Visor, self).__init__(game, priority)

        def mode_started(self):
                self.visor = self.game.switches.visorClosed.is_active():
                if self.game.current_player().visor_position=='up' and not self.visor:
                        self.visor_up()

        def mode_stopped(self):
                pass

        def visor_move(self):
                self.game.coils.Visormotor.enable()

        def visor_active(self):
                return self.game.switches.visorClosed.is_active()
                
## switches
                
        def sw_visorClosed_active(self,sw):
                self.game.coils.Visormotor.disable()

        def sw_visorOpen_active(self,sw):
                self.game.coils.Visormotor.disable()

