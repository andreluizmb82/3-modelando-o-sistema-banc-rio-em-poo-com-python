// Seleciona o formulário
document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("new_client")

  // Verifica se o formulário foi encontrado
  if (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault()

      const formData = new FormData(form)
      const nome = formData.get("nome")
      const idade = formData.get("idade")

      const data = { nome: nome, idade: idade }
      localStorage.setItem("cliente", JSON.stringify(data))

      fetch("http://localhost:8000/employee", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      })
        .then((response) => response.json())
        .then((result) => {
          console.log(client_json._id)
          console.log("Resposta do servidor:", result._id)
          alert("Dados enviados com sucesso!")
        })
        .catch((error) => {
          console.error("Erro ao enviar os dados:", error)
          alert("Erro ao enviar os dados.")
        })
    })
  } else {
    console.error("O formulário não foi encontrado.")
  }
})

function getStoredData() {
  const cliente = JSON.parse(localStorage.getItem("cliente"))
  const conta = JSON.parse(localStorage.getItem("conta"))

  if (cliente && conta) {
    console.log("Nome do cliente:", cliente.nome)
    console.log("Número da conta:", conta.numero)
    console.log("Saldo:", conta.saldo)
  } else {
    console.log("Nenhum dado encontrado no localStorage.")
  }
}
