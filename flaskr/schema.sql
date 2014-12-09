drop table if exists code;

CREATE TABLE code (
  id    INTEGER PRIMARY KEY AUTOINCREMENT,
  date  TEXT NOT NULL,
  code  TEXT NOT NULL,
  key   TEXT NOT NULL UNIQUE 
);


