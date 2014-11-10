var express = require('express');
var router = express.Router();

/* GET test1 listing. */
router.get('/', function(req, res) {
  res.send('call test1');
});

module.exports = router;
