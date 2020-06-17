<!DOCTYPE html>
<html lang="utf-8">
  <head>
    <meta charset="utf-8">
    <title>dbTask2</title>
  </head>
  <body>
    <h1>dbTask2</h1>
    <?php
      include("./connect.php");

      $query = "SELECT * FROM `games`";

      $results = mysqli_query( $link, $query );

      // Loop through the set of results, one record at a time

      while( $record = mysqli_fetch_array( $results ) ) {
          print "<hr>";
          print $record['name']."<br>";
          print $record['cost']."<br>";
          print $record['rating']."<br>";
          print $record['instock']."<br>";
          print "<img src=\"".$record['images']."\" alt=\"".$record['name']."\" /><br>";
      }
    ?>
</body>
</html>