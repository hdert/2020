<!DOCTYPE html>
<html lang="utf-8">

<head>
  <meta charset="utf-8">
  <title>dbTask2</title>
  <link rel="stylesheet" href="/css/styles.css" />
</head>

<body>
  <div class="col-2"></div>
  <div class="col-8">
    <a href="/search.php">
      <h1 class="center">dbTask2</h1>
    </a>

    <table>
      <th>Name</th>
      <th>Cost</th>
      <th>Rating</th>
      <th>Stock</th>
      <th>Image</th>
      <?php
      include("./connect.php");

      $query = "SELECT * FROM `games`;";

      $results = mysqli_query($link, $query);

      // Loop through the set of results, one record at a time

      while ($record = mysqli_fetch_array($results)) {
        print "<tr>
          <td>" . "<p>" . $record['name'] . "</p><br>" . "</td>
          <td>" . "<p>" . $record['cost'] . "</p><br>" . "</td>
          <td>" . "<p>" . $record['rating'] . "</p><br>" . "</td>
          <td>" . "<p>" . $record['instock'] . "</p><br>" . "</td>
          <td>" . "<div class=\"picture\"><a href=\"/" . $record['images'] . "\" target=\"_blank\"><img src=\"/" . $record['images'] . "\" alt=\"" . $record['name'] . "\" /></a></div><br>" . "</td>
        </tr>";
      }
      ?>
    </table>
  </div>
</body>

</html>