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
      <h1 class="center">search</h1>
    </a>

    <form method="POST">
      <label>Search</label>
      <input type="text" name="search" value="<?php print $_POST['search'] ?>" />
      <select name="select" onchange="checkSelect();" id="select">
        <option value="name" <?php if ($_POST['select'] == "name") {
                                print "selected=\"selected\"";
                              } ?>>Name</option>
        <option value="cost" <?php if ($_POST['select'] == "cost") {
                                print "selected=\"selected\"";
                              } ?>>Cost</option>
        <option value="rating" <?php if ($_POST['select'] == "rating") {
                                  print "selected=\"selected\"";
                                } ?>>Rating</option>
      </select>
      <div id="radio">
        <label for="radio">&#60</label>
        <input type="radio" name="costSort" value="<" <?php if ($_POST['costSort'] == "<" && $_POST['select'] == "cost") {
                                                        print "checked=\"checked\"";
                                                      } ?> />
        <label for="radio">&#60&#61</label>
        <input type="radio" name="costSort" value="<=" <?php if ($_POST['costSort'] == "<=") {
                                                          print "checked=\"checked\"";
                                                        } else if ($_POST['costSort'] == "" || $_POST['select'] != "cost") {
                                                          print "checked=\"checked\"";
                                                        } ?> />
        <label for="radio">&#61</label>
        <input type="radio" name="costSort" value="=" <?php if ($_POST['costSort'] == "=" && $_POST['select'] == "cost") {
                                                        print "checked=\"checked\"";
                                                      } ?> />
        <label for="radio">&#62&#61</label>
        <input type="radio" name="costSort" value=">=" <?php if ($_POST['costSort'] == ">=" && $_POST['select'] == "cost") {
                                                          print "checked=\"checked\"";
                                                        } ?> />
        <label for="radio">&#62</label>
        <input type="radio" name="costSort" value=">" <?php if ($_POST['costSort'] == ">" && $_POST['select'] == "cost") {
                                                        print "checked=\"checked\"";
                                                      } ?> />
      </div>
      <input type="submit" value="submit" />
    </form>

    <table>
      <th>Name</th>
      <th>Cost</th>
      <th>Rating</th>
      <th>Stock</th>
      <th>Image</th>

      <?php
      include("./connect.php");
      $search = $_POST['search'];
      $select = $_POST['select'];
      $operater = $_POST['costSort'];

      if ($search) {
        if ($select == "cost") {
          $query = "SELECT * FROM `games` WHERE `$select` $operater '$search'";
        } else if ($select == "rating") {
          $query = "SELECT * FROM `games` WHERE `$select` = '$search'";
        } else {
          $query = "SELECT * FROM `games` WHERE `$select` LIKE '%$search%'";
        }
        $results = mysqli_query($link, $query);
        // Loop through the set of results, one record at a time
        while ($record = mysqli_fetch_array($results)) {
          print "<tr>
            <td>" . "<p>" . $record['name'] . "</p><br>" . "</td>
            <td>" . "<p>" . $record['cost'] . "</p><br>" . "</td>
            <td>" . "<p>" . $record['rating'] . "</p><br>" . "</td>
            <td>" . "<p>" . $record['instock'] . "</p><br>" . "</td>
            <td>" . "<div class=\"picture\"><a href=\"/" . $record['images'] . "\" tarPOST=\"_blank\"><img src=\"/" . $record['images'] . "\" alt=\"" . $record['name'] . "\" /></a></div><br>" . "</td>
          </tr>";
        }
      }
      mysqli_close($link);
      ?>
    </table>
  </div>

  <script src="js/main.js"></script>
</body>

</html>