import sympy


GREEK_LETTER_MAP = {
    # Alpha
    'α': 'alpha',
    '\\alpha': 'alpha',
    '\\char"000391': 'alpha',
    
    # Beta
    'β': 'beta',
    '\\beta': 'beta',
    '\\char"000392': 'beta',
    
    # Gamma
    'γ': 'gamma',
    '\\gamma': 'gamma',
    'Γ': 'Gamma',
    '\\Gamma': 'Gamma',
    
    # Delta
    'δ': 'delta',
    '\\delta': 'delta',
    'Δ': 'Delta',
    '\\Delta': 'Delta',
    
    # Epsilon
    'ε': 'epsilon',
    '\\epsilon': 'epsilon',
    '\\char"000190': 'epsilon',
    'ϵ': 'varepsilon',
    '\\varepsilon': 'varepsilon',
    
    # Zeta
    'ζ': 'zeta',
    '\\zeta': 'zeta',
    '\\char"000396': 'zeta',
    
    # Eta
    'η': 'eta',
    '\\eta': 'eta',
    '\\char"000397': 'eta',
    
    # Theta
    'θ': 'theta',
    '\\theta': 'theta',
    'Θ': 'Theta',
    '\\Theta': 'Theta',
    'ϑ': 'vartheta',
    '\\vartheta': 'vartheta',
    
    # Iota
    'ι': 'iota',
    '\\iota': 'iota',
    '\\char"000399': 'iota',
    
    # Kappa
    'κ': 'kappa',
    '\\kappa': 'kappa',
    '\\char"00039A': 'kappa',
    
    # Lambda
    'λ': 'lambda',
    '\\lambda': 'lambda',
    'Λ': 'Lambda',
    '\\Lambda': 'Lambda',
    
    # Mu
    'μ': 'mu',
    '\\mu': 'mu',
    '\\char"00039C': 'mu',
    
    # Nu
    'ν': 'nu',
    '\\nu': 'nu',
    '\\char"00039D': 'nu',
    
    # Xi
    'ξ': 'xi',
    '\\xi': 'xi',
    'Ξ': 'Xi',
    '\\Xi': 'Xi',
    
    # Omicron
    'ο': 'omicron',
    '\\omicron': 'omicron',
    '\\char"00039F': 'omicron',
    
    # Pi
    'π': 'pi',
    '\\pi': 'pi',
    'Π': 'Pi',
    '\\Pi': 'Pi',
    'ϖ': 'varpi',
    '\\varpi': 'varpi',
    
    # Rho
    'ρ': 'rho',
    '\\rho': 'rho',
    '\\char"0003A1': 'rho',
    'ϱ': 'varrho',
    '\\varrho': 'varrho',
    
    # Sigma
    'σ': 'sigma',
    '\\sigma': 'sigma',
    'Σ': 'Sigma',
    '\\Sigma': 'Sigma',
    'ς': 'varsigma',
    '\\varsigma': 'varsigma',
    
    # Tau
    'τ': 'tau',
    '\\tau': 'tau',
    '\\char"0003A4': 'tau',
    
    # Upsilon
    'υ': 'upsilon',
    '\\upsilon': 'upsilon',
    'Υ': 'Upsilon',
    '\\Upsilon': 'Upsilon',
    
    # Phi
    'φ': 'phi',
    '\\phi': 'phi',
    'Φ': 'Phi',
    '\\Phi': 'Phi',
    'ϕ': 'varphi',
    '\\varphi': 'varphi',
    
    # Chi
    'χ': 'chi',
    '\\chi': 'chi',
    '\\char"0003A7': 'chi',
    
    # Psi
    'ψ': 'psi',
    '\\psi': 'psi',
    'Ψ': 'Psi',
    '\\Psi': 'Psi',
    
    # Omega
    'ω': 'omega',
    '\\omega': 'omega',
    'Ω': 'Omega',
    '\\Omega': 'Omega'
}

sympy_singleton_map = {
    'pi': sympy.S.Pi,
}

def get_symbol(latex_str: str, is_real: bool | None = True):
    latex_str = latex_str.strip()
    letter = GREEK_LETTER_MAP.get(latex_str)
    if letter is None:
        letter = latex_str

    if latex_str.startswith('\\'):
        letter = latex_str[1:]
    
    if letter in sympy_singleton_map:
        return sympy_singleton_map[letter]
    else:
        return sympy.Symbol(letter, real=is_real)