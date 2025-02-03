# llm-siliconflow

[![PyPI](https://img.shields.io/pypi/v/llm-siliconflow.svg)](https://pypi.org/project/llm-siliconflow/)
[![Changelog](https://img.shields.io/github/v/release/WanZheng/llm-siliconflow?include_prereleases&label=changelog)](https://github.com/WanZheng/llm-siliconflow/releases)
[![Tests](https://github.com/WanZheng/llm-siliconflow/actions/workflows/test.yml/badge.svg)](https://github.com/WanZheng/llm-siliconflow/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/WanZheng/llm-siliconflow/blob/main/LICENSE)

Access [siliconflow.cn](https://siliconflow.cn/) models via API

## Installation

Install this plugin in the same environment as [LLM](https://llm.datasette.io/).
```bash
llm install llm-siliconflow
```
## Usage

Obtain a [SiliconFlow API key](https://platform.siliconflow.com/api_keys) and save it like this:

```bash
llm keys set siliconflow
# <Paste key here>
```
Run `llm models` to get a list of models.

Run prompts like this:
```bash
llm -m siliconflow/deepseek-chat 'five great names for a pet ocelot'
llm -m siliconflow/deepseek-reasoner 'solve \\int \\frac{\\ln(x)\\arctan(x)}{x^2+1} dx'
llm -m siliconflow/deepseek-coder 'how to reverse a linked list in python'
```

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd llm-siliconflow
python3 -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
llm install -e '.[test]'
```
To run the tests:
```bash
pytest
```
