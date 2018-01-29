var express = require('express');
var app = express();
var MongoClient = require('mongodb').MongoClient;
var mongoose = require('mongoose');
var token = require('uuid/v4');

var api = require('./api');
var entities = require('./entities');

var AdminToken = "1111-2222-3333-4444";

app.use('/', api);
app.use('/', entities);

var server = app.listen(8081, function () {

  var host = server.address().address;
  var port = server.address().port;

  console.log("Example app listening at http://%s:%s", host, port);

});

mongoose.connect('mongodb://arnarjojo:hopur3rokkar@arnarsdb-shard-00-00-h6wo2.mongodb.net:27017,arnarsdb-shard-00-01-h6wo2.mongodb.net:27017,arnarsdb-shard-00-02-h6wo2.mongodb.net:27017/test?ssl=true&replicaSet=ArnarsDB-shard-0&authSource=admin',function (err, db) {
    if (err) throw err;

    mongoose.connection.db.dropDatabase();
    var users = mongoose.models.Users;
    if(users.schema.indexes.length === 0){
        var User = mongoose.models.Users;
        var admin = User({
            _id: 1, 
            name: "Admin", 
            token: AdminToken, 
            gender: "o"
        });
        admin.save(function(err){
            if(err) throw err;
        });
    }
});

module.exports = app;