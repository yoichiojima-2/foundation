use crate::Error;
use crate::lexer::Token;

#[derive(Debug, Clone, Copy, PartialEq)]
pub enum Op {
    Add,
    Sub,
    Mul,
    Div,
}

#[derive(Debug, PartialEq)]
pub enum Expr {
    Num(f64),
    Neg(Box<Expr>),
    Bin(Box<Expr>, Op, Box<Expr>),
}

pub fn parse(tokens: &[Token]) -> Result<Expr, Error> {
    // Hint: a `Parser { tokens: &[Token], pos: usize }` struct with
    // `peek()` and `next()` methods, and one method per grammar rule.
    todo!()
}
