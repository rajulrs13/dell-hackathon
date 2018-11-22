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
    <h1 class="heading font-weight-light text-xs-center">Select Region</h1>
    <v-progress-linear v-if="loading" class="mt-0" height="3" color="accent" :indeterminate="loading"></v-progress-linear>
    <v-layout row wrap class="mt-3">
        <v-flex xs12>
            <v-form v-model="valid" ref="form">
                <v-container>
                    <v-layout row wrap>
                        <v-flex xs12 sm8>
                            <v-select class="px-2" :items="region" v-model="regionval" :disabled="loading" label="Select Region" :rules="regrules"></v-select>
                        </v-flex>
                        <v-flex xs12 sm4 class="text-xs-center">
                            <v-btn @click="clear()" :disabled="loading" color="error" raised ripple>
                                Clear
                            </v-btn>
                            <v-btn color="accent" :disabled="!valid || loading" :loading="loading" raised ripple @click="submitvalues">
                                Predict
                            </v-btn>
                        </v-flex>
                    </v-layout>
                </v-container>
            </v-form>
        </v-flex>
    </v-layout>
    <br>
    <v-layout row wrap class="mt-3">
        <v-flex xs12>
            <template>
                <v-data-table :headers="headers" v-if="desserts" :items="desserts" class="elevation-1">
                    <template slot="items" slot-scope="props">
                      <td class="text-xs-center">{{ props.item.sno }}</td>
                        <td class="text-xs-center">{{ props.item.name }}</td>
                        <td class="text-xs-center">{{ props.item.calories }}</td>
                        <td class="text-xs-center">{{ props.item.fat }}</td>
                    </template>
                </v-data-table>
            </template>
        </v-flex>
    </v-layout>
</v-container>
</template>

<script>
export default {
  data() {
    return {      
      headers: [
        {
          text: "Priority",
          align: "center",
          sortable: false,
          value: "sno"
        },
        {
          text: "Services",
          align: "center",
          sortable: false,
          value: "services"
        },
        {
          align: "center",
          text: "Lift",
          sortable: false,
          value: "confidences"
        },
        {
          align: "center",
          text: "Confidence",
          sortable: false,
          value: "lift"
        }
      ],
      desserts: "",
      text: "",
      errorsnack: false,
      y: "",
      mode: "",
      timeout: 4000,
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
      regionval: "",
      year: 2019,
      loading: false,
      valid: false,
      locrules: [value => !!value || "Required."],
      regrules: [value => !!value || "Required."]
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
  },
  methods: {
    submitvalues() {
      this.loading = true;
      if (this.regionval == "Global") {
        var desserts = [
          {
            sno:'1',
            value: false,              
            name: "Customer who bought RAM also bought HDD",
            calories: 2.42,
            fat: "38 %"
          },
          { sno:'2',
            value: false,
            name: "Customer who bought HDD also bought RAM",
            calories: 2.22,
            fat: "33 %"
          },
          { sno:'3',
            value: false,
            name: "Customer who bought OS also bought Antivirus",
            calories: 1.84,
            fat: "32 %"
          },
          { sno:'4',
            value: false,
            name: "Customer who bought HDD also bought OS",
            calories: 1.66,
            fat: "28 %"
          },
          { sno:'5',
            value: false,
            name: "Customer who bought OS also bought Office",
            calories: 1.24,
            fat: "18 %"
          }
        ];
        this.desserts = desserts;
      } 
      else if (this.regionval == "USA") {
        var desserts = [
          {
            sno:'1',
            value: false,
            name: "Customer who bought HDD also bought RAM",
            calories: 3.81,
            fat: "38 %"
          },
          {
            sno:'2',
            value: false,
            name: "Customer who bought HDD also bought OS",
            calories: 3.25,
            fat: "32 %"
          },
          {
            sno:'3',
            value: false,
            name: "Customer who bought OS also bought Antivirus",
            calories: 2.84,
            fat: "26 %"
          },
          {
            sno:'4',
            value: false,
            name: "Customer who bought RAM also bought HDD",
            calories: 2.46,
            fat: "24 %"
          },
          {
            sno:'5',
            value: false,
            name: "Customer who bought Antivirus also bought OS",
            calories: 2.24,
            fat: "18 %"
          }
        ];
        this.desserts = desserts;
      
      }

       else if (this.regionval == "India") {
        var desserts = [
          {
            sno:'1',
            value: false,
            name: "Customer who bought RAM also bought HDD",
            calories: 3.42,
            fat: "32 %"
          },
          {
            sno:'2',
            value: false,
            name: "Customer who bought HDD also bought RAM",
            calories: 2.62,
            fat: "22 %"
          },
          {
            sno:'3',
            value: false,
            name: "Customer who bought OS also bought Antivirus",
            calories: 2.18,
            fat: "18 %"
          },
          {
            sno:'4',
            value: false,
            name: "Customer who bought OS also bought HDD",
            calories: 1.66,
            fat: "14 %"
          },
          {
            sno:'5',
            value: false,
            name: "Customer who bought Warranty also bought Antivirus",
            calories: 1.24,
            fat: "12 %"
          }
        ];
        this.desserts = desserts;
      }
       else if (this.regionval == "Singapore") {
        var desserts = [
          {
            sno:'1',
            value: false,
            name: "Customer who bought OS also bought Antivirus",
            calories: 2.06,
            fat: "28 %"
          },
          {
            sno:'2',
            value: false,
            name: "Customer who bought HDD also bought RAM",
            calories: 1.92,
            fat: "22 %"
          },
          {
            sno:'3',
            value: false,
            name: "Customer who bought Office also bought Antivirus",
            calories: 1.56,
            fat: "15 %"
          },
          {
            sno:'4',
            value: false,
            name: "Customer who bought Warranty also bought Antivirus",
            calories: 1.05,
            fat: "12 %"
          },
          {
            sno:'5',
            value: false,
            name: "Customer who bought Warranty also bought HDD",
            calories: 0.45,
            fat: "10 %"
          }
        ];
        this.desserts = desserts;
      }
       else if (this.regionval == "Russia") {
        var desserts = [
          {
            sno:'1',
            value: false,
            name: "Customer who bought RAM also bought HDD",
            calories: 3.31,
            fat: "46 %"
          },
          {
            sno:'2',
            value: false,
            name: "Customer who bought Warranty also bought RAM",
            calories: 2.48,
            fat: "42 %"
          },
          {
            sno:'3',
            value: false,
            name: "Customer who bought HDD also bought Antivirus",
            calories: 2.22,
            fat: "31 %"
          },
          {
            sno:'4',
            value: false,
            name: "Customer who bought HDD also bought OS",
            calories: 1.89,
            fat: "24 %"
          },
          {
            sno:'5',
            value: false,
            name: "Customer who bought OS also bought Office",
            calories: 1.59,
            fat: "18 %"
          }
        ];
        this.desserts = desserts;
      }
       else if (this.regionval == "China") {
        var desserts = [
          {
            sno:'1',
            value: false,
            name: "Customer who bought RAM also bought HDD",
            calories: 2.52,
            fat: " 34 %"
          },
          {
            sno:'2',
            value: false,
            name: "Customer who bought RAM also bought OS",
            calories: 2.03,
            fat: "33 %"
          },
          {
            sno:'3',
            value: false,
            name: "Customer who bought OS also bought Antivirus",
            calories: 1.89,
            fat: "27 %"
          },
          {
            sno:'4',
            value: false,
            name: "Customer who bought HDD also bought OS",
            calories: 1.55,
            fat: "22 %"
          },
          {
            sno:'5',
            value: false,
            name: "Customer who bought OS also bought Warranty",
            calories: 1.22,
            fat: "19 %"
          }
        ];
        this.desserts = desserts;
      }
       else if (this.regionval == "France") {
        var desserts = [
          {
            sno:'1',
            value: false,
            name: "Customer who bought HDD also bought RAM",
            calories: 4.42,
            fat: "44 %"
          },
          {
            sno:'2',
            value: false,
            name: "Customer who bought HDD also bought OS",
            calories: 3.88,
            fat: "38 %"
          },
          {
            sno:'3',
            value: false,
            name: "Customer who bought RAM also bought HDD",
            calories: 2.89,
            fat: "32 %"
          },
          {
            sno:'4',
            value: false,
            name: "Customer who bought Antivirus also bought OS",
            calories: 2.32,
            fat: "22 %"
          },
          {
            sno:'5',
            value: false,
            name: "Customer who bought OS also bought Office",
            calories: 2.18,
            fat: "20 %"
          }
        ];
        this.desserts = desserts;
      }
       else if (this.regionval == "Italy") {
        var desserts = [
          {
            sno:'1',
            value: false,
            name: "Customer who bought Warranty also bought HDD",
            calories: 2.22,
            fat: "38 %"
          },
          {
            sno:'2',
            value: false,
            name: "Customer who bought Warranty also bought RAM",
            calories: 2.16,
            fat: "33 %"
          },
          {
            sno:'3',
            value: false,
            name: "Customer who bought OS also bought Antivirus",
            calories: 1.61,
            fat: "32 %"
          },
          {
            sno:'4',
            value: false,
            name: "Customer who bought HDD also bought RAM",
            calories: 1.43,
            fat: "28 %"
          },
          {
            sno:'5',
            value: false,
            name: "Customer who bought OS also bought Office",
            calories: 1.22,
            fat: "18 %"
          }
        ];
        this.desserts = desserts;
      }
       else if (this.regionval == "Australia") {
        var desserts = [
          {
            sno:'1',
            value: false,
            name: "Customer who bought RAM also bought HDD",
            calories: 2.16,
            fat: "31 %"
          },
          {
            sno:'2',
            value: false,
            name: "Customer who bought HDD also bought OS",
            calories: 2.10,
            fat: "25 %"
          },
          {
            sno:'3',
            value: false,
            name: "Customer who bought OS also bought HDD",
            calories: 1.99,
            fat: "22 %"
          },
          {
            sno:'4',
            value: false,
            name: "Customer who bought Warranty also bought OS",
            calories: 1.66,
            fat: "20 %"
          },
          {
            sno:'5',
            value: false,
            name: "Customer who bought Warranty also bought Office",
            calories: 1.24,
            fat: "15 %"
          }
        ];
        this.desserts = desserts;
      }
       else if (this.regionval == "UK") {
        var desserts = [
          {
            sno:'1',
            value: false,
            name: "Customer who bought RAM also bought HDD",
            calories: 2.42,
            fat: "22 %"
          },
          {
            sno:'2',
            value: false,
            name: "Customer who bought HDD also bought OS",
            calories: 2.22,
            fat: "21 %"
          },
          {
            sno:'3',
            value: false,
            name: "Customer who bought OS also bought Antivirus",
            calories: 1.84,
            fat: "18 %"
          },
          {
            sno:'4',
            value: false,
            name: "Customer who bought HDD also bought RAM",
            calories: 1.66,
            fat: "15 %"
          },
          {
            sno:'5',
            value: false,
            name: "Customer who bought OS also bought Office",
            calories: 1.24,
            fat: "13 %"
          }
        ];
        this.desserts = desserts;
      }
       else if (this.regionval == "UAE") {
        var desserts = [
          {
            sno:'1',
            value: false,
            name: "Customer who bought OS also bought HDD",
            calories: 3.22,
            fat: "41 %"
          },
          {
            sno:'2',
            value: false,
            name: "Customer who bought HDD also bought RAM",
            calories: 3.18,
            fat: "33 %"
          },
          {
            sno:'3',
            value: false,
            name: "Customer who bought OS also bought Antivirus",
            calories: 2.60,
            fat: "28 %"
          },
          {
            sno:'4',
            value: false,
            name: "Customer who bought RAM also bought HDD",
            calories: 2.21,
            fat: "25 %"
          },
          {
            sno:'5',
            value: false,
            name: "Customer who bought OS also bought Office",
            calories: 1.88,
            fat: "21 %"
          }
        ];
        this.desserts = desserts;
      }
       else if (this.regionval == "Japan") {
        var desserts = [
          {
            sno:'1',
            value: false,
            name: "Customer who bought RAM also bought HDD",
            calories: 2.89,
            fat: "35 %"
          },
          {
            sno:'2',
            value: false,
            name: "Customer who bought HDD also bought OS",
            calories: 2.51,
            fat: "31 %"
          },
          {
            sno:'3',
            value: false,
            name: "Customer who bought OS also bought Antivirus",
            calories: 2.22,
            fat: "29 %"
          },
          {
            sno:'4',
            value: false,
            name: "Customer who bought HDD also bought RAM",
            calories: 2.10,
            fat: "24 %"
          },
          {
            sno:'5',
            value: false,
            name: "Customer who bought OS also bought Office",
            calories: 1.88,
            fat: "20 %"
          }
        ];
        this.desserts = desserts;
      }
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
