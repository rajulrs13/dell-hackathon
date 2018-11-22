<template lang="html">
<v-snackbar v-model="snackbar" :bottom="y === 'bottom'" :left="x === 'left'" :multi-line="mode === 'multi-line'" :right="x === 'right'" :timeout="timeout" :top="y === 'top'" :vertical="mode === 'vertical'">
    {{ text }}
    <v-btn :color="color" flat @click="snackbar = false">
        Close
    </v-btn>
</v-snackbar>
</template>

<script>
export default {
    props: [
        'text',
        'color'
    ],
    data() {
        return {
            snackbar: true,
            y: '',
            mode: '',
            timeout: 4000
        }
    }
}
</script>
