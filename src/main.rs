use anyhow::{Result, Context};
use clap::Parser;
use log::info;

mod days;
use crate::days::run;
mod helpers;

/// Program to select Advent of Code 2020 day to run
#[derive(Debug, Parser)]
#[command(author, version, about, long_about = None)]
struct Args {
    /// Advent Day (1-25)
    #[arg(short, long, value_parser=clap::value_parser!(u8).range(1..26))]
    day: u8,
    /// Optional path to puzzle input file
    #[arg(short, long, value_name = "FILE", default_value = ".")]
    path: std::path::PathBuf,
    #[command(flatten)]
    verbose: clap_verbosity_flag::Verbosity,
}

fn main() -> Result<()> {
    let args: Args = Args::parse();
    env_logger::Builder::new()
        .filter_level(args.verbose.log_level_filter())
        .init();

    info!(target: "Start Up Events", "starting");

    let input_day = args.day;
    let input_path = args.path.into_os_string().into_string().unwrap();
    let reader: std::io::BufReader<std::fs::File> = helpers::read_input_from_file(&input_day, &input_path)?;
    
    run(input_day, reader).with_context(|| "Main")?;
    
    Ok(())
}
