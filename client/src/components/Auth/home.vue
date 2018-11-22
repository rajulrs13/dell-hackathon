<template>
<v-app>
    <v-navigation-drawer v-model="drawer" v-if="user" class="grey lighten-5" fixed clipped app width="280">
        <v-list>
            <!-- <v-list-tile to="/">
                <v-list-tile-action>
                    <v-icon>home</v-icon>
                </v-list-tile-action>
                <v-list-tile-title>Home</v-list-tile-title>
            </v-list-tile> -->

            <!-- <v-list-tile to="/dashboard">
                <v-list-tile-action>
                    <v-icon>dashboard</v-icon>
                </v-list-tile-action>
                <v-list-tile-title>Dashboard</v-list-tile-title>
            </v-list-tile> -->

            <v-list-group no-action value="true">
                <v-list-tile slot="activator">
                    <v-list-tile-action>
                        <v-icon>filter_list</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-title>Adoption and Volume</v-list-tile-title>
                </v-list-tile>

                <v-list-tile to="/products">
                    <v-list-tile-action>
                        <v-icon>apps</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-title>Products</v-list-tile-title>
                </v-list-tile>
                <v-list-tile to="/services">
                    <v-list-tile-action>
                        <v-icon>settings</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-title>Services</v-list-tile-title>
                </v-list-tile>
            </v-list-group>
            <v-list-tile to="/revenue">
                <v-list-tile-action>
                    <v-icon>fas fa-dollar-sign</v-icon>
                </v-list-tile-action>
                <v-list-tile-title>Revnue Oppurtunities</v-list-tile-title>
            </v-list-tile>
            <v-list-tile to="/buyingpattern">
                <v-list-tile-action>
                    <v-icon>fas fa-cart-plus</v-icon>
                </v-list-tile-action>
                <v-list-tile-title>Buying Pattern</v-list-tile-title>
            </v-list-tile>
            
        </v-list>
    </v-navigation-drawer>
    <v-toolbar fixed flat color="secondary" app clipped-left>
        <v-toolbar-side-icon v-if="user" @click.native="drawer = !drawer" class="white--text"></v-toolbar-side-icon>
        <!-- <v-toolbar-side-icon @click="drawer = !drawer"></v-toolbar-side-icon> -->
        <v-toolbar-title class="mt-2 white--text">
            <router-link to="/">
                <img width="30"  :src="logo" alt="Logo">
            </router-link>
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items>
            <!-- <v-btn flat class="white--text" icon to="/">
                    <v-icon>home</v-icon>
                </v-btn> -->
            <!-- <v-btn flat class="white--text" v-if="user" to="/dashboard">
                    <v-icon left>dashboard</v-icon>
                    Dashboard
                </v-btn> -->
            <v-btn flat class="white--text" v-if="!user" to="/login">
                <v-icon left>fas fa-sign-in-alt</v-icon>
                Login
            </v-btn>
            <v-btn flat class="white--text" v-if="!user" to="/signup">
                <v-icon left>far fa-user</v-icon>
                Sign Up
            </v-btn>
            <v-btn flat class="white--text" v-if="user" @click="logout">
                <v-icon left>fas fa-sign-out-alt</v-icon>
                Logout
            </v-btn>
        </v-toolbar-items>
    </v-toolbar>
    <v-content>
        <v-container>
            <router-view></router-view>
        </v-container>
    </v-content>
</v-app>
</template>

<script>
import logo from "@/assets/logo.svg";
export default {
    data() {
        return {
            logo: logo,
            drawer: null,            
            cruds: [
                ["Create", "add"],
                ["Read", "insert_drive_file"],
                ["Update", "update"],
                ["Delete", "delete"]
            ]
        };
    },
    methods: {
        logout() {
            this.$store.dispatch("logout");
        }
    },
    computed: {
        user() {
            return this.$store.getters.getUserId;
        }
    }
};
</script>

<style>
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    margin: 0;
}

.toolbar-fixing {
    padding-top: 64px;
}

.navigation-drawer {
    margin-top: 64px !important;
}

@media screen and (max-width: 960px) {
    .toolbar-fixing {
        padding-top: 56px;
    }

    /* .navigation-drawer {
    margin-top: 56px !important;
  } */
}
</style>
