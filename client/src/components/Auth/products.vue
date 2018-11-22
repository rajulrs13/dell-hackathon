<template>
<v-container>
    <v-snackbar v-model="errorsnack" :bottom="y === 'bottom'" :left="x === 'left'" :multi-line="mode === 'multi-line'" :right="x === 'right'" :timeout="timeout" :top="y === 'top'" :vertical="mode === 'vertical'">
        Server Error
        <v-btn color="error" flat @click="errorsnack = false">
            Close
        </v-btn>
    </v-snackbar>
    <alert-component v-if="error" :text="error.message" :color="'error'"></alert-component>
    <alert-component v-if="success" :text="success.message" :color="'success'"></alert-component>
    <h1 class="heading font-weight-light text-xs-center">Enter Product Details</h1>
    <v-progress-linear v-if="loading" class="mt-0" height="3" color="accent" :indeterminate="loading"></v-progress-linear>
    <v-layout row wrap class="mt-3">
        <v-flex xs12>
            <v-form v-model="valid" ref="form">
                <!-- <v-card raised hover class="transparent"> -->
                <!-- <v-crad-text> -->
                <v-container>
                    <v-layout row wrap>
                        <v-flex xs12 sm4>
                            <v-select class="px-2" :items="products" v-model="product" :disabled="loading" label="Select Product" :rules="locrules"></v-select>
                        </v-flex>
                        <v-flex xs12 sm4>
                            <v-select class="px-2" :items="region" v-model="regionval" :disabled="loading" label="Select Region" :rules="regrules"></v-select>
                        </v-flex>
                        <!-- <v-flex xs12 sm4>
                                    <v-text-field class="px-2" label="Prediction Year" type="number" v-model="year" :rules="regrules" :disabled="loading"></v-text-field>
                                </v-flex> -->
                        <v-flex xs12 sm4 class="text-xs-center">
                            <v-btn @click="clear()" :disabled="loading" color="error" raised ripple>
                                Clear
                            </v-btn>
                            <v-btn color="accent" :disabled="!valid || loading" :loading="loading" raised ripple  @click="submitvalues">
                                Predict
                            </v-btn>
                        </v-flex>
                    </v-layout>
                </v-container>
                <!-- </v-crad-text> -->
                <!-- <v-card-actions> -->
                <v-spacer></v-spacer>

                <!-- </v-card-actions> -->
                <!-- </v-card> -->
            </v-form>
        </v-flex>
    </v-layout>
    <br>
    <h2 v-if="predictedoutput" class="mt-2 heading text-xs-center">Predicted value for 2019 = {{this.predictedoutput}} unit(s)</h2>
    <v-layout row wrap class="mt-2">
        <v-flex xs12 sm6>
            <br>
            
            <canvas  id="myChart"></canvas>
        </v-flex>
        <v-flex xs12 sm6>
            <br>
            <canvas id="myBarChart"></canvas>  
            <!-- <div class="text-xs-center">
            <section >
                <div class="columns">
                    <div class="column">
                        <chartjs-bar  v-if="predictedoutput" :backgroundcolor="['#42A5F5','#42A5F5','#42A5F5','#42A5F5','#42A5F5','#42A5F5','#42A5F5','#42A5F5','#42A5F5','#42A5F5','#F44336']"  :labels="barlabel" :data="bardata" :bind="true" ></chartjs-bar>
                    </div>
                </div>
            </section> -->
        <!-- </div> -->
        </v-flex>
    </v-layout>

</v-container>
</template>

<script>
export default {
  data() {
    return {
      options: "",
      barlabel: null,
      bardata: null,
      predictedoutput: null,
      label: "",
      dataset: "",
      text: "",
      errorsnack: false,
      y: "",
      mode: "",
      timeout: 4000,
      products: ["Laptop", "Workstation", "Desktop"],
      region: [
        "Global",
        "USA",
        "India",
        "Singapore",
        "Russia",
        "China",
        "France",
        "Italy",
        "Australia",
        "UK",
        "UAE",
        "Japan"
      ],
      product: "",
      regionval: "",
      year: 2019,
      loading: false,
      valid: false,
      locrules: [value => !!value || "Required."],
      regrules: [value => !!value || "Required."],
      data: []
    };
  },
  methods: {},
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
    }
    // ...mapGetters(["getUserId"]),
    // nextRoute() {
    //   return this.$route.query.redirect || "/";
    // }
  },
  methods: {
    submitvalues() {
      this.loading = true;
      var payload = {
        code: "reg",
        type: "product",
        product: this.product,
        region: this.regionval,
        year: this.year
      };
      var connectionlink = "http://192.168.43.128:8000/predict";
      var config = {
        headers: {
          "Content-Type": "multipart/form-data",
          "Access-Control-Allow-Origin": "*"
        }
      };
      self = this;
      axios
        .post(connectionlink, payload, config)
        .then(function(response) {
          self.predictedoutput = Math.round(response.data.year_val[0]);
          var d = response.data;
          self.$store.dispatch("PlotProductGraph", d).then(function() {
            self.label = self.$store.getters.getlable;
            self.dataset = self.$store.getters.getdatasetypred;
            var temp = self.$store.getters.getdatasety;
            var p = [];
            for (var index = 0; index < temp.length; index++) {
              var obj = {
                x: self.label[index],
                y: temp[index]
              };
              p.push(obj);
            }
            var q = [];
            for (var index = 0; index < self.label.length; index++) {
              var obj = {
                x: self.label[index],
                y: self.dataset[index]
              };
              q.push(obj);
            }
            self.barlabel = self.label;
            self.bardata = temp;
            self.barlabel.push(2019);
            self.bardata.push(Math.round(response.data.year_val[0]));
            var ctx = document.getElementById("myChart").getContext("2d");
            var scatterChart = new Chart(ctx, {
              type: "scatter",
              data: {
                datasets: [
                  {
                    label: "Actual Data",
                    data: p,
                    fill: false,
                    showLine: false,
                    pointBackgroundColor: "#F44336",
                    borderColor: "#F44336"
                  },
                  {
                    label: "Prediction Curve",
                    data: q,
                    type: "line",
                    fill: false,
                    pointRadius: 0,
                    borderColor: "#64B5F6"
                  }
                ]
              },
              options: {
                scales: {
                  yAxes: [
                    {
                      scaleLabel: {
                        display: true,
                        labelString: "Quantity of Product"
                      }
                    }
                  ],
                  xAxes: [
                    {
                      type: "linear",
                      position: "bottom",
                      scaleLabel: {
                        display: true,
                        labelString: "Year"
                      }
                    }
                  ]
                }
              }
            });

            var cttx = document.getElementById("myBarChart").getContext("2d");
            var chart = new Chart(cttx, {
              // The type of chart we want to create
              type: "bar",

              // The data for our dataset
              data: {
                labels: self.barlabel,
                datasets: [
                  {
                    label: "Actual sale",
                    data: self.bardata,
                    backgroundColor: ['#64B5F6','#64B5F6','#64B5F6','#64B5F6','#64B5F6','#64B5F6','#64B5F6','#64B5F6','#64B5F6','#64B5F6','#F44336'],
                  }
                ]
              },

              // Configuration options go here
              options: {
                scales: {
                  yAxes: [
                    {
                      scaleLabel: {
                        display: true,
                        labelString: "Quantity of Product"
                      }
                    }
                  ],
                  xAxes: [
                    {                      
                      scaleLabel: {
                        display: true,
                        labelString: "Year"
                      }
                    }
                  ]
                }
              }
            });
          });
        })
        .catch(error => {
          self.errorsnack = true;
        });
      this.loading = false;
    },
    clear() {
      this.$refs.form.reset();
    }
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
