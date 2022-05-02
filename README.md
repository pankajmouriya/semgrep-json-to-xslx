# semgrep-json-to-xslx

This repo is created just for the purpose of parsing Semgrep scan findings from JSON to xlsx(spreadsheet). Please note, the script has hardcoded filename `result.json` and columns values. Use accordingly

Example command

`semgrep --config p/python-command-injection --config "p/owasp-top-ten"  --json -o result.json`

Contribute
You are welcome to raise a PR and make this script more aggresive and useful. 
