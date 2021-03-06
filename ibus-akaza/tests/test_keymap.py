import gi

gi.require_version('IBus', '1.0')

from gi.repository import IBus

from ibus_akaza.keymap import Keymap, KEY_STATE_PRECOMPOSITION, KEY_STATE_CONVERSION


def test_foobar():
    keymap = Keymap()
    keymap.register([KEY_STATE_PRECOMPOSITION], ['C-j'], 'foobar')

    # chr(106) => j
    # chr(74) => J

    assert keymap.get(KEY_STATE_PRECOMPOSITION, ord('j'), IBus.ModifierType.CONTROL_MASK) == 'foobar'


def test_left():
    keymap = Keymap()
    keymap.register([KEY_STATE_CONVERSION], ['S-Left'], 'foobar')

    # chr(106) => j
    # chr(74) => J

    assert keymap.get(KEY_STATE_CONVERSION, IBus.Left, IBus.ModifierType.SHIFT_MASK) == 'foobar'
