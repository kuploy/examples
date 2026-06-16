const express = require("express");
const { Pool } = require("pg");

const pool = new Pool({ connectionString: process.env.DATABASE_URL }); // injected by the stack
const app = express();

app.get("/", async (_req, res) => {
  await pool.query("CREATE TABLE IF NOT EXISTS visits (count int)");
  await pool.query(
    "INSERT INTO visits (count) SELECT 0 WHERE NOT EXISTS (SELECT 1 FROM visits)",
  );
  const { rows } = await pool.query(
    "UPDATE visits SET count = count + 1 RETURNING count",
  );
  res.send(`Hello from Kuploy Stacks! Visits: ${rows[0].count}`);
});

app.listen(3000, () => console.log("listening on 3000"));
