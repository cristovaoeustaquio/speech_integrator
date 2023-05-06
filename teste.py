# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

"""
PySide6 port of Qt6 example examples/multimedia/audiosources

Audio Devices demonstrates how to create a simple application to list and test
the configuration for the various audio devices available on the target device
or desktop PC.

Note: This Python example is not fully complete as compared to its C++ counterpart.
Only the push mode works at the moment. For the pull mode to work, the class
QIODevice have python bindings that needs to be fixed.
"""
import sys
from typing import Optional

import PySide6
from PySide6.QtCore import QByteArray, QIODevice, QMargins, QRect, Qt, Signal, Slot
from PySide6.QtGui import QPainter, QPalette
from PySide6.QtMultimedia import (
    QAudio,
    QAudioDevice,
    QAudioFormat,
    QAudioSource,
    QMediaDevices,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QPushButton,
    QSlider,
    QVBoxLayout,
    QWidget,
)



class InputTest(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.m_devices = QMediaDevices(self)
        self.m_pullMode = False

        self.initialize_window()
        self.initialize_audio(QMediaDevices.defaultAudioInput())

    def initialize_window(self):
        self.layout = QVBoxLayout(self)

        self.m_device_box = QComboBox(self)
        default_device_info = QMediaDevices.defaultAudioInput()
        self.m_device_box.addItem(
            default_device_info.description(), default_device_info
        )

        for device_info in self.m_devices.audioInputs():
            if device_info != default_device_info:
                self.m_device_box.addItem(device_info.description(), device_info)

        self.m_device_box.activated[int].connect(self.device_changed)
        self.layout.addWidget(self.m_device_box)

        self.m_volume_slider = QSlider(Qt.Horizontal, self)
        self.m_volume_slider.setRange(0, 100)
        self.m_volume_slider.setValue(100)
        self.m_volume_slider.valueChanged.connect(self.slider_changed)
        self.layout.addWidget(self.m_volume_slider)

        self.m_mode_button = QPushButton(self)
        self.m_mode_button.clicked.connect(self.toggle_mode)
        self.layout.addWidget(self.m_mode_button)

        self.m_suspend_resume_button = QPushButton(self)
        self.m_suspend_resume_button.clicked.connect(self.toggle_suspend)
        self.layout.addWidget(self.m_suspend_resume_button)

    def initialize_audio(self, device_info: QAudioDevice):
        format = QAudioFormat()
        format.setSampleRate(8000)
        format.setChannelCount(1)
        format.setSampleFormat(QAudioFormat.Int16)

        self.m_audio_input = QAudioSource(device_info, format)
        initial_volume = QAudio.convertVolume(
            self.m_audio_input.volume(),
            QAudio.LinearVolumeScale,
            QAudio.LogarithmicVolumeScale,
        )
        self.m_volume_slider.setValue(int(round(initial_volume * 100)))
        self.toggle_mode()

    @Slot()
    def toggle_mode(self):
        self.m_audio_input.stop()
        self.toggle_suspend()

        self.m_mode_button.setText("Enable pull mode")
        io = self.m_audio_input.start()

    @Slot()
    def toggle_suspend(self):
        # toggle suspend/resume
        state = self.m_audio_input.state()
        if (state == QAudio.SuspendedState) or (state == QAudio.StoppedState):
            self.m_audio_input.resume()
            self.m_suspend_resume_button.setText("Suspend recording")
        elif state == QAudio.ActiveState:
            self.m_audio_input.suspend()
            self.m_suspend_resume_button.setText("Resume recording")
        # else no-op

    @Slot(int)
    def device_changed(self, index):
        self.m_audio_input.stop()
        self.m_audio_input.disconnect(self)
        self.initialize_audio(self.m_device_box.itemData(index))

    @Slot(int)
    def slider_changed(self, value):
        linearVolume = QAudio.convertVolume(
            value / float(100), QAudio.LogarithmicVolumeScale, QAudio.LinearVolumeScale
        )

        self.m_audio_input.setVolume(linearVolume)


app = QApplication(sys.argv)
app.setApplicationName("Audio Sources Example")
input = InputTest()
input.show()
sys.exit(app.exec())