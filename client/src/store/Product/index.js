export default {
  state: {
    productlable: null,
    productdatasety: null,
    productdatasetypred: null
  },
  getters: {
    getlable(state) {
      return state.productlable;
    },
    getdatasety(state) {
      return state.productdatasety;
    },
    getdatasetypred(state) {
      return state.productdatasetypred;
    }
  },
  mutations: {
    setlable(state, payload) {
      state.productlable = payload;
    },
    setdatasety(state, payload) {
      state.productdatasety = payload;
    },
    setdatasetypred(state, payload) {
      state.productdatasetypred = payload;
    }
  },
  actions: {
    PlotProductGraph({ commit }, payload) {
      return new Promise((resolve, reject) => {
        commit("setLoading", true);
        commit("clearError");
        commit("clearSuccess");
        //console.log('Action')
        var a = payload.X;
        //console.log(a)
        var b = payload.y;
        //console.log(b)
        var c = payload.y_pred;
        //console.log(c)
        var d = [];
        for (var i = 0; i < a.length; i++) {
          d.push(a[i][0]);
        }
        //console.log(d)
        commit("setlable", d);
        commit("setdatasety", b);
        commit("setdatasetypred", c);
        resolve();
      });
    }
  }
};
