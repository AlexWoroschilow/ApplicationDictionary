# -*- coding: utf-8 -*-
# Copyright 2015 Alex Woroschilow (alex.woroschilow@gmail.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import os

from PyQt5 import QtWidgets

from .content import WindowContent


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setContentsMargins(0, 0, 0, 0)
        
        if os.path.exists('css/stylesheet.qss'):
            with open('css/stylesheet.qss') as stream:
                self.setStyleSheet(stream.read())

        self.setWindowTitle('Dictionary')

        self.content = WindowContent(self)
        self.setCentralWidget(self.content)
        
        spacer = QtWidgets.QWidget();
        spacer.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred);
        self.statusBar().addWidget(spacer);

    def addTab(self, name, widget, focus=True):
        if self.content is None or widget is None:
            return None
        
        self.content.addTab(widget, name)

        if focus is not None and focus is True:        
            index = self.content.indexOf(widget) 
            self.content.setCurrentIndex(index)
        