use std::{
    io::BufReader, 
    fs::File
};

use anyhow::{Context, Result};

mod day1;

pub fn run(day: u8, reader: BufReader<File>) -> Result<()> {
    match day {
        1 => day1::run(reader).with_context(|| "Error with day 1")?,
        _ => panic!(),
    }

    Ok(())
}
