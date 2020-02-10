#!/usr/bin/env node

const path = require('path');
const matchersPath = path.join(__dirname, '.github');

console.log(`::add-matcher::${path.join(matchersPath, 'flake8-error-problem-matcher.json')}`);
console.log(`::add-matcher::${path.join(matchersPath, 'flake8-warning-problem-matcher.json')}`);
