-- Creates an index idx_name_first_score
-- on the table names and the first letter of name
-- and the score must be indexed.
DROP INDEX IF EXISTS idx_name_first_score ON names;
CREATE INDEX idx_name_first_score ON names (SUBSTRING(nam, 1, 1) score);
