"""
Commands that write bits of code that is valid for multiple languages
"""

from talon.voice import Context, Key

ctx = Context("general_lang")

ctx.keymap(
    {
        # Operators
        "(op equals | assign | equeft)": " = ",
        "(op (minus | subtract) | deminus)": " - ",
        "(op (plus | add) | deplush)": " + ",
        "(op (times | multiply))": " * ",
        "(op divide | divy)": " / ",
        "([(op | is)] exactly (equal [to] | equals) | triple equals)": " === ",
        "([(op | is)] not exactly (equal [to] | equals) | ranqual | nockle)": " !== ",
        "(op (power | exponent) | to the power [of])": " ** ",
        "op and": " && ",
        "op or": " || ",
        "[op] (arrow | lambo)": "->",
        "[op] fat (arrow | lambo)": " => ",
        # Blocks
        "[brace] block": [" {}", Key("left enter")],
        "(square | brax) block": ["[", Key("enter")],
        "(paren | prex) block": ["(", Key("enter")],
        # Combos
        "coalshock": [":", Key("enter")],
        "comshock": [",", Key("enter")],
        "sinker": [Key("cmd-right ;")],
        "swipe": ", ",
        "coalgap": ": ",
        "[forward] slasher": "// ",
        # Statements
        # Other Keywords
        # Comments
        "comment see": "// ",
        "comment py": "# ",
    }
)
