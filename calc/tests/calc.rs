use calc::*;

// ---------- lexer ----------

#[test]
fn lexes_numbers_and_operators() {
    assert_eq!(
        tokenize("1 + 2.5*(3)"),
        Ok(vec![
            Token::Number(1.0),
            Token::Plus,
            Token::Number(2.5),
            Token::Star,
            Token::LParen,
            Token::Number(3.0),
            Token::RParen,
        ])
    );
}

#[test]
fn lexes_empty_input() {
    assert_eq!(tokenize("   "), Ok(vec![]));
}

#[test]
fn rejects_unknown_char() {
    assert_eq!(tokenize("1 $ 2"), Err(Error::UnexpectedChar('$')));
}

#[test]
fn rejects_malformed_numbers() {
    assert!(tokenize("3.").is_err());
    assert!(tokenize(".5").is_err());
    assert!(tokenize("1.2.3").is_err());
}

// ---------- parser ----------

fn num(n: f64) -> Box<Expr> {
    Box::new(Expr::Num(n))
}

#[test]
fn parses_precedence() {
    let tokens = tokenize("1 + 2 * 3").unwrap();
    assert_eq!(
        parse(&tokens),
        Ok(Expr::Bin(num(1.0), Op::Add, Box::new(Expr::Bin(num(2.0), Op::Mul, num(3.0)))))
    );
}

#[test]
fn parses_left_associative() {
    let tokens = tokenize("8 - 2 - 1").unwrap();
    assert_eq!(
        parse(&tokens),
        Ok(Expr::Bin(Box::new(Expr::Bin(num(8.0), Op::Sub, num(2.0))), Op::Sub, num(1.0)))
    );
}

#[test]
fn parses_parens_and_unary() {
    let tokens = tokenize("-(1 + 2)").unwrap();
    assert_eq!(
        parse(&tokens),
        Ok(Expr::Neg(Box::new(Expr::Bin(num(1.0), Op::Add, num(2.0)))))
    );
}

#[test]
fn parser_errors() {
    assert_eq!(parse(&tokenize("").unwrap()), Err(Error::UnexpectedEof));
    assert_eq!(parse(&tokenize("1 +").unwrap()), Err(Error::UnexpectedEof));
    assert_eq!(parse(&tokenize("(1 + 2").unwrap()), Err(Error::UnexpectedEof));
    assert_eq!(parse(&tokenize("1 2").unwrap()), Err(Error::TrailingInput));
    assert_eq!(
        parse(&tokenize("* 2").unwrap()),
        Err(Error::UnexpectedToken(Token::Star))
    );
    assert_eq!(
        parse(&tokenize("1 + )").unwrap()),
        Err(Error::UnexpectedToken(Token::RParen))
    );
}

// ---------- evaluator / end to end ----------

#[test]
fn evaluates_expressions() {
    assert_eq!(evaluate("1 + 2 * 3"), Ok(7.0));
    assert_eq!(evaluate("(1 + 2) * 3"), Ok(9.0));
    assert_eq!(evaluate("8 - 2 - 1"), Ok(5.0));
    assert_eq!(evaluate("8 / 2 / 2"), Ok(2.0));
    assert_eq!(evaluate("-3 * -2"), Ok(6.0));
    assert_eq!(evaluate("--4"), Ok(4.0));
    assert_eq!(evaluate("1.5 + 1.5"), Ok(3.0));
    assert_eq!(evaluate("1 + 2 * (3 - 4) / 2"), Ok(0.0));
}

#[test]
fn division_by_zero() {
    assert_eq!(evaluate("1 / 0"), Err(Error::DivisionByZero));
    assert_eq!(evaluate("1 / (2 - 2)"), Err(Error::DivisionByZero));
}

#[test]
fn errors_display_something() {
    let msg = evaluate("1 + $").unwrap_err().to_string();
    assert!(!msg.is_empty());
}
