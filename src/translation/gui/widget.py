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
import functools

from PyQt5 import QtWidgets as QtGui
from PyQt5 import QtCore

from .bar import ToolbarWidget
from .bar import StatusbarWidget
from .list import TranslationListWidget
from .browser import TranslationWidget


class TranslatorWidget(QtGui.QWidget):
    _bright = False
    _actions = False

    def __init__(self):
        """

        :param actions: 
        """
        super(TranslatorWidget, self).__init__()
        self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)

        self.toolbar = ToolbarWidget()
        self.status = StatusbarWidget()

        self.translation = TranslationWidget(self)
        self.translations = TranslationListWidget(self)

        self.layout = QtGui.QVBoxLayout(self)
        self.layout.addWidget(self.toolbar, -1)

        splitter = QtGui.QSplitter(self)
        splitter.addWidget(self.translations)
        splitter.addWidget(self.translation)

        self.layout.addWidget(splitter, 1)

        self.layout.addWidget(self.status, -1)

    def setText(self, text):
        """

        :param text: 
        :return: 
        """
        self.toolbar.setText(text)

    def clearTranslation(self):
        """
        
        :return: 
        """
        self.translation.clear()

    def addTranslation(self, translation):
        """
        
        :param translation: 
        :return: 
        """
        self.translation.addTranslation(translation)

    def setTranslation(self, collection):
        """
        
        :param translation: 
        :return: 
        """
        self.translation.setTranslation(collection)

    def clearSuggestion(self):
        """

        :return: 
        """
        self.translations.clear()
        self.status.text(self.tr('Total: %s words') % 0)

    def addSuggestion(self, suggestion):
        """
        
        :param suggestions: 
        :return: 
        """
        self.translations.append(suggestion)
        self.status.text(self.tr('Total: %s words') % self.translations.model().rowCount())

    def setSuggestions(self, suggestions):
        """

        :param translation: 
        :return: 
        """
        self.translations.setSuggestions(suggestions)
        self.status.text('Total: %s words' % self.translations.model().rowCount())

    def onSearchString(self, action):
        """
        
        :param action: 
        :return: 
        """
        self.toolbar.onActionSearch(functools.partial(
            self._onSearchString, action=action, textfield=(self.toolbar.search)
        ))

    def _onSearchString(self, action, textfield):
        """
        
        :param event: 
        :return: 
        """
        if action is not None:
            action(textfield.text())

    def onSuggestionSelected(self, action):
        """
        
        :param action: 
        :return: 
        """
        self.translations.selectionChanged = functools.partial(
            self._onSuggestionSelected, action=(action)
        )

    def _onSuggestionSelected(self, current, previous, action=None):
        """
        
        :param current: 
        :param previous: 
        :param action: 
        :return: 
        """
        for index in self.translations.selectedIndexes():
            entity = self.translations.model().itemFromIndex(index)
            if action is not None:
                action(entity.text())
