import firebase from "@firebase/app";
import "@firebase/auth";
import "@firebase/firestore";

firebase.initializeApp({
  apiKey: "AIzaSyBASXFj0xx7rc3TtGWh7UO-R6aI9NBm3v0",
  authDomain: "dellhackathon-a3fc0.firebaseapp.com",
  databaseURL: "https://dellhackathon-a3fc0.firebaseio.com",
  projectId: "dellhackathon-a3fc0",
  storageBucket: "dellhackathon-a3fc0.appspot.com",
  messagingSenderId: "589056437030"
});

export default firebase;
