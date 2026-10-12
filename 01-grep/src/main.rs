fn main() {
    let args: Vec<String> = std::env::args().collect();
    let query = match args.get(1) {
        Some(q) => q,
        None => {
            eprintln!("usage: minigrep <query> <file>");
            std::process::exit(1);
        }
    };
    let file = match args.get(2) {
        Some(f) => f,
        None => {
            eprintln!("usage: minigrep <query> <file>");
            std::process::exit(1);
        }
    };
    println!("query: {query} / file: {file}");
}
