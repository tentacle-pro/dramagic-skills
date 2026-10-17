---
name: dramagic-character-art
description: >-
  Produce and visually inspect Dramagic character-pack artwork: avatar, full-body signature image and four consistent transparent half-body emotion sprites. Use for generating, finding authorized sources, editing or repairing NPC pack imagery. Provider and workflow agnostic; evaluate actual files, not prompt quality.
---

# Character artwork specification

Use the host's image search/generation/editing tools as appropriate. No particular model, segmentation package, prompt template or fixed multi-step image pipeline is required. Prefer the simplest workflow that meets the output contract.

Read sibling `dramagic-character-pack/references/format.md`. Use one approved identity/design across all six images.

| Asset | Required result | Suggested production size (not a schema minimum) |
|---|---|---|
| Avatar | Recognizable face/hair, centered head and shoulders; legible at 44px circular crop | 512×512 |
| Signature full body | Entire character including head and feet; clear silhouette and meaningful pose; background permitted | About 1024×1536 |
| neutral | Neutral/natural expression, head to mid-thigh, both shoulders/arms comfortably framed; real transparent background | About 1024×1536 |
| smile | Same identity/pose/framing with smile | Same canvas as neutral |
| angry | Same identity/pose/framing with anger | Same canvas as neutral |
| worried | Same identity/pose/framing with anxiety/uncertainty | Same canvas as neutral |

All delivered images are static WebP. Emotion files carry an alpha channel with genuinely transparent background pixels; a painted checkerboard, white backdrop or opaque RGBA container is not a cutout. No extra TTS, video, executable, SVG or HTML files.

## Visual acceptance

Inspect actual output images at useful scale. Evaluate emotion sprites on both light and dark backgrounds:

- Same face, age, hair, outfit, colors, props and hand/limb layout across emotions; expressions differ clearly without redesigning the character.
- Same canvas and alignment across sprites so runtime switching does not jump; head and visible body/arms are not accidentally cropped.
- No residual background boxes, pale/dark halos, missing hair, holes in clothing or checkerboard pixels. Semi-transparent edges may be appropriate; body interiors should not become unintentionally translucent.
- Full-body signature image keeps the complete head and feet; it is not the same composition as the runtime half-body sprite.
- Avatar remains recognizable after a circular crop. Do not automatically use an unrelated face crop.
- Compress without destroying face details or transparent edges. Keep within format byte/pixel budgets. Do not repeatedly upscale a tiny compressed image and call it a high-resolution reference.

If a check fails, repair only what failed and recheck the affected assets. Add processing code only when the host's existing tools cannot meet a repeated deterministic need. Never substitute six placeholders and report visual acceptance.

Keep prompts, provenance research and intermediate masters in the working directory outside the release tree. Return actual file paths and a concise passed/failed visual checklist. The native validator checks structure/decoding/alpha presence, not character consistency, visual quality or rights.
