#!/usr/bin/env python3
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""
Apache Burr Release Script

This script automates the Apache release process with three distinct build steps:
1. Package entire repo (git archive) -> tar.gz for voting
2. Build source distribution (sdist) from tar.gz
3. Build wheel from sdist

Each step produces signed artifacts (GPG + SHA512) that can be uploaded to Apache SVN.

Usage:
    # Full release workflow
    python scripts/apache_release.py all 0.41.0 0 myid

    # Step-by-step workflow
    python scripts/apache_release.py archive 0.41.0 0 --check-licenses
    python scripts/apache_release.py sdist 0.41.0 0
    python scripts/apache_release.py wheel 0.41.0 0
    python scripts/apache_release.py verify 0.41.0 0
    python scripts/apache_release.py upload 0.41.0 0 myid

    # Rebuild just the wheel
    python scripts/apache_release.py wheel 0.41.0 0

    # Dry run
    python scripts/apache_release.py all 0.41.0 0 myid --dry-run

Subcommands:
    archive - Create git archive (voting artifact)
    sdist   - Build source distribution from archive
    wheel   - Build wheel from sdist
    upload  - Upload artifacts to Apache SVN
    all     - Run complete workflow (archive → sdist → wheel → upload)
    verify  - Verify existing artifacts
"""

import argparse
import os
import sys
from typing import NoReturn, Optional

# These will be used when implementing TODO functions:
# import hashlib
# import shutil
# import subprocess
# import tempfile
# from pathlib import Path

# --- Configuration ---
PROJECT_SHORT_NAME = "burr"
VERSION_FILE = "pyproject.toml"
VERSION_PATTERN = r'version\s*=\s*"(\d+\.\d+\.\d+)"'

# Required examples for sdist and wheel (from pyproject.toml)
REQUIRED_EXAMPLES = [
    "__init__.py",
    "email-assistant",
    "multi-modal-chatbot",
    "streaming-fastapi",
    "deep-researcher",
]


# ============================================================================
# Utility Functions
# ============================================================================


def _fail(message: str) -> NoReturn:
    """Print error message and exit."""
    print(f"\n❌ {message}")
    sys.exit(1)


def _print_section(title: str) -> None:
    """Print a formatted section header."""
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80 + "\n")


def _print_step(step_num: int, total: int, description: str) -> None:
    """Print a formatted step header."""
    print(f"\n[Step {step_num}/{total}] {description}")
    print("-" * 80)


# ============================================================================
# Prerequisite Checks
# ============================================================================


def _check_prerequisites(check_rat: bool = False, rat_jar_path: Optional[str] = None) -> bool:
    """Check for required command-line tools.

    Args:
        check_rat: If True, also check for Apache RAT tool
        rat_jar_path: Path to RAT JAR file (required if check_rat is True)

    Returns:
        True if all prerequisites met, False otherwise
    """
    print("Checking for required tools...")
    # TODO: Implement tool checks (git, gpg, svn, flit, node, npm)
    # TODO: If check_rat, verify rat_jar_path exists and is readable, verify java is available
    return True


def _verify_project_root() -> bool:
    """Verify script is running from project root.

    Returns:
        True if in project root, False otherwise
    """
    # TODO: Check for pyproject.toml
    return True


def _get_version_from_file(file_path: str) -> str:
    """Extract version from pyproject.toml.

    Args:
        file_path: Path to pyproject.toml

    Returns:
        Version string (e.g., "0.41.0")
    """
    # TODO: Parse version from file
    return "0.0.0"


def _validate_version(requested_version: str) -> bool:
    """Validate that requested version matches pyproject.toml.

    Args:
        requested_version: Version string requested by user

    Returns:
        True if versions match, False otherwise
    """
    # TODO: Compare requested version with pyproject.toml version
    return True


def _check_git_working_tree() -> None:
    """Check git working tree status and warn if dirty."""
    # TODO: Run git status --porcelain and warn about uncommitted changes
    pass


# ============================================================================
# Git Operations
# ============================================================================


def _create_or_verify_git_tag(version: str, rc_num: str, dry_run: bool) -> bool:
    """Create or verify RC git tag.

    Args:
        version: Version string (e.g., "0.41.0")
        rc_num: RC number (e.g., "0")
        dry_run: If True, don't actually create tag

    Returns:
        True if tag created/verified, False otherwise
    """
    # TODO: Check if tag exists, prompt user if it does, create if not
    return True


# ============================================================================
# Signing and Verification
# ============================================================================


def _sign_artifact(artifact_path: str) -> tuple[str, str]:
    """Sign artifact with GPG and create SHA512 checksum.

    Args:
        artifact_path: Path to artifact to sign

    Returns:
        Tuple of (signature_path, checksum_path)
    """
    # TODO: Create .asc GPG signature and .sha512 checksum
    return ("", "")


def _verify_artifact_signature(artifact_path: str, signature_path: str) -> bool:
    """Verify GPG signature of artifact.

    Args:
        artifact_path: Path to artifact
        signature_path: Path to .asc signature

    Returns:
        True if signature valid, False otherwise
    """
    # TODO: Verify GPG signature
    return True


def _verify_artifact_checksum(artifact_path: str, checksum_path: str) -> bool:
    """Verify SHA512 checksum of artifact.

    Args:
        artifact_path: Path to artifact
        checksum_path: Path to .sha512 checksum

    Returns:
        True if checksum matches, False otherwise
    """
    # TODO: Verify SHA512 checksum
    return True


# ============================================================================
# License Checking (RAT)
# ============================================================================


def _check_licenses_with_rat(
    artifact_path: str, rat_jar_path: str, report_only: bool = False
) -> bool:
    """Run Apache RAT license checker on artifact.

    Args:
        artifact_path: Path to tar.gz to check
        rat_jar_path: Path to Apache RAT JAR file (e.g., /path/to/apache-rat-0.15.jar)
        report_only: If True, report issues but don't fail

    Returns:
        True if licenses OK (or report_only=True), False if issues found
    """
    # TODO: Extract archive, run: java -jar {rat_jar_path} -d {extracted_dir}, parse results
    return True


# ============================================================================
# Step 1: Git Archive (Voting Artifact)
# ============================================================================


def _create_git_archive(version: str, rc_num: str, output_dir: str = "dist") -> str:
    """Create git archive tar.gz for voting.

    This creates a snapshot of the entire repository from git HEAD.
    The archive includes all files tracked by git (respecting .gitignore).

    Args:
        version: Version string (e.g., "0.41.0")
        rc_num: RC number (e.g., "0")
        output_dir: Directory to write artifact to

    Returns:
        Path to created tar.gz file
    """
    # TODO:
    # 1. Clean output_dir
    # 2. Run git archive HEAD --format=tar.gz --prefix=apache-burr-{version}-incubating/
    # 3. Verify no node_modules or other excluded files in archive
    # 4. Sign artifact
    return ""


def _verify_git_archive(archive_path: str) -> bool:
    """Verify git archive contents are correct.

    Args:
        archive_path: Path to tar.gz archive

    Returns:
        True if archive contents valid, False otherwise
    """
    # TODO: Extract and verify no node_modules, build artifacts, etc.
    return True


# ============================================================================
# Step 2: Build Source Distribution (sdist)
# ============================================================================


def _extract_archive_to_temp(archive_path: str) -> str:
    """Extract archive to temporary directory.

    Args:
        archive_path: Path to tar.gz to extract

    Returns:
        Path to temporary directory containing extracted files
    """
    # TODO: Create temp dir, extract archive, return path
    return ""


def _build_sdist_from_archive(archive_path: str, version: str, output_dir: str = "dist") -> str:
    """Build source distribution from git archive.

    This extracts the tar.gz, builds an sdist using flit, and signs it.
    The sdist includes only files specified in pyproject.toml [tool.flit.sdist].

    Args:
        archive_path: Path to tar.gz from step 1
        version: Version string
        output_dir: Directory to write sdist to

    Returns:
        Path to created sdist tar.gz file
    """
    # TODO:
    # 1. Extract archive to temp dir
    # 2. Remove burr/tracking/server/build/ if exists
    # 3. Run flit build --format sdist from temp dir
    # 4. Move sdist to output_dir
    # 5. Rename to apache-burr-{version}-incubating-sdist.tar.gz
    # 6. Sign artifact
    # 7. Cleanup temp dir
    return ""


def _verify_sdist(sdist_path: str) -> bool:
    """Verify sdist contents are correct.

    Args:
        sdist_path: Path to sdist tar.gz

    Returns:
        True if sdist contents valid, False otherwise
    """
    # TODO:
    # 1. Extract and verify structure
    # 2. Check for required files (LICENSE, NOTICE, DISCLAIMER, scripts/, etc.)
    # 3. Check for only 4 required examples
    # 4. Verify no built UI artifacts
    return True


# ============================================================================
# Step 3: Build Wheel from sdist
# ============================================================================


def _build_ui_artifacts(work_dir: str) -> bool:
    """Build UI artifacts for wheel.

    Args:
        work_dir: Working directory (extracted sdist location)

    Returns:
        True if UI build successful, False otherwise
    """
    # TODO:
    # 1. Check for node/npm
    # 2. Clean burr/tracking/server/build/
    # 3. Install burr: pip install -e .
    # 4. Run burr-admin-build-ui
    # 5. Verify build output exists
    return True


def _handle_symlinks_for_wheel(work_dir: str) -> dict:
    """Replace symlinks with copies and track for restoration.

    Args:
        work_dir: Working directory

    Returns:
        Dictionary mapping paths to original symlink info
    """
    # TODO: Replace symlinks with copies, return tracking dict
    return {}


def _restore_symlinks(symlink_info: dict) -> None:
    """Restore original symlinks.

    Args:
        symlink_info: Dictionary from _handle_symlinks_for_wheel
    """
    # TODO: Restore symlinks from tracking dict
    pass


def _copy_examples_for_wheel(work_dir: str) -> tuple[bool, bool, Optional[str]]:
    """Copy required examples into burr/ for wheel packaging.

    Args:
        work_dir: Working directory

    Returns:
        Tuple of (copied, was_symlink, symlink_target)
    """
    # TODO: Copy 4 required examples to burr/examples/
    return (False, False, None)


def _remove_examples_from_burr(
    work_dir: str, was_symlink: bool = False, symlink_target: Optional[str] = None
) -> None:
    """Remove examples from burr/ and optionally restore symlink.

    Args:
        work_dir: Working directory
        was_symlink: If True, restore symlink
        symlink_target: Original symlink target
    """
    # TODO: Remove burr/examples/, restore symlink if needed
    pass


def _build_wheel_from_sdist(sdist_path: str, version: str, output_dir: str = "dist") -> str:
    """Build wheel from source distribution.

    This extracts the sdist, builds UI assets, copies examples, builds wheel with flit.

    Args:
        sdist_path: Path to sdist from step 2
        version: Version string
        output_dir: Directory to write wheel to

    Returns:
        Path to created wheel file
    """
    # TODO:
    # 1. Extract sdist to temp dir
    # 2. Build UI artifacts
    # 3. Handle symlinks
    # 4. Copy examples to burr/
    # 5. Run flit build --format wheel
    # 6. Move wheel to output_dir
    # 7. Rename to apache-burr-{version}-incubating-{tags}.whl
    # 8. Sign artifact
    # 9. Cleanup (remove examples, restore symlinks)
    # 10. Cleanup temp dir
    return ""


def _verify_wheel(wheel_path: str) -> bool:
    """Verify wheel contents are correct.

    Args:
        wheel_path: Path to wheel file

    Returns:
        True if wheel contents valid, False otherwise
    """
    # TODO:
    # 1. Extract wheel and verify structure
    # 2. Check for burr/tracking/server/build/ (UI assets)
    # 3. Check for burr/examples/ with 4 required examples
    # 4. Verify no source artifacts (scripts/, telemetry/ui/src/, etc.)
    return True


# ============================================================================
# Upload to Apache SVN
# ============================================================================


def _upload_to_svn(
    version: str,
    rc_num: str,
    apache_id: str,
    artifacts: list[str],
    dry_run: bool = False,
) -> Optional[str]:
    """Upload artifacts to Apache SVN distribution repository.

    Args:
        version: Version string
        rc_num: RC number
        apache_id: Apache ID for authentication
        artifacts: List of file paths to upload (tar.gz, sdist, wheel, signatures, checksums)
        dry_run: If True, don't actually upload

    Returns:
        SVN URL if successful, None if failed
    """
    # TODO:
    # 1. Create SVN directory structure
    # 2. Upload all artifacts (tar.gz, sdist, wheel, and their .asc/.sha512 files)
    # 3. Return SVN URL
    return None


# ============================================================================
# Email Template Generation
# ============================================================================


def _generate_vote_email(version: str, rc_num: str, svn_url: str, artifacts: list[str]) -> str:
    """Generate [VOTE] email template.

    Args:
        version: Version string
        rc_num: RC number
        svn_url: SVN URL where artifacts are hosted
        artifacts: List of artifact filenames

    Returns:
        Email content as string
    """
    # TODO: Generate email template with checklist and artifact list
    return ""


def _print_vote_email(email_content: str) -> None:
    """Print vote email to console.

    Args:
        email_content: Email content from _generate_vote_email
    """
    # TODO: Print formatted email
    pass


# ============================================================================
# Auto-detection Helpers
# ============================================================================


def _auto_detect_artifact(
    version: str, artifact_type: str, output_dir: str = "dist"
) -> Optional[str]:
    """Auto-detect artifact path based on version and type.

    Args:
        version: Version string (e.g., "0.41.0")
        artifact_type: Type of artifact ('archive', 'sdist', 'wheel')
        output_dir: Directory to search in

    Returns:
        Path to artifact if found, None otherwise
    """
    # TODO: Implement auto-detection logic
    # archive: apache-burr-{version}-incubating-src.tar.gz
    # sdist: apache-burr-{version}-incubating-sdist.tar.gz
    # wheel: apache-burr-{version}-incubating-*.whl (use glob)
    return None


def _collect_all_artifacts(version: str, output_dir: str = "dist") -> list[str]:
    """Collect all artifacts (including signatures and checksums) for upload.

    Args:
        version: Version string
        output_dir: Directory containing artifacts

    Returns:
        List of artifact paths
    """
    # TODO: Find all tar.gz, whl, .asc, .sha512 files
    return []


# ============================================================================
# Command Handlers
# ============================================================================


def cmd_archive(args) -> bool:
    """Handle 'archive' subcommand."""
    _print_section(f"Creating Git Archive - v{args.version}-RC{args.rc_num}")

    # Check if RAT is needed
    check_rat = args.check_licenses or args.check_licenses_report
    if check_rat and not args.rat_jar:
        _fail("--rat-jar is required when using --check-licenses or --check-licenses-report")

    # Prerequisites
    if not _check_prerequisites(check_rat=check_rat, rat_jar_path=args.rat_jar):
        return False
    if not _verify_project_root():
        return False
    if not _validate_version(args.version):
        return False
    _check_git_working_tree()

    # Create archive
    archive_path = _create_git_archive(args.version, args.rc_num, args.output_dir)
    if not archive_path:
        return False

    print(f"\n✅ Archive created: {archive_path}")

    # Optional license check
    if check_rat:
        _print_step(2, 2, "Checking licenses with Apache RAT")
        if not _check_licenses_with_rat(
            archive_path, args.rat_jar, report_only=args.check_licenses_report
        ):
            if not args.check_licenses_report:
                return False

    return True


def cmd_sdist(args) -> bool:
    """Handle 'sdist' subcommand."""
    _print_section(f"Building Source Distribution - v{args.version}-RC{args.rc_num}")

    # Prerequisites
    if not _check_prerequisites():
        return False
    if not _verify_project_root():
        return False
    if not _validate_version(args.version):
        return False

    # Find or use specified archive
    archive_path = args.archive_path
    if not archive_path:
        detected = _auto_detect_artifact(args.version, "archive", args.output_dir)
        if not detected:
            _fail(
                "Could not find git archive. Please specify --archive-path or run 'archive' command first."
            )
        archive_path = detected
        print(f"Using archive: {archive_path}")

    # Build sdist
    sdist_path = _build_sdist_from_archive(archive_path, args.version, args.output_dir)
    if not sdist_path:
        return False

    print(f"\n✅ Source distribution created: {sdist_path}")
    return True


def cmd_wheel(args) -> bool:
    """Handle 'wheel' subcommand."""
    _print_section(f"Building Wheel - v{args.version}-RC{args.rc_num}")

    # Prerequisites
    if not _check_prerequisites():
        return False
    if not _verify_project_root():
        return False
    if not _validate_version(args.version):
        return False

    # Find or use specified sdist
    sdist_path = args.sdist_path
    if not sdist_path:
        detected = _auto_detect_artifact(args.version, "sdist", args.output_dir)
        if not detected:
            _fail("Could not find sdist. Please specify --sdist-path or run 'sdist' command first.")
        sdist_path = detected
        print(f"Using sdist: {sdist_path}")

    # Build wheel
    wheel_path = _build_wheel_from_sdist(sdist_path, args.version, args.output_dir)
    if not wheel_path:
        return False

    print(f"\n✅ Wheel created: {wheel_path}")
    return True


def cmd_upload(args) -> bool:
    """Handle 'upload' subcommand."""
    _print_section(f"Uploading Artifacts - v{args.version}-RC{args.rc_num}")

    # Prerequisites
    if not _check_prerequisites():
        return False
    if not _verify_project_root():
        return False

    # Collect all artifacts
    artifacts = _collect_all_artifacts(args.version, args.artifacts_dir)
    if not artifacts:
        _fail(f"No artifacts found in {args.artifacts_dir}. Please build artifacts first.")

    print(f"Found {len(artifacts)} artifact(s) to upload:")
    for artifact in artifacts:
        print(f"  - {os.path.basename(artifact)}")

    # Upload
    if args.dry_run:
        svn_url = f"https://dist.apache.org/repos/dist/dev/incubator/{PROJECT_SHORT_NAME}/{args.version}-incubating-RC{args.rc_num}"
        print(f"\n[DRY RUN] Would upload to: {svn_url}")
    else:
        svn_url = _upload_to_svn(
            args.version, args.rc_num, args.apache_id, artifacts, dry_run=False
        )
        if not svn_url:
            return False
        print(f"\n✅ Artifacts uploaded to: {svn_url}")

    return True


def cmd_verify(args) -> bool:
    """Handle 'verify' subcommand."""
    _print_section(f"Verifying Artifacts - v{args.version}-RC{args.rc_num}")

    # TODO: Implement verification
    # 1. Check for expected artifacts
    # 2. Verify GPG signatures
    # 3. Verify SHA512 checksums
    # 4. Check archive/sdist/wheel contents
    print("Verification not yet implemented")
    return True


def cmd_all(args) -> bool:
    """Handle 'all' subcommand - run complete workflow."""
    _print_section(f"Apache Burr Release Process - v{args.version}-RC{args.rc_num}")

    if args.dry_run:
        print("*** DRY RUN MODE - No git tags or SVN uploads will be performed ***\n")

    # Check if RAT is needed
    check_rat = args.check_licenses or args.check_licenses_report
    if check_rat and not args.rat_jar:
        _fail("--rat-jar is required when using --check-licenses or --check-licenses-report")

    # Prerequisites
    _print_step(0, 5, "Checking prerequisites")
    if not _check_prerequisites(check_rat=check_rat, rat_jar_path=args.rat_jar):
        return False
    if not _verify_project_root():
        return False
    if not _validate_version(args.version):
        return False
    _check_git_working_tree()

    # Git tagging
    if not args.no_tag and not args.dry_run:
        _print_step(1, 5, "Creating/verifying git tag")
        if not _create_or_verify_git_tag(args.version, args.rc_num, args.dry_run):
            return False

    # Clean dist/
    if args.clean:
        _print_step(1, 5, "Cleaning dist/ directory")
        # TODO: Clean dist/

    artifacts = []

    # Step 1: Git Archive
    _print_step(2, 5, "Creating git archive (voting artifact)")
    archive_path = _create_git_archive(args.version, args.rc_num, args.output_dir)
    if not archive_path:
        return False
    artifacts.append(archive_path)

    if check_rat:
        print("\n[License Check] Checking licenses with Apache RAT")
        print("-" * 80)
        if not _check_licenses_with_rat(
            archive_path, args.rat_jar, report_only=args.check_licenses_report
        ):
            if not args.check_licenses_report:
                return False

    # Step 2: Build sdist
    _print_step(3, 5, "Building source distribution (sdist) from archive")
    sdist_path = _build_sdist_from_archive(archive_path, args.version, args.output_dir)
    if not sdist_path:
        return False
    artifacts.append(sdist_path)

    # Step 3: Build wheel
    _print_step(4, 5, "Building wheel from sdist")
    wheel_path = _build_wheel_from_sdist(sdist_path, args.version, args.output_dir)
    if not wheel_path:
        return False
    artifacts.append(wheel_path)

    # Collect all artifacts (including signatures and checksums)
    all_artifacts = _collect_all_artifacts(args.version, args.output_dir)

    # Upload to SVN
    if not args.no_upload and not args.dry_run:
        _print_step(5, 5, "Uploading artifacts to Apache SVN")
        svn_url = _upload_to_svn(
            args.version, args.rc_num, args.apache_id, all_artifacts, dry_run=False
        )
        if not svn_url:
            return False
    else:
        svn_url = f"https://dist.apache.org/repos/dist/dev/incubator/{PROJECT_SHORT_NAME}/{args.version}-incubating-RC{args.rc_num}"
        if args.dry_run:
            print(f"\n[DRY RUN] Would upload to: {svn_url}")
        else:
            print("\nℹ️  Skipping upload (--no-upload specified)")

    # Generate email template
    _print_section("Release Complete!")
    email_content = _generate_vote_email(args.version, args.rc_num, svn_url, all_artifacts)
    _print_vote_email(email_content)

    return True


# ============================================================================
# Legacy Orchestration (Deprecated)
# ============================================================================


def run_full_release(
    version: str,
    rc_num: str,
    apache_id: str,
    dry_run: bool = False,
    check_licenses: bool = False,
    check_licenses_report: bool = False,
    skip_step1: bool = False,
    skip_step2: bool = False,
    skip_step3: bool = False,
    no_upload: bool = False,
    clean: bool = True,
) -> bool:
    """DEPRECATED: Use cmd_all() instead.

    This function is kept for backwards compatibility but is no longer used.
    """
    print("WARNING: run_full_release() is deprecated. Use subcommands instead.")
    return False


# ============================================================================
# CLI Entry Point
# ============================================================================


def main():
    """Main entry point for the release script."""
    parser = argparse.ArgumentParser(
        description="Apache Burr Release Automation Script",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Full release workflow
  python scripts/apache_release.py all 0.41.0 0 myid

  # Step-by-step workflow
  python scripts/apache_release.py archive 0.41.0 0 --check-licenses
  python scripts/apache_release.py sdist 0.41.0 0
  python scripts/apache_release.py wheel 0.41.0 0
  python scripts/apache_release.py verify 0.41.0 0
  python scripts/apache_release.py upload 0.41.0 0 myid

  # Rebuild just the wheel
  python scripts/apache_release.py wheel 0.41.0 0

  # Dry run
  python scripts/apache_release.py all 0.41.0 0 myid --dry-run

  # With explicit paths
  python scripts/apache_release.py sdist 0.41.0 0 --archive-path /path/to/archive.tar.gz
  python scripts/apache_release.py wheel 0.41.0 0 --sdist-path /path/to/sdist.tar.gz

For more information, see scripts/README.md
        """,
    )

    subparsers = parser.add_subparsers(dest="command", required=True, help="Subcommands")

    # ========================================
    # archive subcommand
    # ========================================
    archive_parser = subparsers.add_parser(
        "archive",
        help="Create git archive (voting artifact)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Create git archive snapshot of repository for voting.",
    )
    archive_parser.add_argument(
        "version",
        help="Release version (e.g., '0.41.0'). Must match version in pyproject.toml.",
    )
    archive_parser.add_argument(
        "rc_num",
        help="Release candidate number (e.g., '0' for RC0, '1' for RC1).",
    )
    archive_parser.add_argument(
        "--output-dir",
        default="dist",
        help="Output directory for artifacts (default: dist)",
    )
    archive_parser.add_argument(
        "--check-licenses",
        action="store_true",
        help="Run Apache RAT license checker (blocking on failure)",
    )
    archive_parser.add_argument(
        "--check-licenses-report",
        action="store_true",
        help="Run Apache RAT license checker (report only, non-blocking)",
    )
    archive_parser.add_argument(
        "--rat-jar",
        default=None,
        help="Path to Apache RAT JAR file (required if using --check-licenses or --check-licenses-report)",
    )

    # ========================================
    # sdist subcommand
    # ========================================
    sdist_parser = subparsers.add_parser(
        "sdist",
        help="Build source distribution from archive",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Build source distribution (sdist) from git archive using flit.",
    )
    sdist_parser.add_argument(
        "version",
        help="Release version (e.g., '0.41.0'). Must match version in pyproject.toml.",
    )
    sdist_parser.add_argument(
        "rc_num",
        help="Release candidate number (e.g., '0' for RC0, '1' for RC1).",
    )
    sdist_parser.add_argument(
        "--archive-path",
        default=None,
        help="Path to git archive tar.gz (default: auto-detect in output-dir)",
    )
    sdist_parser.add_argument(
        "--output-dir",
        default="dist",
        help="Output directory for artifacts (default: dist)",
    )

    # ========================================
    # wheel subcommand
    # ========================================
    wheel_parser = subparsers.add_parser(
        "wheel",
        help="Build wheel from sdist",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Build wheel from source distribution using flit.",
    )
    wheel_parser.add_argument(
        "version",
        help="Release version (e.g., '0.41.0'). Must match version in pyproject.toml.",
    )
    wheel_parser.add_argument(
        "rc_num",
        help="Release candidate number (e.g., '0' for RC0, '1' for RC1).",
    )
    wheel_parser.add_argument(
        "--sdist-path",
        default=None,
        help="Path to sdist tar.gz (default: auto-detect in output-dir)",
    )
    wheel_parser.add_argument(
        "--output-dir",
        default="dist",
        help="Output directory for artifacts (default: dist)",
    )
    wheel_parser.add_argument(
        "--skip-ui-build",
        action="store_true",
        help="Skip UI build (use existing build artifacts)",
    )

    # ========================================
    # upload subcommand
    # ========================================
    upload_parser = subparsers.add_parser(
        "upload",
        help="Upload artifacts to Apache SVN",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Upload all artifacts to Apache SVN distribution repository.",
    )
    upload_parser.add_argument(
        "version",
        help="Release version (e.g., '0.41.0').",
    )
    upload_parser.add_argument(
        "rc_num",
        help="Release candidate number (e.g., '0' for RC0, '1' for RC1).",
    )
    upload_parser.add_argument(
        "apache_id",
        help="Your Apache ID for SVN authentication.",
    )
    upload_parser.add_argument(
        "--artifacts-dir",
        default="dist",
        help="Directory containing artifacts to upload (default: dist)",
    )
    upload_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be uploaded without actually uploading",
    )

    # ========================================
    # all subcommand
    # ========================================
    all_parser = subparsers.add_parser(
        "all",
        help="Run complete release workflow",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Run complete release workflow: archive → sdist → wheel → upload",
    )
    all_parser.add_argument(
        "version",
        help="Release version (e.g., '0.41.0'). Must match version in pyproject.toml.",
    )
    all_parser.add_argument(
        "rc_num",
        help="Release candidate number (e.g., '0' for RC0, '1' for RC1).",
    )
    all_parser.add_argument(
        "apache_id",
        help="Your Apache ID for SVN authentication.",
    )
    all_parser.add_argument(
        "--output-dir",
        default="dist",
        help="Output directory for artifacts (default: dist)",
    )
    all_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Build artifacts but don't create git tags or upload to SVN",
    )
    all_parser.add_argument(
        "--no-upload",
        action="store_true",
        help="Build artifacts but skip SVN upload",
    )
    all_parser.add_argument(
        "--no-tag",
        action="store_true",
        help="Don't create git RC tag",
    )
    all_parser.add_argument(
        "--clean",
        action="store_true",
        default=True,
        help="Clean dist/ directory before starting (default: True)",
    )
    all_parser.add_argument(
        "--no-clean",
        dest="clean",
        action="store_false",
        help="Don't clean dist/ directory before starting",
    )
    all_parser.add_argument(
        "--check-licenses",
        action="store_true",
        help="Run Apache RAT license checker on archive (blocking on failure)",
    )
    all_parser.add_argument(
        "--check-licenses-report",
        action="store_true",
        help="Run Apache RAT license checker on archive (report only, non-blocking)",
    )
    all_parser.add_argument(
        "--rat-jar",
        default=None,
        help="Path to Apache RAT JAR file (required if using --check-licenses or --check-licenses-report)",
    )

    # ========================================
    # verify subcommand
    # ========================================
    verify_parser = subparsers.add_parser(
        "verify",
        help="Verify existing artifacts",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Verify signatures, checksums, and contents of existing artifacts.",
    )
    verify_parser.add_argument(
        "version",
        help="Release version (e.g., '0.41.0').",
    )
    verify_parser.add_argument(
        "rc_num",
        help="Release candidate number (e.g., '0' for RC0, '1' for RC1).",
    )
    verify_parser.add_argument(
        "--artifacts-dir",
        default="dist",
        help="Directory containing artifacts to verify (default: dist)",
    )

    # Parse arguments
    args = parser.parse_args()

    # Dispatch to appropriate command handler
    success = False
    try:
        if args.command == "archive":
            success = cmd_archive(args)
        elif args.command == "sdist":
            success = cmd_sdist(args)
        elif args.command == "wheel":
            success = cmd_wheel(args)
        elif args.command == "upload":
            success = cmd_upload(args)
        elif args.command == "all":
            success = cmd_all(args)
        elif args.command == "verify":
            success = cmd_verify(args)
        else:
            print(f"Unknown command: {args.command}")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)

    if success:
        print("\n✅ Command completed successfully!")
        sys.exit(0)
    else:
        print("\n❌ Command failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()
