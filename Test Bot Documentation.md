# Test Bot Documentation

## Components

- main.py
- Constants.py

## main.py

The bot is using the telebot library given by telegram it uses the API_KEY also given by telegram which can be found in Constans.py.

This bot is handling the following commands:
| Command | description  |
|----- | -----|
| /start | Starting message of the bot |
| /help | Lists commands and explenation of the link evaluation  | 
| /sendTestLinks | Sends 2 Links; Developer tool which was used for testing   |
| /ok <link1> ; <link2> ; <link n> | Will forward links to assigned groups [OK_Group] found in Constatns.py |
| /notOK <link1> ; <link2> ; <link n> | Will forward links to assigned groups [Not_OK_Group] found in Constatns.py |
| /ListOKGroups | List the chat_id of [OK_Group] found in Constatns.py|
| /ListNotOKGroups | List the chat_id of [Not_OK_Group] found in Constatns.py|

## Constants.py

The Constatns file is used to hold the following Items:

| Item | description  |
|----- | -----|
|API_KEY | The API_KEY of the Bot|
|OK_Group | Holds the chat_id's of the groups the bot is supposed to send the messages to if the link is ok; This item is an array which can be expanded. The sending to multiple groups has already been implemented to main.py|
|Not_OK_Group | Holds the chat_id's of the groups the bot is supposed to send the messages to if the link is not ok; This item is an array which can be expanded. The sending to multiple groups has already been implemented to main.py|
## Plugins

Dillinger is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| GitHub | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |

