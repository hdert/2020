<!DOCTYPE html>
<html lang="utf-8">

<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
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

    $query = $mysqli->prepare("SELECT * FROM `games`");
    $query->execute();
    $results = $query->get_result();
    // Loop through the set of results, one record at a time
    while ($record = $results->fetch_array()) {
      print "<div class=\"picture col-4\">
        <a href=\"/view.php?id=" . $record['id'] . "\">
          <img src=\"/" . $record['images'] . "\" alt=\"" . $record['name'] . "\" />
        </a>
      </div>";
    }
    $query->close();
    ?>
  </div>
</body>

</html>