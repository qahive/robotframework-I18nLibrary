*** Settings ***
Documentation    Suite description
library  I18nLibrary

*** Variables ***
${login.login}    ${EMPTY}


*** Test Cases ***
Demo load language from yml file
    # Set locale and fallback
    Set Locale Language    th
    Set Fallback Language    en
    # Force preload specific languages
    Set Pre Load Language    th
    Set Pre Load Language    en
    # Load path
    Load Path Append    ./Resources
    # Force generate test variables
    ${x} =    Generate Test Variables
    # Log variables    
    Log Variables    
    Log    ${login.login}
