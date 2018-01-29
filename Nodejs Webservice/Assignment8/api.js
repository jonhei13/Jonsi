var express = require('express');
var bodyParser = require('body-parser');
var router = express.Router();
const uuid = require('uuid/v4');

var app = require('./index');
var User = require('./entities').model('Users');
var Company = require('./entities').model('Companies');
var Punches = require('./entities').model('Punches');
var AdminToken = "1111-2222-3333-4444";

// parse application/json
router.use(bodyParser.json());

router.use(bodyParser.urlencoded({ extended: true }));

//Smá inmemory test data
var userList = [];
var companyList = [];

router.get('/api/users', function (req, res) {
    User.find({}, function(err, users){
        if(err) throw err;

        console.log(users);
        res.send(users);
    });
});

router.get('/api/companies', function (req, res) {

    Company.find({}, function(err, companies) {
        if (err) throw err;

        console.log(companies);

        res.send(companies);
      });
});

router.get('/api/companies/:id', function (req, res) {
    var companyId = req.params.id;

    Company.findById(companyId, function(err, company) {
        if (err) throw err;

        console.log(company);

        if(company == null)
        {
            res.status(404).send("Company with ID " + companyId + " not found");
        }
        else
        {
            res.send(company);
        }
      });
});

router.post('/api/companies', function(req, res){
    res.setHeader('Content-Type', 'application/json');

    if (req.body.name == undefined)
    {
        console.log("Error Failed to add to list, name and punchCount must have values");
        res.status(412).send(JSON.stringify({Error: "Failed to add to list, name and punchCount must have values"}));
    }
    else
    {
        if(req.headers.authorization === AdminToken)
        {
            Company.find({}, function(err1, results){
                if(err1) throw err1;

                var count = results.length;
                var newCompany = Company({
                    _id: count+1,
                    name: req.body.name,
                    punchCount: req.body.punchCount === undefined ? 10 : req.body.punchCount
                });

                newCompany.save(function(err2){
                    if(err2) throw err2;

                    res.status(201).send(JSON.stringify({
                        ID: newCompany._id,
                        Name: newCompany.name,
                        punchCount: newCompany.punchCount
                    }));
                });
            });
        }
        else
        {
            res.status(401).send(JSON.stringify({Error: "Token missing or wrong."}));
        }
    }
});

router.post('/api/users', function(req, res){
    res.setHeader('Content-Type', 'application/json');

    if (req.body.name == undefined || req.body.gender == undefined)
    {
        console.log("Error Failed to add to list, name and gender must have values");
        res.status(412).send(JSON.stringify({Error: "Failed to add to list, name and gender must have values"}));
    }
    else
    {
        if(req.headers.authorization === AdminToken)
        {
            User.find({}, function(err1, results){
                if(err1) throw err1;

                var count = results.length;
                var newUser = User({
                    _id: count+1,
                    name: req.body.name,
                    token: uuid(),
                    gender: req.body.gender
                });

                newUser.save(function(err2){
                    if(err2) throw err2;
                    console.log(req.headers.authorization);
                    res.status(201).send(JSON.stringify({
                        ID: newUser._id,
                        Name: newUser.name,
                        Token: newUser.token,
                        Gender: newUser.gender
                    }));
                });
            });
        }
        else
        {
            res.status(401).send(JSON.stringify({Error: "Token missing or wrong."}));
        }
    }
});

router.post('/api/my/punches', function(req, res){
    res.setHeader('Content-Type', 'application/json');

    if (req.body.company_id == undefined)
    {
        console.log("Error Failed to add to list, company_id must have a value");
        res.status(412).send(JSON.stringify({Error: "Failed to add to listError Failed to add punch, must define company_id"}));
    }
    else
    {
        User.find({Token: req.headers.authorization}, function(err, result){
            if(err) throw err;
            if(result === null)
            {
                res.status(401).send(JSON.stringify({Error: "Token missing or wrong."}));
            }
            var userId = result._id;

            Company.findOne({ _id: req.body.company_id}, function(err1, result1){
                if(err1) throw err1;
                if(result1.length === 0)
                {
                    res.status(404).send(JSON.stringify({Error: "Company ID not available."}));
                }
                Punches.find({}, function(err2, result2){
                    Punches.find({used: false, company_id: req.body.company_id, user_Id: userId}, function(err3, result3){
                        count2 = result2.length;
                        count3 = result3.length;
                        if(result3.length+1 < result1._doc.punchCount)
                        {
                            var newRecord = Punches({
                                _id: count2+1,
                                company_id: req.body.company_id,
                                user_Id: userId,
                                created: Date.now(),
                                used: false
                            });
                            newRecord.save(function(err4){
                                if(err4) throw err4;

                                res.status(201).send(JSON.stringify({ID: _id}));
                            });
                        }
                        else
                        {
                            var newRecord = Punches({
                                _id: count2+1,
                                company_id: req.body.company_id,
                                user_Id: userId,
                                created: Date.now(),
                                used: true
                            });
                            newRecord.save(function(err5){
                                if(err5) throw err5;

                                res.status(201).send(JSON.stringify({discount: true}));
                            });
                            Punches.update({used: false, company_id: req.body.company_id, user_Id: userId}, {used: true}, function(err6){
                                if(err6) throw err6;
                            });
                        }
                    });
                });
            });
        });
    }
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


module.exports = router;
