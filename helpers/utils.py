class Utility:
    SUPERSCRIPT_MAP = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")
    SUBSCRIPT_MAP = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

    superscript_map = {
        '0': '\u2070',
        '1': '\u00B9',
        '2': '\u00B2',
        '3': '\u00B3',
        '4': '\u2074',
        '5': '\u2075',
        '6': '\u2076',
        '7': '\u2077',
        '8': '\u2078',
        '9': '\u2079',
        '.': '\u00B7',
        'i': '\u2071'
    }

    @staticmethod
    def to_superscript(num):
        return ''.join(Utility.superscript_map[digit] for digit in str(num))


    @staticmethod
    def format_root_of_unity(n, power):
        if power % n == 0:
            return '1'
        exp_text = str((power) % n).translate(Utility.SUPERSCRIPT_MAP)
        return f"ζ{str(n).translate(Utility.SUBSCRIPT_MAP)}{exp_text}"

