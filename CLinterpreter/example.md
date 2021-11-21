# Using Clinterpreter
This module allows evaluate expressions in left-associative Combinatory Logic.

You can do parenthese matching with `parenthese_match()`. For example, `parenthese_match("(CI(KI))(CIK)")` will return `'(CI(KI))'`.

You can encode strings of CL as Python lists, or vice versa. For example, `encoding("S(CI(KI))(CIK)")` will return `['S', ['C', 'I', ['K', 'I']], ['C', 'I', 'K']]`. Likewise `encoding(["S",["K","S"],"K","x","y","z"])` will return `'S(KS)Kxyz'`.

The following primitive combinators are native to the package and others can easily be added: `I, K, B, C, W, S, Y, M, F`. For example, `S_combinator("xyz")` will return `'xz(yz)'`.

You can do a single reduction of a CL expression with `evaluate()`. For example, `evaluate("S(KS)Kxyz")` will return `'(KS)x(Kx)yz'`.

To evaluate CL expressions until a fixed point is reached you can use `recur()`. Recur also accounts for cycles. Recur has two optional arguments `print_steps` and `write_steps`, which will print each step or write each step, respectively, in the sucessive evaluation of CL expressions.
