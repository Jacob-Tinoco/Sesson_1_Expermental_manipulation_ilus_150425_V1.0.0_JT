#!/usr/bin/env python3
"""
Pseudocode: replace_logos_mac09.py
Replaces all “logo” items under the “Grupo ENFOQUE” parent group
with randomly selected PNGs from a local folder, without repeats.
"""

# ──────────────────────────────────────────────────────────────────────────────
# IMPORTS & CONFIGURATION
# ──────────────────────────────────────────────────────────────────────────────
IMPORT logging, subprocess, sys, tempfile
FROM pathlib IMPORT Path

CONSTANT PARENT_GROUP_NAME = "Grupo ENFOQUE"
CONSTANT CANDIDATE_FOLDERS = ["logos", "LOGOS"]

# ──────────────────────────────────────────────────────────────────────────────
# UTILITY FUNCTIONS
# ──────────────────────────────────────────────────────────────────────────────
FUNCTION find_logos_folder(base_dir: Path) → Path or None:
    FOR each folder_name IN CANDIDATE_FOLDERS:
        candidate = base_dir / folder_name
        IF candidate.is_dir():
            RETURN candidate
    RETURN None

FUNCTION build_jsx_script(parent_group: str, logos_folder: Path) → str:
    """
    Fill in JSX_TEMPLATE with:
     - parent_group name
     - absolute path to logos_folder
    """
    RETURN JSX_TEMPLATE.format( group=parent_group, folder=str(logos_folder) )

FUNCTION execute_jsx(js_code: str) → None:
    """
    1. Write js_code to a temp .jsx file.
    2. Call osascript to run it in Illustrator.
    3. Log success or error, then delete the temp file.
    """
    temp_file = write_temp_file(js_code, suffix=".jsx")
    result = run_shell([
        "osascript", "-e",
        f'tell application "Adobe Illustrator" to do javascript file "{temp_file}"'
    ])
    IF result.exit_code != 0:
        logger.error("ExtendScript error: %s", result.stderr)
        sys.exit(result.exit_code)
    logger.info("JSX executed successfully.")
    delete_file(temp_file)

# ──────────────────────────────────────────────────────────────────────────────
# MAIN PIPELINE
# ──────────────────────────────────────────────────────────────────────────────
FUNCTION main() → None:
    base_dir = Path.cwd()
    logos_dir = find_logos_folder(base_dir)
    IF NOT logos_dir:
        logger.error("No logos folder found in %s", base_dir)
        sys.exit(1)

    logger.info("Using logos folder: %s", logos_dir)
    jsx_code = build_jsx_script(PARENT_GROUP_NAME, logos_dir)
    execute_jsx(jsx_code)

IF __name__ == "__main__":
    main()
