import { db } from './firebase';

const SerialPort = require('serialport');
const parsers = SerialPort.parsers;

// Use um delimitador `\r\n` como terminador de linha
const parser = new parsers.Readline({
  delimiter: '\r\n'
});

const portaSerial = new SerialPort('COM3', {
  baudRate: 9600
});

portaSerial.pipe(parser);

portaSerial.on('open', () => console.log('Porta aberta'));

parser.on('data', function (dados) {
  console.log('main.js => retorno =>', dados);
  enviarParaLoopback(dados);
});

const objetoParaEnviar = {
    campo1: "valor1",
    campo2: "valor2",
    // Outros campos e valores
  };
  
  // Para o Cloud Firestore (Firestore)
  db.collection("usuarios").add(objetoParaEnviar)
    .then((docRef) => {
      console.log("Documento adicionado com ID: ", docRef.id);
    })
    .catch((erro) => {
      console.error("Erro ao adicionar documento: ", erro);
    });
  
  // Para o Realtime Database (Database)
  // db.ref("seuCaminho").set(objetoParaEnviar);
  
