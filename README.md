# Backtrader Wrapper

It is a Backtrader wrapper to implement trading strategies.

Also, you can find some example strategies implemented.

# Deploy (python 3.7)

```sh
$ git clone https://github.com/Python-para-Trading/wrapper-backtrader.git
$ cd wrapper-backtrader
$ virtualenv -p python3.7 env
$ source env/bin/activate
$ pip install -r requirements.txt
```

# Run

```sh
$ python run.py
```

# Advanced use

You can modify the `settings.py` file to run strategies with different
configurations.

You can write your own strategy on a new file in `strategies` folder and import
this strategy in strategies/__init__.py
After, you can use your strategy on the parameter 'strategy' in settings.CONFIG.

# Define tu propia estrategia paso a paso:

1 - Escribimos nuestra estrategia en un fichero python situado en la carpeta `strategies`.

2 - Importamos nuestra estrategia en `strategies.__init__.py`. Ejemplo:

from .nombre_fichero import NombreEstrategia

3 - En el `settings.py` modificamos la variable CONFIG['strategies'] para añadir nuestra estrategia.

4 - Ejecutamos el wrapper mediante:

python run.py


# TODO:

* Documentation for settings
* Improve 'optimization' mode: https://backtest-rookies.com/2017/06/26/optimize-strategies-backtrader/ (code 3)
* ML strategy utils
* 'walk_forward', 'paper', 'live' modes utils
* Communication module with Darwinex: https://github.com/darwinex/dwx-zeromq-connector/
* Communication module with IB
* PyMC3 strategy utils
* Implement Sortino Ratio like a new analyzer on Backtrader: https://backtest-rookies.com/2017/11/08/backtrader-creating-analyzers/
* pep8 linter(flake8)
* codecov
