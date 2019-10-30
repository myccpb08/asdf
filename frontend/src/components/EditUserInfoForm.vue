<template>
    <v-form class="editForm" ref="form">
        <v-text-field v-model="password" label="PASSWORD" type="password"/>
        <v-layout justify-center pa-10>
            <v-btn large color="indigo white--text" @click="onSubmit">수정</v-btn>
        </v-layout>
    </v-form>
</template>

<script>
export default {
    data: () => ({
        password: "",
    }),
    methods: {
        onSubmit() {

        },
    }
}
</script>

<style>
    .editForm {
        top: 50%;
        left: 50%;
    }
</style>
