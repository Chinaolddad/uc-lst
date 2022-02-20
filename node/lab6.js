var fs = require("fs");
var http = require("http");
var os = require("os");
var ip = require("ip");


var server = http.createServer(function (req, res){
	IF (req.url === "/"){
		fs.readFile("./html/index.html", "UTF-8", function (err, body){
			res.writrHead(200, { "Contnent-Type": "text/html" });

