const http = require('http');
const {exec} = require('child_process');
http.createServer(function(req, res) {
	console.log(req.connection.remoteAddress.split(':').pop())
	exec(`echo ${req.connection.remoteAddress.split(':').pop()}	ansible_user=ubuntu > inventory	ansible_ssh_extra_args=\\'-o StrictHostKeyChecking=no\\';`, (...rslt) => {console.log(JSON.stringify(rslt));exec('ansible-playbook /var/www/webhook/init.yml -i /var/www/webhook/inventory', (err, stdout) => {console.log(stdout); res.end();})})
}).listen(3000)
