# Jenho Spelling Assistant

A small bot that works off slash commands and is hosted on AWS Lambda. 

Users send a slash command, to which the bot then knows to send data to an interactions endpoint on the AWS side. Python code on AWS Lambda then takes the data and sends it back with a proper spellchecked message (if applicable).

## Technologies

Uses PySpellchecker library to correct spellings. Also utilizes Flask to interact with requests sent to interactions endpoint.


