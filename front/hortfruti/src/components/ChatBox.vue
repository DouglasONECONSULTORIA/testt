<template>
	<div class="chat-container">
		<div class="chat-box">
			<div v-for="(msg, index) in messages" :key="index" class="message" :class="{'user': msg.fromUser, 'bot': !msg.fromUser}">
			{{ msg.text }}
			</div>
		</div>
		<input v-model="userMessage" @keyup.enter="sendMessage" placeholder="Digite sua mensagem..." />
	<button @click="sendMessage">Enviar</button>
	</div>
</template>
  
<script>
	import axios from 'axios';
	
	export default {
		data() {
		return {
			name: 'ChatBox',
			userMessage: '',
			messages: []
		};
		},
		methods: {
		async sendMessage() {
			if (!this.userMessage.trim()) return;
	
			this.messages.push({ text: this.userMessage, fromUser: true });
			let question = encodeURIComponent(this.userMessage);
			this.userMessage = '';
	
			try {
			let response = await axios.get(`http://127.0.0.1:8000/?question=${question}`);
			this.messages.push({ text: response.data.answer, fromUser: false });
			} catch (error) {
			this.messages.push({ text: 'Erro ao conectar com o servidor.', fromUser: false });
			}
		}
		}
	};
</script>
  
<style>
  .chat-container {
	width: 300px;
	margin: auto;
	display: flex;
	flex-direction: column;
	align-items: center;
  }
  .chat-box {
	width: 100%;
	height: 400px;
	overflow-y: auto;
	border: 1px solid #ccc;
	padding: 10px;
	margin-bottom: 10px;
	background: #f9f9f9;
  }
  .message {
	padding: 8px;
	margin: 5px;
	border-radius: 5px;
	max-width: 80%;
  }
  .user {
	background: #d1e7fd;
	align-self: flex-end;
	text-align: right;
  }
  .bot {
	background: #e2e2e2;
	align-self: flex-start;
	text-align: left;
  }
  input {
	width: 80%;
	padding: 8px;
	margin-bottom: 5px;
  }
  button {
	padding: 8px;
  }
</style>
  