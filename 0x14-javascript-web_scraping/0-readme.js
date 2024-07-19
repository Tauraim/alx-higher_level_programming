#!/usr/bin/node

const fs = require('fs');
// import the built-in Node.js 'fs' module.

fs.readFile(process.argv[2], 'utf8', function (error, content) {
	//use fs.readFile() to read the contents of a file specified as command-line argument
	// 'utf8' specifies the encoding of the file being read
	
	if (error) {
		// if an error occurs during the file read operation, the 'error' parameter will contain	console.error(Error reading the file:', error);
	
	} else {
		// if the file is read successfully, the 'content' paramter will contain the contents of the file as a string.console.log(content);
	}
});