fn get_arg(args: &[String], i: usize) -> &str {
    match args.get(i) {
        Some(arg) => arg,
        None => {
            eprintln!("usage: minigrep <query> <file>");
            std::process::exit(1);
        }
    }
}

fn read_file(file: &str) -> String {
    match std::fs::read_to_string(file) {
        Ok(content) => content,
        Err(e) => {
            eprintln!("cannot read {file}: {e}");
            std::process::exit(1);
        }
    }
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

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let query = get_arg(&args, 1);
    let file = get_arg(&args, 2);
    let contents = read_file(file);
    for line in search(query, &contents) {
        println!("{line}");
    }
}
