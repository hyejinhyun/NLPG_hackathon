<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8" >
<style>
table{border:1px solid gray; border-collapse:collapse;}
td{border:1px solid gray;padding:5px;}
</style>
</head>
<body>
<?php

$conn = mysqli_connect("localhost", "root", "171217");
mysqli_query($conn,'SET NAMES utf8');
if (!$conn) {
echo "Unable to connect to DB: " . mysqli_error();
exit;
}

if (!mysqli_select_db($conn,"test")) {
echo "Unable to select mydbname: " . mysqli_error();
exit;
}

$sql = "SELECT *
FROM sample
LIMIT 10";

$result = mysqli_query($conn,$sql);

if (!$result) {
echo "Could not successfully run query ($sql) from DB: " . mysqli_error();
exit;
}

if (mysqli_num_rows($result) == 0) {
echo "No rows found, nothing to print so am exiting";
exit;
}

// While a row of data exists, put that row in $row as an associative array
// Note: If you're expecting just one row, no need to use a loop
// Note: If you put extract($row); inside the following loop, you'll
// then create $userid, $fullname, and $userstatus
echo "<table>";
while ($row = mysqli_fetch_assoc($result)) {
echo "<tr><td>{$row['id']}</td><td>{$row['title']}</td><td>{$row['content']}</td><td>{$row['url']}</td></tr>";
}
echo "</table>";
mysqli_free_result($result);

?>
</body>
</html>