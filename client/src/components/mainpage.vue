<template>
<section>
    <!--Dell Banner Section -->
    <section>
        <v-parallax style="background-image:linear-gradient(#0D47A1,#2196F3)" height="400">
            <v-layout column align-center justify-center class="white--text">
                <!-- Logo Image -->
                <img  :src="logo" alt="Dell_logo" height="200">
                <!-- <h1 class="white--text mb-2 mt-3 display-2 text-xs-center"></h1> -->

                <!-- Get started button -->
                <v-btn round large class="primary mt-4" :href="userstatus">
                    <v-icon size="30" left>fas fa-play-circle</v-icon>
                    Get Started
                </v-btn>
            </v-layout>
        </v-parallax>
    </section>


    <!-- About the product -->
    <section>
        <br>
        <br>
        <v-layout row wrap class="" align-center>
            <v-flex xs12 class="my-3">
                <div class="text-xs-center">
                    <v-icon size="100" class="primary--text">announcement</v-icon>
                    <h2 class=" headline ">About Services - Asset & Entitlement Inventory</h2>
                    <span class="subheading font-weight-thin">
                                " We Predict revenue opportunity, adoption of new product & service offers and purchasing insights based on Asset and
                                    Entitlement database records maintained by Dell."
                            </span>
                </div>
            </v-flex>
        </v-layout>
        <br>
        <br>
     </section>


    <!-- Product Offerings -->
     <section>
            <v-layout row wrap class="my-5" align-center>
                <v-flex xs12 class="my-3">
                    <div class="text-xs-center">
                        <h2 class=" headline">Getting Started - Product Offerings</h2>
                    </div>
                </v-flex>
                <v-flex xs12 class="my-3">
                    <v-layout row wrap align-center>
                        <v-flex xs12 md3>
                            <v-card class="elevation-0 transparent">
                                <v-card-text class="text-xs-center">
                                    <v-icon size="120" class="primary--text">fas fa-globe</v-icon>
                                </v-card-text>
                                <v-card-title primary-title class="layout justify-center">
                                    <div class="headline text-xs-center font-weight-light">Forecast the volumes factors</div>
                                </v-card-title>
                            </v-card>
                        </v-flex>
                        <v-flex xs12 md3>
                            <v-card class="elevation-0 transparent">
                                <v-card-text class="text-xs-center">

                                    <v-icon size="120" class="primary--text ">fas fa-laptop</v-icon>
                                </v-card-text>
                                <v-card-title primary-title class="layout justify-center">
                                    <div class="headline text-xs-center font-weight-light">Adoption of Products and Services</div>
                                </v-card-title>
                            </v-card>
                        </v-flex>
                        <v-flex xs12 md3>
                            <v-card class="elevation-0 transparent">
                                <v-card-text class="text-xs-center">

                                    <v-icon size="120" class="primary--text ">fas fa-dollar-sign</v-icon>
                                </v-card-text>
                                <v-card-title primary-title class="layout justify-center">
                                    <div class="headline text-xs-center font-weight-light">Upcoming revenue opportunities</div>
                                </v-card-title>
                            </v-card>
                        </v-flex>
                        <v-flex xs12 md3>
                            <v-card class="elevation-0 transparent">
                                <v-card-text class="text-xs-center">

                                    <v-icon size="120" class="primary--text ">fas fa-cart-plus</v-icon>
                                </v-card-text>
                                <v-card-title primary-title class="layout justify-center">
                                    <div class="headline text-xs-center font-weight-light">Predict the Purchasing pattern</div>
                                </v-card-title>
                            </v-card>
                        </v-flex>
                    </v-layout>
                </v-flex>
            </v-layout>
     </section>
     
     <!-- Footer -->
     <v-footer height="auto">
            <v-layout row wrap>
                <v-flex xs12>
                    <v-card flat tile class="primary lighten-1 white--text text-xs-center">
                        <v-card-text>
                            <v-btn v-for="icon in icons" :href="icon.link" :key="icon.social" class="mx-3 white--text"  icon>
                                <v-icon size="24px">{{ icon.social }}</v-icon>
                            </v-btn>
                        </v-card-text>
                        <v-card-text class="mb-2">
                            We would love to hear what you think. Drop us a line, whether it is praise or criticism, a question, a suggestion or just a hello. Go ahead and send it!
                        </v-card-text>

                        <v-divider></v-divider>

                        <v-card-text class="white--text">
                            &copy;2018 — <strong>DELL</strong>
                        </v-card-text>
                    </v-card>
                </v-flex>
            </v-layout>
     </v-footer>

    </section>
</template>

<script>
import router from "../router/index";
import logo from "../assets/logo.svg";

export default {
    data: function () {
        return {
            logo: logo,
            icons: [{
                    social : "fab fa-facebook",
                    link : "https://www.facebook.com/Dell/"
                },
                {
                    social : "fab fa-twitter",
                    link : "https://twitter.com/Dell"
                },
                {
                    social : "fab fa-google-plus",
                    link : "https://plus.google.com/117161668189080869053"
                },
                {
                    social : "fab fa-linkedin",
                    link : "https://www.linkedin.com/company/dell/?originalSubdomain=in"
                },
                {
                    social : "fab fa-instagram",
                    link : "https://www.instagram.com/dell/"
                }
            ]
        };
    },
    computed: {
        userstatus() {
            if (
                this.$store.getters.getUserId !== null &&
                this.$store.getters.getUserId !== undefined
            ) {
                return "/products";
            } else {
                return "/login";
            }
        }
    }
};
</script>

    

