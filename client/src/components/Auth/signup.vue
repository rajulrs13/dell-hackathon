<template>
<v-container>   
    <alert-component v-if="error" :text="error.message" :color="'error'"></alert-component>
    <alert-component v-if="success" :text="success.message" :color="'success'"></alert-component>
    <v-layout>
        <v-flex xs12 sm8 offset-sm2>
            <v-card>
                <v-card-title class="grey lighten-3">
                    <v-icon class="ml-2 mr-3">person</v-icon>
                    <h1 class="font-weight-light">Sign Up</h1>
                </v-card-title>
                <v-progress-linear v-if="loading" class="mt-0" height="3" color="accent" :indeterminate="loading"></v-progress-linear>
                <v-form ref="signUpForm" width="500" @submit.prevent="signUp" v-model="valid">
                    <v-layout row wrap>
                        <!-- Name -->
                        <v-flex class="px-4" xs12 sm6>
                            <v-text-field :disabled="loading" v-model="name" :rules="[rules.required, rules.name]" required value="" label="Name *"></v-text-field>
                        </v-flex>
                        <!-- Email -->
                        <v-flex class="px-4" xs12 sm6>
                            <v-text-field :disabled="loading" v-model="email" :rules="rules.emailRules" label="E-mail *" required></v-text-field>
                        </v-flex>
                        <!-- Id -->
                        <v-flex class="px-4" xs12 sm6>
                            <v-text-field :disabled="loading" v-model="empid" type="number" :rules="[rules.required, rules.idmin]" name="input-password" hint="Enter your 9 digit ID" label="Employee ID *" counter="9" required></v-text-field>
                        </v-flex>
                        <!-- Contact -->
                        <v-flex class="px-4" xs12 sm6>
                            <v-text-field :disabled="loading" v-model="contact" type="number" :rules="[rules.required,rules.mincontact]" name="input-password" hint="Enter 10-digit Mobile Number" label="Contact *" counter="10" required></v-text-field>
                        </v-flex>
                        <!-- Password -->
                        <v-flex class="px-4" xs12 sm6>
                            <v-text-field :disabled="loading" v-model="password" :rules="[rules.required]" :append-icon="showPassword ? 'visibility_off' : 'visibility'" :type="showPassword ? 'text' : 'password'" name="input-password" label="Password *" autocomplete="off" hint="At least 6 characters" required @click:append="showPassword = !showPassword"></v-text-field>
                        </v-flex>
                        <!-- Re password -->
                        <v-flex class="px-4" xs12 sm6>
                            <v-text-field :disabled="loading" v-model="repassword" :rules="[rules.required, rules.repassword]" :append-icon="showPassword ? 'visibility_off' : 'visibility'" :type="showPassword ? 'text' : 'password'" name="input-password" label="Confirm Password *" autocomplete="off" hint="At least 6 characters" required @click:append="showPassword = !showPassword"></v-text-field>
                        </v-flex>
                    </v-layout>

                    <v-card-actions>
                        <br>
                        <br>
                        <v-spacer></v-spacer>
                        <v-btn  :disabled="loading" color="error" @click="clear">Clear</v-btn>
                        <v-btn type="submit" :disabled="!valid || loading" color="success" :loading="loading">Submit</v-btn>
                    </v-card-actions>
                </v-form>
            </v-card>
        </v-flex>
    </v-layout>
</v-container>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  data() {
    return {
      valid: false,
      showPassword: false,
      response: "",
      name: "",
      password: "",
      empid: null,
      contact: "",
      repassword: "",
      email: "",
      rules: {
        required: value => !!value || "Required.",
        min: v => v.length >= 6 || "Min 6 characters",
        mincontact: v => v.length == 10 || "It Should be of 10 digits",
        idmin: v => v.length == 9 || "It Should be of 9 digits",
        name: value =>
          value.trim().split(" ").length > 1 || "Enter Last Name too",
        emailRules: [
          v => !!v || "E-mail is required",
          v => /.+@.+/.test(v) || "E-mail must be valid"
        ],
        password: value =>
          value == this.repassword || "Both Passwords must be same.",
        repassword: value =>
          value == this.password || "Both Passwords must be same."
      }
    };
  },
  methods: {
    async signUp() {
      var payload = {
        name: this.name,
        password: this.password,
        contact: this.contact,
        email: this.email,
        empid: this.empid
      };
      try {
        this.response = await this.$store.dispatch("signUpUser", payload);
      } catch (ex) {
        alert(ex);
      }      
    },
    clear() {
      this.name = "";
      this.password = "";
      this.repassword = "";
      this.contact = "";
      this.email = "";
      this.empid = "";
      this.$refs.signUpForm.reset();
      console.clear();
    }
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
    ...mapGetters(["getUserId"]),
    nextRoute() {
      return this.$route.query.redirect || "/";
    }
  },
  watch: {
    // user(auth) {
    //     if (!!auth) {
    //         this.dialog = true
    //         setTimeout(() => (this.$router.replace(this.nextRoute)), 1200)

    //     }
    // },
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
