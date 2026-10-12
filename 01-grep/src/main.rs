fn read_file(file: &str) -> Result<String, std::io::Error> {
    std::fs::read_to_string(file)
}

fn search<'a>(query: &str, contents: &'a str) -> Vec<&'a str> {
    let mut res = Vec::new();
    for line in contents.lines() {
        if line.contains(query) {
            res.push(line);
        }
    }
    res
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let args: Vec<String> = std::env::args().collect();
    let query = args.get(1).ok_or("usage minigrep <query> <file>")?;
    let file = args.get(2).ok_or("usage minigrep <query> <file>")?;
    let contents = read_file(file)?;
    for line in search(query, &contents) {
        println!("{line}");
    }
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn finds_one_line() {
        let query = "hello";
        let contents = "hello world";
        let result = search(query, contents);
        assert_eq!(result, vec!["hello world"]);
    }

    #[test]
    fn skips_non_matching_lines() {
        let query = "hello";
        let contents = "hello world\nbye world";
        let result = search(query, contents);
        assert_eq!(result, vec!["hello world"]);
    }

    #[test]
    fn finds_nothing() {
        let query = "hello";
        let contents = "bye world";
        let result = search(query, contents);
        assert!(result.is_empty());
    }
}
