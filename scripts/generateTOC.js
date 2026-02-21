#!/usr/bin/env node

# TODO: Does not handle e.g. " ~ 100". Should be "--100" but produces "-100" or something

const fs = require('fs');

// Read filename from command line
const filename = process.argv[2];
if (!filename) {
  console.error('Usage: node toc.js <markdown-file>');
  process.exit(1);
}

// Read file
const markdown = fs.readFileSync(filename, 'utf8');

// Remove code blocks
const withoutCodeBlocks = markdown.replace(/```[\s\S]*?```/g, '');

// Extract ### headings
const h3Regex = /^###\s+(.+)$/gm;
let match;
const toc = [];
const seenAnchors = new Set();

while ((match = h3Regex.exec(withoutCodeBlocks)) !== null) {
  const title = match[1].trim();

  // Create URL-safe anchor
  let anchor = title
    .toLowerCase()
    .replace(/[^a-z0-9_\- ~]/g, '')   // Remove unsafe characters
    .replace(/\s+/g, '-')             // Spaces to dashes
    .replace(/^-+|-+$/g, '')          // Trim hyphens
    .replace(/~/g, '-');              // ~ to dashes

  // Ensure uniqueness
  let originalAnchor = anchor;
  let counter = 1;
  while (seenAnchors.has(anchor)) {
    anchor = `${originalAnchor}-${counter}`;
    counter++;
  }
  seenAnchors.add(anchor);

  toc.push(`* [${title}](#${anchor})`);
}

// Output TOC
console.log('## Table of Contents');
console.log(toc.join('\n'));
