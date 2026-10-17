use crate::Error;

#[derive(Debug, Clone, PartialEq)]
pub enum Token {
    Number(f64),
    Plus,
    Minus,
    Star,
    Slash,
    LParen,
    RParen,
}

pub fn tokenize(src: &str) -> Result<Vec<Token>, Error> {
    // Hint: iterate with `src.chars().peekable()` so you can look ahead
    // while reading a number without consuming the next char.
    todo!()
}
