<template>
<v-container>
    <alert-component v-if="error" :text="error.message" :color="'error'"></alert-component>
    <alert-component v-if="success" :text="success.message" :color="'success'"></alert-component>
    <h1 class="heading font-weight-light text-xs-center">Dashboard</h1>
</v-container>
</template>

<script>
export default {
  data() {
    return {
    }
  },
  methods: {    
  },
  computed: {
    user() {
      return this.$store.getters.getUserId;
    },
    loading() {
      return this.$store.getters.loading;
    },
    success() {
      return this.$store.getters.success;
    },
    error() {
      return this.$store.getters.error;
    },
    // ...mapGetters(["getUserId"]),
    // nextRoute() {
    //   return this.$route.query.redirect || "/";
    // }
  },
  watch: {    
    error(err) {
      if (!!err) {
        setTimeout(() => this.$store.dispatch("clearError"), 3000);
      }
    },
    success(con) {
      if (!!con) {
        setTimeout(() => this.$store.dispatch("clearSuccess"), 2000);
      }
    }
  }
};
</script>
