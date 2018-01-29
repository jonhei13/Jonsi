var mongoose = require('mongoose');
var express = require('express');
var model = express();

var Schema = mongoose.Schema;

var UserModelSchema = new mongoose.Schema({
    _id: Number,
    name: String,
    token: String,
    gender: String
  },{
    versionKey: false

});

var CompanyModelSchema = new mongoose.Schema({
    _id: Number,
    name: String,
    punchCount: { type: Number, default: 10 }
  },{
    versionKey: false
  });

var PunchModelSchema = new mongoose.Schema({
    _id: Number,
    company_id: Number,
    user_id: Number,
    created: Date,
    used: { type: Boolean, default: false }
  },{
    versionKey: false
  });

var UserModel = mongoose.model('Users', UserModelSchema);
var CompanyModel = mongoose.model('Companies', CompanyModelSchema);
var PunchModel = mongoose.model('Punches', PunchModelSchema);

module.exports = UserModel;
module.exports = CompanyModel;
module.exports = PunchModel;
