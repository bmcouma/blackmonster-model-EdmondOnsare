const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');
const regex = /src=['"](assets\/pictures\/[^'"]+)['"]/g;
let missing = 0;
let match;
while ((match = regex.exec(html)) !== null) {
  if (!fs.existsSync(match[1])) {
    console.log('MISSING:', match[1]);
    missing++;
  }
}
console.log('Total missing:', missing);
