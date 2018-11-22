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
    <h1 class="heading font-weight-light text-xs-center">Enter Customer Details</h1>
    <v-progress-linear v-if="loading" class="mt-0" height="3" color="accent" :indeterminate="loading"></v-progress-linear>
    <v-layout row wrap class="mt-3">
        <v-flex xs12>
            <v-form v-model="valid" ref="form">
                <v-container>
                    <v-layout row wrap>
                        <v-flex xs12 sm4>
                            <v-text-field class="px-2" label="Customer Age" type="number" min="18" max="60" v-model="age" :rules="regrules" :disabled="loading"></v-text-field>
                        </v-flex>
                        <v-flex xs12 sm4>
                            <v-select class="px-2" :items="regions" v-model="region" :disabled="loading" label="Location of Customer" :rules="regrules"></v-select>
                        </v-flex>
                        <v-flex xs12 sm4>
                            <v-select class="px-2" :items="rams" v-model="ram" :disabled="loading" label="Select RAM capacity" suffix="GB" :rules="locrules"></v-select>
                        </v-flex>
                        <v-flex xs12 sm4>
                            <v-select class="px-2" :items="hdds" v-model="hdd" :disabled="loading" label="Select HDD capacity" suffix="GB" :rules="regrules"></v-select>
                        </v-flex>
                        <v-flex xs12 sm4>
                            <v-select class="px-2" :items="warranties" v-model="warranty" :disabled="loading" label="Warranty Period" :rules="regrules" suffix="years"></v-select>
                        </v-flex>
                        <v-flex xs12 sm4>
                            <v-select class="px-2" :items="years" v-model="year" :disabled="loading" label="Select year of purchase" :rules="regrules"></v-select>
                        </v-flex>
                        <v-flex hidden-xs sm4>
                        </v-flex>
                        <v-flex hidden-xs sm4>
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
    <v-container>
        <h1 v-if="message" class="font-weight-light">Predictions :- </h1>
        <ul>
           <h2><li class="mt-2" v-for="m in message" :key="i">{{m}}</li></h2> 
        </ul>
    </v-container>
</v-container>
</template>

<script>
export default {
    data() {
        return {
            message: "",
            regions: [
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
            region: "",
            warranty: "",
            warranties: [1, 2, 3, 4, 5],
            rams: [2, 4, 8, 16, 32],
            hdds: [180, 240, 360, 500, 1000, 2000],
            years: [
                "2009",
                "2010",
                "2011",
                "2012",
                "2013",
                "2014",
                "2015",
                "2016",
                "2017",
                "2018"
            ],
            age: "",
            ram: "",
            hdd: "",
            text: "",
            errorsnack: false,
            y: "",
            mode: "",
            timeout: 4000,
            year: "",
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
        // ...mapGetters(["getUserId"]),
        // nextRoute() {
        //   return this.$route.query.redirect || "/";
        // }
    },
    methods: {
        submitvalues() {
            this.loading = true;
            var payload = {
                code: "class",
                age: this.age,
                ram: this.ram,
                hdd: this.hdd,
                location: this.region,
                warranty: this.warranty,
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
                .then(function (response) {
                    var payload = response.data;
                    console.log(response.data);
                    var result = self.genString(payload);
                    self.message = result;
                })
                .catch(error => {
                    self.errorsnack = true;
                });
            this.loading = false;
        },
        genString(payload) {
            var x = payload.suggestions;
            var message = [];
            if (x.Need == "No") {
                message.push(
                    "Requirements of the Customer is up to date. No Services required"
                );
                return message;
            } else {
                if (x.RAM.length > 0) {
                    message.push(
                        "It seems that the RAM configuraton of the customer is low and it should be upgraded. SUGGESTION : Also company can offer upgradation of HDD because most customers upgrade their HDD with RAM"
                    );
                }
                if (x.HDD.length > 0) {
                    message.push(
                        "It seems that the HDD configuraton of the customer is low and it should be upgraded. SUGGESTION : Also company can offer upgradation of RAM and OS because most customers upgrade their RAM and OS with HDD"
                    );
                }
                if (x.Warranty == "Yes") {
                    message.push(
                        "SUGGESTION :  Company can offer customer to upgrade the warranty of the product as their is already expired or will expire shortly"
                    );
                }
                return message;
            }
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
