# RampRules

from procgame import *
import locale

# all paths
game_path = "C:\P-ROC\pyprocgame-master\games\VXtra_start/"
speech_path = game_path +"sound/speech/"
sound_path = game_path +"sound/fx/"
music_path = game_path +"sound/music/"
dmd_path = game_path +"dmd/"

class Ramp_rules(game.Mode):
    # __init__ is wat ie sowieso als eerste uitvoert. Hier kunnen we bv. alle geluiden 'laden'
    def __init__(self, game, priority):
        super(Ramp_rules, self).__init__(game, priority)
        #Dit hoeft niet meer, geluiden worden geregistreerd in general_play
        #self.game.sound.register_sound('ramp_sound', sound_path+"spin6.wav")

    # modestarted net zo: dit doet ie in het begin, beetje dubbelop misschien....

    def mode_started(self):
        print "Eerste code testrules gestart"
        self.game.effects.ramp_down()
        # stel je wilt een variabele gebruiken in de 'ramprules'. Deze wordt nu aan het begin van elke bal (dan wordt 'generalplay' en dus ook 'ramprules' geladen) op 0 gezet. Het aantal onthouden tussen ballen door, kan ook, maar dat moet weer anders.
        self.ramp_aantal_geschoten=0

    def mode_stopped(self):
        print("ramprules gestopt")


## switches

    #In de les gedaan, alleen stond dat toen nog in generalplay.py in plaats van in een losse ramprules.py:
    def sw_rampenter_active(self,sw):
        self.play_animation_spaceship()
        self.game.sound.play("sound_spin6")
        self.game.effects.flash_top_mid()
        self.game.score(5000)

    #Dit is nieuwe code, om wat meer spel te krijgen met echte 'regels' met een variabele verwerkt
    def sw_rampexit_active(self,sw):
        self.game.score(10000)
        self.game.coils.TopFlash3.schedule(schedule=0x0f0f0f0f, cycle_seconds=1, now=True)
        self.game.coils.TopFlash4.schedule(schedule=0xf0f0f0f0, cycle_seconds=1, now=True)
        self.ramp_aantal_geschoten+=1
        print self.ramp_aantal_geschoten
        if self.ramp_aantal_geschoten==4:
            self.game.effects.ramp_up()
            self.delay(name='ramp_countdown', event_type=None, delay=5, handler=self.ramp_count_down)
        self.game.coils.RobotFaceInsB.schedule(schedule=0x0f0f0f0f, cycle_seconds=1, now=True)




## Lampen

    def update_lamps(self):
        if self.ramp_aantal_geschoten==4:
            self.game.effects.drive_lamp('score_energy','slow')
        elif self.ramp_aantal_geschoten==3:
            self.game.effects.drive_lamp('score_energy','medium')
        elif self.ramp_aantal_geschoten==2:
            self.game.effects.drive_lamp('score_energy','fast')
        elif self.ramp_aantal_geschoten==1:
            self.game.effects.drive_lamp('score_energy','superfast')
        else:
            self.game.effects.drive_lamp('score_energy','off')



## Mode functions


    def ramp_count_down(self):
        self.ramp_aantal_geschoten-=1
        print self.ramp_aantal_geschoten
        if self.ramp_aantal_geschoten==0:
            self.game.effects.ramp_down()
        else:
            self.delay(name='ramp_countdown', event_type=None, delay=5, handler=self.ramp_count_down)
        self.update_lamps()


    def sw_scoreEnergy_active(self,sw):
        if self.ramp_aantal_geschoten==4:
            self.game.score(1000000)
            self.energyscore=1000000
        if self.ramp_aantal_geschoten==3:
            self.game.score(500000)
            self.energyscore=500000
        if self.ramp_aantal_geschoten==2:
            self.game.score(250000)
            self.energyscore=250000
        if self.ramp_aantal_geschoten==1:
            self.game.score(100000)
            self.energyscore=100000
        self.game.coils.TopFlash3.schedule(schedule=0x0f0f0f0f, cycle_seconds=1, now=True)
        self.game.coils.TopFlash4.schedule(schedule=0xf0f0f0f0, cycle_seconds=1, now=True)
        self.score_energy_animation()


## Animations

    def play_animation_spaceship(self):
        anim = dmd.Animation().load(dmd_path+'spaceship.dmd')
        self.animation_layer = dmd.AnimatedLayer(frames=anim.frames, opaque=False, repeat=False, hold=False, frame_time=4)
        self.layer = dmd.GroupedLayer(128, 32, [self.animation_layer])
        self.delay(name='clear_layer', event_type=None, delay=6, handler=self.clear_layer)

    def clear_layer(self):
         self.layer = None
