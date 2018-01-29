var express = require('express');
var app = express();
var bodyParser = require('body-parser');


// parse application/json
app.use(bodyParser.json());

app.use(bodyParser.urlencoded({ extended: true }));


//Smá inmemory test data
var userList = [];
var companyList = [];

app.get('/api/users', function (req, res) {
    res.send(userList);
});

app.get('/api/companies', function (req, res) {
    res.send(companyList);

});

app.get('/api/companies/:id', function (req, res) {
    var companyId = req.params.id;
    
    var companyToReturn = null;

    for(var i = 0; i < companyList.length; i++)
    {
        if(companyList[i].id == companyId)
        {
            companyToReturn = companyList[i];
        }
    }

    if(companyToReturn == null)
    {
        res.send("Company with ID " + companyId + " not found");
    }
    else
    {
        res.send(companyToReturn);
    }
});

app.post('/api/companies', function(req, res){
    res.setHeader('Content-Type', 'application/json');
    console.log(req.body);
    console.log(req.body.name);
    if (req.body.name === undefined || req.body.punchCount === undefined){
        res.status(412).send("Error Failed to add to list, name and punchcount must have values");
        console.log("Error Failed to add to list, name and punchcount must have values");
    }
    else{
        res.send(JSON.stringify({
            name: req.body.name || null,
            punchCount: req.body.punchCount || null
        }));
        var newCompany = { id: ObjectSize(companyList), name: req.body.name, punches: req.body.punchCount};
        companyList.push(newCompany);
        //debugging output for the terminal
        console.log('New company added: ID: ' + ObjectSize(companyList) + ', Name: ' + req.body.name + ', punchCount: ' + req.body.punchCount);
    }
});

app.post('/api/users', function(req, res){
    res.setHeader('Content-Type', 'application/json');
 
    res.send(JSON.stringify({
        name: req.body.name || null,
        email: req.body.email || null
    }));
    if (req.body.name == undefined || req.body.email == undefined){
        console.log("Error Failed to add to list, name and email must have values");
    }
    else{
        var newUser = { id: ObjectSize(userList), name: req.body.name, email: req.body.email, punches: []};
        userList.push(newUser);
        //debugging output for the terminal
        console.log('New user added: ID: ' + ObjectSize(userList) + ', Name: ' + req.body.name + ', email: ' + req.body.email);
    }
});

app.get('/api/users/:id/punches', function(req, res){
    userListTemp = [];
    userList.forEach(function(item){
      if(item.id == req.params.id){
        if(req.query.company == null){
            userListTemp.push(item);
        }
        else if(req.query.company != null)
        {
            item.punches.forEach(function(punch){
                if(punch.CID == req.query.company){
                    userListTemp.push(item);
                }
            });
        }
        else{
          res.status(404);
        }
      }
      else{
        res.status(404);
      }
    });
    res.send(userListTemp);
});

app.post('/api/users/:id/punches', function(req, res) {
    res.setHeader('Content-Type', 'application/json');
    if(req.body.id == null) {
        console.log("Error Failed to add to list");
    }
    else{
        userList.forEach(function(item){
            if(item.id == req.params.id){
                var isEmpty = true;
                item.punches.forEach(function(punch) {
                    if(punch.CID == req.body.id) {
                        punch.count++;
                        isEmpty = false;
                        res.send({ Status: 'Successfully added punch' });
                    }
                });
                if(isEmpty){
                    var companyName = '';
                    companyList.forEach(function(comp) {
                        if(req.body.id == comp.id) {
                            companyName = comp.name;
                        }
                    });
                    if(companyName == '') {
                        res.status(404);
                    }
                    else{
                        var newCount = { CID: req.body.id, name: companyName, count: 1 };
                        item.punches.push(newCount);
                        res.send({ Status: 'Successfully added punch' });
                    }
                }
            }
        });
        res.status(404).send({error: 'Something went wrong'});
    }
});

var server = app.listen(8081, function () {

  var host = server.address().address
  var port = server.address().port

  console.log("Example app listening at http://%s:%s", host, port)

});

function ObjectSize(obj)
{
    var count = 1;

    for(var prop in obj)
        {
            if (Object.prototype.hasOwnProperty.call(obj, prop)) {
                count++;
            }
        }
    return count;
}