"""Whitelist assembly helper; the native validator remains authoritative."""
import argparse
import json
from pathlib import Path
import re
import zipfile


ASSET_PATH = re.compile(r"(?:[a-z0-9_-]+/)*[a-z0-9_-]+(?:\.[a-z0-9_-]+)*\.webp\Z")


def unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def package(source: Path, target: Path):
    source = source.resolve(strict=True)
    if target.suffix != ".dramagic-character-pack":
        raise ValueError("Output must end in .dramagic-character-pack")
    manifest_path = source / "manifest.json"
    if manifest_path.is_symlink() or manifest_path.stat().st_size > 2 * 1024 * 1024:
        raise ValueError("Unsafe or oversized manifest")
    raw = manifest_path.read_bytes()
    manifest = json.loads(raw.decode("utf-8"), object_pairs_hook=unique_pairs)
    if manifest.get("schema_version") != "3.0":
        raise ValueError("Only 3.0 is supported; convert legacy manifests first")
    characters = manifest["characters"]
    if not isinstance(characters, list) or not 1 <= len(characters) <= 100:
        raise ValueError("Expected 1–100 characters")
    refs = set()
    for character in characters:
        ui, sprites = character["ui_metadata"], character["payload"]["emotion_sprites"]
        refs.update([ui["avatar_path"], ui["fullbody_path"], *(sprites[key] for key in ("neutral", "smile", "angry", "worried"))])
        identity = character.get("references", {}).get("identity")
        if identity is not None:
            refs.add(identity)
    files = []
    total = len(raw)
    for ref in sorted(refs):
        if not isinstance(ref, str) or len(ref) > 240 or not ASSET_PATH.fullmatch(ref):
            raise ValueError(f"Unsafe asset path: {ref}")
        path = source
        for component in ref.split("/"):
            path = path / component
            if path.is_symlink():
                raise ValueError(f"Symlink asset: {ref}")
        if not path.is_file() or not path.resolve().is_relative_to(source):
            raise ValueError(f"Missing or unsafe asset: {ref}")
        size = path.stat().st_size
        if size > 16 * 1024 * 1024:
            raise ValueError(f"Oversized asset: {ref}")
        total += size
        files.append((ref, path))
    if total > 512 * 1024 * 1024 or len(files) + 1 > 2048:
        raise ValueError("Package exceeds resource budget")
    target = target.absolute()
    # An exclusive output prevents accidental replacement; failures remove only our output.
    with target.open("xb") as output:
        try:
            with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, allowZip64=False) as archive:
                archive.writestr("manifest.json", raw)
                for ref, path in files:
                    archive.write(path, ref)
            if output.tell() > 256 * 1024 * 1024:
                raise ValueError("Compressed package exceeds 256 MiB")
        except BaseException:
            output.close()
            target.unlink(missing_ok=True)
            raise
    return len(files)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    count = package(args.source, args.output)
    print(f"Assembled {count} unique WebP files. NOT YET VALIDATED: run the native character-pack validator before importing/distributing.")


if __name__ == "__main__":
    main()
