import Vue from 'vue'
import Vuex from 'vuex'
import user from './User'
import shared from './Shared'
import product from './Product'
import service from './Services'
Vue.use(Vuex)



export const store = new Vuex.Store({
    modules:{     
      user:user,
      shared:shared,
      product:product,
      service:service
    }
  })
  