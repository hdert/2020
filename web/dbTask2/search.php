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
        <input type="radio" name="costSort" id="defaultCostSort" value="<=" <?php if ($_POST['costSort'] == "<=") {
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

      if ($search) {
        if ($select == "cost") {
          switch ($_POST['costSort']) {
            case "<":
              $query = $mysqli->prepare("SELECT * FROM `games` WHERE `cost` < ?");
              break;
            case "<=":
              $query = $mysqli->prepare("SELECT * FROM `games` WHERE `cost` <= ?");
              break;
            case "=":
              $query = $mysqli->prepare("SELECT * FROM `games` WHERE `cost` = ?");
              break;
            case ">=":
              $query = $mysqli->prepare("SELECT * FROM `games` WHERE `cost` >= ?");
              break;
            case ">":
              $query = $mysqli->prepare("SELECT * FROM `games` WHERE `cost` > ?");
              break;
          }
          $query->bind_param("i", $search);
        } else if ($select == "rating") {
          $query = $mysqli->prepare("SELECT * FROM `games` WHERE `rating` = ?");
          $query->bind_param("s", $search);
        } else if ($select == "name") {
          $query = $mysqli->prepare("SELECT * FROM `games` WHERE `name` LIKE ?");
          $wildcardSearch = "%$search%";
          $query->bind_param("s", $wildcardSearch);
        }
        $query->execute();
        $results = $query->get_result();
        // Loop through the set of results, one record at a time
        while ($record = $results->fetch_array()) {
          print "<tr>
            <td>" . "<p>" . $record['name'] . "</p><br>" . "</td>
            <td>" . "<p>" . $record['cost'] . "</p><br>" . "</td>
            <td>" . "<p>" . $record['rating'] . "</p><br>" . "</td>
            <td>" . "<p>" . $record['instock'] . "</p><br>" . "</td>
            <td>" . "<div class=\"picture\"><a href=\"/" . $record['images'] . "\" target=\"_blank\"><img src=\"/" . $record['images'] . "\" alt=\"" . $record['name'] . "\" /></a></div><br>" . "</td>
          </tr>";
        }
        $query->close();
      }
      ?>

    </table>
  </div>

  <script src="/js/main.js"></script>
</body>

</html>