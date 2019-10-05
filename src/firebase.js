import Firebase from 'firebase'

const firebaseApp = Firebase.initializeApp({
    apiKey: "AIzaSyCUQhrczfmzYVD48qz0HUCDnPYGDU17_ws",
    authDomain: "cheetah-7dfa6.firebaseapp.com",
    databaseURL: "https://cheetah-7dfa6.firebaseio.com",
    projectId: "cheetah-7dfa6",
    storageBucket: "cheetah-7dfa6.appspot.com",
    messagingSenderId: "117386835749"
});

export const db = firebaseApp.database();
export const module_enrolment = db.ref("module_enrolment")