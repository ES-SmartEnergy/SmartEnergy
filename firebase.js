var admin = require("firebase");

var serviceAccount = require("path/to/serviceAccountKey.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://smart-energy-695e0-default-rtdb.firebaseio.com"
});

const db = admin.firestore();

export {db};