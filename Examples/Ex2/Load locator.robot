*** Settings ***
Documentation    Suite description
library  I18nLibrary


*** Test Cases ***
Demo load data from yml file
    # Set locale and fallback
    Set Locale Language    en
    Set Fallback Language    th
    # Force preload specific languages
    Set Pre Load Language    en
    Set Pre Load Language    th
    Load Path Append    ./Resources
    # Force generate test variables
    ${x} =    Generate Suite Variables
    # Log variables
    Log Variables
    # Log    ${login.login}
