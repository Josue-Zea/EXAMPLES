<template>
    <div>
        <h1>PostList</h1>
        <h5 v-for="(item, index) in users" :key="index">
            <h1 v-if="index%2===0">{{ item.id }}</h1>
            <h6 v-else>{{ item.id }}</h6>
        </h5>
    </div>
</template>

<script>
export default {
    name: 'PostList',
    data () {
        return {
            users: []
        }
    },
    async created () {
        const result = await fetch('https://jsonplaceholder.typicode.com/posts');
        this.users = await result.json();
    }
}
</script>