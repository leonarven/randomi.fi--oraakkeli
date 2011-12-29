<?php
	$msg = $_GET["q"];
	$url = "http://www.lintukoto.net/viihde/oraakkeli/index.php";
	preg_match_all('/<input type=\'hidden\' name=\'rnd\' value=\'(.*)\'>/', file_get_contents($url), $arr);

	$ch = curl_init();
	curl_setopt ($ch, CURLOPT_URL, $url);
	curl_setopt ($ch, CURLOPT_HEADER, 0);
	curl_setopt ($ch, CURLOPT_POSTFIELDS, "kysymys_".$arr[1][0]."=".$msg."&rnd=".$arr[1][0]);
	ob_start();
	curl_exec ($ch);
	curl_close ($ch);
	$content = ob_get_contents();
	ob_end_clean();

	preg_match_all('/<div class=\'(.*)\'>(.*)<\/div>/', $content, $arr);
	$return = htmlspecialchars($arr[2][2]);
	file_put_contents("oraakkeli.log",file_get_contents("oraakkeli.log").$msg.": ".$return."\n");
	die($return);
?>
