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
        """
        changes the TV from on to off, or off to on
        :return: NA
        """
        self.__status = not self.__status
        self.update_tv()
        self.screen.turn_on(self.__status,self.__channel)

    def mute(self):
        """
        Mutes or Unmutes the TV if the TV is on
        :return: NA
        """
        if self.__status:
            self.__muted = not self.__muted
            self.update_tv()

    def channel_up(self):
        """
        increments the channel up by one if the tv is on, if it is at the maximum channel, it loops it to the minimum
        channel
        :return:NA
        """
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
        """
        increments the channel down by one if the tv is on, if it is at the minimum channel, it loops it to the maximum
        channel
        :return: NA
        """
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
        """
        increments the volume up by one if the tv is on, if it is at the max volume, nothing happens and it stays at max
        volume.
        If the TV is muted, it unmutes the TV and nothing else happens
        :return:NA
        """
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
        """
        increments the volume down by one if the tv is on, if it is at the minimum volume, nothing happens and it stays
        at minimum volume.
        If the TV is muted, it unmutes the TV and nothing else happens
        :return: NA
        """
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
        """
        Creates a string that contains all of the relevant information for the TV
        :return: a string containing power, volume, and channel
        """
        if self.__muted:
            return f"TV status:\nPower = {self.__status}\nChannel = {self.__channel}\nVolume = Muted"
        return f"TV status:\nPower = {self.__status}\nChannel = {self.__channel}\nVolume = {self.__volume}"

    def update_tv(self):
        """
        sets the text label on the remote to the toString method
        :return: NA
        """
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

    def set_channel(self, channel:int):
        """
        Sets the screen Image to the current channel image
        :param channel: current channel
        :return: NA
        """
        self.image_holder.setPixmap(self.channels[channel])

    def turn_on(self, on_or_off:bool, channel:int):
        """
        if TV is turned off sets screen to black
        if TV is turned on sets screen to current channel
        :param on_or_off: boolean that states whether TV is on or off
        :param channel: Current channel 
        :return: NA
        """
        if on_or_off:
            self.image_holder.setPixmap(self.channels[channel])
        else:
            self.image_holder.setPixmap(self.black)
