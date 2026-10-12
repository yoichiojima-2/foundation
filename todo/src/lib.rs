#[derive(Debug, PartialEq)]
enum Status { Open, Done, Dropped }

#[derive(Debug, PartialEq)]
struct Todo {
    status: Status,
    priority: bool,
    text: String,
    tags: Vec<String>,
    due: Option<String>
}

fn parse_status(line: &str) -> Option<Status> {
    if line.starts_with("- [ ]") {
        return Some(Status::Open);
    } else if line.starts_with("- [x]") {
        if line.contains("dropped") {
            return Some(Status::Dropped);
        } else {
            return Some(Status::Done);
        }
    } else {
        return None;
    }
}

fn parse_priority(line: &str) -> bool {
    todo!()
}

fn parse_text(line: &str) -> String {
    todo!()
}

fn parse_tags(line: &str) -> Vec<String> {
    todo!()
}

fn parse_due(line: &str) -> Option<String> {
    todo!()
}

fn make_todo(line: &str) -> Option<Todo> {
    Some(
        Todo {
            status: parse_status(line)?,
            priority: parse_priority(line),
            text: parse_text(line),
            tags: parse_tags(line),
            due: parse_due(line)
        }
    )
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn parses_status_open() {
        assert_eq!(parse_status("- [ ]").unwrap(), Status::Open);
    }

    #[test]
    fn parses_status_done() {
        assert_eq!(parse_status("- [x]").unwrap(), Status::Done);
    }

    #[test]
    fn parses_status_dropped() {
        assert_eq!(parse_status("- [x] task dropped: 2026-09-12").unwrap(), Status::Dropped);
    }

    #[test]
    fn parses_done_with_dropped_text() {
        assert_eq!(parse_status("- [x] task done but mentions dropped").unwrap(), Status::Done);
    }
}
