local mysql = require 'resty.mysql'
local db, err = mysql:new()
if not db then
  ngx.say("failed to instantiate mysql: ", err)
  return
end

db:set_timeout(1000) -- 1 sec
local ok, err, errno, sqlstate = db:connect{
  host = '127.0.0.1',
  port = 3307,
  data_base = 'test',
  user = 'root',
  password = 'root',
  max_packet_size = 1024 * 1024
}
if not ok then
  ngx.say("failed to connect: ", err, ": ", errno, " ", sqlstate)
  return
end

ngx.say("Connected to MySQL ...")

local res, err, errno, sqlstate = db:query("drop table if exists cats")
if not res then
  ngx.say("bad result: ", err, ": ", errno, ": ", sqlstate, ".")
  return
end

res, err, errno, sqlstate = db:query("create table cats id serial primary key, name varchar(5)")
if not res then
  ngx.say("bad result: ", err, ": ", errno, ": ", sqlstate, ".")
  return
end

ngx.say("table cats created.")

res, err, errno, sqlstate = db:query("insert into cats (name) values (\'Bob\'),(\'\'),(null)")
if not res then
  ngx.say("bad result: ", err, ": ", errno, ": ", sqlstate, ".")
  return
end

ngx.say(res.affected_rows, " rows inserted into table cats ", "(last insert id: ", res.insert_id, ")")

-- run a select query, expected about 10 rows in
-- the result set:
res, err, errno, sqlstate = db:query("select * from cats order by id asc", 10)
if not res then
  ngx.say("bad result: ", err, ": ", errno, ": ", sqlstate, ".")
  return
end

local cjson = require "cjson"
ngx.say("result: ", cjson.encode(res))

-- put it into the connection pool of size 100,
-- with 10 seconds max idle timeout
local ok, err = db:set_keepalive(10000, 100)
if not ok then
  ngx.say("failed to set keepalive: ", err)
  return
end

