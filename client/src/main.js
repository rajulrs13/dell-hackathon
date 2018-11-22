import Vue from "vue";
import App from "./App";
import router from "./router";
import Vuetify from "vuetify";
import { store } from "./store/store";
import "vuetify/dist/vuetify.min.css";
import * as firebase from "firebase";
import AlertComponent from "./components/Shared/alert.vue";
import Firebase from "./firebase/firebase";

// Helpers
import colors from "vuetify/es5/util/colors";

Vue.use(Vuetify, {
  theme: {
    primary: "#2196F3",
    secondary: "#0D47A1",
    accent: colors.orange,
    error: colors.red.lighten1,
    warning: colors.purple.accent4,
    info: colors.blue.base,
    success: colors.green.base
  }
});

Vue.config.productionTip = false;
Vue.component("alert-component", AlertComponent);
Vue.use(VueCharts)

/* eslint-disable no-new */
new Vue({
  el: "#app",
  router,
  store: store,
  render: h => h(App),
  created() {
    firebase.auth().onAuthStateChanged(user => {
      if (user) {
        store.dispatch("autoSignIn", user);
      }
    });
  }
});
