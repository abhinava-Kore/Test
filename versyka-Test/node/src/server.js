const express = require('express');
const _ = require('lodash');
const minimist = require('minimist');

const options = minimist(process.argv.slice(2));
const app = express();
const port = Number(options.port || process.env.PORT || 3000);

app.use(express.json());

// Deliberately retained Express 4 route syntax for an Express 5 upgrade review.
app.get('/files/*', (req, res) => {
  const requestedPath = req.params[0] || '';
  res.json({ path: requestedPath, normalized: _.trim(requestedPath, '/') });
});

app.get('/health', (req, res) => {
  res.json({ status: 'ok' });
});

app.listen(port, () => {
  console.log(`Fixture listening on ${port}`);
});
