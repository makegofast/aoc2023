use std::{
    io::{BufReader, BufRead},
    fs::File
};

use anyhow::{Context, Result};
use log::debug;

pub fn run(reader: BufReader<File>) -> Result<()> {
    debug!("I work!");
    for line in reader.lines() {
        println!("{}", line.with_context(|| "Text")?);
    }

    Ok(())
}
