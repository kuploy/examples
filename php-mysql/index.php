<?php
// Each value is injected by a separate stack connection.
$db = new mysqli(
    getenv('DB_HOST'),
    getenv('DB_USER'),
    getenv('DB_PASSWORD'),
    getenv('DB_NAME')
);
$db->query("CREATE TABLE IF NOT EXISTS visits (count INT)");
$db->query("INSERT INTO visits (count) SELECT 0 WHERE NOT EXISTS (SELECT 1 FROM visits)");
$db->query("UPDATE visits SET count = count + 1");
$n = $db->query("SELECT count FROM visits")->fetch_row()[0];
echo "Hello from Kuploy Stacks! Visits: {$n}";
