<template>
    <header class='navbar-section' >
        <section>
            <img src="../assets/logo.png" alt="Logo">
        </section>
        <section>
            <p> Olá usuario </p>
        </section>
    </header>
</template>

<script>
export default {
        name: 'TheHeader',
        props: {
            msg: String
        }
    }
</script>

<style>
    .navbar-section {
        display: flex;
        justify-content: space-between;
        padding: 10px;
        background-color: #1a5005;
        height: 20%;

    }
    .navbar-section section {
        display: flex;
        align-items: center;
        margin: 0 1rem;

    }
    img {
        width: 80px;
        height: auto;

    }
    .navbar-section p {
        font-size: 20px;
        color: white;
    }
</style>