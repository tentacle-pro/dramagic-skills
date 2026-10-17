---
name: dramagic-character-release
description: Validate and package a Dramagic 3.0 character release from existing manifest and artwork, or convert a legacy 2.0 manifest with explicit author/package/version. Use for import-ready ZIP assembly, missing-reference troubleshooting and release checks. Do not generate artwork unless the user also requests it.
---

# Character release

Read sibling `dramagic-character-pack/references/format.md` and the JSON schema there. Release contains only `manifest.json` and its referenced static WebP files. An archive suffix is `.dramagic-character-pack`, not `.zip`, although its container is ZIP.

## Release checks

1. Obtain stable author ID, pack ID and three-part numeric release version. Do not invent an official identity or reuse someone else's namespace. Same name with different content is an update, not a new trusted source.
2. Validate all required fields against the bundled schema; check voice against the supplied voice catalog. JSON schema alone cannot detect duplicate keys, decode WebP, enforce UTF-8 byte budgets or prove safety.
3. Confirm all six required assets per character exist. Allow identity to reuse neutral; do not duplicate the bytes simply because two manifest fields reference the same file. Apply the art skill's manual checklist separately.
4. Run `tools/package.mjs` from this bundle root with source directory and NEW output path. It copies only referenced media, rejects unsafe paths/duplicate keys/links, and asks a ZIP implementation for store/deflate output. It does not execute package files or download media.
5. Run the authoritative native validator against the finished archive. In the client checkout: `cargo run --manifest-path src-tauri/Cargo.toml --example validate_character_pack -- PACKAGE`. Outside the checkout, use a compatible separately supplied validator; do not pretend the skill bundle includes a prebuilt binary. If unavailable, clearly label the result unverified and do not call it import-ready.
6. Deliver the package, validation result and separate visual-check report. Keep reports, prompts, source screenshots and workflow files outside the archive. Do not upload or publish it without the user's request and rights/permission checks.

## Legacy input

The client importer only accepts 3.0 user packages. The authoring converter `scripts/convert-character-pack-v2.ts` in the client checkout requires SOURCE OUTPUT AUTHOR_ID PACK_ID VERSION; it projects manifest data only and discards old root/audio fields. It is not a full pack converter. Collect the referenced WebP files, run the same packaging/validation and preserve the original source directory.

If the validator rejects a release, report the concrete failure and fix the producer/reference. Do not disable validation, rename a corrupt file extension or add fake missing images to force acceptance.
