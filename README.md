# python-project-lvl2

<a href="https://codeclimate.com/github/gato-naranja/python-project-lvl2/maintainability"><img src="https://api.codeclimate.com/v1/badges/44b83298ab4181bff76c/maintainability" /></a>
<a href="https://travis-ci.com/github/gato-naranja/python-project-lvl1/jobs/371752498"><img src="https://travis-ci.com/gato-naranja/python-project-lvl2.svg?branch=master" /></a>
<a href="https://codeclimate.com/github/gato-naranja/python-project-lvl2/test_coverage"><img src="https://api.codeclimate.com/v1/badges/44b83298ab4181bff76c/test_coverage" /></a>
<a href="https://actions-badge.atrox.dev/gato-naranja/python-project-lvl2/goto?ref=master"><img alt="Build Status" src="https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Fgato-naranja%2Fpython-project-lvl2%2Fbadge%3Fref%3Dmaster&style=flat" /></a>


## Install package

For install:
```
pip install -i https://test.pypi.org/simple/ gato-naranja-generate-diff --extra-index-url https://pypi.org/simple/
```
<a href="https://asciinema.org/a/lvf8QuQCTsqOLS4ZwH7QDqWbU" target="_blank"><img src="https://asciinema.org/a/lvf8QuQCTsqOLS4ZwH7QDqWbU.svg" /></a>

## Run diff in help mode

You can run package and to see parameters as:
```
$env/bin/gendiff -h
```
<a href="https://asciinema.org/a/IVIgvr1XV6ZPKA7kjPm8cfvbd" target="_blank"><img src="https://asciinema.org/a/IVIgvr1XV6ZPKA7kjPm8cfvbd.svg" /></a>

## Run diff simple files

For compare simple files YAML and JSON formats:
```
$env/bin/gendiff file1.json file2.json
```
or
```
$env/bin/gendiff file1.yaml file2.yaml
```
<a href="https://asciinema.org/a/DpuiMnQsHfvjt7txgAsgQMPpY" target="_blank"><img src="https://asciinema.org/a/DpuiMnQsHfvjt7txgAsgQMPpY.svg" /></a>

## Run diff complex files
For compare complex files YAML and JSON formats:
```
gendiff file1.json file2.json
```
<a href="https://asciinema.org/a/qzFytjjg5K7tHnq1wb1MFa99s" target="_blank"><img src="https://asciinema.org/a/qzFytjjg5K7tHnq1wb1MFa99s.svg" /></a>

## Output diff in plain format
For output diff results in plain format you can use '-f' or '--format' option with the value 'plain':
```
gendiff -f plain file1.json file2.json
```
<a href="https://asciinema.org/a/x2Al0RdAzK1vqOjqq8b6GlCjz" target="_blank"><img src="https://asciinema.org/a/x2Al0RdAzK1vqOjqq8b6GlCjz.svg" /></a>
