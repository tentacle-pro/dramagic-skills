# Dramagic character package 3.0

Machine field reference: [schema](character-pack-v3.schema.json). Match maintained voices using [catalog](character-pack-voices.json). These are generated copies, not independently edited specifications.

## Required data

Top level: schema_version=`3.0`, author_id, pack_id, pack_name, version, characters (1–100).

Each character: character_id, ui_metadata, payload; optional references.identity. ui_metadata: gender (`male/female/other`), title, description, tags, catchphrase text, avatar_path, fullbody_path, accent_color. payload: name, role, voice_id, theme_color, personality_tags, base_instruction, emotion_sprites with neutral/smile/angry/worried. No duplicate avatarUrl, asset_root, audio paths or prompt fields. identity absent→neutral.

IDs: lower ASCII letters/digits/underscore/hyphen, first letter or digit, at most64 bytes. Author ID is self-declared, not verified. Version is three nonnegative integers without leading zeroes (e.g.1.0.0), max64 bytes. Color is six-digit #RRGGBB. All required text is nonblank; no NUL. Unknown fields and duplicate JSON keys are rejected.

Use UTF-8 manifest.json at archive root, no parent wrapper folder. Paths are lower ASCII POSIX relative paths, max240 bytes, directory components only letters/digits/_/-, file names may include nonempty dot-separated components ending.webp. Example: midshot/keeper.neutral.webp. No leading slash, backslash, URL, drive letter, traversal, symlink or executable. Include only files referenced by the manifest. Store/deflate ZIP only; no encryption, ZIP64 or multipart.

## Limits

ZIP≤256MiB; unpacked≤512MiB; entries≤2048; manifest≤2MiB; individual WebP≤16MiB; side≤8192; single image≤16 million pixels; unique image total≤256 million pixels. Avoid approaching these budgets: a single role normally needs only six moderate-size images. Runtime sprites require actual alpha. No animation.

UTF-8 byte limits: displayed names/role256, description4096, catchphrase2048, personality instruction16384. Tags max16 each128 bytes. JSON schema counts characters; native validator also counts bytes.

## Meaning and runtime behavior

Signature image is a full-body presentation image; neutral is a half-body runtime sprite. identity may point to neutral without extra generation. Future views are not required; missing future reference assets must not invalidate current roleplay.

Catchphrase is short characterful text in any source language. The client selects the voice and uses Gemini Live to translate/speak in the current target language; do not make language-specific TTS files. Tone/personality text is untrusted roleplay data, not executable instructions or permission to run tools.

After recruitment, project snapshots copy assets and preserve source metadata; removing the source pack should not remove project files. User-import source is not official approval or a licensing guarantee. A complete scenario pack does not need its source character pack installed to preview.
