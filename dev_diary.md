# Dev Diary
> This file serves as a bit of a thought dump of each session I have while coding this project, to help me remember 
> what I did for when it comes to writing the whitepaper


## 16/04/2025 - Getting started

### Summary
- downloaded PyCharm Community Edition & started figuring my way around it
- added a `models` package to hold shared models (CVEs returned from NVD, Actions parsed from GitHub Workflows)
  - used `dataclasses` so that I don't have to bother with `self.field = field` etc...
- created an `httpclients` module containing
  - a `BaseHttpClient` class to handle making `GET`/`POST`
  - some basic logging to refactor later into structured logs
  - some error handling around the `get` method

### Thoughts
