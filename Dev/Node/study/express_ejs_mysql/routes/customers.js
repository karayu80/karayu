var express = require('express');
var router = express.Router();

/*
*	GET customers listing.
*/

router.get('/', function(req, res) {
	req.getConnection(function(err, connection) {
		connection.query('SELECT * FROM customer', function(err,rows) {
			if(err)
				console.log("Error Selection : %s ", err);

			res.render('customers', {page_title:"Customers - Node.js", data:rows});
		});
	});
});

router.get('/add', function(req, res) {
	res.render('add_customer', {page_title:"Add Customers - Node.js"});
});

router.post('/add', function(req, res) {
	var input = JSON.parse(JSON.stringify(req.body));
	req.getConnection(function(err, connection) {
		var data = {
			name 	: input.name,
			address : input.address,
			email 	: input.email,
			phone 	: input.phone
		};

		var query = connection.query("INSERT INTO customer set ? ", data, function(err, rows) {
			if(err)
				console.log("error inserting : %s ", err );

			res.redirect('/customers');
		});
	});
});

router.get('/edit/:id', function(req, res) {
	console.log("call get edit %d", req.params.id);
	var id = req.params.id;
	req.getConnection(function(err, connection) {
		connection.query('SELECT * FROM customer WHERE id = ?', id, function(err, rows) {
			if(err)
				console.log("Error Selecting : %s", err);

			res.render('edit_customer', {page_title:"Edit Customers - Node.js", data:rows});
		});
	});
});

router.post('/edit/:id', function(req, res) {
	console.log("call post edit %d", req.params.id);
	var input = JSON.parse(JSON.stringify(req.body));
	var id = req.params.id;

	req.getConnection(function(err, connection) {
		var data = {
			name 	: input.name,
			address : input.address,
			email 	: input.email,
			phone 	: input.phone
		};

		var query = connection.query("UPDATE customer set ? WHERE id = ?", [data, id], function(err, rows) {
			if (err)
				console.log("Error Updateing : %s", err);

			res.redirect('/customers');
		});
	});

});

router.get('/delete/:id', function(req, res) {
	console.log("call get delete %d", req.params.id);
	var id = req.params.id;
	req.getConnection(function(err, connection) {
		connection.query('SELECT * FROM customer WHERE id = ?', id, function(err, rows) {
			if(err)
				console.log("Error Selecting : %s", err);

			res.render('delete_customer', {page_title:"Delete Customers - Node.js", data:rows});
		});
	});
});

router.post('/delete/:id', function(req, res) {
	console.log("call post delete %d", req.params.id);
	var id = req.params.id;
	var input = JSON.parse(JSON.stringify(req.body));
	console.log(input);
	req.getConnection(function(err, connection) {
		var data = {
			name 	: input.name,
			address : input.address,
			email 	: input.email,
			phone 	: input.phone
		};

		var query = connection.query("DELETE FROM customer WHERE id = ?", id, function(err, rows) {
			if(err)
				console.log("Error deleteing : %s ", err);

			res.redirect('/customers');
		});
	});

});

module.exports = router;
