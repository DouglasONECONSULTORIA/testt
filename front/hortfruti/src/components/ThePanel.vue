<template>
  <div class='paineis'>
    <div class="painel1">
      <h1>Oxente Horti Fruti</h1>
      <div class="input-product">
        <input type="text" placeholder="Digite o código do produto">
        <button>Enviar</button>
      </div>
    </div>
    <div class="painel2">
      <div class='Produtos'>
        //Adicionar o componente TheProducts
      </div>
    </div>
  </div>
</template>

<script>
// export default {
//   name: 'ThePanel'
// }
export default {
  data() {
    return {
      name: "ChatBox",
      isChatVisible: true,  // Define se o chat está visível
      isChatOpen: false,    // Define se o chat está aberto ou fechado
      messageCount: 3,      // Simulando notificações
      newMessage: "",       // Mensagem do input
      chatMessages: [       // Mensagens simuladas
        { text: "Olá, como posso ajudar?", time: "10:30", avatar: "https://via.placeholder.com/40" },
        { text: "Preciso de suporte.", time: "10:31", avatar: "https://via.placeholder.com/40" }
      ]
    };
  },
  methods: {
    toggleChat() {
      this.isChatOpen = !this.isChatOpen;
      if (this.isChatOpen) {
        this.messageCount = 0; // Zerar contador ao abrir
      }
    },
    closeChat() {
      this.isChatVisible = false;
    },
    sendMessage() {
      if (this.newMessage.trim() !== "") {
        this.chatMessages.push({
          text: this.newMessage,
          time: new Date().toLocaleTimeString().slice(0, 5),
          avatar: "https://via.placeholder.com/40"
        });
        this.newMessage = "";
      }
    }
  }
};
</script>

<style scoped>
  .paineis {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 10px;
    flex-grow: 1;
    width: 100%;
    height: 80vh;
  }

  .painel1, .painel2 {
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    margin: 0 5px;
    justify-content: space-between;
    background-color: #f1b30a;
    border-radius: 10px;
    height: 100%;
    padding: 15px;
  
    
  }

  .painel1 {
    width: 30%;
  }
  .painel2 {
    width: 70%;
  }

  .input-product {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    margin-top: 10px;
  }

  .input-product button {
    background-color: #1a5005;
    color: white;
    border: none;
    padding: 10px;
    margin-top: 10px;
    cursor: pointer;
    border-radius: 10px;
  }

  button:active {
  transform: scale(0.95);            
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); 
  background-color: #45a049; 
  }

  .input-product input{ 
    padding: 0 10px;
    height: 30px;
    border-radius: 5px;
    border: none;

  }

</style>
