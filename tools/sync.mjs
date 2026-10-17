import { readFileSync, writeFileSync } from 'node:fs';
const mappings = [['../../schemas/character-pack-v3.schema.json', '../skills/dramagic-character-pack/references/character-pack-v3.schema.json'], ['../../schemas/character-pack-voices.json', '../skills/dramagic-character-pack/references/character-pack-voices.json']];
for (const [source, destination] of mappings) {
  const content = readFileSync(new URL(source, import.meta.url), 'utf8');
  const target = new URL(destination, import.meta.url);
  if (process.argv.includes('--check')) { if (readFileSync(target, 'utf8') !== content) throw new Error(`Stale ${destination}`); }
  else writeFileSync(target, content);
}
console.log('Skill format/voice snapshots synchronized');
