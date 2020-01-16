# Copyright 2020 Atthaboon S.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import i18n
from robot.libraries.BuiltIn import BuiltIn


__version__ = '0.1.3'

class I18nLibrary:
    """
    I18nLibrary translator library for support in robotframework
    """
    def __init__(self):
        i18n.config.set('enable_memoization', True)
        i18n.config.set('pre_load_langs', [])
        i18n.set('prefer', '')
        i18n.set('is_prefer', False)
        i18n.resource_loader.init_yaml_loader()

    def load_path_append(self, append_path):
        """
        Auto load language from specific path
        :param append_path:
        :return:
        """
        i18n.load_path.append(append_path)

        # Load lang files to memory
        for lang in i18n.config.get('pre_load_langs'):
            i18n.resource_loader.load_directory(append_path, lang)
            subfolders = self._get_list_of_sub_folders(append_path)
            for folder_path in subfolders:
                i18n.resource_loader.load_directory(folder_path, lang)

    def _get_list_of_sub_folders(self, dirName):
        listOfFile = os.listdir(dirName)
        allFiles = list()
        # Iterate over all the entries
        for entry in listOfFile:
            # Create full path
            fullPath = os.path.join(dirName, entry)
            # If entry is a directory then get the list of files in this directory
            if os.path.isdir(fullPath):
                allFiles.append(fullPath)
                allFiles = allFiles + self._get_list_of_sub_folders(fullPath)
        return allFiles

    def set_pre_load_language(self, language):
        langs = i18n.config.get('pre_load_langs')
        langs.append(language)
        i18n.config.set('pre_load_langs', langs)

    def set_locale_language(self, language):
        i18n.set('locale', language)

    def set_fallback_language(self, language):
        i18n.set('fallback', language)

    def set_prefer_language(self, language):
        i18n.set('prefer', language)
        i18n.set('is_prefer', True)

    def translate_message(self, message):
        return i18n.t(message)

    def translate_message_for_specific_language(self, message, language):
        return i18n.t(message, locale=language)

    def translate_message_with_prefer_language(self, message, second_fallback):
        return i18n.t(message, default=i18n.t(message, locale=second_fallback))

    def generate_suite_variables(self):
        robot_buildIn = BuiltIn()
        is_prefer = i18n.get('is_prefer')
        prefer_lang = i18n.get('prefer')
        keys = self._get_all_unique_keys()
        for key in keys:
            value = ''
            if is_prefer:
                value = self.translate_message_with_prefer_language(key, prefer_lang)
            else:
                value = self.translate_message(key)
            robot_buildIn.set_suite_variable('${'+key+'}', value)

    def _get_all_unique_keys(self):
        key_list = []
        container = i18n.translations.container
        for lang in container.keys():
            lang_dicts = container.get(lang)
            key_list += list(lang_dicts.keys())
        key_set = set(key_list)
        key_unique_list = list(key_set)
        return  key_unique_list
