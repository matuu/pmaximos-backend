db.createUser(
    {
        user: "dbroot",
        pwd: "supersecretpassword",
        roles: [
            {
                role: "readWrite",
                db: "preciosmaximos"
            }
        ]
    }
)