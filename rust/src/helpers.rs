use std::{
    path::PathBuf, 
    fs::File, 
    io::BufReader
};

use anyhow::{Context, Result};

pub fn read_input_from_file(input_day: &u8, input_path: &String) -> Result<BufReader<File>> {
    let path = resolve_path(input_day, input_path);
    let path_string = format!("{}", path.display());

    let f: File = File::open(path)
        .with_context(|| format!("could not read file '{path_string}'"))?;
    let reader: BufReader<File> = BufReader::new(f);

    Ok(reader)
}

fn resolve_path(input_day: &u8, input_path: &String) -> PathBuf {
    let mut path = PathBuf::from(input_path);

    if input_path == "." {
        path.clear();
        path.push(input_path);
        path.push(format!("inputs/day{input_day}.txt"))
    }

    path
}