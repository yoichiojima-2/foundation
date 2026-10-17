# calc: a tokenizer + recursive-descent parser + evaluator

Goal: turn a string like `1 + 2 * (3 - 4) / 2` into a number, built in three
layers you write by hand. No dependencies, no regex.

## Layer 1: tokenizer (`src/lexer.rs`)

`tokenize(&str) -> Result<Vec<Token>, Error>`

Tokens: `Number(f64)`, `Plus`, `Minus`, `Star`, `Slash`, `LParen`, `RParen`.
Whitespace is skipped. Numbers are digits with an optional single `.`
(`3`, `3.5`; `3.` and `.5` are errors). Any other character is
`Error::UnexpectedChar(c)`.

## Layer 2: parser (`src/parser.rs`)

`parse(&[Token]) -> Result<Expr, Error>`

Grammar (precedence climbs downward, `*` `/` bind tighter than `+` `-`,
everything is left-associative):

```
expr   := term   (("+" | "-") term)*
term   := unary  (("*" | "/") unary)*
unary  := "-" unary | atom
atom   := Number | "(" expr ")"
```

Produce an AST:

```rust
enum Expr {
    Num(f64),
    Neg(Box<Expr>),
    Bin(Box<Expr>, Op, Box<Expr>),
}
enum Op { Add, Sub, Mul, Div }
```

Errors: `Error::UnexpectedToken(Token)` when a token can't start/continue the
current rule, `Error::UnexpectedEof` when input ends mid-expression, and
`Error::TrailingInput` when tokens remain after a complete expression.

## Layer 3: evaluator (`src/eval.rs`)

`eval(&Expr) -> Result<f64, Error>`. Division by zero is
`Error::DivisionByZero`.

## Public API (`src/lib.rs`)

`pub fn evaluate(src: &str) -> Result<f64, Error>` chains the three layers.
`Error` implements `Display` and `std::error::Error`.

## Done when

`cargo test -p calc` passes. Then write `src/main.rs` as a REPL
(read a line, print the result or the error, loop) and try it.

## Stretch

- `^` right-associative exponent (hint: `unary := atom ("^" unary)?` style)
- Error positions: carry a byte offset in `Error` and point at it in output
- Replace `f64` with a `Value` enum and add booleans + comparisons
