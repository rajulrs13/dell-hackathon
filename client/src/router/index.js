import Vue from "vue";
import Router from "vue-router";
import { store } from "../store/store";
import Mainpage from "@/components/mainpage";
import Login from "@/components/Auth/login";
import Home from "@/components/Auth/home";
import SignUp from "@/components/Auth/signup";
import Dashboard from "@/components/Dashboard/dashboard";
import Products from "@/components/Auth/products";
import Services from "@/components/Auth/services";
import Test from "@/components/Auth/test";
import Revenue from "@/components/Auth/revenue";
import BuyingPattern from "@/components/Auth/buyingpattern";
Vue.use(Router);

const router = new Router({
  routes: [
    {
      path: "*",
      redirect: "/"
    },
    {
      path: "/",
      name: "Mainpage",
      component: Mainpage
    },
    {
      path: "/home",
      name: "Home",
      component: Home,
      children:[
        {
          path: "/login",
          name: "Login",
          component: Login,
          meta: {
            notloggedin: true
          }
        },
        {
          path: "/test",
          name: "Test",
          component: Test,
          meta: {
            notloggedin: true
          }
        },
        {
          path: "/signup",
          name: "SignUp",
          component: SignUp,
          meta: {
            notloggedin: true
          }
        },
        {
          path: "/dashboard",
          name: "Dashboard",
          component: Dashboard,
          meta: {
            notloggedin: true
          }
        },
        {
          path: "/revenue",
          name: "Revenue",
          component: Revenue,
          meta: {
            notloggedin: true
          }
        },
        {
          path: "/buyingpattern",
          name: "BuyingPattern",
          component: BuyingPattern,
          meta: {
            notloggedin: true
          }
        },
        {
          path: "/products",
          name: "Products",
          component: Products,
          meta: {
            notloggedin: true
          }
        },
        {
          path: "/services",
          name: "Services",
          component: Services,
          meta: {
            notloggedin: true
          }
        }
      ]
    },    
  ],
  mode: "history"
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.authRequired)) {
    if (!store.getters.getUserId) {
      next({
        path: "/signin",
        query: { redirect: to.fullPath }
      });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
