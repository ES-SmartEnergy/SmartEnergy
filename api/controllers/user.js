import { db, db_autenticar } from "../db.js";

export const autenticarUser = (req, res) => {
  // Consulta SQL para buscar o usuário pelo nome de usuário
  const q = 'SELECT * FROM autenticacao WHERE username = ?';
  
  db_autenticar.query(q, [req.body.email], (err, results) => {
    if (err) return res.json(err);

    // Verifique se o nome de usuário foi encontrado no banco de dados
    if (results.length === 0) {
      res.status(401).json( {message: "Nome de usuário não encontrado"} ); // Nome de usuário não encontrado
      return;
    }

    const user = results[0];
    const hashedPassword = user.password;

    // Verifique a senha usando bcrypt
    if (user.password === req.body.password) {
      console.log("deu bom")
      return res.status(200).json(results)
    } else {
      return res.status(401).json( {message: "senha invalida"} );
    }
  });
};

export const getUsers = (_, res) => {
    const q = "SELECT * FROM usuarios";

    db.query(q, (err, data) => {
        if (err) return res.json(err);

        return res.status(200).json(data);
    });
};

export const addUser = (req, res) => {
    const q =
      "INSERT INTO usuarios(`nome`, `email`, `telefone`, `data_nascimento`) VALUES(?)";
  
    const values = [
      req.body.nome,
      req.body.email,
      req.body.telefone,
      req.body.data_nascimento,
    ];
  
    db.query(q, [values], (err) => {
      if (err) return res.json(err);
  
      return res.status(200).json("Usuário criado com sucesso.");
    });
  };

  export const updateUser = (req, res) => {
    const q =
      "UPDATE usuarios SET `nome` = ?, `email` = ?, `telefone` = ?, `data_nascimento` = ? WHERE `id` = ?";
  
    const values = [
      req.body.nome,
      req.body.email,
      req.body.telefone,
      req.body.data_nascimento,
    ];
  
    db.query(q, [...values, req.params.id], (err) => {
      if (err) return res.json(err);
  
      return res.status(200).json("Usuário atualizado com sucesso.");
    });
  };
  
  export const deleteUser = (req, res) => {
    const q = "DELETE FROM usuarios WHERE `id` = ?";
  
    db.query(q, [req.params.id], (err) => {
      if (err) return res.json(err);
  
      return res.status(200).json("Usuário deletado com sucesso.");
    });
  };