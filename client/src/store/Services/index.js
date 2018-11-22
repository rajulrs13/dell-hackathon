export default {
    state: {
      servicelable: null,
      servicedatasety: null,
      servicedatasetypred: null
    },
    getters: {
      getservicelable(state) {
        return state.servicelable;
      },
      getservicedatasety(state) {
        return state.servicedatasety;
      },
      getservicedatasetypred(state) {
        return state.servicedatasetypred;
      }
    },
    mutations: {
      setservicelable(state, payload) {
        state.servicelable = payload;
      },
      setservicedatasety(state, payload) {
        state.servicedatasety = payload;
      },
      setservicedatasetypred(state, payload) {
        state.servicedatasetypred = payload;
      }
    },
    actions: {
      PlotServiceGraph({ commit }, payload) {
        return new Promise((resolve, reject) => {
          commit("setLoading", true);
          commit("clearError");
          commit("clearSuccess");
          console.log('Action')
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
          commit("setservicelable", d);
          commit("setservicedatasety", b);
          commit("setservicedatasetypred", c);
          resolve();
        });
      }
    }
  };
  