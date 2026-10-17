//! See SPEC.md for what to build.

pub mod eval;
pub mod lexer;
pub mod parser;

pub use eval::eval;
pub use lexer::{Token, tokenize};
pub use parser::{Expr, Op, parse};

#[derive(Debug, PartialEq)]
pub enum Error {
    UnexpectedChar(char),
    UnexpectedToken(Token),
    UnexpectedEof,
    TrailingInput,
    DivisionByZero,
}

impl std::fmt::Display for Error {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        todo!("render each variant for humans")
    }
}

impl std::error::Error for Error {}

pub fn evaluate(src: &str) -> Result<f64, Error> {
    todo!("tokenize -> parse -> eval")
}
