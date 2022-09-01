# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->
## [0.4.0](https://github.com/cognitivefactory/interactive-clustering-gui/releases/tag/0.4.0) - 2022-09-01

<small>[Compare with 0.3.0](https://github.com/cognitivefactory/interactive-clustering-gui/compare/0.3.0...0.4.0)</small>

### Bug Fixes
- correct expected status for constraints approval in js ([8c8ed8d](https://github.com/cognitivefactory/interactive-clustering-gui/commit/8c8ed8df2b9523b24517353de263062fe231d181) by SCHILD Erwan).

### Build
- update flake8 (incompatibilities) ([3b9461d](https://github.com/cognitivefactory/interactive-clustering-gui/commit/3b9461d77337c5c6925c74711f7e659e302722e7) by SCHILD Erwan).

### Code Refactoring
- add confirmation when modify annotation in html/js ([9c2dbdb](https://github.com/cognitivefactory/interactive-clustering-gui/commit/9c2dbdba397605ba754b78fd32b550339ce910c9) by SCHILD Erwan).
- change constraints summary default order in js ([a0b94b0](https://github.com/cognitivefactory/interactive-clustering-gui/commit/a0b94b077f1b349b631680161fccbbd326da1c2a) by SCHILD Erwan).
- move welcome page to '/' ([ae94345](https://github.com/cognitivefactory/interactive-clustering-gui/commit/ae943458530a22b7651813bdb71ae6fe11897b87) by SCHILD Erwan).
- pyproject.toml ([a8b0323](https://github.com/cognitivefactory/interactive-clustering-gui/commit/a8b032322f416acee1751af7edd5588a13351d1f) by SCHILD Erwan).

### Features
- add direct link to constraints to annotate, with some ux refactor ([9522360](https://github.com/cognitivefactory/interactive-clustering-gui/commit/9522360325b9482bb659a62d02aa293905d1c848) by SCHILD Erwan).


## [0.3.0](https://github.com/cognitivefactory/interactive-clustering-gui/releases/tag/0.3.0) - 2022-08-26

<small>[Compare with 0.2.1](https://github.com/cognitivefactory/interactive-clustering-gui/compare/0.2.1...0.3.0)</small>

### Build
- config for command line input ([36351ab](https://github.com/cognitivefactory/interactive-clustering-gui/commit/36351abd5805fd061272e075eaabb47638981b29) by Erwan SCHILD).

### Code Refactoring
- remove test for cli ([3dc8291](https://github.com/cognitivefactory/interactive-clustering-gui/commit/3dc82918c47ca09fce23e510fabea8705d08513c) by Erwan SCHILD).
- update config for command line input ([6a5c573](https://github.com/cognitivefactory/interactive-clustering-gui/commit/6a5c573837c1acb17d1240b76726d8a8ee6c0d10) by Erwan SCHILD).
- make format ([3e16a95](https://github.com/cognitivefactory/interactive-clustering-gui/commit/3e16a95f3c018ee4576c3fde13e29a6858840e7a) by Erwan SCHILD).

### Features
- add a command line to run the app ([7957239](https://github.com/cognitivefactory/interactive-clustering-gui/commit/795723933d9ded7129122bf8ab36f7d16a06a540) by Erwan SCHILD).

## [0.2.1](https://github.com/cognitivefactory/interactive-clustering-gui/releases/tag/0.2.1) - 2022-08-25

<small>[Compare with 0.2.0](https://github.com/cognitivefactory/interactive-clustering-gui/compare/0.2.0...0.2.1)</small>

### Bug Fixes
- remove direct dependency to spacy-models/fr-core-news-md ([f02894d](https://github.com/cognitivefactory/interactive-clustering-gui/commit/f02894ddf67a5bc11263706e4561c8f70dfb9bf9) by Erwan SCHILD).

## [0.2.0](https://github.com/cognitivefactory/interactive-clustering-gui/releases/tag/0.2.0) - 2022-08-25

<small>[Compare with 0.1.3](https://github.com/cognitivefactory/interactive-clustering-gui/compare/0.1.3...0.2.0)</small>

### Bug Fixes
- handle timezone and pickle5 ([abad506](https://github.com/cognitivefactory/interactive-clustering-gui/commit/abad5062afb20b3ad7e0ef9d79e9f99b3f99a71d) by Erwan SCHILD).

### Build
- add .gitignore ([14addf6](https://github.com/cognitivefactory/interactive-clustering-gui/commit/14addf6fa09944ee0aa66336dff80e50aa8c1ec5) by Erwan SCHILD).
- update pyproject.toml with url dependencies ([e2c147a](https://github.com/cognitivefactory/interactive-clustering-gui/commit/e2c147a2cb38f2e89c16cf92c8dd517460b6a29d) by Erwan SCHILD).
- update copier-pdm template to 0.9.10 ([fa67838](https://github.com/cognitivefactory/interactive-clustering-gui/commit/fa678388f534a279c1d71ad840e63540dc079885) by Erwan SCHILD).

### Code Refactoring
- remove MVP app ([6173cde](https://github.com/cognitivefactory/interactive-clustering-gui/commit/6173cde665b9f1aeccb96c136ce0a95844f7dacb) by Erwan SCHILD).

### Features
- implementation of web application (background tasks, constraints annotation, conflicts resolution) ([c51c2bd](https://github.com/cognitivefactory/interactive-clustering-gui/commit/c51c2bd94f525b5997a320ad5148d7148a62be6b) by Erwan SCHILD).
- MVP sans parametres ([c39591e](https://github.com/cognitivefactory/interactive-clustering-gui/commit/c39591eddcbcdce3b4bd7e96f8c8dfbdc6fcdf8d) by Clémentine Misiak).

## [0.1.3](https://github.com/cognitivefactory/interactive-clustering-gui/releases/tag/0.1.3) - 2021-09-01

<small>[Compare with 0.1.2](https://github.com/cognitivefactory/interactive-clustering-gui/compare/0.1.2...0.1.3)</small>

### Build
- update project from poetry to pdm ([845aa72](https://github.com/cognitivefactory/interactive-clustering-gui/commit/845aa725dac169fb400d69ee4f200033e3d1972a) by Erwan SCHILD).
- update .gitignore with migration from poetry to pdm ([3b5999b](https://github.com/cognitivefactory/interactive-clustering-gui/commit/3b5999bb3a1f147077477a33e7c55c56863fa119) by Erwan SCHILD).
- prepare migration from poetry to pdm ([371cb99](https://github.com/cognitivefactory/interactive-clustering-gui/commit/371cb99a4e6c22285a38f510a524859c705702f6) by Erwan SCHILD).

### Code Refactoring
- add py.typed file ([7017f8f](https://github.com/cognitivefactory/interactive-clustering-gui/commit/7017f8fdfe463e736e8bc5020ae2ec677ad3b9cb) by Erwan SCHILD).

## [0.1.2](https://github.com/cognitivefactory/interactive-clustering-gui/releases/tag/0.1.2) - 2021-05-19

<small>[Compare with 0.1.1](https://github.com/cognitivefactory/interactive-clustering-gui/compare/0.1.1...0.1.2)</small>

### Build
- update pyproject.toml with dependencies ([46391c7](https://github.com/cognitivefactory/interactive-clustering-gui/commit/46391c76d1e2f7b7c1f45378805168ef2a3891ec) by Erwan SCHILD).

## [0.1.1](https://github.com/cognitivefactory/interactive-clustering-gui/releases/tag/0.1.1) - 2021-05-18

<small>[Compare with 0.1.0](https://github.com/cognitivefactory/interactive-clustering-gui/compare/0.1.0...0.1.1)</small>

## [0.1.0](https://github.com/cognitivefactory/interactive-clustering-gui/releases/tag/0.1.0) - 2021-05-18

<small>[Compare with first commit](https://github.com/cognitivefactory/interactive-clustering-gui/compare/e6a9c56c7926cb54b1b0d005c1b0c2d1b6f17ce9...0.1.0)</small>

### Build
- correct install sources ([4c3d590](https://github.com/cognitivefactory/interactive-clustering-gui/commit/4c3d59099d65ce856d43bdde548881d707f1f36c) by Erwan SCHILD).
- init package ([83c57bb](https://github.com/cognitivefactory/interactive-clustering-gui/commit/83c57bb93fe6836ddc060209a24b78e728cec369) by Erwan SCHILD).
- initialize repository ([e6a9c56](https://github.com/cognitivefactory/interactive-clustering-gui/commit/e6a9c56c7926cb54b1b0d005c1b0c2d1b6f17ce9) by Erwan SCHILD).
