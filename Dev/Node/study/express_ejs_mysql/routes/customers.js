var express = require('express');
var router = express.Router();

/*
*	GET customers listing.
*/

// get customer list
router.get('/', function(req, res) {
	req.getConnection(function(err, connection) {
		connection.query('SELECT * FROM customer', function(err,rows) {
			if(err)
				console.log("Error Selection : %s ", err);

			res.render('customers', {page_title:"Customers - Node.js", data:rows});
		});
	});
});

// get add form for customer
router.get('/add', function(req, res) {
	res.render('add_customer', {page_title:"Add Customers - Node.js"});
});

// add customer
router.post('/', function(req, res) {
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
				console.log("Error Inserting : %s ", err );

			res.redirect('/customers');
		});
	});
});

// get edit form for user
router.get('/:id/edit', function(req, res) {
	var id = req.params.id;
	req.getConnection(function(err, connection) {
		connection.query('SELECT * FROM customer WHERE id = ?', id, function(err, rows) {
			if(err)
				console.log("Error Selecting : %s", err);

			res.render('edit_customer', {page_title:"Edit Customers - Node.js", data:rows});
		});
	});
});

// modify user data
router.put('/:id', function(req, res) {
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

// get delete form
router.get('/:id/delete', function(req, res) {
	var id = req.params.id;
	req.getConnection(function(err, connection) {
		connection.query('SELECT * FROM customer WHERE id = ?', id, function(err, rows) {
			if(err)
				console.log("Error Selecting : %s", err);

			res.render('delete_customer', {page_title:"Delete Customers - Node.js", data:rows});
		});
	});
});

// delete user data
router.delete('/:id', function(req, res) {
	var id = req.params.id;
	var input = JSON.parse(JSON.stringify(req.body));
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
