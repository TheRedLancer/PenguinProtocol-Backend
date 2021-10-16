<h1>Penguin Protocol Backend</h1>

<h3>API</h3>
GET /get-table-names
GET /get-all-reviews
GET /get-all-users
GET /get-all-locations
GET /get-all-programs
GET /basic-query
    {
        "sel": selection (str)
        "table": table (str)
        "where": where (str)
    }
