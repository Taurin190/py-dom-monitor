var users =
    [
        {
            user: "python",
            pwd: "python",
            roles: [
                {
                    role: "readWrite",
                    db: "monitor"
                }
            ]
        }
    ];

for (var i = 0, length = users.length; i < length; ++i) {
    db.createUser(users[i]);
}