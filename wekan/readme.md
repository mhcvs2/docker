<pre><code>
use admin
db.createUser(
  {
    user: "root",
    pwd: "root.123",
    roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]
  }
)


</code></pre>
