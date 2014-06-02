# General play
# all gameplay items that don't belong to a specific mode

import procgame
import locale
import logging
from os import listdir, walk
from os.path import join, splitext
from time import time
from procgame import *

# Dit importeert alle code uit het bestand 'ramprules.py'
from ramprules import *
from bumpers import *
from visor import *

# all paths
game_path = "C:\P-ROC\pyprocgame-master\games\VXtra_start/"
speech_path = game_path+"sound/speech/"
sound_path = game_path +"sound/fx/"
music_path = game_path +"sound/music/"
dmd_path = game_path +"dmd/"
lampshow_path = game_path +"lampshows/"
supported_sound = ['.wav', '.aiff', '.ogg', '.mp3']

class Generalplay(game.Mode):

        def __init__(self, game, priority):
            super(Generalplay, self).__init__(game, priority)

            # register modes: hij maakt van de code die onder 'Ramp_rules' staat een object. Het nummer gaat over prioriteit die bv belangrijk is voor animaties:
            
            self.ramp_rules = Ramp_rules(self.game, 38)
            self.bumper_rules = Bumpers(self.game, 20)
            self.visor_rules = Visor(self.game, 38)
            self.start_time = 0
            
            self.register_all_sounds()
            #register animation layers
##            self.showroom_text = dmd.TextLayer(70, 22, self.game.fonts['07x5'], "center", opaque=False)
##            self.showroom_bgnd = dmd.FrameLayer(opaque=False, frame=dmd.Animation().load(dmd_path+'showroom.dmd').frames[0])
##            self.showroom_layer = dmd.GroupedLayer(128, 32, [self.showroom_bgnd, self.showroom_text])
##            self.showroom_layer.transition = dmd.PushTransition(direction='north')
##
##            self.ramp_text = dmd.TextLayer(70, 23, self.game.fonts['07x5'], "center", opaque=False)

            #register lampshow
            self.game.lampctrl.register_show('rampenter_show', lampshow_path+"rampenter.lampshow")

            self.lamps_ramp = ['megaScore','Rtimelock','Rlock','Rextraball']
            self.willekeurigevariabele=0

        def reset(self):
             pass
           
        def mode_started(self):
             # Bij het begin start ie dus de code uit het object ramprules 
             self.game.modes.add(self.ramp_rules)
             self.game.modes.add(self.bumper_rules)
             self.game.modes.add(self.visor_rules)
             self.game.sound.play_music('music_starwars_intro', loops=-1)
             self.game.sound.play('speech_Prepare_to_fire')
        
        def register_all_sounds(self):
             # Register all sounds!
             for (dirpath, dirnames, filenames) in walk(speech_path):
                for filename in filenames:
                    if splitext(filename)[1] in supported_sound:
                        sound = "speech_" + splitext(filename)[0].replace(" ", "_")
                        print "SOUND REGISTERED:", sound
                        self.game.sound.register_sound(sound, join(dirpath, filename))
                        
             for (dirpath, dirnames, filenames) in walk(sound_path):
                for filename in filenames:
                    if splitext(filename)[1] in supported_sound:
                        sound = "sound_" + splitext(filename)[0].replace(" ", "_")
                        print "SOUND REGISTERED:", sound
                        self.game.sound.register_sound(sound, join(dirpath, filename))
                        
             for (dirpath, dirnames, filenames) in walk(music_path):
                for filename in filenames:
                    if splitext(filename)[1] in supported_sound:
                        sound = "music_" + splitext(filename)[0].replace(" ", "_")
                        print "SOUND REGISTERED:", sound
                        self.game.sound.register_music(sound, join(dirpath, filename))

        def mode_stopped(self):
             self.game.modes.remove(self.ramp_rules)
             self.game.modes.remove(self.bumper_rules)
             self.game.modes.remove(self.visor_rules)

        def mode_tick(self):
             pass

## lamps and animations

        def update_lamps(self):
             #Steven (ook kan: if self.game.ramp_move.ramp_up:
             # wel gaan hier problemen komen met modes: als die ook de lampjes willen aansturen....daarnaast gaat de lampupdate niet vaak genoeg
             if self.willekeurigevariabele==1:
                self.game.effects.drive_lamp('advance_planet','medium')
             else:
                self.game.effects.drive_lamp('advance_planet','off')




##        def play_spinner(self):
##             # use spinner_turns to select frame, divide with // operator to increase needed turns
##             anim = dmd.Animation().load(dmd_path+'mystery.dmd')
##             self.animation_layer = dmd.FrameLayer(opaque=False, frame=anim.frames[self.spinner_turns//2])
##             self.layer = dmd.GroupedLayer(128, 32, [self.animation_layer])
##             self.delay(name='clear_display', event_type=None, delay=2, handler=self.clear_layer)
##
##        def play_mystery_ready(self):
##            if self.animation_status=='ready':
##                anim = dmd.Animation().load(dmd_path+'mystery_ready.dmd')
##                self.animation_layer = dmd.AnimatedLayer(frames=anim.frames, opaque=False, repeat=True, hold=False, frame_time=10)
##                self.animation_layer.add_frame_listener(-1, self.clear_layer)
##                self.layer = dmd.GroupedLayer(128, 32, [self.animation_layer])
##                self.animation_status = 'running'
               
##        def clear_layer(self):
##             self.layer = None


## mode functions



## Switches regular gameplay
        def sw_shooterLane_open_for_100ms(self,sw):
             self.game.coils.RvisorGI.schedule(schedule=0x0f0f0f0f, cycle_seconds=1, now=True) 
             self.start_time = time()
             self.game.sound.play_music('music_starwars_theme', loops=-1)
             
        def sw_eject_active_for_1400ms(self, sw):
             self.game.coils.Ejecthole_LeftInsBFlash.pulse(40)

        def sw_outhole_active_for_500ms(self, sw):
             self.game.coils.outhole_knocker.pulse(40)

        def sw_slingL_active(self,sw):
             self.game.sound.play("sound_slings")
             self.game.score(100)

        def sw_slingR_active(self,sw):
             self.game.sound.play("sound_slings")
             self.game.score(100)

        def sw_Routlane_active(self,sw):
             self.game.sound.play("sound_evil_laugh")
             self.game.score(25000)
             if time() - 30 < self.start_time:
                     print "GRATIS BAL!"
             
        def sw_Loutlane_active(self,sw):
             self.game.sound.play("sound_evil_laugh")
             self.game.score(25000)
             if time() - 30 < self.start_time:
                     print "GRATIS BAL!"
