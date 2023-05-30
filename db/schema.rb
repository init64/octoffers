require "sqlite3"
$db = SQLite3::Database.new("database.db")

$db.execute(<<-SQL)
  CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY,
    role TXT,
    link TXT,
    category TXT,
    checked BOOL
  );
SQL
