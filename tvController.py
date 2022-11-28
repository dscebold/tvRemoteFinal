from PyQt5.QtWidgets import *
from Labs.src.tvRemoteFinal.tvRemote import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Television(QMainWindow, Ui_remote):

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
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

    def mute(self):
        self.__muted = not self.__muted
        self.update_tv()

    def channel_up(self):
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
                self.update_tv()
            else:
                self.__channel += 1
                self.update_tv()

    def channel_down(self):
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
                self.update_tv()
            else:
                self.__channel -= 1
                self.update_tv()

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
