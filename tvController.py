from PyQt5.QtWidgets import *
from tvRemote import *
from Labs.src.tvRemoteFinal.screen import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Television(QMainWindow, Ui_remote):

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 4

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.screen = Screen()
        self.screen.show()
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.powerButton.clicked.connect(lambda: self.power())
        self.volumeUpButton.clicked.connect(lambda: self.volume_up())
        self.volumeDownButton.clicked.connect(lambda: self.volume_down())
        self.channelUpButton.clicked.connect(lambda: self.channel_up())
        self.channelDownButton.clicked.connect(lambda: self.channel_down())
        self.muteButton.clicked.connect(lambda: self.mute())

    def power(self):
        self.__status = not self.__status
        self.update_tv()
        self.screen.turn_on(self.__status,self.__channel)

    def mute(self):
        self.__muted = not self.__muted
        self.update_tv()

    def channel_up(self):
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
                self.update_tv()
                self.screen.set_channel(self.__channel)
            else:
                self.__channel += 1
                self.update_tv()
                self.screen.set_channel(self.__channel)

    def channel_down(self):
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
                self.update_tv()
                self.screen.set_channel(self.__channel)
            else:
                self.__channel -= 1
                self.update_tv()
                self.screen.set_channel(self.__channel)




    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.mute()
                self.update_tv()
            elif self.__volume == Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
                self.update_tv()
            else:
                self.__volume += 1
                self.update_tv()

    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.mute()
                self.update_tv()
            elif self.__volume == Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME
                self.update_tv()
            else:
                self.__volume -= 1
                self.update_tv()

    def __str__(self):
        if self.__muted:
            return f"TV status:\nPower = {self.__status}\nChannel = {self.__channel}\nVolume = Muted"
        return f"TV status:\nPower = {self.__status}\nChannel = {self.__channel}\nVolume = {self.__volume}"

    def update_tv(self):
        self.status_label.setText(self.__str__())


class Screen(QMainWindow, Ui_Screen):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()
        self.avatar = QtGui.QPixmap("avatar.jpg").scaled(250, 400)
        self.ferb = QtGui.QPixmap("ferb.jpg").scaled(250, 400)
        self.gravity_falls = QtGui.QPixmap("gravityFalls.jpg").scaled(250, 400)
        self.sherlock = QtGui.QPixmap("sherlock.jpg").scaled(250, 400)
        self.the_clone_wars = QtGui.QPixmap("theCloneWars.jpg").scaled(250, 400)
        self.black = QtGui.QPixmap("black.jpg").scaled(250, 400)
        self.channels = [self.avatar, self.ferb, self.gravity_falls, self.sherlock, self.the_clone_wars]
        self.image_holder.setPixmap(self.black)

    def set_channel(self, channel):
        self.image_holder.setPixmap(self.channels[channel])

    def turn_on(self, on_or_off, channel):
        if on_or_off:
            self.image_holder.setPixmap(self.channels[channel])
        else:
            self.image_holder.setPixmap(self.black)
