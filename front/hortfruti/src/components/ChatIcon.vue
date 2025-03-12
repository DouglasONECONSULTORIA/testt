<template>
    <div class="chat-icon">
        <img id='icon-chat' src="../assets/chat-icon.png" alt="Chat">
    </div>
</template>

<script>
export default {
    name: 'ChatIcon',
    props: {
        msg: String
    }
}
</script>

<style>
    .chat-icon {
        position: fixed;
        bottom: 60px;
        right: 20px;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
    }
    
    #icon-chat {
        width: 80px;
        height: auto;
        filter: grayscale(100%);
    }
</style>