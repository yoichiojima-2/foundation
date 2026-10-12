fn get_arg(args: &[String], i: usize) -> &String {
    match args.get(i) {
        Some(arg) => arg,
        None => {
            eprintln!("usage: minigrep <query> <file>");
            std::process::exit(1);
        }
    }
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let query = get_arg(&args, 1);
    let file = get_arg(&args, 2);
    println!("query: {query} / file: {file}");
}
