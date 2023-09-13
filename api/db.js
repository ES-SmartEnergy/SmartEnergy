import mysql from "mysql"

export const db = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "030101",
    database: "crud"
})

export const db_autenticar = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "030101",
    database: "autenticacao"
})