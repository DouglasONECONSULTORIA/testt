<template>
  <TheHeader/>
  <ThePanel/>
  <ChatIcon/>
  <ChatBox/>
</template>

<script>
import ThePanel from './components/ThePanel.vue';
import TheHeader from './components/TheHeader.vue';
import ChatIcon from './components/ChatIcon.vue';
import ChatBox from './components/ChatBox.vue';

export default {
  name: 'App',
  components: {
    ThePanel, 
    TheHeader,
    ChatIcon, 
    ChatBox
  }
}
</script>

<style>
/** Reset css **/
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  /* overflow: hidden; */

}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
}
</style>
