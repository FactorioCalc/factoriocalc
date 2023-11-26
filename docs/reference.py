import os
import sys
sys.path.insert(0, os.path.abspath('../'))

import factoriocalc as fc
import types
import pdb

def _repr(obj):
    if type(obj) is tuple:
        return '('+', '.join(_repr(o) for o in obj)+')'
    elif isinstance(obj, type):
        return obj.__name__
    else:
        return repr(obj)

def documentSymbol(module, symname, docValue = True):
    sym = getattr(module, symname)

    if isinstance(sym, type):
        if issubclass(sym, Exception):
            return f'.. autoexception:: {symname}\n\n'
        else:
            return f'.. autoclass:: {symname}\n\n'
    elif isinstance(sym, types.FunctionType):
        return f'.. autofunction:: {symname}\n\n'
    else:
        res = [f'.. py:data:: {symname}\n']
        if docValue:
            val = sym
            valstr = _repr(val)
            if symname == valstr:
                res.append(f'   :type: {type(val).__name__}\n')
            else:
                res.append(f'   :value: {valstr}\n')
        res.append('\n')
        return ''.join(res)

def documentSymbols(modulestr, *, also = (), docValues = True):
    module = getattr(fc, modulestr)
    return ''.join(documentSymbol(module, symname, docValue = docValues) for symname in [*module.__all__, *also])

def documentExtraSymbols():
    return ''.join(documentSymbol(fc, symname) for symname in fc._extraSymbols)


# def documentConfigSymbols():
#     module = getattr(fc, 'config')
#     symbols = [sym for sym in dir(module) if not sym.startswith('_')]
#     return ''.join(f'.. py:data:: config.{symname}\n   :type: ContextVar\n' for symname in symbols)

print(f'''.. DO NOT EDIT
.. generated by reference.py

.. default-role:: py:obj
.. highlight:: none

.. |nbsp| unicode:: 0xa0
   :trim:

`factoriocalc` package
======================

.. py:module:: factoriocalc

Main package.  Most symbols in submodules are available in this package.  If a
symbol is not mentioned as belonging to a submodule, the location should be
considered an implementation detail.

Fractions
---------

.. autofunction:: frac

.. autofunction:: div

.. py:class:: Frac

   Class used internally for all calculation, should normally use `frac` to
   create a `Frac`.  See `fracs.Frac` for complete documentation.

Core
----

.. py:currentmodule:: factoriocalc

{documentSymbols('core')}
{documentSymbols('data', docValues = False)}

`mch` module
------------

.. automodule:: factoriocalc.mch
   :no-members:

   .. autofunction:: _find

`itm` module
------------

.. automodule:: factoriocalc.itm
   :no-members:

   .. autofunction:: _find

   When the gameInfo context variable is configured for the base game this module
   also provides a few special items:

   .. py:data:: _combined_research

      Result of `rcp._combined_research <factoriocalc.rcp._combined_research>`.

   .. py:data:: _military_research

      Result of `rcp._military_research <factoriocalc.rcp._military_research>`.

   .. py:data:: _production_research

      Result of `rcp._production_research <factoriocalc.rcp._production_research>`.

`rcp` module
------------

.. automodule:: factoriocalc.rcp
   :no-members:

   .. autofunction:: _find

   When the gameInfo context variable is configured for the base game this module
   also provides some special recipes:

   .. py:data:: space_science_pack

      Recipe to produce 1000 `itm.space_science_pack` in a `RocketSilo <factoriocalc.RocketSilo>`.

   .. py:data:: _combined_research

      Recipe to consume all 7 science packs at a rate of 1/s in a `FakeLab <factoriocalc.FakeLab>`.

   .. py:data:: _military_research

      Recipe to consume all but the production science pack at a rate of 1/s in a
      `FakeLab <factoriocalc.FakeLab>`.

   .. py:data:: _production_research

      Recipe to consume all but the military science pack at a rate of 1/s in a
      `FakeLab <factoriocalc.FakeLab>`.

`config` module
---------------

.. automodule:: factoriocalc.config

`presets` module
----------------

.. automodule:: factoriocalc.presets
   :no-members:

   When the gameInfo context variable is configured for the base game this module
   provides:

   .. py:data:: MP_EARLY_GAME
      :value: {fc.presets.MP_EARLY_GAME!r}

   .. py:data:: MP_LATE_GAME
      :value: {fc.presets.MP_LATE_GAME!r}

   .. py:data:: MP_MAX_PROD
      :value: {fc.presets.MP_MAX_PROD!r}

   .. py:data:: SPEED_BEACON
      :value: {fc.presets.SPEED_BEACON!r}

   .. py:data:: sciencePacks
      :type: set
      :value: {fc.presets.sciencePacks!r}

Units
-----

.. py:currentmodule:: factoriocalc

{documentSymbols('units')}

Boxes and Produce
-----------------

.. py:currentmodule:: factoriocalc

{documentSymbols('_box')}
.. autoclass:: SolveRes
{documentSymbols('_produce')}


.. _blueprints:

Blueprints
----------

.. py:currentmodule:: factoriocalc
{documentSymbols('blueprint')}

JSON Conversion
---------------

.. py:currentmodule:: factoriocalc

{documentSymbols('jsonconv')}

Helpers
-------

.. py:currentmodule:: factoriocalc

{documentSymbols('helper')}

`setGameConfig`
---------------

.. py:currentmodule:: factoriocalc

{documentSymbol(fc.import_, 'setGameConfig')}
{documentSymbol(fc.import_, 'userRecipesFile')}

`mods` module
-------------

.. automodule:: factoriocalc.mods

Miscellaneous
-------------

These symbols are not imported by ``from factorocalc import *``.

.. py:currentmodule:: factoriocalc
{documentExtraSymbols()}

`machine` module
----------------

.. automodule:: factoriocalc.machine

`setGameConfig` internals
-------------------------

.. py:currentmodule:: factoriocalc

These symbols are only useful when adding support for new mods and are not
imported by ``from factorocalc import *``.

{''.join(documentSymbol(fc.import_, symname) for symname in fc.import_.__all__ if symname not in ('setGameConfig', 'userRecipesFile'))}

`fracs` module
--------------

.. py:currentmodule:: factoriocalc.fracs

.. automodule:: factoriocalc.fracs
   :no-members:

{documentSymbols('fracs', also = ['Rational'])}

`solver` module
---------------

.. py:currentmodule:: factoriocalc.solver

.. automodule:: factoriocalc.solver
   :no-members:

{documentSymbols('solver')}
''')

