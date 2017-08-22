# Destiny API Frameworks
#### Project Goals: 
Build useable frameworks in multiple languages for Bungie's Desitiny API that are self-creating/self-updating from scrapes made by 
the DestinyDevs endpoint scraper.

## Project Information
#### Universal Data
This software scrapes the JSON files provided by https://github.com/DestinyDevs/BungieNetPlatform/
The intent is to take the JSON scrape files and automatically create a set of useable classes and
methods that allows access to the Bungie API for the Destiny video game.

JSON Scrape Source:
https://destinydevs.github.io/BungieNetPlatform/data/api-data.json

ENUMS Scrape Source:
https://destinydevs.github.io/BungieNetPlatform/data/enums.json

Write a class generator for your language of choice.

#### Python Class
class-creator.py scapes the endpoint JSON and creates the endpoints.py framework class.

#### C# Enums
C# Implementation Enums to avoid ManifestDB lookups.
