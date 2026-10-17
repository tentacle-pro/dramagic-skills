---
name: dramagic-character-pack
description: Create or revise a Dramagic importable character pack, including character identity, personality, Gemini voice selection and the 3.0 manifest. Use when users ask for a custom casting character, NPC asset pack, or a complete Dramagic character-making workflow. Coordinate art and release skills without prescribing an image provider.
---

# Dramagic character pack

Produce a usable character, not just a prompt collection. Use whatever image search, generation and editing capabilities the host Agent actually has; do not invent tool access or claim generated files that do not exist.

## Establish the brief

Use information already supplied. Ask only for missing decisions that change the result: role/personality, visual direction, desired number of characters, and stable author/package identity. Prefer original fictional characters or assets the user has rights to use. Do not copy an existing official Dramagic character merely to demonstrate import; acceptance characters should be clearly distinguishable by name and appearance.

Before producing art, describe each character's recognizable face, hair, clothing, accessories, silhouette, signature color and personality in a short production brief. Choose a stable ASCII character ID. Keep internal prompts, sources and work files outside the release tree.

## Read the contract

Read [format.md](references/format.md) for filenames, required data, compatibility and validation boundaries. For precise fields consult the bundled `character-pack-v3.schema.json`. Read `character-pack-voices.json` to match a maintained voice ID and its actual description to the character. Recommend a voice with one short reason; a description is not a guarantee of audible identity or provider availability. Do not generate TTS audio: the client translates and speaks the catchphrase through Live in the selected learning language.

## Produce the deliverables

1. Create the manifest and assets in a new working directory; never overwrite another package without consent.
2. Follow sibling `dramagic-character-art/SKILL.md` for required images and visual acceptance. If the host cannot create/process images, say so and return an explicit incomplete state, not a successful package.
3. Write one natural catchphrase expressing the character's manner and intended speaking situation. Keep personality instructions about roleplay behavior only; never add requests for tool access, credentials or bypassing system rules.
4. Prefer `references.identity` pointing to the neutral half-body image. It is a reusable identity reference, not a promise of 3D-ready geometry. Do not produce four-view sheets unless separately requested; they are not required by this version.
5. Follow sibling `dramagic-character-release/SKILL.md` to whitelist files, validate and package.

## Handoff

Give the package path and whether the native validator passed; list the character name/ID, author/package/version, selected voice and signature color. Separately report manual visual checks and anything still incomplete. No prompts, workflow files, logs or test reports belong inside the importable ZIP.

When testing a new custom character, verify it appears under user-imported packages and retains its source metadata after recruitment. Import success alone does not establish save/reopen, source-package removal or scenario exchange success. Local import does not certify copyright ownership or authorize official publication.
