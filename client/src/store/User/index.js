import * as firebase from "firebase";
import db from "../../firebase/db";
import router from "../../router/index";

export default {
  state: {
    userid: null
  },
  getters: {
    getUserId(state) {
      return state.userid;
    }
  },
  mutations: {
    setUserId(state, payload) {
      state.userid = payload;
    }
  },
  actions: {
    signUpUser({ commit, dispatch }, payload) {
      commit("setLoading", true);
      commit("clearError");
      commit("clearSuccess");
      firebase
        .auth()
        .createUserWithEmailAndPassword(payload.email, payload.password)
        .then(function(data) {
          db.collection("employee")
            .doc(data.user.uid)
            .set({
              name: payload.name,
              contact: payload.contact,
              email: payload.email,
              empid: payload.empid
            })
            .then(function() {
              
              dispatch("signUserIn", {
                email: payload.email,
                password: payload.password
              });
            })
            .catch(function(error) {
              commit("setLoading", false);
              commit("setError", error);
            });
        })
        .catch(error => {
          commit("setLoading", false);
          commit("setError", error);
        });
    },
    autoSignIn({ commit }, payload) {
      commit("setLoading", true);
      commit("clearError");
      commit("clearSuccess");
      commit("setUserId", payload.uid);
      commit("setSuccess", { message: "Logged In Successfully", status: true });
      commit("setLoading", false);
    },
    signUserIn({ commit, dispatch }, payload) {
      commit("setLoading", true);
      commit("clearError");
      commit("clearSuccess");
      firebase
        .auth()
        .signInWithEmailAndPassword(payload.email, payload.password)
        .then(data => {
          commit("setUserId", data.user.uid);          
          commit("setSuccess", {
            message: "Logged In Successfully",
            status: true
          });
          router.replace("/products");          
          commit("setLoading", false);
          setTimeout(() => dispatch("clearSuccess"), 2000);
        })
        .catch(error => {
          commit("setLoading", false);
          commit("setError", error);
        });
    },
    logout({ commit, dispatch }) {
      firebase.auth().signOut();
      commit("setUserId", null);            
      router.push("/login");
      commit("setSuccess", {
        message: "Logged Out Successfully",
        status: true
      });
      setTimeout(() => dispatch("clearSuccess"), 2000);
    }
  }
};
