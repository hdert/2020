<!DOCTYPE html>
<html lang="utf-8">

<head>
  <meta charset="utf-8" />
  <title>dbTask2</title>
  <link rel="stylesheet" href="/css/styles.css" />
</head>

<body>
  <div class="col-2"></div>
  <div class="col-8">
    <a href="/">
      <h1 class="center">gallery</h1>
    </a>

    <?php
    include("./connect.php");

    $query = "SELECT * FROM `games`";
    $results = mysqli_query($link, $query);
    // Loop through the set of results, one record at a time
    while ($record = mysqli_fetch_array($results)) {
      print "<div class=\"picture col-4\">
        <a href=\"/view.php?id=" . $record['id'] . "\">
          <img src=\"/" . $record['images'] . "\" alt=\"" . $record['name'] . "\" />
        </a>
      </div>";
    }
    mysqli_close($link);
    ?>
  </div>
</body>

</html>