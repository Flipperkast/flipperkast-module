#
# Effects
#
# Basic mode for general effects and control of game items (lamps, coils, etc.)
# Loaded in startup, so also operational in Attract mode
# 


import procgame
import locale
from procgame import *

game_path = game_path = "C:\P-ROC\pyprocgame-master\games\VXtra_start/"
speech_path = game_path +"sound/speech/"
sound_path = game_path +"sound/fx/"
music_path = game_path +"sound/music/"
dmd_path = game_path +"dmd/"

class Effects(game.Mode):

        def __init__(self, game):
            super(Effects, self).__init__(game, 4)
            self.game.sound.register_sound('ramp_up', sound_path+"rampup.wav")


# Lamp effects

        def drive_lamp_schedule(self, lamp_name, schedule=0x0f0f0f0f, cycle_seconds=0, now=True):
            self.game.lamps[lamp_name].schedule(schedule=schedule, cycle_seconds=cycle_seconds, now=now)

        def drive_lamp(self, lamp_name, style='on',time=2):
            if style == 'slow':
               self.game.lamps[lamp_name].schedule(schedule=0x00ff00ff, cycle_seconds=0, now=True)
            elif style == 'medium':
              self.game.lamps[lamp_name].schedule(schedule=0x0f0f0f0f, cycle_seconds=0, now=True)
            elif style == 'fast':
                self.game.lamps[lamp_name].schedule(schedule=0x55555555, cycle_seconds=0, now=True)
            elif style == 'superfast':
                self.game.lamps[lamp_name].schedule(schedule=0x99999999, cycle_seconds=0, now=True)
            elif style == 'on':
                self.game.lamps[lamp_name].enable()
            elif style == 'off':
                self.game.lamps[lamp_name].disable()
                # also cancel any pending delays
                self.cancel_delayed(lamp_name+'_medium')
                self.cancel_delayed(lamp_name+'_fast')
                self.cancel_delayed(lamp_name+'_superfast')
            elif style == 'smarton':
                self.game.lamps[lamp_name].schedule(schedule=0xaaaaaaaa, cycle_seconds=0, now=True)
                self.delay(name=lamp_name+'_on', event_type=None, delay=0.6, handler=self.game.lamps[lamp_name].enable)
            elif style == 'smartoff':
                self.game.lamps[lamp_name].schedule(schedule=0xaaaaaaaa, cycle_seconds=0, now=True)
                self.delay(name=lamp_name+'_off', event_type=None, delay=0.6, handler=self.game.lamps[lamp_name].disable)
            elif style == 'timeout':
                self.game.lamps[lamp_name].schedule(schedule=0x0f0f0f0f, cycle_seconds=0, now=True)
                if time>10:
                    self.delay(name=lamp_name+'_medium', event_type=None, delay=time-10, handler=self.drive_medium, param=lamp_name)
                if time>5:
                    self.delay(name=lamp_name+'_fast', event_type=None, delay=time-5, handler=self.drive_fast, param=lamp_name)
                if time>1:
                    self.delay(name=lamp_name+'_superfast', event_type=None, delay=time-1, handler=self.drive_super_fast, param=lamp_name)
                self.delay(name=lamp_name+'_off', event_type=None, delay=time, handler=self.game.lamps[lamp_name].disable)

        def drive_super_fast(self, lamp_name):
             self.game.lamps[lamp_name].schedule(schedule=0x99999999, cycle_seconds=0, now=True)

        def drive_fast(self, lamp_name):
             self.game.lamps[lamp_name].schedule(schedule=0x55555555, cycle_seconds=0, now=True)

        def drive_medium(self, lamp_name):
             self.game.lamps[lamp_name].schedule(schedule=0x0f0f0f0f, cycle_seconds=0, now=True)

        def gi_on(self):
             self.game.coils.GIPlayfield.disable()
             self.game.coils.GIInsB.disable()
             self.game.coils.RvisorGI.disable()

        def gi_off(self):
             self.game.coils.GIPlayfield.pulse(0)
             self.game.coils.GIInsB.pulse(0)
             self.game.coils.RvisorGI.pulse(0)

        def gi_blinking(self, schedule=0x0f0f0f0f, cycle_seconds=1, now=True):
             self.game.coils.GIPlayfield.schedule(schedule=schedule, cycle_seconds=cycle_seconds, now=now)
             self.game.coils.GIInsB.schedule(schedule=schedule, cycle_seconds=cycle_seconds, now=now)
             self.game.coils.RvisorGI.schedule(schedule=schedule, cycle_seconds=cycle_seconds, now=now)

##        def update_ramp_lamps(self):
##            # called from ramp_move to update lamps after change in rampstatus
##            # add call to lamp update function for specifik mode
##            self.game.base_game_mode.missions_modes.update_ramp_lamps()

# AC-Select coils

        def ramp_up(self):
             if self.game.switches.rampdown.is_active():
                 self.game.coils.RampRaise_LowPlFlash.pulse(40)
                 self.game.sound.play("ramp_up")
                 print 'rampup'
        def ramp_down(self):
             if self.game.switches.rampdown.is_inactive():
                 self.game.coils.RampLow_EnergyFlash.pulse(35)
                 print 'rampdown'

        def flash_top_mid(self):
             self.game.coils.Solenoidselect.schedule(schedule=0xffffffff, cycle_seconds=0.6, now=True)
             self.game.coils.trough.schedule(schedule=0xff00ff00, cycle_seconds=0.5, now=True)


# Music control

##        def rk_play_music(self, tune='main_theme'):
##             #always fade_out previous music
##             self.game.sound.fadeout_music(time_ms=200)
##             #start selected tune
##             if tune == 'main_theme':
##                 self.game.sound.play_music('main_theme', loops=-1)
##             if tune == 'stop':
##                 self.game.sound.stop_music()

# Ball control

        def flippers(self, flip_on=True):
             if flip_on:
                self.game.coils.flipperEnable.enable()
             else:
                self.game.coils.flipperEnable.disable()

        def release_stuck_balls(self):
             #outhole
             if self.game.switches.outhole.is_active():
                 self.game.coils.outhole_knocker.pulse(30)

        def eject_ball(self, location='all'):
             pass   
             #left eject
##             if location == 'all' or location == 'Leject':
##                if self.game.switches.Leject.is_active():
##                    self.game.coils.Leject.pulse(20)
##
##             #center eject
##             if location == 'all' or location == 'Ceject':
##                if self.game.switches.Ceject.is_active():
##                    self.game.coils.Ceject.pulse(22)
##
##             #upper left kicker
##             if location == 'all' or location == 'upperLkicker':
##                if self.game.switches.upperLkicker.is_active():
##                    self.game.coils.ACselect.pulse(35)
##                    self.game.coils.rearFlash_upLeftkicker.pulse(30)

        def ball_search(self):
             self.game.coils.outhole_knocker.pulse(40)


