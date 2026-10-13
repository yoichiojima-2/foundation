const USAGE: &str = "usage: minigrep <query> <file>";

struct Config {
    query: String,
    file: String,
    ignore_case: bool,
}

impl Config {
    fn build(args: &[String]) -> Result<Config, Box<dyn std::error::Error>> {
        let query = args.get(1).ok_or(USAGE)?.clone();
        let file = args.get(2).ok_or(USAGE)?.clone();
        let ignore_case = std::env::var("IGNORE_CASE").is_ok();
        Ok(Config {
            query,
            file,
            ignore_case,
        })
    }
}

fn read_file(file: &str) -> Result<String, String> {
    std::fs::read_to_string(file).map_err(|e| format!("cannot read {file}: {e}"))
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

fn search_case_insensitive<'a>(query: &str, contents: &'a str) -> Vec<&'a str> {
    let mut res = Vec::new();
    let query_lower = query.to_lowercase();
    for line in contents.lines() {
        if line.to_lowercase().contains(&query_lower) {
            res.push(line);
        }
    }
    res
}

fn run() -> Result<(), Box<dyn std::error::Error>> {
    let args: Vec<String> = std::env::args().collect();
    let config = Config::build(&args)?;
    let contents = read_file(&config.file)?;
    let lines = if config.ignore_case {
        search_case_insensitive(&config.query, &contents)
    } else {
        search(&config.query, &contents)
    };
    for line in lines {
        println!("{line}");
    }
    Ok(())
}

fn main() {
    if let Err(e) = run() {
        eprintln!("{e}");
        std::process::exit(1);
    }
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

    #[test]
    fn case_insensitive_uppercase_in_query() {
        let query = "Hello";
        let contents = "hello world\nbye world";
        let result = search_case_insensitive(query, contents);
        assert_eq!(result, vec!["hello world"]);
    }

    #[test]
    fn case_insensitive_uppercase_in_line() {
        let query = "hello";
        let contents = "Hello world\nhello world";
        let result = search_case_insensitive(query, contents);
        assert_eq!(result, vec!["Hello world", "hello world"]);
    }
}