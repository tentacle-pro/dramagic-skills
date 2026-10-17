# Dramagic character-pack Skills — local draft

Three provider-neutral Agent Skills for the 3.0 character format:

- `dramagic-character-pack`: brief, manifest, personality and maintained voice matching.
- `dramagic-character-art`: six-image output specification and visual acceptance.
- `dramagic-character-release`: whitelist packaging, native validation and handoff.

This is a local development bundle, not a published open-source release. Repository/license and redistribution rights must be confirmed before publication. No project artwork is bundled. No Skills are automatically installed globally.

## Use in another Agent

Copy the three directories under `skills/` into the host's documented Skills directory, keeping sibling names. For reliable access to the packaging helper, keep this entire bundle and provide its absolute root to the Agent: `tools/` is shared and may not be automatically installed by a host that copies individual skills. Alternatively attach/read the relevant SKILL.md and give the bundle root explicitly. Agents without file/image tools must report the limitation rather than pretend to create a package.

Example request:

> Use the Dramagic character-pack skills to create one original character: Mara Venn, a fictional tidal observatory night keeper. Distinctive silver braid, rust-orange waterproof coat, brass tide gauge; calm dry humor, not a doctor/police officer or an existing official character. Author ID `local-test`, package ID `tidal-keeper`, version `1.0.0`. Use your available image tools. Deliver an importable package and separate visual/validation report; no TTS or prompts inside the package.

This is a suggested first independent acceptance character, not generated artwork or an already approved package. Confirm the actual new design with the user before costly generation if needed.

## Tool use

Node + Python3.10+ standard library are needed only for the optional whitelist assembler:

```sh
node tools/package.mjs WORKING_RELEASE_DIR NEW_OUTPUT.dramagic-character-pack
```

The assembler is not the safety authority: run a compatible native validator afterward. In the client checkout:

```sh
cargo run --manifest-path src-tauri/Cargo.toml --example validate_character_pack -- PACKAGE
```

That Cargo command is run from the client root, not this bundle. The native validator is not bundled as a portable binary yet. Without it, label output assembled/unverified. No runtime downloads, script execution from packs or media provider credentials are required by these tools.

Maintainers regenerate canonical schema/voices in the client, then run `node character-pack-skills/tools/sync.mjs`; `--check` detects drift. Distributed Skills use only copied references and never depend on the user's adjacent repository at runtime. Do not edit copied JSON as a second source.

See `evals/evals.json` for first manual trial cases. Visual quality must be checked from real images; structural tests do not prove appearance, transparency quality or licensing. The ambiguous previous doctor test does not establish custom-source recruitment acceptance. Re-run that chain with a unique character: import → recruit → save/reopen → uninstall source pack → export/reimport scenario → preview.
