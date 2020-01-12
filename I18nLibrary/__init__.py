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
import i18n

__version__ = '0.1.0'

class I18nLibrary:
    """
    I18nLibrary translator library for support in robotframework
    """

    def load_path_append(self, append_path):
        """
        Auto load language from specific path
        :param append_path:
        :return:
        """
        i18n.load_path.append(append_path)

    def set_locale_language(self, language):
        i18n.set('locale', language)

    def set_fallback_language(self, language):
        i18n.set('fallback', language)

    def translate_message(self, messsage):
        return i18n.t(messsage)

    def translate_message_for_specific_language(self, messsage, language):
        return i18n.t(messsage, locale=language)

    def translate_message_with_prefer_second_layer_fallback(self, message, second_fallback):
        return i18n.t(message, default=i18n.t(message, locale=second_fallback))
