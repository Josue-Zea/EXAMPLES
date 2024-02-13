<template>
    <div>
        <h1>Formulario</h1>
        <h6>See data:</h6>
        <p>Email: {{ form.email }}</p>
        <form action="">
            <label for="">Email : </label>
            <input
                type="text"
                placeholder="Enter an email"
                v-model="form.email"
            >
            <br />
            <br />
            <label for="">Password : </label>
            <input
                type="password"
                placeholder="Enter a password"
                v-model="form.password"
            >
            <br />
            <br />
            <button
                type="button"
                v-on:click="login"
            >Login</button>
        </form>
    </div>
</template>

<script>
export default {
    name: 'LoginPage',
    data() {
        return {
            form: {
                email: '',
                password: ''
            }
        }
    },
    methods: {
        login() {
            console.log(this.form.email);
            console.log(this.form.password);
        }
    }
}
</script>