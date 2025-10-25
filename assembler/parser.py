#!/usr/bin/env python3
import subprocess
import os


def convert_s_to_binary(input_file: str, output_file: str):
    """Convert .s assembly file to binary machine code"""

    print(f"Converting {input_file} to binary machine code...")

    # Step 1: Compile .s file to object file
    try:
        subprocess.run(
            [
                "clang-18",
                "--target=riscv32",
                "-march=rv32imfv",
                "-mno-relax",
                "-O0",
                "-c",
                input_file,
                "-o",
                "temp.o",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as e:
        print("Error during compilation:")
        print(e.stderr)
        return

    # Step 2: Extract binary section
    try:
        subprocess.run(
            [
                "llvm-objcopy-18",
                "-O",
                "binary",
                "--only-section=.text",
                "temp.o",
                "temp.bin",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as e:
        print("Error extracting binary:")
        print(e.stderr)
        return

    # Step 3: Read binary and detect instruction length
    binary_strings = []
    try:
        with open("temp.bin", "rb") as f:
            data = f.read()

        i = 0
        while i < len(data):
            if i + 4 > len(data):
                # Handle potential 16-bit or trailing rv_instructions at the end
                if i + 2 <= len(data):
                    instr_bytes = data[i : i + 2]
                    binary_str = "".join(
                        format(b, "08b") for b in reversed(instr_bytes)
                    )
                    binary_strings.append(binary_str)
                    i += 2
                break

            # Peek at the 2 least significant bits of the first byte
            low_bits = data[i] & 0b11

            if low_bits == 0b11:
                # 32-bit instruction
                instr_bytes = data[i : i + 4]
                binary_str = "".join(format(b, "08b") for b in reversed(instr_bytes))
                binary_strings.append(binary_str)
                i += 4
            else:
                # 16-bit compressed instruction
                instr_bytes = data[i : i + 2]
                binary_str = "".join(format(b, "08b") for b in reversed(instr_bytes))
                binary_strings.append(binary_str)
                i += 2
    except FileNotFoundError:
        print("Error: temp.bin not found.")
        return

    # Step 4: Write output
    with open(output_file, "w") as f:
        for binary in binary_strings:
            f.write(f"{binary}\n")

    # Cleanup
    os.remove("temp.o")
    os.remove("temp.bin")

    print(f"Done! Binary code saved to {output_file}")
    print(f"Total instructions: {len(binary_strings)}")


if __name__ == "__main__":
    convert_s_to_binary("outputs/assembly.s", "outputs/machine-code/binary_output.txt")
