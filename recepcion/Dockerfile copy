FROM rust:1.70.0-slim-bullseye

COPY ./recepcion/main.rs /recepcion/src/main.rs
COPY ./recepcion/Cargo.toml /recepcion/Cargo.toml
WORKDIR /recepcion

EXPOSE 8051
EXPOSE 3002

RUN cargo build --release

# Run the binary
CMD ["./target/release/recepcion"]
