#
# Bonus
#
# Calculates end-of-ball bonus
#
__author__="Pieter"
__date__ ="$10 Sep 2012 20:36:37 PM$"


import procgame
import locale
from procgame import *

#all paths
game_path = "C:\P-ROC\pyprocgame-dev\games\VXtra_start/"
speech_path = game_path +"speech/"
sound_path = game_path +"sound/"
music_path = game_path +"music/"
dmd_path = game_path +"dmd/"

class Bonus(game.Mode):
    """docstring for Bonus"""
    def __init__(self, game, priority):
        super(Bonus, self).__init__(game, priority)

        self.bonus_bgnd = dmd.FrameLayer(opaque=False, frame=dmd.Animation().load(dmd_path+'bonus_bgnd.dmd').frames[0])
        self.title_layer = dmd.TextLayer(128/2, 4, self.game.fonts['num_09Bx7'], "center")
        self.value_layer = dmd.TextLayer(128/2, 15, self.game.fonts['num_14x10'], "center")
        self.bonus_layer = dmd.GroupedLayer(128, 32, [self.bonus_bgnd, self.title_layer, self.value_layer])

        self.bonus_counter = 0
        self.delay_time = 2.5

        #self.game.sound.register_music('bonus_tune', music_path+"gaspump_bonus.aiff")

        # check for flippersbuttons pressed at start for faster bonuscount
        if self.game.switches.flipperLwR.is_active() and self.game.switches.flipperLwL.is_active():
            self.delay_time = 0.250
            self.game.coils.flipperEnable.disable()
        else:
            self.delay_time = 2.5

    def mode_started(self):
        # Disable the flippers
        # NOT SYS11: self.game.enable_flippers(enable=False)
        print("Debug, Bonus Mode Started")

    def mode_stopped(self):
        # Enable the flippers
        # NOT SYS11: self.game.enable_flippers(enable=True)
        print("Debug, Bonus Mode Ended")

    def mode_tick(self):
        ## Hit both flippers for faster bonuscount
        if self.game.switches.flipperLwR.is_active() and self.game.switches.flipperLwL.is_active():
            self.delay_time = 0.250
            # disable flippers
            self.game.coils.flipperEnable.disable()

## mode functions

    def get_bonus_miles(self):
            miles = 2 * 10000 #self.game.get_player_stats('miles_collected')
            return miles

    def get_bonus_combos(self):
            ramps =  2 * 50000
            return ramps

    def get_bonus_x(self):
            bonus_x = self.game.get_player_stats('bonus_x')
            return bonus_x

    def calculate(self,callback):
            self.callback = callback
            self.base()

    def base(self):

            self.bonus_x = self.get_bonus_x()
            self.total_base = self.get_bonus_miles()

            if self.bonus_x>1:
                x_display = ' X'+str(self.bonus_x)
            else:
                x_display=''

            self.title_layer.set_text('BONUS MILES'+ x_display)
            self.value_layer.set_text(locale.format("%d", self.total_base, True))
            self.layer = self.bonus_layer

            self.delay(name='bonus_total', event_type=None, delay=self.delay_time, handler=self.combos)

    def combos(self):

            self.bonus_x = self.get_bonus_x()
            self.total_combos = self.get_bonus_combos()

            if self.bonus_x>1:
                x_display = ' X'+str(self.bonus_x)
            else:
                x_display=''

            self.title_layer.set_text('RAMPS'+ x_display)
            self.value_layer.set_text(locale.format("%d", self.total_combos, True))
            self.layer = self.bonus_layer

            self.delay(name='bonus_total', event_type=None, delay=self.delay_time, handler=self.total)

    def total(self):

            if self.bonus_counter == 0:
                total_bonus = (self.total_base * self.bonus_x) + (self.total_combos * self.bonus_x)
                self.title_layer.set_text('TOTAL BONUS',seconds=self.delay_time)
                self.value_layer.set_text(locale.format("%d", total_bonus, True),seconds=self.delay_time)
                self.layer = self.bonus_layer
                self.game.score(total_bonus)

                self.delay(name='bonus_total', event_type=None, delay=self.delay_time, handler=self.total)
                #self.delay(name='bonus_total', event_type=None, delay=self.delay_time, handler=self.callback)
            else:
                self.callback()

            self.bonus_counter += 1
