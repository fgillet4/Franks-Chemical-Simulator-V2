#!/bin/bash

# Check if wasm-pack is installed
if ! command -v wasm-pack &> /dev/null
then
    echo "wasm-pack could not be found, please install it first."
    exit 1
fi

# Define paths relative to the script location
SCRIPT_DIR="$(dirname "$0")"
ROOT_DIR="${SCRIPT_DIR}/.."
RUST_DIR="${ROOT_DIR}/rust"
DIST_DIR="${ROOT_DIR}/dist/wasm"

# Navigate to the Rust directory and build the WebAssembly module
echo "Navigating to Rust project directory: ${RUST_DIR}"
cd "${RUST_DIR}" || exit

echo "Building the WebAssembly module with wasm-pack..."
wasm-pack build --target web

# Check if build was successful
if [ ! -d "${RUST_DIR}/pkg" ]; then
    echo "Build failed, exiting..."
    exit 1
fi

# Move the built WebAssembly package to the distribution directory
echo "Moving built package to ${DIST_DIR}..."
mkdir -p "${DIST_DIR}"
mv pkg/* "${DIST_DIR}/"

echo "Build and move completed successfully."
