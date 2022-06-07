<<<<<<< HEAD
#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
fs.readFile(file, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
=======
#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
fs.readFile(file, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
>>>>>>> ed0629124a858a4ef5e5d11aba10cebc6c2241ea
