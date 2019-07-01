# roboforex

Bdswiss bot with python useful for entering new orders at times when you are away from devices connected to the network.
To use the bot you must have an account on the dbswiss broker.


## Installation

- Use the package manager [pip](https://pip.pypa.io/en/stable/) to install selenium, requests and pyfiglet.

```bash
pip install selenium
pip install request
pip install pyfiglet
```
- Download and install [chromedriver](http://chromedriver.chromium.org/downloads/).

## Usage

```python

  # For Login
  bot = Bdswissbot('USERNAME', 'PASSWORD')
  bot.signIn()

  # Start new order
  bot.searchValues(currency, lots, action, lot, sl, tp)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


## License
[MIT](https://choosealicense.com/licenses/mit/)
