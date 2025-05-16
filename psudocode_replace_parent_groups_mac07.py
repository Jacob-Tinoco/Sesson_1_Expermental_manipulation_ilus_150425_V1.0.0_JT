#!/usr/bin/env python3
"""
Pseudocode: replace_parent_groups_mac07.py
Replaces each top-level “F” or “B” group with a blank PNG selected at random,
aligning it by its bottom edge and preserving original width/proportion.
"""

# ──────────────────────────────────────────────────────────────────────────────
# IMPORTS & GLOBALS
# ──────────────────────────────────────────────────────────────────────────────
IMPORT logging, subprocess, sys, tempfile, json
FROM pathlib IMPORT Path

CONSTANT PARENT_GROUPS = ["F", "B"]
CONSTANT BLANKS_FOLDER = "BLANKS"

# ──────────────────────────────────────────────────────────────────────────────
# HELPERS
# ──────────────────────────────────────────────────────────────────────────────
FUNCTION find_blanks_folder(base_dir: Path) → Path or None:
    folder = base_dir / BLANKS_FOLDER
    RETURN folder IF folder.is_dir() ELSE None

FUNCTION build_jsx_script(parent_groups: List[str], blanks_folder: Path) → str:
    """
    1. Parse all PNGs in blanks_folder, separate into poolF and poolB by suffix.
    2. Shuffle each pool.
    3. Locate all GroupItems/PlacedItems named “F” or “B” in the document.
    4. Replace each with the next PNG from the matching pool,
       setting width, aligning bottom edge, and preserving proportion.
    """
    return JSX_TEMPLATE.format(
        parent_names=json.dumps(parent_groups),
        folder=str(blanks_folder)
    )

FUNCTION execute_jsx(js_code: str) → None:
    # Same pattern as replace_logos: write temp file, run via osascript, log & cleanup
    temp_file = write_temp_file(js_code, suffix=".jsx")
    result = run_shell_command([...])
    IF result.exit_code != 0:
        logger.error("ExtendScript error: %s", result.stderr)
        sys.exit(result.exit_code)
    logger.info("JSX executed successfully.")
    delete_file(temp_file)

# ──────────────────────────────────────────────────────────────────────────────
# MAIN FLOW
# ──────────────────────────────────────────────────────────────────────────────
FUNCTION main() → None:
    base_dir = Path.cwd()
    blanks_dir = find_blanks_folder(base_dir)
    IF NOT blanks_dir:
        logger.error("BLANKS folder missing in %s", base_dir)
        sys.exit(1)

    logger.info("BLANKS folder found: %s", blanks_dir)
    jsx_code = build_jsx_script(PARENT_GROUPS, blanks_dir)
    execute_jsx(jsx_code)

IF __name__ == "__main__":
    main()
