<?php
//connect to dabase
$conn = mysqli_connect('192.168.178.57', 'phpUser', 'WebsiteConnector03', 'dbObjectRecognition');

//check conncection
if (!$conn) {
    echo 'Connection error: ' . mysqli_connect_error();
}

//write query
$sql = 'SELECT object, amount, processedImages FROM tbObjects_Amount WHERE objectID = 3 OR objectID = 4 OR objectID = 5';

//make query & get result
$result = mysqli_query($conn, $sql);

//fech the resulting rows as an array
$objects = mysqli_fetch_all($result, MYSQLI_ASSOC);

mysqli_free_result($result);

//close connection
mysqli_close($conn);
?>

<!-- Header -->
<!DOCTYPE html>
<html lang="de">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>M126 - Objekterkennung</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="css/style.css">
    <link rel="apple-touch-icon" sizes="57x57" href="favicon/apple-icon-57x57.png">
    <link rel="apple-touch-icon" sizes="60x60" href="favicon/apple-icon-60x60.png">
    <link rel="apple-touch-icon" sizes="72x72" href="favicon/apple-icon-72x72.png">
    <link rel="apple-touch-icon" sizes="76x76" href="favicon/apple-icon-76x76.png">
    <link rel="apple-touch-icon" sizes="114x114" href="favicon/apple-icon-114x114.png">
    <link rel="apple-touch-icon" sizes="120x120" href="favicon/apple-icon-120x120.png">
    <link rel="apple-touch-icon" sizes="144x144" href="favicon/apple-icon-144x144.png">
    <link rel="apple-touch-icon" sizes="152x152" href="favicon/apple-icon-152x152.png">
    <link rel="apple-touch-icon" sizes="180x180" href="favicon/apple-icon-180x180.png">
    <link rel="icon" type="image/png" sizes="192x192" href="favicon/android-icon-192x192.png">
    <link rel="icon" type="image/png" sizes="32x32" href="favicon/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="96x96" href="favicon/favicon-96x96.png">
    <link rel="icon" type="image/png" sizes="16x16" href="favicon/favicon-16x16.png">
    <link rel="manifest" href="favicon/manifest.json">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="msapplication-TileImage" content="favicon/ms-icon-144x144.png">
    <meta name="theme-color" content="#ffffff">
</head>

<!-- Body -->

<body>

    <!-- Table -->
    <div class="container-xl container-box-shape">

        <table class="table">

            <thead class="thead-dark">
                <tr>
                    <th scope="col">Erkannte Objekte</th>
                    <th scope="col">Anzahl Erkennungen</th>
                    <th scope="col">Anzahl Scans</th>
                </tr>
            </thead>
            <tbody><?php foreach ($objects as $obj) { ?>
                    <tr>
                        <td><?php echo htmlspecialchars($obj['object']); ?></td>
                        <td><?php echo htmlspecialchars($obj['amount']); ?></td>
                        <td><?php echo htmlspecialchars($obj['processedImages']); ?></td>
                    </tr>
                <?php } ?>
            </tbody>

        </table>
        <p class="endnote">M126: Projektarbeit von Mike Dätwyler und Moritz Rast</p>
    </div>


</body>

</html>