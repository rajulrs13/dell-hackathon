<template>
<v-container>
    <v-flex xs12 sm6>
        <div class="text-xs-center">
            <section class="container">
                <div class="columns">
                    <div class="column">
                        <chartjs-bar :backgroundcolor="['#42A5F5','#42A5F5','#42A5F5','#42A5F5','#42A5F5','#42A5F5','#42A5F5','#42A5F5','#42A5F5','#42A5F5',]" :labels="label" :data="dataset" :bind="true"></chartjs-bar>
                    </div>
                </div>
            </section>
        </div>
    </v-flex>
</v-container>
</template>

<script>
export default {
  data() {
    return {
      label: "",
      dataset: ""      
    };
  },
  computed: {
    error() {
      return this.$store.getters.error;
    },
    success() {
      return this.$store.getters.success;
    },
    loading() {
      return this.$store.getters.loading;
    }
  },
  created() {
      this.label=this.$store.getters.getlable
      this.dataset=this.$store.getters.getdatasety
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
  },
  methods: {    
  }
};
</script>