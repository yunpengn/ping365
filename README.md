# ping365

[![CI pipeline](https://github.com/yunpengn/ping365/workflows/CI%20pipeline/badge.svg)](https://github.com/yunpengn/ping365/actions)
[![Ping APIs](https://github.com/yunpengn/ping365/workflows/Ping%20APIs/badge.svg)](https://github.com/yunpengn/ping365/actions)

A simple toolkit to automatically & periodically ping Office 365 APIs.

## How does it work

The mechanism of this application is so easy that it is very hard to explain.

## Setup Instructions

- Create a virtual environment `virtualenv .venv`.
- Enter the virtual environment `source .venv/bin/activate`.
- Install dependencies `pip3 install -r requirements.txt`.
- Export environment variables:
```bash
export APP_ID=<value_here>
export APP_SECRET=<value_here>
export APP_REFRESH_TOKEN=<value_here>
```

## Licence

[GNU General Public Licence 3.0](LICENSE)
